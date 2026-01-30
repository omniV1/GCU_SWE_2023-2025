#!/usr/bin/env python3
"""
Multi-Agent Quality Gate System - Full Pipeline Demo

This script demonstrates the complete feedforward multi-agent architecture
for predicting SonarQube quality gate outcomes.

Architecture:
    [Code Input] → [NLP Agent] → [Classification Agents] → [Supervisor] → [Architecture Agent]
                                        ↓
                              [Confusion Matrix Evaluation]
                                        ↓
                              [Optimal Activation Selection]
"""

import json
import time
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import box

# Import our agents
from agents.multi_lang_agent import MultiLanguageAgent, calculate_total_signals
from agents.classifiers import BugGateClassifier, VulnerabilityGateClassifier
from agents.supervisor import SupervisorAgent
from agents.architecture_agent import ArchitectureAgent

console = Console()

# Sample code snippets for demonstration
DEMO_SAMPLES = {
    "clean_code": {
        "filename": "clean_example.py",
        "code": '''
def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_maximum(numbers):
    """Find the maximum value in a list."""
    if not numbers:
        return None
    return max(numbers)
''',
        "expected_bug": "PASS",
        "expected_vuln": "PASS"
    },
    "complex_code": {
        "filename": "complex_example.py",
        "code": '''
def process_data(data, config, options, flags, settings):
    result = []
    if data:
        if config:
            if options:
                for item in data:
                    if item.get('valid'):
                        if item.get('type') == 'A':
                            for sub in item.get('children', []):
                                if sub.get('active'):
                                    result.append(process_sub(sub, config, options))
    return result
''',
        "expected_bug": "FAIL",
        "expected_vuln": "PASS"
    },
    "vulnerable_code": {
        "filename": "vulnerable_example.py",
        "code": '''
import os

def get_user_data(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    password = "super_secret_password_12345"
    os.system("echo " + user_id)
    return eval(user_id)
''',
        "expected_bug": "PASS",
        "expected_vuln": "FAIL"
    }
}


def demo_step(step_num, title, description):
    """Display a demo step header"""
    console.print()
    console.print(Panel(
        f"[bold]{description}[/bold]",
        title=f"[cyan]Step {step_num}: {title}[/cyan]",
        border_style="cyan"
    ))
    time.sleep(0.5)


def demo_agent_output(agent_name, output):
    """Display agent output"""
    console.print(f"\n[yellow]>>> {agent_name} Output:[/yellow]")
    if isinstance(output, dict):
        for key, value in output.items():
            console.print(f"    {key}: {value}")
    else:
        console.print(f"    {output}")


def run_demo():
    """Run the complete multi-agent pipeline demo"""

    # Title
    console.print()
    console.print(Panel.fit(
        "[bold green]Multi-Agent Quality Gate System[/bold green]\n"
        "[dim]Feedforward Architecture with Adaptive Classification[/dim]\n\n"
        "This demo shows how multiple specialized agents work together\n"
        "to predict SonarQube quality gate outcomes.",
        border_style="green"
    ))
    console.print()
    time.sleep(1)

    # =========================================================================
    # PHASE 1: Initialize Agents
    # =========================================================================
    demo_step(1, "Agent Initialization",
              "Creating specialized agents for each task in the pipeline")

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        task = progress.add_task("Initializing agents...", total=5)

        nlp_agent = MultiLanguageAgent()
        progress.update(task, advance=1, description="NLP Feature Extraction Agent ✓")
        time.sleep(0.3)

        bug_classifier = BugGateClassifier(verbose=False)
        progress.update(task, advance=1, description="Bug Gate Classifier ✓")
        time.sleep(0.3)

        vuln_classifier = VulnerabilityGateClassifier(verbose=False)
        progress.update(task, advance=1, description="Vulnerability Gate Classifier ✓")
        time.sleep(0.3)

        bug_supervisor = SupervisorAgent("Bug Gate")
        vuln_supervisor = SupervisorAgent("Vulnerability Gate")
        progress.update(task, advance=1, description="Supervisor Agents ✓")
        time.sleep(0.3)

        arch_agent = ArchitectureAgent()
        progress.update(task, advance=1, description="Architecture Agent ✓")

    console.print("\n[green]✓ All 5 agents initialized[/green]")

    # =========================================================================
    # PHASE 2: Feature Extraction (NLP Agent)
    # =========================================================================
    demo_step(2, "NLP Feature Extraction",
              "The NLP Agent analyzes code and extracts features for classification")

    all_features = {}

    for name, sample in DEMO_SAMPLES.items():
        console.print(f"\n[cyan]Analyzing: {sample['filename']}[/cyan]")
        console.print(f"[dim]{sample['code'][:100]}...[/dim]")

        features = nlp_agent.extract_features(sample['code'], sample['filename'])
        calculate_total_signals(features['vulnerability_features'])
        all_features[name] = features

        # Show extracted features
        bug_f = features['bug_features']
        vuln_f = features['vulnerability_features']

        console.print(f"  [yellow]Bug Features:[/yellow]")
        console.print(f"    Complexity: {bug_f.get('max_complexity', 0)}")
        console.print(f"    Nesting Depth: {bug_f.get('max_nesting', 0)}")
        console.print(f"    Function Length: {bug_f.get('max_function_length', 0)}")

        console.print(f"  [yellow]Vulnerability Features:[/yellow]")
        console.print(f"    SQL Injection: {vuln_f.get('sql_injection', 0)}")
        console.print(f"    Eval/Exec: {vuln_f.get('eval_exec', 0)}")
        console.print(f"    Hardcoded Secrets: {vuln_f.get('hardcoded_secrets', 0)}")
        console.print(f"    Command Injection: {vuln_f.get('command_injection', 0)}")

        time.sleep(0.5)

    # =========================================================================
    # PHASE 3: Classification with Different Activations
    # =========================================================================
    demo_step(3, "Classification Agent Comparison",
              "Testing Sigmoid vs ReLU activation functions on each sample")

    activations = ['sigmoid', 'relu']
    results = {act: {'bug': [], 'vuln': []} for act in activations}
    ground_truth_bug = []
    ground_truth_vuln = []

    for name, sample in DEMO_SAMPLES.items():
        features = all_features[name]
        ground_truth_bug.append(sample['expected_bug'])
        ground_truth_vuln.append(sample['expected_vuln'])

        console.print(f"\n[cyan]{sample['filename']}[/cyan] (Expected: Bug={sample['expected_bug']}, Vuln={sample['expected_vuln']})")

        for activation in activations:
            # Bug classification
            bug_result = bug_classifier.classify(features['bug_features'], activation=activation)
            results[activation]['bug'].append(bug_result)

            # Vulnerability classification - map feature names
            vuln_features = {
                'total_vulnerability_signals': features['vulnerability_features'].get('total_signals', 0),
                'eval_usage': features['vulnerability_features'].get('eval_exec', 0),
                'sql_concat': features['vulnerability_features'].get('sql_injection', 0),
                'hardcoded_secrets': features['vulnerability_features'].get('hardcoded_secrets', 0),
            }
            vuln_result = vuln_classifier.classify(vuln_features, activation=activation)
            results[activation]['vuln'].append(vuln_result)

            bug_match = "✓" if bug_result == sample['expected_bug'] else "✗"
            vuln_match = "✓" if vuln_result == sample['expected_vuln'] else "✗"

            console.print(f"  [{activation.upper():7}] Bug: {bug_result} {bug_match}  Vuln: {vuln_result} {vuln_match}")

        time.sleep(0.3)

    # =========================================================================
    # PHASE 4: Supervisor Evaluation (Confusion Matrices)
    # =========================================================================
    demo_step(4, "Supervisor Agent Evaluation",
              "Building confusion matrices to evaluate each activation strategy")

    activation_metrics = {}

    for activation in activations:
        console.print(f"\n[yellow]Evaluating {activation.upper()} activation:[/yellow]")

        # Bug gate evaluation
        bug_metrics = bug_supervisor.evaluate(results[activation]['bug'], ground_truth_bug)
        vuln_metrics = vuln_supervisor.evaluate(results[activation]['vuln'], ground_truth_vuln)

        activation_metrics[activation] = {
            'bug': bug_metrics,
            'vuln': vuln_metrics
        }

        # Display confusion matrix
        bug_cm = bug_metrics['confusion_matrix']
        console.print(f"\n  [cyan]Bug Gate Confusion Matrix ({activation}):[/cyan]")
        console.print(f"    TP={bug_cm['true_positive']} FP={bug_cm['false_positive']} TN={bug_cm['true_negative']} FN={bug_cm['false_negative']}")
        console.print(f"    Accuracy: {bug_metrics['accuracy']:.1%}")
        console.print(f"    Specificity: {bug_metrics['specificity']:.1%}")
        console.print(f"    Sensitivity: {bug_metrics['sensitivity']:.1%}")

        vuln_cm = vuln_metrics['confusion_matrix']
        console.print(f"\n  [cyan]Vulnerability Gate Confusion Matrix ({activation}):[/cyan]")
        console.print(f"    TP={vuln_cm['true_positive']} FP={vuln_cm['false_positive']} TN={vuln_cm['true_negative']} FN={vuln_cm['false_negative']}")
        console.print(f"    Accuracy: {vuln_metrics['accuracy']:.1%}")
        console.print(f"    Specificity: {vuln_metrics['specificity']:.1%}")
        console.print(f"    Sensitivity: {vuln_metrics['sensitivity']:.1%}")

        time.sleep(0.5)

    # =========================================================================
    # PHASE 5: Architecture Agent Selection
    # =========================================================================
    demo_step(5, "Architecture Agent Selection",
              "Selecting optimal activation based on specificity optimization")

    console.print("\n[yellow]Architecture Agent analyzing results...[/yellow]")
    time.sleep(0.5)

    # Bug gate selection
    bug_results = {act: activation_metrics[act]['bug'] for act in activations}
    best_bug_activation, _ = arch_agent.select_best_activation(
        bug_results, target_metric='specificity', threshold=0.85
    )

    # Vuln gate selection
    vuln_results = {act: activation_metrics[act]['vuln'] for act in activations}
    best_vuln_activation, _ = arch_agent.select_best_activation(
        vuln_results, target_metric='specificity', threshold=0.85
    )

    console.print(f"\n[green]✓ Optimal Bug Gate Activation: {best_bug_activation.upper()}[/green]")
    console.print(f"[green]✓ Optimal Vulnerability Gate Activation: {best_vuln_activation.upper()}[/green]")

    # =========================================================================
    # PHASE 6: Final Results
    # =========================================================================
    demo_step(6, "Final Pipeline Results",
              "Summary of the multi-agent classification system")

    # Results table
    table = Table(title="Pipeline Performance Summary", box=box.ROUNDED)
    table.add_column("Quality Gate", style="cyan")
    table.add_column("Best Activation", style="green")
    table.add_column("Accuracy", justify="right")
    table.add_column("Specificity", justify="right")
    table.add_column("Sensitivity", justify="right")

    bug_m = activation_metrics[best_bug_activation]['bug']
    vuln_m = activation_metrics[best_vuln_activation]['vuln']

    table.add_row(
        "Bug Gate",
        best_bug_activation.upper(),
        f"{bug_m['accuracy']:.1%}",
        f"{bug_m['specificity']:.1%}",
        f"{bug_m['sensitivity']:.1%}"
    )
    table.add_row(
        "Vulnerability Gate",
        best_vuln_activation.upper(),
        f"{vuln_m['accuracy']:.1%}",
        f"{vuln_m['specificity']:.1%}",
        f"{vuln_m['sensitivity']:.1%}"
    )

    console.print()
    console.print(table)

    # Architecture diagram
    console.print()
    console.print(Panel(
        """[bold]Feedforward Multi-Agent Architecture[/bold]

[Code Input]
     ↓
[NLP Feature Extraction Agent]
     ↓
     ├──→ [Bug Gate Classifier] ──→ [Bug Supervisor]
     │         (ReLU/Sigmoid)           (Confusion Matrix)
     │                                        ↓
     └──→ [Vuln Gate Classifier] ─→ [Vuln Supervisor]
              (ReLU/Sigmoid)           (Confusion Matrix)
                                             ↓
                                   [Architecture Agent]
                                   (Selects Optimal Activation)
                                             ↓
                                      [Final Output]
""",
        title="[cyan]System Architecture[/cyan]",
        border_style="cyan"
    ))

    console.print("\n[bold green]Demo Complete![/bold green]")
    console.print("[dim]Run 'python train_with_sonarqube.py' to train on real SonarQube data[/dim]")


if __name__ == "__main__":
    run_demo()
