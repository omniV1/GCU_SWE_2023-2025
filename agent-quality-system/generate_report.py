#!/usr/bin/env python3
# generate_report.py - Generate HTML reports for code quality analysis

import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path

from rich.console import Console

console = Console()

def load_optimal_config():
    """Load the trained optimal configuration"""
    config_path = os.path.join(os.path.dirname(__file__), 'data/results/optimal_config.json')
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def load_batch_results(results_file):
    """Load results from a batch analysis JSON file"""
    try:
        with open(results_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Code Quality Analysis Report</title>
    <style>
        :root {{
            --primary: #e94560;
            --secondary: #0f3460;
            --success: #00d9a5;
            --danger: #e94560;
            --bg-dark: #1a1a2e;
            --bg-card: #16213e;
            --text: #eaeaea;
            --text-muted: #a0a0a0;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, var(--bg-dark) 0%, #0f0f23 100%);
            color: var(--text);
            min-height: 100vh;
            padding: 2rem;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .header {{
            text-align: center;
            margin-bottom: 3rem;
            padding: 2rem;
            background: var(--bg-card);
            border-radius: 15px;
            border: 1px solid var(--secondary);
        }}
        .header h1 {{
            font-size: 2.5rem;
            background: linear-gradient(90deg, var(--primary), #ff6b9d);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }}
        .header .subtitle {{ color: var(--text-muted); font-size: 1.1rem; }}
        .header .timestamp {{ margin-top: 1rem; color: var(--text-muted); font-size: 0.9rem; }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }}
        .card {{
            background: var(--bg-card);
            border-radius: 12px;
            padding: 1.5rem;
            border: 1px solid var(--secondary);
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        .card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(233, 69, 96, 0.2);
        }}
        .card h3 {{
            color: var(--primary);
            margin-bottom: 1rem;
            font-size: 1.2rem;
        }}
        .stat-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
        }}
        .stat {{
            text-align: center;
            padding: 1rem;
            background: rgba(15, 52, 96, 0.5);
            border-radius: 8px;
        }}
        .stat-value {{
            font-size: 2rem;
            font-weight: bold;
            color: var(--primary);
        }}
        .stat-value.success {{ color: var(--success); }}
        .stat-value.danger {{ color: var(--danger); }}
        .stat-label {{
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-top: 0.3rem;
        }}
        .progress-bar {{
            height: 12px;
            background: var(--secondary);
            border-radius: 6px;
            overflow: hidden;
            margin-top: 0.5rem;
        }}
        .progress-fill {{
            height: 100%;
            border-radius: 6px;
        }}
        .progress-fill.success {{ background: linear-gradient(90deg, var(--success), #00ffcc); }}
        .progress-fill.warning {{ background: linear-gradient(90deg, #ffc107, #ffeb3b); }}
        .progress-fill.danger {{ background: linear-gradient(90deg, var(--danger), #ff6b9d); }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 1rem;
        }}
        th, td {{
            padding: 0.75rem 1rem;
            text-align: left;
            border-bottom: 1px solid var(--secondary);
        }}
        th {{
            background: var(--secondary);
            color: var(--primary);
            font-weight: 600;
        }}
        tr:hover {{ background: rgba(15, 52, 96, 0.3); }}
        .badge {{
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
        }}
        .badge-pass {{
            background: rgba(0, 217, 165, 0.2);
            color: var(--success);
        }}
        .badge-fail {{
            background: rgba(233, 69, 96, 0.2);
            color: var(--danger);
        }}
        .section {{ margin-bottom: 2rem; }}
        .section-title {{
            font-size: 1.5rem;
            color: var(--text);
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid var(--primary);
        }}
        .footer {{
            text-align: center;
            margin-top: 3rem;
            padding: 2rem;
            color: var(--text-muted);
            font-size: 0.9rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <h1>Code Quality Analysis Report</h1>
            <p class="subtitle">Multi-Agent Quality Gate System - GCU Coursework Analysis</p>
            <p class="timestamp">Generated: {timestamp}</p>
        </header>
        {content}
        <footer class="footer">
            <p>Generated by Multi-Agent Code Quality System</p>
            <p>Optimizing for Specificity with Deep Learning-Inspired Architecture</p>
        </footer>
    </div>
</body>
</html>
"""

def generate_overview_section(stats):
    pass_rate = stats['overall_pass_rate']
    pass_class = 'success' if pass_rate >= 80 else 'warning' if pass_rate >= 60 else 'danger'
    
    return f"""
    <section class="section">
        <h2 class="section-title">Overview</h2>
        <div class="grid">
            <div class="card">
                <h3>Files Analyzed</h3>
                <div class="stat-grid">
                    <div class="stat">
                        <div class="stat-value">{stats['total_files']}</div>
                        <div class="stat-label">Total Files</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value {pass_class}">{pass_rate:.1f}%</div>
                        <div class="stat-label">Pass Rate</div>
                    </div>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill {pass_class}" style="width: {pass_rate}%"></div>
                </div>
            </div>
            <div class="card">
                <h3>Quality Gates</h3>
                <div class="stat-grid">
                    <div class="stat">
                        <div class="stat-value success">{stats['overall_passed']}</div>
                        <div class="stat-label">Passed</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value danger">{stats['overall_failed']}</div>
                        <div class="stat-label">Failed</div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """

def generate_gates_section(stats):
    bug_rate = stats['bug_gate_pass_rate']
    vuln_rate = stats['vuln_gate_pass_rate']
    bug_class = 'success' if bug_rate >= 80 else 'warning' if bug_rate >= 60 else 'danger'
    vuln_class = 'success' if vuln_rate >= 80 else 'warning' if vuln_rate >= 60 else 'danger'
    
    return f"""
    <section class="section">
        <h2 class="section-title">Quality Gate Results</h2>
        <div class="grid">
            <div class="card">
                <h3>Bug Gate</h3>
                <div class="stat-grid">
                    <div class="stat">
                        <div class="stat-value success">{stats['bug_gate_passed']}</div>
                        <div class="stat-label">Passed</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value danger">{stats['bug_gate_failed']}</div>
                        <div class="stat-label">Failed</div>
                    </div>
                </div>
                <p style="margin-top: 1rem; color: var(--text-muted);">Pass Rate: <strong>{bug_rate:.1f}%</strong></p>
                <div class="progress-bar">
                    <div class="progress-fill {bug_class}" style="width: {bug_rate}%"></div>
                </div>
            </div>
            <div class="card">
                <h3>Vulnerability Gate</h3>
                <div class="stat-grid">
                    <div class="stat">
                        <div class="stat-value success">{stats['vuln_gate_passed']}</div>
                        <div class="stat-label">Passed</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value danger">{stats['vuln_gate_failed']}</div>
                        <div class="stat-label">Failed</div>
                    </div>
                </div>
                <p style="margin-top: 1rem; color: var(--text-muted);">Pass Rate: <strong>{vuln_rate:.1f}%</strong></p>
                <div class="progress-bar">
                    <div class="progress-fill {vuln_class}" style="width: {vuln_rate}%"></div>
                </div>
            </div>
        </div>
    </section>
    """

def generate_metrics_section(stats):
    return f"""
    <section class="section">
        <h2 class="section-title">Code Quality Metrics</h2>
        <div class="grid">
            <div class="card">
                <h3>Cyclomatic Complexity</h3>
                <div class="stat-grid">
                    <div class="stat">
                        <div class="stat-value">{stats['complexity']['avg']:.1f}</div>
                        <div class="stat-label">Average</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value">{stats['complexity']['max']}</div>
                        <div class="stat-label">Maximum</div>
                    </div>
                </div>
            </div>
            <div class="card">
                <h3>Nesting Depth</h3>
                <div class="stat-grid">
                    <div class="stat">
                        <div class="stat-value">{stats['nesting']['avg']:.1f}</div>
                        <div class="stat-label">Average</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value">{stats['nesting']['max']}</div>
                        <div class="stat-label">Maximum</div>
                    </div>
                </div>
            </div>
            <div class="card">
                <h3>Function Length</h3>
                <div class="stat-grid">
                    <div class="stat">
                        <div class="stat-value">{stats['function_length']['avg']:.0f}</div>
                        <div class="stat-label">Avg Lines</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value">{stats['function_length']['max']}</div>
                        <div class="stat-label">Max Lines</div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """

def generate_vulnerabilities_section(stats):
    vb = stats['vulnerability_breakdown']
    total_vulns = sum(vb.values())
    
    vuln_items = ""
    vuln_types = [
        ('SQL Injection', vb['sql_injection'], 'Use parameterized queries'),
        ('Eval/Exec Usage', vb['eval_exec'], 'Avoid dynamic code execution'),
        ('Hardcoded Secrets', vb['hardcoded_secrets'], 'Use environment variables'),
        ('Command Injection', vb['command_injection'], 'Avoid shell=True and os.system()'),
        ('Pickle Deserialize', vb['pickle_deserialization'], 'Use safer alternatives like JSON'),
    ]
    
    for name, count, fix in vuln_types:
        badge_class = 'badge-fail' if count > 0 else 'badge-pass'
        vuln_items += f"""
        <tr>
            <td>{name}</td>
            <td><span class="badge {badge_class}">{count} files</span></td>
            <td style="color: var(--text-muted);">{fix}</td>
        </tr>
        """
    
    return f"""
    <section class="section">
        <h2 class="section-title">Security Vulnerabilities</h2>
        <div class="card">
            <h3>Detected Vulnerability Types</h3>
            <table>
                <thead>
                    <tr>
                        <th>Vulnerability Type</th>
                        <th>Files Affected</th>
                        <th>Recommended Fix</th>
                    </tr>
                </thead>
                <tbody>
                    {vuln_items}
                </tbody>
            </table>
        </div>
    </section>
    """

def generate_files_section(results):
    rows = ""
    # Sort: failures first, then by filename
    for r in sorted(results, key=lambda x: (x['overall'] == 'PASS', x['filename']))[:50]:
        bug_badge = 'badge-pass' if r['bug_gate'] == 'PASS' else 'badge-fail'
        vuln_badge = 'badge-pass' if r['vulnerability_gate'] == 'PASS' else 'badge-fail'
        overall_badge = 'badge-pass' if r['overall'] == 'PASS' else 'badge-fail'
        
        rows += f"""
        <tr>
            <td style="font-family: monospace; max-width: 300px; overflow: hidden; text-overflow: ellipsis;">{r['filename']}</td>
            <td><span class="badge {bug_badge}">{r['bug_gate']}</span></td>
            <td><span class="badge {vuln_badge}">{r['vulnerability_gate']}</span></td>
            <td><span class="badge {overall_badge}">{r['overall']}</span></td>
        </tr>
        """
    
    return f"""
    <section class="section">
        <h2 class="section-title">File-by-File Results (Top 50)</h2>
        <div class="card">
            <table>
                <thead>
                    <tr>
                        <th>Filename</th>
                        <th>Bug Gate</th>
                        <th>Vulnerability Gate</th>
                        <th>Overall</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>
        </div>
    </section>
    """

def generate_report(batch_results_file=None, output_file='report.html'):
    """Generate the HTML report"""
    
    if batch_results_file:
        data = load_batch_results(batch_results_file)
        if not data:
            console.print(f"[red]Error: Could not load {batch_results_file}[/red]")
            return None
        stats = data['statistics']
        results = data['file_results']
    else:
        console.print("[red]Error: No input file provided[/red]")
        return None
    
    # Build content sections
    content = ""
    content += generate_overview_section(stats)
    content += generate_gates_section(stats)
    content += generate_metrics_section(stats)
    content += generate_vulnerabilities_section(stats)
    content += generate_files_section(results)
    
    # Generate final HTML
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html = HTML_TEMPLATE.format(timestamp=timestamp, content=content)
    
    # Save report
    os.makedirs(os.path.dirname(output_file) or '.', exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return output_file

def main():
    parser = argparse.ArgumentParser(description='Generate HTML report from code quality analysis')
    parser.add_argument('-i', '--input', required=True, help='Input JSON file from batch_analyze.py')
    parser.add_argument('-o', '--output', default='data/results/quality_report.html', help='Output HTML file')
    
    args = parser.parse_args()
    
    console.print("[bold green]Multi-Agent Code Quality - Report Generator[/bold green]\n")
    
    output_file = generate_report(args.input, args.output)
    
    if output_file:
        console.print(f"\n[bold green]Report generated: {output_file}[/bold green]")

if __name__ == "__main__":
    main()
