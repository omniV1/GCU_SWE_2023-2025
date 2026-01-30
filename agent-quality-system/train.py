# train.py

import json
import os
from agents.nlp_agent import NLPAgent
from agents.classifiers import BugGateClassifier, VulnerabilityGateClassifier
from agents.supervisor import SupervisorAgent
from agents.architecture_agent import ArchitectureAgent
from rich.console import Console

console = Console()

def load_training_data():
    """Load all training samples and their labels"""
    training_dir = "data/training"
    labels_path = "data/labels.json"
    
    # Load labels
    with open(labels_path, 'r') as f:
        labels = json.load(f)
    
    # Load code files
    samples = []
    for filename in os.listdir(training_dir):
        if filename.endswith('.py'):
            filepath = os.path.join(training_dir, filename)
            with open(filepath, 'r') as f:
                code = f.read()
            
            if filename in labels:
                samples.append({
                    'filename': filename,
                    'code': code,
                    'labels': labels[filename]
                })
    
    console.print(f"[green]Loaded {len(samples)} training samples[/green]\n")
    return samples

def train_gate(gate_name, classifier, samples, feature_key, label_key):
    """Train a single quality gate by testing different activations"""
    console.print(f"\n{'='*60}")
    console.print(f"[bold cyan]Training {gate_name}[/bold cyan]")
    console.print(f"{'='*60}\n")
    
    # Initialize components
    nlp_agent = NLPAgent()
    supervisor = SupervisorAgent(gate_name)
    architecture_agent = ArchitectureAgent()
    
    # Extract features for all samples
    features_list = []
    ground_truth = []
    
    for sample in samples:
        features = nlp_agent.extract_features(sample['code'], sample['filename'])
        features_list.append(features[feature_key])
        ground_truth.append(sample['labels'][label_key])
    
    console.print(f"\nExtracted features from {len(features_list)} samples\n")
    
    # Test different activation functions
    activations = ['sigmoid', 'relu']
    results = {}
    
    for activation in activations:
        console.print(f"\n[yellow]Testing {activation.upper()} activation...[/yellow]")
        
        # Get predictions
        predictions = []
        for features in features_list:
            prediction = classifier.classify(features, activation=activation)
            predictions.append(prediction)
        
        # Evaluate
        metrics = supervisor.evaluate(predictions, ground_truth)
        supervisor.display_results(metrics, activation)
        
        results[activation] = metrics
    
    # Select best activation
    best_activation, all_results = architecture_agent.select_best_activation(
        results,
        target_metric='specificity',
        threshold=0.85
    )
    
    return best_activation, all_results

def main():
    """Main training function"""
    console.print("[bold green]Starting Multi-Agent Quality Gate Training[/bold green]\n")
    
    # Load data
    samples = load_training_data()
    
    if len(samples) < 5:
        console.print("[red]Error: Need at least 5 training samples[/red]")
        return
    
    # Train Bug Gate
    bug_classifier = BugGateClassifier()
    bug_best, bug_results = train_gate(
        "Bug Gate",
        bug_classifier,
        samples,
        'bug_features',
        'bug_gate'
    )
    
    # Train Vulnerability Gate
    vuln_classifier = VulnerabilityGateClassifier()
    vuln_best, vuln_results = train_gate(
        "Vulnerability Gate",
        vuln_classifier,
        samples,
        'vulnerability_features',
        'vulnerability_gate'
    )
    
    # Final Summary
    console.print(f"\n{'='*60}")
    console.print("[bold green]Training Complete - Optimal Configuration:[/bold green]")
    console.print(f"{'='*60}\n")
    
    console.print(f"Bug Gate: [bold]{bug_best.upper()}[/bold] activation")
    console.print(f"  └─ Specificity: {bug_results[bug_best]['specificity']:.2%}")
    console.print(f"  └─ Accuracy: {bug_results[bug_best]['accuracy']:.2%}\n")
    
    console.print(f"Vulnerability Gate: [bold]{vuln_best.upper()}[/bold] activation")
    console.print(f"  └─ Specificity: {vuln_results[vuln_best]['specificity']:.2%}")
    console.print(f"  └─ Accuracy: {vuln_results[vuln_best]['accuracy']:.2%}\n")
    
    # Save configuration
    config = {
        'bug_gate': {
            'activation': bug_best,
            'metrics': bug_results[bug_best]
        },
        'vulnerability_gate': {
            'activation': vuln_best,
            'metrics': vuln_results[vuln_best]
        }
    }
    
    with open('data/results/optimal_config.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    console.print("[green]Configuration saved to data/results/optimal_config.json[/green]")

if __name__ == "__main__":
    # Create results directory if it doesn't exist
    os.makedirs('data/results', exist_ok=True)
    main()
