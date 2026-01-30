# agents/supervisor.py

import numpy as np
from rich.console import Console
from rich.table import Table

console = Console()

class SupervisorAgent:
    """Evaluates classifier performance using confusion matrices"""
    
    def __init__(self, gate_name):
        self.gate_name = gate_name
        self.name = f"{gate_name} Supervisor Agent"
    
    def evaluate(self, predictions, ground_truth):
        """
        Build confusion matrix and calculate metrics
        
        Args:
            predictions (list): List of 'PASS' or 'FAIL' predictions
            ground_truth (list): List of actual 'PASS' or 'FAIL' labels
            
        Returns:
            dict: Metrics including confusion matrix, accuracy, specificity
        """
        if len(predictions) != len(ground_truth):
            raise ValueError("Predictions and ground truth must have same length")
        
        # Build confusion matrix
        tp = sum(1 for p, g in zip(predictions, ground_truth) if p == 'FAIL' and g == 'FAIL')
        fp = sum(1 for p, g in zip(predictions, ground_truth) if p == 'FAIL' and g == 'PASS')
        tn = sum(1 for p, g in zip(predictions, ground_truth) if p == 'PASS' and g == 'PASS')
        fn = sum(1 for p, g in zip(predictions, ground_truth) if p == 'PASS' and g == 'FAIL')
        
        total = len(predictions)
        
        # Calculate metrics
        accuracy = (tp + tn) / total if total > 0 else 0
        
        # Specificity = TN / (TN + FP) - optimizing for this as you specified
        specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
        
        # Sensitivity (recall) = TP / (TP + FN)
        sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0
        
        # Precision = TP / (TP + FP)
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        
        metrics = {
            'confusion_matrix': {
                'true_positive': tp,
                'false_positive': fp,
                'true_negative': tn,
                'false_negative': fn
            },
            'accuracy': round(accuracy, 4),
            'specificity': round(specificity, 4),  # Key metric for your system
            'sensitivity': round(sensitivity, 4),
            'precision': round(precision, 4),
            'total_samples': total
        }
        
        return metrics
    
    def display_results(self, metrics, activation_name):
        """Display confusion matrix and metrics in a nice table"""
        cm = metrics['confusion_matrix']
        
        console.print(f"\n[bold cyan]{self.gate_name} - {activation_name}[/bold cyan]")
        
        # Confusion Matrix Table
        table = Table(title="Confusion Matrix")
        table.add_column("", style="bold")
        table.add_column("Predicted PASS", justify="center")
        table.add_column("Predicted FAIL", justify="center")
        
        table.add_row(
            "Actual PASS",
            f"[green]{cm['true_negative']}[/green]",
            f"[red]{cm['false_positive']}[/red]"
        )
        table.add_row(
            "Actual FAIL",
            f"[red]{cm['false_negative']}[/red]",
            f"[green]{cm['true_positive']}[/green]"
        )
        
        console.print(table)
        
        # Metrics Table
        metrics_table = Table(title="Performance Metrics")
        metrics_table.add_column("Metric", style="cyan")
        metrics_table.add_column("Value", justify="right")
        
        metrics_table.add_row("Accuracy", f"{metrics['accuracy']:.2%}")
        metrics_table.add_row("[bold]Specificity (Target)[/bold]", f"[bold]{metrics['specificity']:.2%}[/bold]")
        metrics_table.add_row("Sensitivity", f"{metrics['sensitivity']:.2%}")
        metrics_table.add_row("Precision", f"{metrics['precision']:.2%}")
        
        console.print(metrics_table)
        
        return metrics
