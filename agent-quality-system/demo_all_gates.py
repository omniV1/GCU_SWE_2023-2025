#!/usr/bin/env python3
"""
Comprehensive Demo - All 8 Quality Gates
Uses trained optimal configuration from SonarQube ground truth.
"""

import os
import json
import sys
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.tree import Tree

from agents.enhanced_feature_extractor import EnhancedFeatureExtractor
from agents.all_gate_classifiers import AllGatesClassificationPipeline

console = Console()


def load_config(path="data/results/all_gates_optimal_config.json"):
    """Load trained optimal configuration"""
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        console.print("[yellow]No trained config found, using defaults[/yellow]")
        return {'gates': {}}


def analyze_file(filepath):
    """Analyze a single file through all 8 gates"""
    extractor = EnhancedFeatureExtractor(verbose=False)
    config = load_config()
    
    # Convert config format
    pipeline_config = {}
    for gate_name, gate_config in config.get('gates', {}).items():
        pipeline_config[gate_name] = {'activation': gate_config.get('activation', 'sigmoid')}
    
    pipeline = AllGatesClassificationPipeline(pipeline_config, verbose=True)
    
    # Read file
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        code = f.read()
    
    # Extract features
    console.print(Panel.fit(
        f"[bold cyan]Analyzing: {os.path.basename(filepath)}[/bold cyan]",
        border_style="cyan"
    ))
    
    console.print("\n[yellow]Step 1: Feature Extraction[/yellow]")
    features = extractor.extract_all_features(code, filepath)
    
    # Display extracted features
    feature_tree = Tree("[bold]Extracted Features[/bold]")
    
    bug_branch = feature_tree.add("[cyan]Bug Features[/cyan]")
    for k, v in features['bug_features'].items():
        bug_branch.add(f"{k}: {v}")
    
    vuln_branch = feature_tree.add("[red]Vulnerability Features[/red]")
    for k, v in features['vulnerability_features'].items():
        if v > 0:
            vuln_branch.add(f"[red]{k}: {v}[/red]")
    
    hotspot_branch = feature_tree.add("[yellow]Security Hotspot Features[/yellow]")
    for k, v in features['security_hotspot_features'].items():
        if v > 0:
            hotspot_branch.add(f"[yellow]{k}: {v}[/yellow]")
    
    console.print(feature_tree)
    
    # Classify through all gates
    console.print("\n[yellow]Step 2: Classification through All 8 Gates[/yellow]")
    
    results = pipeline.classify(
        features['bug_features'],
        features['vulnerability_features'],
        features['project_features']
    )
    
    # Display results
    console.print("\n")
    results_table = Table(title="Quality Gate Results")
    results_table.add_column("Quality Gate", style="cyan")
    results_table.add_column("Activation", justify="center")
    results_table.add_column("Result", justify="center")
    
    gate_order = [
        ('bug_gate', 'Bug Gate'),
        ('vulnerability_gate', 'Vulnerability Gate'),
        ('security_hotspot_gate', 'Security Hotspot Gate'),
        ('reliability_gate', 'Reliability Gate'),
        ('security_gate', 'Security Gate'),
        ('maintainability_gate', 'Maintainability Gate'),
        ('coverage_gate', 'Coverage Gate'),
        ('duplication_gate', 'Duplication Gate'),
    ]
    
    for gate_key, gate_name in gate_order:
        result = results.get(gate_key, 'N/A')
        activation = pipeline.activations.get(gate_key, 'N/A').upper()
        color = "green" if result == "PASS" else "red"
        results_table.add_row(gate_name, activation, f"[{color}]{result}[/{color}]")
    
    console.print(results_table)
    
    # Overall result
    overall = results.get('overall', 'FAIL')
    color = "green" if overall == "PASS" else "red"
    console.print(f"\n[bold {color}]Overall Result: {overall}[/bold {color}]")
    
    # Recommendations
    if overall == "FAIL":
        console.print("\n[yellow]Recommendations:[/yellow]")
        if results.get('bug_gate') == 'FAIL':
            console.print("  • Reduce code complexity and nesting depth")
        if results.get('vulnerability_gate') == 'FAIL':
            console.print("  • Fix security vulnerabilities (SQL injection, eval, etc.)")
        if results.get('security_hotspot_gate') == 'FAIL':
            console.print("  • Review security-sensitive code (crypto, file ops, network)")
        if results.get('security_gate') == 'FAIL':
            console.print("  • Remove hardcoded secrets and fix injection vulnerabilities")
        if results.get('coverage_gate') == 'FAIL':
            console.print("  • Add unit tests to increase code coverage")
        if results.get('duplication_gate') == 'FAIL':
            console.print("  • Refactor duplicated code blocks")
    
    return results


def analyze_project(project_path):
    """Analyze an entire project through all 8 gates"""
    extractor = EnhancedFeatureExtractor(verbose=False)
    config = load_config()
    
    # Convert config format
    pipeline_config = {}
    for gate_name, gate_config in config.get('gates', {}).items():
        pipeline_config[gate_name] = {'activation': gate_config.get('activation', 'sigmoid')}
    
    pipeline = AllGatesClassificationPipeline(pipeline_config, verbose=False)
    
    console.print(Panel.fit(
        f"[bold cyan]Analyzing Project: {os.path.basename(project_path)}[/bold cyan]",
        border_style="cyan"
    ))
    
    # Find source files
    extensions = {'.py', '.java', '.cs', '.js', '.ts', '.c', '.cpp'}
    skip_patterns = {'node_modules', 'venv', '.git', '__pycache__'}
    
    files = []
    for root, dirs, filenames in os.walk(project_path):
        dirs[:] = [d for d in dirs if d not in skip_patterns and not d.startswith('.')]
        for f in filenames:
            if os.path.splitext(f)[1].lower() in extensions:
                files.append(os.path.join(root, f))
    
    console.print(f"Found {len(files)} source files\n")
    
    # Aggregate results
    all_results = []
    gate_failures = {gate: 0 for gate in pipeline.get_gate_names()}
    
    for filepath in files[:100]:  # Limit to 100 files
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                code = f.read()
            
            features = extractor.extract_all_features(code, filepath)
            results = pipeline.classify(
                features['bug_features'],
                features['vulnerability_features'],
                features['project_features']
            )
            
            all_results.append({'file': filepath, 'results': results})
            
            for gate in pipeline.get_gate_names():
                if results.get(gate) == 'FAIL':
                    gate_failures[gate] += 1
                    
        except Exception:
            continue
    
    # Display summary
    console.print(f"\n[bold]Analyzed {len(all_results)} files[/bold]\n")
    
    summary_table = Table(title="Project Quality Gate Summary")
    summary_table.add_column("Quality Gate", style="cyan")
    summary_table.add_column("Files Passed", justify="center")
    summary_table.add_column("Files Failed", justify="center")
    summary_table.add_column("Pass Rate", justify="center")
    summary_table.add_column("Project Status", justify="center")
    
    gate_order = [
        ('bug_gate', 'Bug Gate'),
        ('vulnerability_gate', 'Vulnerability Gate'),
        ('security_hotspot_gate', 'Security Hotspot Gate'),
        ('reliability_gate', 'Reliability Gate'),
        ('security_gate', 'Security Gate'),
        ('maintainability_gate', 'Maintainability Gate'),
        ('coverage_gate', 'Coverage Gate'),
        ('duplication_gate', 'Duplication Gate'),
    ]
    
    project_results = {}
    
    for gate_key, gate_name in gate_order:
        failed = gate_failures.get(gate_key, 0)
        passed = len(all_results) - failed
        rate = passed / len(all_results) * 100 if all_results else 0
        
        # Project fails if ANY file fails (strict) or >20% fail (lenient)
        project_status = "PASS" if failed == 0 else "FAIL"
        project_results[gate_key] = project_status
        
        rate_color = "green" if rate >= 80 else "yellow" if rate >= 50 else "red"
        status_color = "green" if project_status == "PASS" else "red"
        
        summary_table.add_row(
            gate_name,
            f"[green]{passed}[/green]",
            f"[red]{failed}[/red]" if failed > 0 else "0",
            f"[{rate_color}]{rate:.1f}%[/{rate_color}]",
            f"[{status_color}]{project_status}[/{status_color}]"
        )
    
    console.print(summary_table)
    
    # Overall
    overall_pass = all(v == "PASS" for v in project_results.values())
    color = "green" if overall_pass else "red"
    status = "PASS" if overall_pass else "FAIL"
    console.print(f"\n[bold {color}]Overall Project Status: {status}[/bold {color}]")
    
    return project_results


def main():
    console.print(Panel.fit(
        "[bold green]Multi-Agent Code Quality System[/bold green]\n"
        "[dim]All 8 Quality Gates Demo[/dim]",
        border_style="green"
    ))
    
    # Check for trained config
    config = load_config()
    if config.get('gates'):
        console.print("[green]✓ Loaded trained configuration[/green]")
        
        # Show configured activations
        act_table = Table(title="Trained Activations", show_header=True)
        act_table.add_column("Gate", style="cyan")
        act_table.add_column("Activation", justify="center")
        
        for gate, conf in config['gates'].items():
            act_table.add_row(gate.replace('_', ' ').title(), conf['activation'].upper())
        
        console.print(act_table)
    else:
        console.print("[yellow]Using default configuration[/yellow]")
    
    # Get input
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        # Default demo file
        target = "demo_code.py"
        
        # Create demo file if it doesn't exist
        if not os.path.exists(target):
            demo_code = '''
# Demo code with various quality issues

import os
import pickle

API_KEY = "FAKE_SECRET_KEY_12345_DEMO_ONLY"  # Hardcoded secret!

def complex_function(data, config, options):
    """Function with high complexity and nesting"""
    if data:
        if config.get('enabled'):
            if options.get('mode') == 'advanced':
                for item in data:
                    for sub in item:
                        if sub.get('valid'):
                            # SQL injection vulnerability
                            query = "SELECT * FROM users WHERE id = " + str(sub['id'])
                            
                            # Command injection
                            os.system("process " + sub['name'])
                            
                            # Insecure deserialization
                            result = pickle.loads(sub['data'])
                            
                            # Dangerous eval
                            eval(sub['expression'])
    return True

# Duplicate code block 1
def process_a(x):
    result = x * 2
    result = result + 10
    result = result / 5
    return result

# Duplicate code block 2
def process_b(x):
    result = x * 2
    result = result + 10
    result = result / 5
    return result
'''
            with open(target, 'w') as f:
                f.write(demo_code)
            console.print(f"[dim]Created demo file: {target}[/dim]\n")
    
    # Analyze
    if os.path.isfile(target):
        analyze_file(target)
    elif os.path.isdir(target):
        analyze_project(target)
    else:
        console.print(f"[red]Error: {target} not found[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()
