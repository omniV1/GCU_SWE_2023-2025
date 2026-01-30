# agents/architecture_agent.py

from rich.console import Console

console = Console()

class ArchitectureAgent:
    """Selects optimal activation function based on specificity"""
    
    def __init__(self):
        self.name = "Architecture Selection Agent"
    
    def select_best_activation(self, results_dict, target_metric='specificity', threshold=0.90):
        """
        Select best activation function based on target metric
        
        Args:
            results_dict (dict): {activation_name: metrics_dict}
            target_metric (str): Metric to optimize ('specificity', 'accuracy', etc.)
            threshold (float): Minimum acceptable value for target metric
            
        Returns:
            tuple: (best_activation, all_results_with_status)
        """
        console.print(f"\n[bold yellow][Architecture Agent][/bold yellow] Evaluating activation functions...")
        console.print(f"Target metric: [bold]{target_metric}[/bold]")
        console.print(f"Threshold: [bold]{threshold:.2%}[/bold]\n")
        
        # Find best activation based on target metric, with accuracy as tiebreaker
        best_activation = None
        best_score = -1
        best_accuracy = -1
        
        for activation, metrics in results_dict.items():
            score = metrics.get(target_metric, 0)
            accuracy = metrics.get('accuracy', 0)
            
            # Check if meets threshold
            meets_threshold = score >= threshold
            status = "✓ MEETS THRESHOLD" if meets_threshold else "✗ BELOW THRESHOLD"
            
            console.print(f"{activation.upper():12} | {target_metric}: {score:.2%} | accuracy: {accuracy:.2%} | {status}")
            
            # Use accuracy as tiebreaker when target metrics are equal
            if score > best_score or (score == best_score and accuracy > best_accuracy):
                best_score = score
                best_accuracy = accuracy
                best_activation = activation
        
        # Final selection
        console.print(f"\n[bold green]Selected: {best_activation.upper()}[/bold green] "
                     f"({target_metric}: {best_score:.2%}, accuracy: {best_accuracy:.2%})")
        
        if best_score < threshold:
            console.print(f"[bold red]⚠ WARNING: Best score {best_score:.2%} is below threshold {threshold:.2%}[/bold red]")
        
        return best_activation, results_dict
