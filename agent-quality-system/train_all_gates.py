#!/usr/bin/env python3
"""
Training Script for All 8 Quality Gates
Optimizes activation functions (Sigmoid vs ReLU) for each gate
using SonarQube ground truth labels.
"""

import os
import json
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress

from agents.enhanced_feature_extractor import EnhancedFeatureExtractor
from agents.all_gate_classifiers import AllGatesClassificationPipeline
from agents.supervisor import SupervisorAgent

console = Console()


def load_sonar_labels(path="data/results/sonar_all_gates_labels.json"):
    """Load SonarQube ground truth labels"""
    with open(path, 'r') as f:
        return json.load(f)


def load_sonar_results(path="data/results/sonar_comprehensive_metrics.json"):
    """Load SonarQube comprehensive results"""
    with open(path, 'r') as f:
        return json.load(f)


def find_project_files(project_path, max_files=100):
    """Find source files in a project"""
    extensions = {'.py', '.java', '.cs', '.js', '.ts', '.c', '.cpp', '.h'}
    skip_patterns = {'node_modules', 'venv', '.git', 'bin', 'obj', '__pycache__', 
                     '.venv', 'target', 'vendor', 'dist', 'build'}
    
    source_files = []
    
    for root, dirs, files in os.walk(project_path):
        dirs[:] = [d for d in dirs if d not in skip_patterns and not d.startswith('.')]
        
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in extensions:
                source_files.append(os.path.join(root, f))
                if len(source_files) >= max_files:
                    return source_files
    
    return source_files


def extract_project_features(project_path, extractor, max_files=50):
    """Extract aggregated features for a project"""
    files = find_project_files(project_path, max_files)
    
    if not files:
        return None
    
    # Aggregate features
    all_bug_features = []
    all_vuln_features = []
    all_hotspot_features = []
    all_project_features = []
    
    for filepath in files:
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                code = f.read()
            
            features = extractor.extract_all_features(code, filepath)
            all_bug_features.append(features['bug_features'])
            all_vuln_features.append(features['vulnerability_features'])
            all_hotspot_features.append(features['security_hotspot_features'])
            all_project_features.append(features['project_features'])
            
        except Exception:
            continue
    
    if not all_bug_features:
        return None
    
    # Aggregate bug features (take max for risk-based metrics)
    agg_bug = {
        'avg_complexity': max(f.get('avg_complexity', 0) for f in all_bug_features),
        'max_complexity': max(f.get('max_complexity', 0) for f in all_bug_features),
        'max_nesting': max(f.get('max_nesting', 0) for f in all_bug_features),
        'avg_function_length': max(f.get('avg_function_length', 0) for f in all_bug_features),
        'max_function_length': max(f.get('max_function_length', 0) for f in all_bug_features),
        'num_functions': sum(f.get('num_functions', 0) for f in all_bug_features),
        'lines_of_code': sum(f.get('lines_of_code', 0) for f in all_bug_features),
        'error_handling_score': sum(f.get('error_handling_score', 50) for f in all_bug_features) // len(all_bug_features),
    }
    
    # Aggregate vulnerability features (sum for cumulative risk)
    agg_vuln = {
        'sql_injection': sum(f.get('sql_injection', 0) for f in all_vuln_features),
        'eval_exec': sum(f.get('eval_exec', 0) for f in all_vuln_features),
        'command_injection': sum(f.get('command_injection', 0) for f in all_vuln_features),
        'hardcoded_secrets': sum(f.get('hardcoded_secrets', 0) for f in all_vuln_features),
        'xss_risk': sum(f.get('xss_risk', 0) for f in all_vuln_features),
        'path_traversal': sum(f.get('path_traversal', 0) for f in all_vuln_features),
        'total_vulnerability_signals': sum(f.get('total_vulnerability_signals', 0) for f in all_vuln_features),
    }
    
    # Aggregate hotspot features
    agg_hotspot = {
        'security_hotspots': sum(f.get('security_hotspots', 0) for f in all_hotspot_features),
        'crypto_usage': sum(f.get('crypto_usage', 0) for f in all_hotspot_features),
        'file_operations': sum(f.get('file_operations', 0) for f in all_hotspot_features),
        'network_operations': sum(f.get('network_operations', 0) for f in all_hotspot_features),
    }
    
    # Aggregate project features
    test_files = sum(1 for f in all_project_features if f.get('has_test_files', 0))
    agg_project = {
        'has_test_files': 1 if test_files > 0 else 0,
        'test_file_ratio': test_files / len(files),
        'has_test_framework': max(f.get('has_test_framework', 0) for f in all_project_features),
        'duplication_ratio': sum(f.get('duplication_ratio', 0) for f in all_project_features) / len(all_project_features),
        'has_tests': 1 if test_files > 0 else 0,
    }
    
    return {
        'bug_features': agg_bug,
        'vulnerability_features': {**agg_vuln, **agg_hotspot},
        'project_features': agg_project,
        'files_analyzed': len(all_bug_features),
    }


def train_gate(gate_name, classifier_class, features_list, ground_truth):
    """Train a single gate by testing Sigmoid vs ReLU"""
    supervisor = SupervisorAgent(gate_name)
    
    results = {}
    
    for activation in ['sigmoid', 'relu']:
        predictions = []
        classifier = classifier_class(verbose=False)
        
        for features in features_list:
            pred = classifier.classify(features, activation=activation)
            predictions.append(pred)
        
        metrics = supervisor.evaluate(predictions, ground_truth)
        results[activation] = metrics
    
    # Select best based on specificity, then accuracy as tiebreaker
    best = max(results.items(), 
               key=lambda x: (x[1]['specificity'], x[1]['accuracy']))
    
    return best[0], results


def main():
    console.print(Panel.fit(
        "[bold cyan]Multi-Agent Quality Gate Training[/bold cyan]\n"
        "[dim]All 8 Quality Gates with SonarQube Ground Truth[/dim]",
        border_style="cyan"
    ))
    
    # Load SonarQube data
    console.print("\n[yellow]Loading SonarQube ground truth...[/yellow]")
    labels = load_sonar_labels()
    sonar_data = load_sonar_results()
    
    console.print(f"  Loaded {len(labels)} project labels\n")
    
    # Extract features for each project
    console.print("[yellow]Extracting features from projects...[/yellow]")
    extractor = EnhancedFeatureExtractor(verbose=False)
    
    project_features = {}
    base_dir = Path("/run/media/omniv/T7/GCU_SWE_2023-2025")
    
    # Map SonarQube keys to actual paths
    project_paths = {
        p['project']: p 
        for p in sonar_data.get('projects', [])
    }
    
    with Progress() as progress:
        task = progress.add_task("Extracting...", total=len(labels))
        
        for project_key in labels.keys():
            # Find project path
            project_name = project_key.replace('-', ' ').title().replace(' ', '-')
            
            # Try to find the directory
            possible_paths = [
                base_dir / project_key,
                base_dir / project_key.upper(),
                base_dir / project_name,
            ]
            
            # Also check directories that match
            for item in base_dir.iterdir():
                if item.is_dir() and project_key.replace('-', '').lower() in item.name.replace('-', '').lower():
                    possible_paths.insert(0, item)
            
            project_path = None
            for p in possible_paths:
                if p.exists():
                    project_path = p
                    break
            
            if project_path:
                features = extract_project_features(str(project_path), extractor)
                if features:
                    project_features[project_key] = features
            
            progress.advance(task)
    
    console.print(f"  Extracted features from {len(project_features)} projects\n")
    
    if not project_features:
        console.print("[red]No project features extracted![/red]")
        return
    
    # Prepare training data for each gate
    gate_configs = {}
    gate_metrics = {}
    
    gates_to_train = [
        'bug_gate',
        'vulnerability_gate',
        'security_hotspot_gate',
        'reliability_gate',
        'security_gate',
        'maintainability_gate',
        'coverage_gate',
        'duplication_gate',
    ]
    
    console.print("[yellow]Training classifiers for each gate...[/yellow]\n")
    
    for gate_name in gates_to_train:
        console.print(f"  Training: [cyan]{gate_name}[/cyan]...")
        
        # Prepare features and ground truth
        features_list = []
        ground_truth = []
        
        for project_key, features in project_features.items():
            if project_key in labels:
                gt = labels[project_key].get(gate_name, 'PASS')
                ground_truth.append(gt)
                
                # Select appropriate features based on gate type
                if gate_name in ['bug_gate', 'reliability_gate', 'maintainability_gate']:
                    features_list.append(features['bug_features'])
                elif gate_name in ['vulnerability_gate', 'security_hotspot_gate', 'security_gate']:
                    features_list.append(features['vulnerability_features'])
                else:
                    features_list.append(features['project_features'])
        
        if not features_list:
            console.print(f"    [red]No data for {gate_name}[/red]")
            continue
        
        # Get classifier class
        from agents.all_gate_classifiers import (
            BugGateClassifier, VulnerabilityGateClassifier,
            SecurityHotspotClassifier, ReliabilityGateClassifier,
            SecurityGateClassifier, MaintainabilityGateClassifier,
            CoverageGateClassifier, DuplicationGateClassifier
        )
        
        classifier_map = {
            'bug_gate': BugGateClassifier,
            'vulnerability_gate': VulnerabilityGateClassifier,
            'security_hotspot_gate': SecurityHotspotClassifier,
            'reliability_gate': ReliabilityGateClassifier,
            'security_gate': SecurityGateClassifier,
            'maintainability_gate': MaintainabilityGateClassifier,
            'coverage_gate': CoverageGateClassifier,
            'duplication_gate': DuplicationGateClassifier,
        }
        
        # Train
        best_activation, results = train_gate(
            gate_name, classifier_map[gate_name], features_list, ground_truth
        )
        
        gate_configs[gate_name] = {
            'activation': best_activation,
            'metrics': results[best_activation]
        }
        gate_metrics[gate_name] = results
        
        spec = results[best_activation]['specificity']
        acc = results[best_activation]['accuracy']
        console.print(f"    → Best: [green]{best_activation.upper()}[/green] "
                      f"(Specificity: {spec:.1%}, Accuracy: {acc:.1%})")
    
    # Display summary
    console.print("\n")
    console.print(Panel.fit(
        "[bold green]Training Complete[/bold green]",
        border_style="green"
    ))
    
    summary_table = Table(title="Optimal Configuration for All Gates")
    summary_table.add_column("Quality Gate", style="cyan")
    summary_table.add_column("Activation", justify="center")
    summary_table.add_column("Specificity", justify="center")
    summary_table.add_column("Accuracy", justify="center")
    summary_table.add_column("Sensitivity", justify="center")
    
    for gate_name, config in gate_configs.items():
        metrics = config['metrics']
        summary_table.add_row(
            gate_name.replace('_', ' ').title(),
            config['activation'].upper(),
            f"{metrics['specificity']:.1%}",
            f"{metrics['accuracy']:.1%}",
            f"{metrics['sensitivity']:.1%}"
        )
    
    console.print(summary_table)
    
    # Save configuration
    output_config = {
        'gates': gate_configs,
        'training_info': {
            'projects_used': len(project_features),
            'ground_truth_source': 'SonarQube'
        }
    }
    
    config_path = Path("data/results/all_gates_optimal_config.json")
    with open(config_path, 'w') as f:
        json.dump(output_config, f, indent=2)
    
    console.print(f"\n[green]Configuration saved to: {config_path}[/green]")
    
    # Also save detailed metrics
    metrics_path = Path("data/results/all_gates_training_metrics.json")
    with open(metrics_path, 'w') as f:
        json.dump(gate_metrics, f, indent=2, default=str)
    
    console.print(f"[green]Detailed metrics saved to: {metrics_path}[/green]")


if __name__ == "__main__":
    main()
