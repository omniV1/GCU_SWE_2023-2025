#!/usr/bin/env python3
"""
Compare Multi-Agent System predictions with SonarQube ground truth.
Calculates accuracy, specificity, and confusion matrices.
"""

import json
import os
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from agents.multi_lang_agent import MultiLanguageAgent
from agents.classifiers import BugGateClassifier, VulnerabilityGateClassifier

console = Console()


def load_sonar_results(path="data/results/sonar_results.json"):
    """Load SonarQube scan results"""
    with open(path, 'r') as f:
        return json.load(f)


def load_optimal_config(path="data/results/optimal_config.json"):
    """Load trained optimal configuration"""
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            'bug_gate': {'activation': 'relu'},
            'vulnerability_gate': {'activation': 'relu'}
        }


def analyze_project_files(project_path, max_files=50):
    """Analyze all source files in a project and aggregate results"""
    agent = MultiLanguageAgent()
    bug_classifier = BugGateClassifier(verbose=False)
    vuln_classifier = VulnerabilityGateClassifier(verbose=False)
    config = load_optimal_config()
    
    bug_activation = config['bug_gate']['activation']
    vuln_activation = config['vulnerability_gate']['activation']
    
    # Find source files using os.walk (faster than rglob)
    extensions = {'.py', '.java', '.cs', '.js', '.ts', '.c', '.cpp', '.h'}
    skip_patterns = {'node_modules', 'venv', '.git', 'bin', 'obj', '__pycache__', 
                     '.venv', 'target', 'vendor', 'dist', 'build'}
    source_files = []
    
    for root, dirs, files in os.walk(project_path):
        # Skip directories we don't want
        dirs[:] = [d for d in dirs if d not in skip_patterns and not d.startswith('.')]
        
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in extensions:
                source_files.append(os.path.join(root, f))
                if len(source_files) >= max_files:
                    break
        
        if len(source_files) >= max_files:
            break
    
    if not source_files:
        return None
    
    # Aggregate results
    bug_fails = 0
    vuln_fails = 0
    total_files = 0
    
    for filepath in source_files:
        try:
            # Read file content
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                code_text = f.read()
            
            # Get language and extract features
            language = agent.get_language(filepath)
            if language == 'unknown':
                continue
            
            features = agent.extract_features(code_text, filepath)
            if features is None:
                continue
            
            total_files += 1
            
            # Bug classification
            bug_features = features.get('bug_features', {})
            bug_result = bug_classifier.classify(bug_features, activation=bug_activation)
            if bug_result == 'FAIL':
                bug_fails += 1
            
            # Vulnerability classification
            vuln_features = features.get('vulnerability_features', {})
            vuln_result = vuln_classifier.classify(vuln_features, activation=vuln_activation)
            if vuln_result == 'FAIL':
                vuln_fails += 1
                
        except Exception:
            continue
    
    if total_files == 0:
        return None
    
    # Project-level prediction: FAIL if ANY file fails
    return {
        'total_files': total_files,
        'bug_fails': bug_fails,
        'vuln_fails': vuln_fails,
        'bug_gate': 'FAIL' if bug_fails > 0 else 'PASS',
        'vulnerability_gate': 'FAIL' if vuln_fails > 0 else 'PASS'
    }


def calculate_metrics(predictions, ground_truth, gate_name):
    """Calculate confusion matrix and metrics"""
    tp = fp = tn = fn = 0
    
    for pred, gt in zip(predictions, ground_truth):
        if pred == 'FAIL' and gt == 'FAIL':
            tp += 1
        elif pred == 'FAIL' and gt == 'PASS':
            fp += 1
        elif pred == 'PASS' and gt == 'PASS':
            tn += 1
        elif pred == 'PASS' and gt == 'FAIL':
            fn += 1
    
    total = tp + fp + tn + fn
    accuracy = (tp + tn) / total if total > 0 else 0
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
    sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    
    return {
        'gate_name': gate_name,
        'confusion_matrix': {'TP': tp, 'FP': fp, 'TN': tn, 'FN': fn},
        'accuracy': accuracy,
        'specificity': specificity,
        'sensitivity': sensitivity,
        'precision': precision,
        'total': total
    }


def display_comparison(comparisons, metrics):
    """Display comparison results"""
    console.print(Panel.fit(
        "[bold cyan]Multi-Agent System vs SonarQube[/bold cyan]\n"
        "[dim]Ground Truth Validation[/dim]",
        border_style="cyan"
    ))
    
    # Comparison table
    table = Table(title="Project-by-Project Comparison")
    table.add_column("Project", style="cyan")
    table.add_column("Bug (Ours)", justify="center")
    table.add_column("Bug (Sonar)", justify="center")
    table.add_column("Match?", justify="center")
    table.add_column("Vuln (Ours)", justify="center")
    table.add_column("Vuln (Sonar)", justify="center")
    table.add_column("Match?", justify="center")
    
    for comp in comparisons:
        bug_match = "✓" if comp['bug_match'] else "✗"
        bug_color = "green" if comp['bug_match'] else "red"
        vuln_match = "✓" if comp['vuln_match'] else "✗"
        vuln_color = "green" if comp['vuln_match'] else "red"
        
        our_bug_color = "red" if comp['our_bug'] == 'FAIL' else "green"
        sonar_bug_color = "red" if comp['sonar_bug'] == 'FAIL' else "green"
        our_vuln_color = "red" if comp['our_vuln'] == 'FAIL' else "green"
        sonar_vuln_color = "red" if comp['sonar_vuln'] == 'FAIL' else "green"
        
        table.add_row(
            comp['project'][:30],
            f"[{our_bug_color}]{comp['our_bug']}[/{our_bug_color}]",
            f"[{sonar_bug_color}]{comp['sonar_bug']}[/{sonar_bug_color}]",
            f"[{bug_color}]{bug_match}[/{bug_color}]",
            f"[{our_vuln_color}]{comp['our_vuln']}[/{our_vuln_color}]",
            f"[{sonar_vuln_color}]{comp['sonar_vuln']}[/{sonar_vuln_color}]",
            f"[{vuln_color}]{vuln_match}[/{vuln_color}]"
        )
    
    console.print(table)
    
    # Metrics tables
    for m in metrics:
        console.print(f"\n[bold cyan]{m['gate_name']} - Performance vs SonarQube[/bold cyan]")
        
        cm = m['confusion_matrix']
        cm_table = Table(title="Confusion Matrix")
        cm_table.add_column("", style="bold")
        cm_table.add_column("Pred: PASS", justify="center")
        cm_table.add_column("Pred: FAIL", justify="center")
        cm_table.add_row("Actual: PASS", f"[green]TN={cm['TN']}[/green]", f"[red]FP={cm['FP']}[/red]")
        cm_table.add_row("Actual: FAIL", f"[red]FN={cm['FN']}[/red]", f"[green]TP={cm['TP']}[/green]")
        console.print(cm_table)
        
        metrics_table = Table(title="Metrics")
        metrics_table.add_column("Metric", style="cyan")
        metrics_table.add_column("Value", justify="right")
        metrics_table.add_row("Accuracy", f"{m['accuracy']:.1%}")
        metrics_table.add_row("[bold]Specificity[/bold]", f"[bold]{m['specificity']:.1%}[/bold]")
        metrics_table.add_row("Sensitivity (Recall)", f"{m['sensitivity']:.1%}")
        metrics_table.add_row("Precision", f"{m['precision']:.1%}")
        console.print(metrics_table)


def main():
    console.print("[bold green]Comparing Multi-Agent System with SonarQube Ground Truth[/bold green]\n")
    
    # Load SonarQube results
    sonar_data = load_sonar_results()
    successful_results = [r for r in sonar_data['results'] if 'error' not in r]
    
    console.print(f"Found {len(successful_results)} SonarQube-scanned projects\n")
    
    comparisons = []
    bug_predictions = []
    bug_ground_truth = []
    vuln_predictions = []
    vuln_ground_truth = []
    
    for result in successful_results:
        project_name = result['project_name']
        project_path = result['project_path']
        sonar_status = result['gate_status']
        
        console.print(f"Analyzing: {project_name}...", end=" ")
        
        # Get our system's prediction
        our_result = analyze_project_files(project_path)
        
        if our_result is None:
            console.print("[yellow]skipped (no files)[/yellow]")
            continue
        
        console.print(f"[green]done ({our_result['total_files']} files)[/green]")
        
        # Compare
        bug_match = our_result['bug_gate'] == sonar_status['bug_gate']
        vuln_match = our_result['vulnerability_gate'] == sonar_status['vulnerability_gate']
        
        comparisons.append({
            'project': project_name,
            'our_bug': our_result['bug_gate'],
            'sonar_bug': sonar_status['bug_gate'],
            'bug_match': bug_match,
            'our_vuln': our_result['vulnerability_gate'],
            'sonar_vuln': sonar_status['vulnerability_gate'],
            'vuln_match': vuln_match
        })
        
        bug_predictions.append(our_result['bug_gate'])
        bug_ground_truth.append(sonar_status['bug_gate'])
        vuln_predictions.append(our_result['vulnerability_gate'])
        vuln_ground_truth.append(sonar_status['vulnerability_gate'])
    
    if not comparisons:
        console.print("[red]No projects to compare![/red]")
        return
    
    # Calculate metrics
    bug_metrics = calculate_metrics(bug_predictions, bug_ground_truth, "Bug Gate")
    vuln_metrics = calculate_metrics(vuln_predictions, vuln_ground_truth, "Vulnerability Gate")
    
    # Display results
    console.print("\n")
    display_comparison(comparisons, [bug_metrics, vuln_metrics])
    
    # Summary
    bug_accuracy = sum(1 for c in comparisons if c['bug_match']) / len(comparisons)
    vuln_accuracy = sum(1 for c in comparisons if c['vuln_match']) / len(comparisons)
    
    console.print(f"\n[bold]Overall Agreement with SonarQube:[/bold]")
    console.print(f"  Bug Gate: {bug_accuracy:.1%}")
    console.print(f"  Vulnerability Gate: {vuln_accuracy:.1%}")
    
    # Save comparison results
    comparison_data = {
        'comparisons': comparisons,
        'bug_metrics': bug_metrics,
        'vuln_metrics': vuln_metrics,
        'overall_bug_agreement': bug_accuracy,
        'overall_vuln_agreement': vuln_accuracy
    }
    
    with open('data/results/sonarqube_comparison.json', 'w') as f:
        json.dump(comparison_data, f, indent=2)
    
    console.print(f"\n[green]Comparison saved to data/results/sonarqube_comparison.json[/green]")


if __name__ == "__main__":
    main()
