#!/usr/bin/env python3
# batch_analyze.py - Analyze entire directories of Python code

import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path
from agents.nlp_agent import NLPAgent
from agents.classifiers import BugGateClassifier, VulnerabilityGateClassifier
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.panel import Panel

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

def find_python_files(directory, exclude_patterns=None):
    """Find all Python files in a directory recursively"""
    if exclude_patterns is None:
        exclude_patterns = ['venv', '__pycache__', '.git', 'node_modules', '.env', 'migrations']
    
    python_files = []
    directory = Path(directory)
    
    for filepath in directory.rglob('*.py'):
        # Skip excluded directories
        skip = False
        for pattern in exclude_patterns:
            if pattern in str(filepath):
                skip = True
                break
        if not skip:
            python_files.append(filepath)
    
    return sorted(python_files)

def analyze_file_silent(filepath, config, nlp_agent, bug_classifier, vuln_classifier):
    """Analyze a single file without console output"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            code_text = f.read()
    except Exception as e:
        return None
    
    filename = os.path.basename(filepath)
    
    # Extract features
    features = nlp_agent.extract_features(code_text, filename)
    
    # Classify
    bug_activation = config['bug_gate']['activation']
    vuln_activation = config['vulnerability_gate']['activation']
    
    # Temporarily suppress print statements
    import io
    import contextlib
    
    with contextlib.redirect_stdout(io.StringIO()):
        bug_result = bug_classifier.classify(features['bug_features'], activation=bug_activation)
        vuln_result = vuln_classifier.classify(features['vulnerability_features'], activation=vuln_activation)
    
    overall = "PASS" if (bug_result == "PASS" and vuln_result == "PASS") else "FAIL"
    
    return {
        'filepath': str(filepath),
        'filename': filename,
        'bug_gate': bug_result,
        'vulnerability_gate': vuln_result,
        'overall': overall,
        'bug_features': features['bug_features'],
        'vulnerability_features': features['vulnerability_features']
    }

def batch_analyze(directory, config, output_file=None):
    """Analyze all Python files in a directory"""
    
    console.print(Panel.fit(
        f"[bold cyan]Batch Analysis: {directory}[/bold cyan]",
        border_style="cyan"
    ))
    
    # Find all Python files
    python_files = find_python_files(directory)
    
    if not python_files:
        console.print("[yellow]No Python files found in the specified directory.[/yellow]")
        return None
    
    console.print(f"\n[green]Found {len(python_files)} Python files to analyze[/green]\n")
    
    # Initialize components
    nlp_agent = NLPAgent()
    bug_classifier = BugGateClassifier()
    vuln_classifier = VulnerabilityGateClassifier()
    
    results = []
    
    # Analyze with progress bar
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console
    ) as progress:
        task = progress.add_task("Analyzing files...", total=len(python_files))
        
        for filepath in python_files:
            result = analyze_file_silent(filepath, config, nlp_agent, bug_classifier, vuln_classifier)
            if result:
                results.append(result)
            progress.advance(task)
    
    # Generate statistics
    stats = calculate_statistics(results)
    
    # Display results
    display_batch_results(results, stats)
    
    # Save results if output file specified
    if output_file:
        save_results(results, stats, output_file)
    
    return {
        'results': results,
        'stats': stats,
        'directory': str(directory),
        'timestamp': datetime.now().isoformat()
    }

def calculate_statistics(results):
    """Calculate statistics from batch analysis results"""
    total = len(results)
    
    if total == 0:
        return None
    
    # Overall stats
    passed = sum(1 for r in results if r['overall'] == 'PASS')
    failed = total - passed
    
    # Bug gate stats
    bug_passed = sum(1 for r in results if r['bug_gate'] == 'PASS')
    bug_failed = total - bug_passed
    
    # Vulnerability gate stats
    vuln_passed = sum(1 for r in results if r['vulnerability_gate'] == 'PASS')
    vuln_failed = total - vuln_passed
    
    # Complexity stats
    complexities = [r['bug_features']['max_complexity'] for r in results]
    nestings = [r['bug_features']['max_nesting'] for r in results]
    lengths = [r['bug_features']['max_function_length'] for r in results]
    
    # Vulnerability counts
    sql_issues = sum(1 for r in results if r['vulnerability_features']['sql_concat'] > 0 or r['vulnerability_features']['sql_format'] > 0)
    eval_issues = sum(1 for r in results if r['vulnerability_features']['eval_usage'] > 0)
    secret_issues = sum(1 for r in results if r['vulnerability_features']['hardcoded_secrets'] > 0)
    command_issues = sum(1 for r in results if r['vulnerability_features']['os_system'] > 0 or r['vulnerability_features']['shell_true'] > 0)
    pickle_issues = sum(1 for r in results if r['vulnerability_features']['pickle_usage'] > 0)
    
    return {
        'total_files': total,
        'overall_passed': passed,
        'overall_failed': failed,
        'overall_pass_rate': passed / total * 100,
        'bug_gate_passed': bug_passed,
        'bug_gate_failed': bug_failed,
        'bug_gate_pass_rate': bug_passed / total * 100,
        'vuln_gate_passed': vuln_passed,
        'vuln_gate_failed': vuln_failed,
        'vuln_gate_pass_rate': vuln_passed / total * 100,
        'complexity': {
            'avg': sum(complexities) / total,
            'max': max(complexities),
            'min': min(complexities)
        },
        'nesting': {
            'avg': sum(nestings) / total,
            'max': max(nestings),
            'min': min(nestings)
        },
        'function_length': {
            'avg': sum(lengths) / total,
            'max': max(lengths),
            'min': min(lengths)
        },
        'vulnerability_breakdown': {
            'sql_injection': sql_issues,
            'eval_exec': eval_issues,
            'hardcoded_secrets': secret_issues,
            'command_injection': command_issues,
            'pickle_deserialization': pickle_issues
        }
    }

def display_batch_results(results, stats):
    """Display batch analysis results in a nice format"""
    
    if not stats:
        console.print("[red]No results to display[/red]")
        return
    
    console.print("\n" + "="*70)
    console.print("[bold cyan]BATCH ANALYSIS RESULTS[/bold cyan]")
    console.print("="*70 + "\n")
    
    # Summary Table
    summary_table = Table(title="Overall Summary", show_header=True, header_style="bold cyan")
    summary_table.add_column("Metric", style="cyan")
    summary_table.add_column("Value", justify="right")
    summary_table.add_column("Percentage", justify="right")
    
    summary_table.add_row(
        "Total Files Analyzed",
        str(stats['total_files']),
        "-"
    )
    
    pass_color = "green" if stats['overall_pass_rate'] >= 80 else "yellow" if stats['overall_pass_rate'] >= 60 else "red"
    summary_table.add_row(
        "Overall PASS",
        f"[{pass_color}]{stats['overall_passed']}[/{pass_color}]",
        f"[{pass_color}]{stats['overall_pass_rate']:.1f}%[/{pass_color}]"
    )
    summary_table.add_row(
        "Overall FAIL",
        f"[red]{stats['overall_failed']}[/red]",
        f"[red]{100 - stats['overall_pass_rate']:.1f}%[/red]"
    )
    
    console.print(summary_table)
    
    # Gate Breakdown Table
    gate_table = Table(title="\nGate Breakdown", show_header=True, header_style="bold yellow")
    gate_table.add_column("Quality Gate", style="yellow")
    gate_table.add_column("Passed", justify="center")
    gate_table.add_column("Failed", justify="center")
    gate_table.add_column("Pass Rate", justify="right")
    
    bug_color = "green" if stats['bug_gate_pass_rate'] >= 80 else "yellow" if stats['bug_gate_pass_rate'] >= 60 else "red"
    gate_table.add_row(
        "Bug Gate",
        f"[green]{stats['bug_gate_passed']}[/green]",
        f"[red]{stats['bug_gate_failed']}[/red]",
        f"[{bug_color}]{stats['bug_gate_pass_rate']:.1f}%[/{bug_color}]"
    )
    
    vuln_color = "green" if stats['vuln_gate_pass_rate'] >= 80 else "yellow" if stats['vuln_gate_pass_rate'] >= 60 else "red"
    gate_table.add_row(
        "Vulnerability Gate",
        f"[green]{stats['vuln_gate_passed']}[/green]",
        f"[red]{stats['vuln_gate_failed']}[/red]",
        f"[{vuln_color}]{stats['vuln_gate_pass_rate']:.1f}%[/{vuln_color}]"
    )
    
    console.print(gate_table)
    
    # Code Quality Metrics Table
    metrics_table = Table(title="\nCode Quality Metrics", show_header=True, header_style="bold magenta")
    metrics_table.add_column("Metric", style="magenta")
    metrics_table.add_column("Average", justify="right")
    metrics_table.add_column("Max", justify="right")
    metrics_table.add_column("Min", justify="right")
    
    metrics_table.add_row(
        "Cyclomatic Complexity",
        f"{stats['complexity']['avg']:.2f}",
        str(stats['complexity']['max']),
        str(stats['complexity']['min'])
    )
    metrics_table.add_row(
        "Nesting Depth",
        f"{stats['nesting']['avg']:.2f}",
        str(stats['nesting']['max']),
        str(stats['nesting']['min'])
    )
    metrics_table.add_row(
        "Max Function Length",
        f"{stats['function_length']['avg']:.1f}",
        str(stats['function_length']['max']),
        str(stats['function_length']['min'])
    )
    
    console.print(metrics_table)
    
    # Vulnerability Breakdown Table
    vuln_table = Table(title="\nVulnerability Breakdown", show_header=True, header_style="bold red")
    vuln_table.add_column("Vulnerability Type", style="red")
    vuln_table.add_column("Files Affected", justify="center")
    
    vb = stats['vulnerability_breakdown']
    vuln_table.add_row("SQL Injection", str(vb['sql_injection']))
    vuln_table.add_row("Eval/Exec Usage", str(vb['eval_exec']))
    vuln_table.add_row("Hardcoded Secrets", str(vb['hardcoded_secrets']))
    vuln_table.add_row("Command Injection", str(vb['command_injection']))
    vuln_table.add_row("Pickle Deserialization", str(vb['pickle_deserialization']))
    
    console.print(vuln_table)
    
    # Show top issues
    failed_files = [r for r in results if r['overall'] == 'FAIL']
    if failed_files:
        console.print("\n[bold red]Files Requiring Attention:[/bold red]")
        issues_table = Table(show_header=True, header_style="bold")
        issues_table.add_column("File", style="cyan", max_width=50)
        issues_table.add_column("Bug Gate", justify="center")
        issues_table.add_column("Vuln Gate", justify="center")
        issues_table.add_column("Issues", style="yellow")
        
        for r in failed_files[:15]:  # Show top 15
            issues = []
            if r['bug_gate'] == 'FAIL':
                if r['bug_features']['max_nesting'] > 4:
                    issues.append(f"nesting={r['bug_features']['max_nesting']}")
                if r['bug_features']['max_complexity'] > 15:
                    issues.append(f"complexity={r['bug_features']['max_complexity']}")
            if r['vulnerability_gate'] == 'FAIL':
                vf = r['vulnerability_features']
                if vf['sql_concat'] or vf['sql_format']:
                    issues.append("SQL")
                if vf['eval_usage']:
                    issues.append("eval")
                if vf['hardcoded_secrets']:
                    issues.append("secrets")
                if vf['os_system'] or vf['shell_true']:
                    issues.append("cmd_inj")
            
            bug_color = "green" if r['bug_gate'] == "PASS" else "red"
            vuln_color = "green" if r['vulnerability_gate'] == "PASS" else "red"
            
            issues_table.add_row(
                r['filename'],
                f"[{bug_color}]{r['bug_gate']}[/{bug_color}]",
                f"[{vuln_color}]{r['vulnerability_gate']}[/{vuln_color}]",
                ", ".join(issues) if issues else "-"
            )
        
        console.print(issues_table)
        
        if len(failed_files) > 15:
            console.print(f"[yellow]... and {len(failed_files) - 15} more files[/yellow]")

def save_results(results, stats, output_file):
    """Save results to a JSON file"""
    output_data = {
        'timestamp': datetime.now().isoformat(),
        'statistics': stats,
        'file_results': results
    }
    
    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=2)
    
    console.print(f"\n[green]Results saved to: {output_file}[/green]")

def main():
    parser = argparse.ArgumentParser(
        description='Batch analyze Python files for code quality',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python batch_analyze.py /path/to/project
  python batch_analyze.py . -o results.json
  python batch_analyze.py ~/coursework --output analysis_results.json
        """
    )
    parser.add_argument('directory', help='Directory to analyze')
    parser.add_argument('-o', '--output', help='Output JSON file for results')
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.directory):
        console.print(f"[red]Error: '{args.directory}' is not a valid directory[/red]")
        sys.exit(1)
    
    console.print("[bold green]Multi-Agent Code Quality - Batch Analyzer[/bold green]\n")
    
    # Load configuration
    console.print("Loading trained configuration...")
    config = load_optimal_config()
    console.print("[green]✓ Configuration loaded[/green]\n")
    
    # Run batch analysis
    batch_analyze(args.directory, config, args.output)

if __name__ == "__main__":
    main()
