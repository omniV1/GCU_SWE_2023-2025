# demo.py

import json
from agents.nlp_agent import NLPAgent
from agents.classifiers import BugGateClassifier, VulnerabilityGateClassifier
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def load_optimal_config():
    """Load the trained optimal configuration"""
    try:
        with open('data/results/optimal_config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        console.print("[red]Error: No trained configuration found. Run train.py first.[/red]")
        exit(1)

def analyze_code(code_text, filename, config):
    """Analyze code using optimal configuration"""
    
    console.print(Panel.fit(
        f"[bold cyan]Analyzing: {filename}[/bold cyan]",
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
            console.print("  • Reduce function complexity and nesting depth")
        if vuln_result == "FAIL":
            console.print("  • Fix security vulnerabilities before committing")
    
    return {
        'bug_gate': bug_result,
        'vulnerability_gate': vuln_result,
        'overall': overall
    }

def main():
    """Main demo function"""
    console.print("[bold green]Multi-Agent Code Quality Analysis Demo[/bold green]\n")
    
    # Load configuration
    console.print("Loading trained configuration...")
    config = load_optimal_config()
    console.print("[green]✓ Configuration loaded[/green]\n")
    
    # Example: Analyze a new code file
    test_code = """
def process_user_data(user_id, action, params):
    # This function has multiple issues
    if user_id is not None:
        if action == 'update':
            if params.get('force'):
                if params.get('cascade'):
                    for table in get_tables():
                        for column in table.columns:
                            for row in table.rows:
                                if row.needs_update:
                                    # SQL injection vulnerability
                                    query = "UPDATE " + table.name + " SET value = " + params['value']
                                    execute(query)
    
    # Hardcoded credentials
    api_key = "sk_live_1234567890abcdef"
    
    return True
"""
    
    result = analyze_code(test_code, "new_code.py", config)

if __name__ == "__main__":
    main()
