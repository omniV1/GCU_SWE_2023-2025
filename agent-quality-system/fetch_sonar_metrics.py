#!/usr/bin/env python3
"""
Fetch comprehensive SonarQube metrics for all scanned projects.
Exports data for training the multi-agent quality gate system.
"""

import json
import requests
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# SonarQube configuration
SONAR_URL = "http://localhost:9000"
SONAR_USER = "admin"
SONAR_PASS = "S&o2015.20222"

# All metrics we want to fetch
METRICS = [
    "bugs",
    "vulnerabilities", 
    "security_hotspots",
    "code_smells",
    "reliability_rating",
    "security_rating",
    "sqale_rating",  # Maintainability rating
    "coverage",
    "duplicated_lines_density",
    "ncloc",  # Lines of code
    "cognitive_complexity",
    "sqale_debt_ratio",  # Technical debt ratio
]

# Rating conversion (SonarQube uses 1-5, we convert to letter grades)
RATING_MAP = {
    "1.0": "A",
    "2.0": "B", 
    "3.0": "C",
    "4.0": "D",
    "5.0": "E"
}


def get_projects():
    """Get all projects from SonarQube"""
    try:
        response = requests.get(
            f"{SONAR_URL}/api/components/search",
            params={"qualifiers": "TRK"},
            auth=(SONAR_USER, SONAR_PASS),
            timeout=10
        )
        if response.status_code == 200:
            return response.json().get("components", [])
    except Exception as e:
        console.print(f"[red]Error fetching projects: {e}[/red]")
    return []


def get_project_metrics(project_key):
    """Get all metrics for a project"""
    try:
        response = requests.get(
            f"{SONAR_URL}/api/measures/component",
            params={
                "component": project_key,
                "metricKeys": ",".join(METRICS)
            },
            auth=(SONAR_USER, SONAR_PASS),
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            measures = data.get("component", {}).get("measures", [])
            return {m["metric"]: m.get("value", "N/A") for m in measures}
    except Exception as e:
        console.print(f"[red]Error fetching metrics for {project_key}: {e}[/red]")
    return {}


def get_quality_gate_status(project_key):
    """Get quality gate status for a project"""
    try:
        response = requests.get(
            f"{SONAR_URL}/api/qualitygates/project_status",
            params={"projectKey": project_key},
            auth=(SONAR_USER, SONAR_PASS),
            timeout=10
        )
        if response.status_code == 200:
            return response.json().get("projectStatus", {})
    except Exception as e:
        console.print(f"[red]Error fetching quality gate: {e}[/red]")
    return {}


def determine_gate_statuses(metrics, qg_status):
    """Determine PASS/FAIL for each quality gate based on metrics"""
    gates = {}
    
    # Bug Gate: FAIL if bugs > 0
    bugs = int(float(metrics.get("bugs", 0)))
    gates["bug_gate"] = "FAIL" if bugs > 0 else "PASS"
    
    # Vulnerability Gate: FAIL if vulnerabilities > 0
    vulns = int(float(metrics.get("vulnerabilities", 0)))
    gates["vulnerability_gate"] = "FAIL" if vulns > 0 else "PASS"
    
    # Security Hotspot Gate: FAIL if security_hotspots > 0
    hotspots = int(float(metrics.get("security_hotspots", 0)))
    gates["security_hotspot_gate"] = "FAIL" if hotspots > 0 else "PASS"
    
    # Reliability Gate: FAIL if rating is D or E (4.0 or 5.0)
    reliability = float(metrics.get("reliability_rating", 1.0))
    gates["reliability_gate"] = "FAIL" if reliability >= 4.0 else "PASS"
    
    # Security Gate: FAIL if rating is D or E
    security = float(metrics.get("security_rating", 1.0))
    gates["security_gate"] = "FAIL" if security >= 4.0 else "PASS"
    
    # Maintainability Gate: FAIL if rating is D or E
    maintainability = float(metrics.get("sqale_rating", 1.0))
    gates["maintainability_gate"] = "FAIL" if maintainability >= 4.0 else "PASS"
    
    # Coverage Gate: FAIL if coverage < 80%
    coverage = float(metrics.get("coverage", 0))
    gates["coverage_gate"] = "FAIL" if coverage < 80.0 else "PASS"
    
    # Duplication Gate: FAIL if duplication > 3%
    duplication = float(metrics.get("duplicated_lines_density", 0))
    gates["duplication_gate"] = "FAIL" if duplication > 3.0 else "PASS"
    
    # Overall: SonarQube's quality gate status
    gates["sonarqube_overall"] = qg_status.get("status", "UNKNOWN")
    
    return gates


def display_results(results):
    """Display results in a nice table"""
    console.print(Panel.fit(
        "[bold cyan]SonarQube Comprehensive Metrics[/bold cyan]\n"
        "[dim]All 9 Quality Gates[/dim]",
        border_style="cyan"
    ))
    
    # Summary table
    table = Table(title="Project Quality Gate Summary")
    table.add_column("Project", style="cyan")
    table.add_column("Bugs", justify="center")
    table.add_column("Vulns", justify="center")
    table.add_column("Hotspots", justify="center")
    table.add_column("Smells", justify="center")
    table.add_column("Rel", justify="center")
    table.add_column("Sec", justify="center")
    table.add_column("Maint", justify="center")
    table.add_column("Cov%", justify="center")
    table.add_column("Dup%", justify="center")
    
    for r in results:
        m = r["metrics"]
        g = r["gates"]
        
        # Color code ratings
        rel_rating = RATING_MAP.get(m.get("reliability_rating", "1.0"), "?")
        sec_rating = RATING_MAP.get(m.get("security_rating", "1.0"), "?")
        maint_rating = RATING_MAP.get(m.get("sqale_rating", "1.0"), "?")
        
        rel_color = "green" if rel_rating in ["A", "B"] else "yellow" if rel_rating == "C" else "red"
        sec_color = "green" if sec_rating in ["A", "B"] else "yellow" if sec_rating == "C" else "red"
        maint_color = "green" if maint_rating in ["A", "B"] else "yellow" if maint_rating == "C" else "red"
        
        bugs = m.get("bugs", "0")
        vulns = m.get("vulnerabilities", "0")
        hotspots = m.get("security_hotspots", "0")
        smells = m.get("code_smells", "0")
        cov = m.get("coverage", "0")
        dup = m.get("duplicated_lines_density", "0")
        
        bug_color = "green" if bugs == "0" else "red"
        vuln_color = "green" if vulns == "0" else "red"
        hotspot_color = "green" if hotspots == "0" else "yellow"
        
        table.add_row(
            r["project"][:25],
            f"[{bug_color}]{bugs}[/{bug_color}]",
            f"[{vuln_color}]{vulns}[/{vuln_color}]",
            f"[{hotspot_color}]{hotspots}[/{hotspot_color}]",
            smells,
            f"[{rel_color}]{rel_rating}[/{rel_color}]",
            f"[{sec_color}]{sec_rating}[/{sec_color}]",
            f"[{maint_color}]{maint_rating}[/{maint_color}]",
            f"{float(cov):.1f}",
            f"{float(dup):.1f}"
        )
    
    console.print(table)
    
    # Gate breakdown
    console.print("\n[bold]Quality Gate Breakdown:[/bold]")
    gate_names = [
        ("bug_gate", "Bug Gate"),
        ("vulnerability_gate", "Vulnerability Gate"),
        ("security_hotspot_gate", "Security Hotspot Gate"),
        ("reliability_gate", "Reliability Gate"),
        ("security_gate", "Security Gate"),
        ("maintainability_gate", "Maintainability Gate"),
        ("coverage_gate", "Coverage Gate (≥80%)"),
        ("duplication_gate", "Duplication Gate (≤3%)"),
    ]
    
    gate_table = Table(title="Gate Pass Rates")
    gate_table.add_column("Quality Gate", style="cyan")
    gate_table.add_column("Passed", justify="center")
    gate_table.add_column("Failed", justify="center")
    gate_table.add_column("Pass Rate", justify="center")
    
    for gate_key, gate_name in gate_names:
        passed = sum(1 for r in results if r["gates"].get(gate_key) == "PASS")
        failed = len(results) - passed
        rate = passed / len(results) * 100 if results else 0
        
        rate_color = "green" if rate >= 80 else "yellow" if rate >= 50 else "red"
        gate_table.add_row(
            gate_name,
            f"[green]{passed}[/green]",
            f"[red]{failed}[/red]",
            f"[{rate_color}]{rate:.1f}%[/{rate_color}]"
        )
    
    console.print(gate_table)


def main():
    console.print("[bold green]Fetching SonarQube Comprehensive Metrics[/bold green]\n")
    
    # Get all projects
    projects = get_projects()
    if not projects:
        console.print("[red]No projects found in SonarQube![/red]")
        console.print("Make sure SonarQube is running and has scanned projects.")
        return
    
    console.print(f"Found {len(projects)} projects\n")
    
    results = []
    for project in projects:
        project_key = project["key"]
        console.print(f"Fetching metrics for: {project_key}...", end=" ")
        
        metrics = get_project_metrics(project_key)
        qg_status = get_quality_gate_status(project_key)
        gates = determine_gate_statuses(metrics, qg_status)
        
        results.append({
            "project": project_key,
            "metrics": metrics,
            "gates": gates,
            "quality_gate_status": qg_status
        })
        
        console.print("[green]done[/green]")
    
    # Display results
    display_results(results)
    
    # Save comprehensive results
    output_data = {
        "source": "SonarQube",
        "projects": results,
        "gate_definitions": {
            "bug_gate": "FAIL if bugs > 0",
            "vulnerability_gate": "FAIL if vulnerabilities > 0",
            "security_hotspot_gate": "FAIL if security_hotspots > 0",
            "reliability_gate": "FAIL if reliability_rating >= D",
            "security_gate": "FAIL if security_rating >= D",
            "maintainability_gate": "FAIL if sqale_rating >= D",
            "coverage_gate": "FAIL if coverage < 80%",
            "duplication_gate": "FAIL if duplicated_lines_density > 3%"
        }
    }
    
    output_path = Path("data/results/sonar_comprehensive_metrics.json")
    with open(output_path, "w") as f:
        json.dump(output_data, f, indent=2)
    
    console.print(f"\n[green]Results saved to: {output_path}[/green]")
    
    # Create training labels with all gates
    labels = {}
    for r in results:
        labels[r["project"]] = r["gates"]
    
    labels_path = Path("data/results/sonar_all_gates_labels.json")
    with open(labels_path, "w") as f:
        json.dump(labels, f, indent=2)
    
    console.print(f"[green]Training labels saved to: {labels_path}[/green]")


if __name__ == "__main__":
    main()
