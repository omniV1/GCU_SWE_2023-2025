#!/usr/bin/env python3
# analyze.py - Analyze any Python file for quality gate issues

import sys
import json
import os
from agents.nlp_agent import NLPAgent
from agents.classifiers import BugGateClassifier, VulnerabilityGateClassifier
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def load_optimal_config():
    """Load the trained optimal configuration"""
    config_path = os.path.join(os.path.dirname(__file__), 'data/results/optimal_config.json')
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        console.print("[red]Error: No trained configuration found. Run train.py first.[/red]")
        sys.exit(1)

def analyze_file(filepath, config):
    """Analyze a Python file using the optimal configuration"""
    
    # Read the file
    try:
        with open(filepath, 'r') as f:
            code_text = f.read()
    except FileNotFoundError:
        console.print(f"[red]Error: File not found: {filepath}[/red]")
        return None
    except Exception as e:
        console.print(f"[red]Error reading file: {e}[/red]")
        return None
    
    filename = os.path.basename(filepath)
    
    console.print(Panel.fit(
        f"[bold cyan]Analyzing: {filepath}[/bold cyan]",
        border_style="cyan"
    ))
    
    # Extract features
    console.print("\n[yellow]Step 1: NLP Feature Extraction[/yellow]")
    nlp_agent = NLPAgent()
    features = nlp_agent.extract_features(code_text, filename)
    
    # Bug Gate Classification
    console.print("\n[yellow]Step 2: Bug Gate Classification[/yellow]")
    bug_classifier = BugGateClassifier()
    bug_activation = config['bug_gate']['activation']
    bug_result = bug_classifier.classify(features['bug_features'], activation=bug_activation)
    
    # Vulnerability Gate Classification
    console.print("\n[yellow]Step 3: Vulnerability Gate Classification[/yellow]")
    vuln_classifier = VulnerabilityGateClassifier()
    vuln_activation = config['vulnerability_gate']['activation']
    vuln_result = vuln_classifier.classify(features['vulnerability_features'], activation=vuln_activation)
    
    # Summary
    console.print("\n" + "="*60)
    console.print("[bold]PREDICTION SUMMARY[/bold]")
    console.print("="*60)
    
    results_table = Table()
    results_table.add_column("Quality Gate", style="cyan")
    results_table.add_column("Activation", style="yellow")
    results_table.add_column("Result", justify="center")
    
    bug_color = "green" if bug_result == "PASS" else "red"
    vuln_color = "green" if vuln_result == "PASS" else "red"
    
    results_table.add_row(
        "Bug Gate",
        bug_activation.upper(),
        f"[{bug_color}]{bug_result}[/{bug_color}]"
    )
    results_table.add_row(
        "Vulnerability Gate",
        vuln_activation.upper(),
        f"[{vuln_color}]{vuln_result}[/{vuln_color}]"
    )
    
    console.print(results_table)
    
    # Overall verdict
    overall = "PASS" if (bug_result == "PASS" and vuln_result == "PASS") else "FAIL"
    color = "green" if overall == "PASS" else "red"
    
    console.print(f"\n[bold {color}]Overall: {overall}[/bold {color}]")
    
    if overall == "FAIL":
        console.print("\n[yellow]Recommendations:[/yellow]")
        if bug_result == "FAIL":
            bf = features['bug_features']
            console.print("  • Reduce function complexity and nesting depth")
            console.print(f"    - Max complexity: {bf['max_complexity']} (threshold: 15)")
            console.print(f"    - Max nesting: {bf['max_nesting']} (threshold: 4)")
            console.print(f"    - Max function length: {bf['max_function_length']} lines (threshold: 100)")
        if vuln_result == "FAIL":
            vf = features['vulnerability_features']
            console.print("  • Fix security vulnerabilities:")
            if vf['sql_concat'] > 0 or vf['sql_format'] > 0:
                console.print("    - SQL injection patterns detected - use parameterized queries")
            if vf['eval_usage'] > 0:
                console.print("    - Dangerous eval/exec usage detected - avoid dynamic code execution")
            if vf['hardcoded_secrets'] > 0:
                console.print("    - Hardcoded secrets detected - use environment variables")
            if vf['os_system'] > 0 or vf['shell_true'] > 0:
                console.print("    - Command injection risks detected - avoid shell=True and os.system()")
            if vf['pickle_usage'] > 0:
                console.print("    - Pickle deserialization detected - use safe alternatives like JSON")
    
    return {
        'bug_gate': bug_result,
        'vulnerability_gate': vuln_result,
        'overall': overall,
        'features': features
    }

def main():
    """Main function"""
    if len(sys.argv) < 2:
        console.print("[bold]Usage:[/bold] python analyze.py <python_file> [file2.py ...]")
        console.print("\nExample: python analyze.py my_code.py")
        sys.exit(1)
    
    console.print("[bold green]Multi-Agent Code Quality Analyzer[/bold green]\n")
    
    # Load configuration
    console.print("Loading trained configuration...")
    config = load_optimal_config()
    console.print("[green]✓ Configuration loaded[/green]\n")
    
    # Analyze each file
    results = {}
    for filepath in sys.argv[1:]:
        result = analyze_file(filepath, config)
        if result:
            results[filepath] = result
        console.print("\n" + "-"*60 + "\n")
    
    # Summary if multiple files
    if len(results) > 1:
        console.print("\n[bold]OVERALL SUMMARY[/bold]")
        summary_table = Table()
        summary_table.add_column("File", style="cyan")
        summary_table.add_column("Bug Gate", justify="center")
        summary_table.add_column("Vuln Gate", justify="center")
        summary_table.add_column("Overall", justify="center")
        
        for filepath, result in results.items():
            bug_color = "green" if result['bug_gate'] == "PASS" else "red"
            vuln_color = "green" if result['vulnerability_gate'] == "PASS" else "red"
            overall_color = "green" if result['overall'] == "PASS" else "red"
            
            summary_table.add_row(
                os.path.basename(filepath),
                f"[{bug_color}]{result['bug_gate']}[/{bug_color}]",
                f"[{vuln_color}]{result['vulnerability_gate']}[/{vuln_color}]",
                f"[{overall_color}]{result['overall']}[/{overall_color}]"
            )
        
        console.print(summary_table)

if __name__ == "__main__":
    main()
