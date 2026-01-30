#!/usr/bin/env python3
# batch_analyze_all.py - Analyze ALL programming languages in a directory
# Uses trained multi-agent architecture with adaptive activation selection

import os
import sys
import json
import argparse
import signal
from datetime import datetime
from pathlib import Path
from collections import defaultdict
from contextlib import contextmanager

from agents.multi_lang_agent import MultiLanguageAgent, calculate_total_signals
from agents.classifiers import BugGateClassifier, VulnerabilityGateClassifier
from agents.supervisor import SupervisorAgent
from agents.architecture_agent import ArchitectureAgent
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.panel import Panel

console = Console()

# Path to trained configuration
SCRIPT_DIR = Path(__file__).parent
CONFIG_PATH = SCRIPT_DIR / "data" / "results" / "optimal_config.json"


class TimeoutError(Exception):
    pass


@contextmanager
def timeout(seconds):
    """Context manager for timing out operations (Unix only)"""
    def signal_handler(_signum, _frame):
        raise TimeoutError(f"Operation timed out after {seconds} seconds")

    # Only use signal-based timeout on Unix systems
    if hasattr(signal, 'SIGALRM'):
        old_handler = signal.signal(signal.SIGALRM, signal_handler)
        signal.alarm(seconds)
        try:
            yield
        finally:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, old_handler)
    else:
        # On Windows, just yield without timeout
        yield


def load_trained_config():
    """Load optimal configuration from training, or use defaults"""
    if CONFIG_PATH.exists():
        try:
            with open(CONFIG_PATH, 'r') as f:
                config = json.load(f)
            console.print(f"[green]✓ Loaded trained config from {CONFIG_PATH.name}[/green]")
            return config, True
        except Exception as e:
            console.print(f"[yellow]Warning: Could not load config: {e}[/yellow]")

    # Default configuration (used before training)
    console.print("[yellow]Using default configuration (run train.py to optimize)[/yellow]")
    return {
        'bug_gate': {'activation': 'relu', 'metrics': {'specificity': 0.0, 'accuracy': 0.0}},
        'vulnerability_gate': {'activation': 'relu', 'metrics': {'specificity': 0.0, 'accuracy': 0.0}}
    }, False


class AdaptiveClassificationPipeline:
    """
    Multi-agent feedforward pipeline with adaptive architecture selection.

    Architecture:
        [NLP Feature Extraction] → [Classification Agents] → [Supervisor] → [Architecture Agent]
                                          ↑                       |
                                          └───── If accuracy < threshold, try next activation
    """

    ACTIVATIONS = ['relu', 'sigmoid']  # Available activation strategies

    def __init__(self, trained_config=None, target_threshold=0.85, verbose=False):
        # Create classifiers in silent mode for batch processing
        self.bug_classifier = BugGateClassifier(verbose=verbose)
        self.vuln_classifier = VulnerabilityGateClassifier(verbose=verbose)
        self.architecture_agent = ArchitectureAgent()
        self.target_threshold = target_threshold

        # Load trained optimal activations
        if trained_config:
            self.bug_activation = trained_config.get('bug_gate', {}).get('activation', 'relu')
            self.vuln_activation = trained_config.get('vulnerability_gate', {}).get('activation', 'relu')
        else:
            self.bug_activation = 'relu'
            self.vuln_activation = 'relu'

        # Track architecture decisions
        self.architecture_log = []

    def classify_file(self, bug_features, vuln_features):
        """
        Feedforward pass through the classification pipeline.
        Uses trained optimal activation functions.
        """
        # Bug Gate Classification
        bug_result = self.bug_classifier.classify(bug_features, activation=self.bug_activation)

        # Vulnerability Gate Classification
        vuln_result = self.vuln_classifier.classify(vuln_features, activation=self.vuln_activation)

        return bug_result, vuln_result

    def evaluate_and_adapt(self, predictions, ground_truth, gate_name):
        """
        Supervisor evaluates predictions. If accuracy < threshold,
        Architecture Agent selects a different activation.

        This is the iterative convergence loop.
        """
        supervisor = SupervisorAgent(gate_name)

        # Test all activations
        results = {}
        for activation in self.ACTIVATIONS:
            # Re-classify with this activation
            if gate_name == "Bug Gate":
                classifier = self.bug_classifier
            else:
                classifier = self.vuln_classifier

            # Get predictions with this activation
            preds = [classifier.classify(f, activation=activation) for f in predictions]

            # Evaluate
            metrics = supervisor.evaluate(preds, ground_truth)
            results[activation] = metrics

        # Architecture Agent selects best
        best_activation, _ = self.architecture_agent.select_best_activation(
            results, target_metric='specificity', threshold=self.target_threshold
        )

        self.architecture_log.append({
            'gate': gate_name,
            'selected': best_activation,
            'results': results
        })

        return best_activation, results


# Supported file extensions
SUPPORTED_EXTENSIONS = {
    '.py': 'Python',
    '.java': 'Java', 
    '.cs': 'C#',
    '.c': 'C',
    '.h': 'C Header',
    '.cpp': 'C++',
    '.ts': 'TypeScript',
    '.js': 'JavaScript',
    '.tsx': 'TypeScript React',
    '.jsx': 'JavaScript React',
}

def find_source_files(directory, exclude_patterns=None):
    """Find all source files in a directory recursively"""
    if exclude_patterns is None:
        exclude_patterns = [
            'venv', '__pycache__', '.git', 'node_modules', '.env',
            'migrations', 'dist', 'build', 'bin', 'obj', 'packages',
            '.idea', '.vs', '.vscode', 'target', '.gradle',
            '.obsidian',  # Obsidian plugins (third-party code)
            'vendor',     # Composer/Go vendor dependencies
            'publish/',   # .NET publish output
            'wwwroot/_content/',  # ASP.NET Core framework content
            '/plugins/',  # Plugin directories (often third-party)
        ]
    
    source_files = []
    directory = Path(directory)
    
    for ext in SUPPORTED_EXTENSIONS.keys():
        for filepath in directory.rglob(f'*{ext}'):
            # Skip excluded directories
            skip = False
            filepath_str = str(filepath)
            for pattern in exclude_patterns:
                if pattern in filepath_str:
                    skip = True
                    break
            if not skip:
                source_files.append(filepath)
    
    return sorted(source_files)

def analyze_file_silent(filepath, agent, pipeline, timeout_seconds=5):
    """
    Analyze a single file using the multi-agent pipeline.

    Flow:
        1. NLP Agent extracts features
        2. Classification Agents (Bug + Vuln) classify using trained activations
        3. Results returned for supervisor evaluation
    """
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            code_text = f.read()
    except Exception:
        return None

    # Extract features with timeout to prevent hanging
    try:
        with timeout(timeout_seconds):
            features = agent.extract_features(code_text, str(filepath))
    except TimeoutError:
        return None
    except Exception:
        return None

    # Calculate total vulnerability signals
    calculate_total_signals(features['vulnerability_features'])

    # Get features
    bug_features = features['bug_features']
    vuln_features = features['vulnerability_features']

    # Classification via multi-agent pipeline (using trained activations)
    bug_result, vuln_result = pipeline.classify_file(bug_features, vuln_features)

    overall = 'PASS' if (bug_result == 'PASS' and vuln_result == 'PASS') else 'FAIL'

    return {
        'filepath': str(filepath),
        'filename': filepath.name,
        'language': features['language'],
        'bug_gate': bug_result,
        'vulnerability_gate': vuln_result,
        'overall': overall,
        'bug_features': bug_features,
        'vulnerability_features': vuln_features,
        'activations_used': {
            'bug_gate': pipeline.bug_activation,
            'vulnerability_gate': pipeline.vuln_activation
        }
    }

def calculate_statistics(results):
    """Calculate statistics from batch analysis results"""
    total = len(results)
    if total == 0:
        return None
    
    # Overall stats
    passed = sum(1 for r in results if r['overall'] == 'PASS')
    failed = total - passed
    
    # Gate stats
    bug_passed = sum(1 for r in results if r['bug_gate'] == 'PASS')
    vuln_passed = sum(1 for r in results if r['vulnerability_gate'] == 'PASS')
    
    # By language
    by_language = defaultdict(lambda: {'total': 0, 'passed': 0, 'failed': 0})
    for r in results:
        lang = r['language']
        by_language[lang]['total'] += 1
        if r['overall'] == 'PASS':
            by_language[lang]['passed'] += 1
        else:
            by_language[lang]['failed'] += 1
    
    # Complexity stats
    complexities = [r['bug_features'].get('max_complexity', 0) for r in results]
    nestings = [r['bug_features'].get('max_nesting', 0) for r in results]
    
    # Vulnerability counts by type
    vuln_counts = defaultdict(int)
    for r in results:
        vf = r['vulnerability_features']
        for key, value in vf.items():
            if key != 'total_signals' and isinstance(value, (int, float)) and value > 0:
                vuln_counts[key] += 1
    
    return {
        'total_files': total,
        'overall_passed': passed,
        'overall_failed': failed,
        'overall_pass_rate': passed / total * 100,
        'bug_gate_passed': bug_passed,
        'bug_gate_failed': total - bug_passed,
        'bug_gate_pass_rate': bug_passed / total * 100,
        'vuln_gate_passed': vuln_passed,
        'vuln_gate_failed': total - vuln_passed,
        'vuln_gate_pass_rate': vuln_passed / total * 100,
        'by_language': dict(by_language),
        'complexity': {
            'avg': sum(complexities) / total if total > 0 else 0,
            'max': max(complexities) if complexities else 0,
            'min': min(complexities) if complexities else 0
        },
        'nesting': {
            'avg': sum(nestings) / total if total > 0 else 0,
            'max': max(nestings) if nestings else 0,
            'min': min(nestings) if nestings else 0
        },
        'vulnerability_counts': dict(vuln_counts)
    }

def get_relative_path(filepath, base_dir):
    """Get a shortened relative path for display"""
    try:
        rel = Path(filepath).relative_to(Path(base_dir).resolve())
        return str(rel)
    except ValueError:
        # If can't make relative, return last 2-3 parts of path
        parts = Path(filepath).parts
        if len(parts) > 3:
            return str(Path(*parts[-3:]))
        return str(Path(*parts[-2:])) if len(parts) > 1 else Path(filepath).name


def display_results(results, stats, base_dir=None):
    """Display batch analysis results"""
    if not stats:
        console.print("[red]No results to display[/red]")
        return
    
    console.print("\n" + "="*70)
    console.print("[bold cyan]MULTI-LANGUAGE ANALYSIS RESULTS[/bold cyan]")
    console.print("="*70 + "\n")
    
    # Summary Table
    summary_table = Table(title="Overall Summary", show_header=True, header_style="bold cyan")
    summary_table.add_column("Metric", style="cyan")
    summary_table.add_column("Value", justify="right")
    summary_table.add_column("Percentage", justify="right")
    
    summary_table.add_row("Total Files Analyzed", str(stats['total_files']), "-")
    
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
    
    # By Language Table
    lang_table = Table(title="\nResults by Language", show_header=True, header_style="bold magenta")
    lang_table.add_column("Language", style="magenta")
    lang_table.add_column("Total", justify="center")
    lang_table.add_column("Passed", justify="center")
    lang_table.add_column("Failed", justify="center")
    lang_table.add_column("Pass Rate", justify="right")
    
    for lang, data in sorted(stats['by_language'].items(), key=lambda x: x[1]['total'], reverse=True):
        rate = data['passed'] / data['total'] * 100 if data['total'] > 0 else 0
        rate_color = "green" if rate >= 80 else "yellow" if rate >= 60 else "red"
        lang_table.add_row(
            SUPPORTED_EXTENSIONS.get(f'.{lang}', lang.title()),
            str(data['total']),
            f"[green]{data['passed']}[/green]",
            f"[red]{data['failed']}[/red]",
            f"[{rate_color}]{rate:.1f}%[/{rate_color}]"
        )
    
    console.print(lang_table)
    
    # Gate Breakdown
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
    
    # Vulnerability Types
    if stats['vulnerability_counts']:
        vuln_table = Table(title="\nVulnerability Types Found", show_header=True, header_style="bold red")
        vuln_table.add_column("Vulnerability Type", style="red")
        vuln_table.add_column("Files Affected", justify="center")
        
        # Map technical names to friendly names
        vuln_names = {
            'sql_injection': 'SQL Injection',
            'eval_exec': 'Eval/Exec Usage',
            'hardcoded_secrets': 'Hardcoded Secrets',
            'command_injection': 'Command Injection',
            'buffer_overflow': 'Buffer Overflow Risk',
            'format_string': 'Format String Vuln',
            'memory_leak_risk': 'Memory Leak Risk',
            'xss_risk': 'XSS Risk',
            'prototype_pollution': 'Prototype Pollution',
            'unsafe_deserialization': 'Unsafe Deserialization',
            'xxe_vulnerability': 'XXE Vulnerability',
            'path_traversal': 'Path Traversal',
            'pickle_usage': 'Pickle Deserialization',
        }
        
        for vuln_type, count in sorted(stats['vulnerability_counts'].items(), key=lambda x: x[1], reverse=True):
            if count > 0:
                name = vuln_names.get(vuln_type, vuln_type.replace('_', ' ').title())
                vuln_table.add_row(name, str(count))
        
        console.print(vuln_table)
    
    # Top Issues
    failed_files = [r for r in results if r['overall'] == 'FAIL']
    if failed_files:
        console.print("\n[bold red]Top Files Requiring Attention:[/bold red]")
        issues_table = Table(show_header=True, header_style="bold")
        issues_table.add_column("File Path", style="cyan", max_width=70, overflow="ellipsis")
        issues_table.add_column("Lang", justify="center", width=4)
        issues_table.add_column("Bug", justify="center", width=4)
        issues_table.add_column("Vuln", justify="center", width=4)
        issues_table.add_column("Issues", style="yellow", max_width=20)

        for r in failed_files[:20]:
            issues = []
            bf = r['bug_features']
            vf = r['vulnerability_features']

            if bf.get('max_nesting', 0) > 4:
                issues.append(f"nest={bf['max_nesting']}")
            if bf.get('max_complexity', 0) > 15:
                issues.append(f"cx={bf['max_complexity']}")
            if vf.get('sql_injection', 0):
                issues.append("SQL")
            if vf.get('eval_exec', 0):
                issues.append("eval")
            if vf.get('hardcoded_secrets', 0):
                issues.append("secrets")
            if vf.get('command_injection', 0):
                issues.append("cmd_inj")
            if vf.get('buffer_overflow', 0):
                issues.append("buffer")
            if vf.get('xss_risk', 0):
                issues.append("XSS")

            bug_color = "green" if r['bug_gate'] == "PASS" else "red"
            vuln_color = "green" if r['vulnerability_gate'] == "PASS" else "red"

            # Show relative path instead of just filename
            display_path = get_relative_path(r['filepath'], base_dir) if base_dir else r['filename']

            issues_table.add_row(
                display_path,
                r['language'][:4],
                f"[{bug_color}]{r['bug_gate']}[/{bug_color}]",
                f"[{vuln_color}]{r['vulnerability_gate']}[/{vuln_color}]",
                ", ".join(issues) if issues else "-"
            )

        console.print(issues_table)

        if len(failed_files) > 20:
            console.print(f"[yellow]... and {len(failed_files) - 20} more files[/yellow]")

def display_pipeline_info(config, is_trained):
    """Display information about the classification pipeline"""
    console.print("\n[bold cyan]Multi-Agent Classification Pipeline[/bold cyan]")
    console.print("="*50)

    if is_trained:
        console.print("[green]✓ Using trained optimal configuration[/green]")
    else:
        console.print("[yellow]⚠ Using default configuration (run train.py first)[/yellow]")

    # Show architecture
    console.print("\n[bold]Pipeline Architecture:[/bold]")
    console.print("  [NLP Agent] → Feature Extraction")
    console.print("       ↓")
    console.print("  [Bug Classifier] → " +
                 f"[cyan]{config['bug_gate']['activation'].upper()}[/cyan] activation")
    console.print("  [Vuln Classifier] → " +
                 f"[cyan]{config['vulnerability_gate']['activation'].upper()}[/cyan] activation")
    console.print("       ↓")
    console.print("  [Supervisor] → Confusion Matrix Evaluation")

    if is_trained:
        bug_metrics = config['bug_gate'].get('metrics', {})
        vuln_metrics = config['vulnerability_gate'].get('metrics', {})
        console.print(f"\n[bold]Trained Metrics:[/bold]")
        console.print(f"  Bug Gate: Specificity={bug_metrics.get('specificity', 0):.2%}, "
                     f"Accuracy={bug_metrics.get('accuracy', 0):.2%}")
        console.print(f"  Vuln Gate: Specificity={vuln_metrics.get('specificity', 0):.2%}, "
                     f"Accuracy={vuln_metrics.get('accuracy', 0):.2%}")

    console.print("="*50 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description='Analyze ALL programming languages in a directory using multi-agent pipeline',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Supported Languages:
{chr(10).join(f'  {ext}: {name}' for ext, name in SUPPORTED_EXTENSIONS.items())}

Multi-Agent Architecture:
  1. NLP Agent - Extracts code features (complexity, vulnerabilities)
  2. Classification Agents - Classify using trained activation functions
  3. Supervisor Agent - Evaluates via confusion matrices
  4. Architecture Agent - Selects optimal activation strategy

Examples:
  python batch_analyze_all.py /path/to/project
  python batch_analyze_all.py . -o all_results.json
  python train.py  # Run first to train optimal activations
        """
    )
    parser.add_argument('directory', help='Directory to analyze')
    parser.add_argument('-o', '--output', help='Output JSON file for results')
    parser.add_argument('--show-pipeline', action='store_true',
                       help='Show detailed pipeline information')

    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        console.print(f"[red]Error: '{args.directory}' is not a valid directory[/red]")
        sys.exit(1)

    console.print(Panel.fit(
        "[bold green]Multi-Agent Code Quality Analyzer[/bold green]\n"
        "Adaptive Architecture with Trained Classifiers\n"
        f"Languages: Python, Java, C#, C/C++, TypeScript, JavaScript",
        border_style="green"
    ))

    # Load trained configuration
    trained_config, is_trained = load_trained_config()

    # Create classification pipeline
    pipeline = AdaptiveClassificationPipeline(trained_config)

    # Show pipeline info
    if args.show_pipeline or not is_trained:
        display_pipeline_info(trained_config, is_trained)
    
    # Find all source files
    console.print(f"\nScanning [cyan]{args.directory}[/cyan] for source files...")
    source_files = find_source_files(args.directory)
    
    if not source_files:
        console.print("[yellow]No source files found.[/yellow]")
        return
    
    # Count by language
    lang_counts = defaultdict(int)
    for f in source_files:
        ext = f.suffix.lower()
        lang_counts[SUPPORTED_EXTENSIONS.get(ext, ext)] += 1
    
    console.print(f"\n[green]Found {len(source_files)} source files:[/green]")
    for lang, count in sorted(lang_counts.items(), key=lambda x: x[1], reverse=True):
        console.print(f"  • {lang}: {count} files")
    
    # Initialize NLP feature extraction agent
    nlp_agent = MultiLanguageAgent()
    results = []

    # Analyze with progress bar
    console.print()
    skipped_large = 0
    skipped_timeout = 0
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TextColumn("({task.completed}/{task.total})"),
        console=console,
        refresh_per_second=10,
    ) as progress:
        task = progress.add_task("Analyzing files...", total=len(source_files))

        for filepath in source_files:
            # Update description to show current file
            progress.update(task, description=f"Analyzing: {filepath.name[:30]}")

            # Skip very large files to prevent hanging
            try:
                file_size = filepath.stat().st_size
                if file_size > 1_000_000:  # Skip files > 1MB
                    skipped_large += 1
                    progress.advance(task)
                    continue
            except OSError:
                progress.advance(task)
                continue

            # Run through multi-agent pipeline
            result = analyze_file_silent(filepath, nlp_agent, pipeline, timeout_seconds=5)
            if result:
                results.append(result)
            else:
                skipped_timeout += 1
            progress.advance(task)

    if skipped_large > 0:
        console.print(f"[yellow]Skipped {skipped_large} files larger than 1MB[/yellow]")
    if skipped_timeout > 0:
        console.print(f"[yellow]Skipped {skipped_timeout} files (timeout or error)[/yellow]")
    
    # Calculate statistics
    stats = calculate_statistics(results)

    # Display results (pass base directory for relative paths)
    display_results(results, stats, base_dir=args.directory)
    
    # Save results
    if args.output:
        output_data = {
            'timestamp': datetime.now().isoformat(),
            'directory': str(args.directory),
            'pipeline_config': {
                'trained': is_trained,
                'bug_gate_activation': pipeline.bug_activation,
                'vulnerability_gate_activation': pipeline.vuln_activation,
                'trained_metrics': trained_config if is_trained else None
            },
            'statistics': stats,
            'file_results': results
        }

        with open(args.output, 'w') as f:
            json.dump(output_data, f, indent=2)

        console.print(f"\n[green]Results saved to: {args.output}[/green]")

    # Show pipeline summary
    console.print(f"\n[bold cyan]Pipeline Summary:[/bold cyan]")
    console.print(f"  Bug Gate Activation: [cyan]{pipeline.bug_activation.upper()}[/cyan]")
    console.print(f"  Vulnerability Gate Activation: [cyan]{pipeline.vuln_activation.upper()}[/cyan]")
    if not is_trained:
        console.print(f"\n[yellow]Tip: Run 'python train.py' to optimize activation functions[/yellow]")

if __name__ == "__main__":
    main()
