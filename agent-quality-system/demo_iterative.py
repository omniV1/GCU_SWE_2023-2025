#!/usr/bin/env python3
"""
Demo - Iterative Feedforward Pipeline with Confidence Scoring
Shows multiple passes until convergence.
"""

import os
import sys
from rich.console import Console
from rich.panel import Panel

from agents.enhanced_feature_extractor import EnhancedFeatureExtractor
from agents.iterative_pipeline import IterativeFeedforwardPipeline

console = Console()


def main():
    console.print(Panel.fit(
        "[bold cyan]Iterative Feedforward Pipeline Demo[/bold cyan]\n"
        "[dim]Multiple passes until convergence[/dim]",
        border_style="cyan"
    ))
    
    # Get target file
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = "demo_code.py"
        if not os.path.exists(target):
            # Create demo file with issues
            demo_code = '''
import os
import pickle

# Hardcoded secret
API_KEY = "sk_live_1234567890abcdef"

def complex_nested_function(data, config):
    """High complexity function"""
    if data:
        if config.get('enabled'):
            for item in data:
                for sub in item:
                    if sub.get('valid'):
                        # SQL injection
                        query = "SELECT * FROM users WHERE id = " + str(sub['id'])
                        # Command injection
                        os.system("process " + sub['name'])
                        # Insecure deserialization
                        result = pickle.loads(sub['data'])
                        eval(sub['expr'])
    return True
'''
            with open(target, 'w') as f:
                f.write(demo_code)
            console.print(f"[dim]Created demo file: {target}[/dim]\n")
    
    if not os.path.exists(target):
        console.print(f"[red]File not found: {target}[/red]")
        sys.exit(1)
    
    # Read file
    with open(target, 'r', encoding='utf-8', errors='ignore') as f:
        code = f.read()
    
    console.print(f"[yellow]Analyzing: {target}[/yellow]\n")
    
    # Extract features
    extractor = EnhancedFeatureExtractor(verbose=False)
    features = extractor.extract_all_features(code, target)
    
    # Show extracted features summary
    console.print("[cyan]Features Extracted:[/cyan]")
    console.print(f"  Complexity: {features['bug_features'].get('max_complexity', 0)}")
    console.print(f"  Nesting: {features['bug_features'].get('max_nesting', 0)}")
    console.print(f"  Vuln Signals: {features['vulnerability_features'].get('total_vulnerability_signals', 0)}")
    console.print()
    
    # Run iterative pipeline
    pipeline = IterativeFeedforwardPipeline(verbose=True)
    
    console.print("[yellow]Running iterative classification...[/yellow]\n")
    
    result = pipeline.classify_iterative(
        features['bug_features'],
        features['vulnerability_features'],
        features['project_features']
    )
    
    console.print()
    pipeline.display_result(result)


if __name__ == "__main__":
    main()
