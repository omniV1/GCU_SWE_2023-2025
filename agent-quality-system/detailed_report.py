#!/usr/bin/env python3
# detailed_report.py - Enhanced analytics and detailed reporting for code quality analysis

import json
import argparse
from pathlib import Path
from collections import defaultdict
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.tree import Tree

console = Console()

# Severity levels and recommendations
VULNERABILITY_INFO = {
    'sql_injection': {
        'severity': 'CRITICAL',
        'name': 'SQL Injection',
        'description': 'User input directly concatenated into SQL queries',
        'recommendation': 'Use parameterized queries or prepared statements',
        'example_fix': "cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))",
        'cwe': 'CWE-89',
        'owasp': 'A03:2021 Injection'
    },
    'eval_exec': {
        'severity': 'CRITICAL',
        'name': 'Eval/Exec Usage',
        'description': 'Dynamic code execution that can run arbitrary code',
        'recommendation': 'Use ast.literal_eval() for data parsing, or refactor to avoid dynamic execution',
        'example_fix': "Use ast.literal_eval(data) instead of eval(data)",
        'cwe': 'CWE-95',
        'owasp': 'A03:2021 Injection'
    },
    'command_injection': {
        'severity': 'CRITICAL',
        'name': 'Command Injection',
        'description': 'Shell commands executed with user-controlled input',
        'recommendation': 'Use subprocess with shell=False and pass args as list',
        'example_fix': "subprocess.run(['ls', '-la', directory], shell=False)",
        'cwe': 'CWE-78',
        'owasp': 'A03:2021 Injection'
    },
    'hardcoded_secrets': {
        'severity': 'HIGH',
        'name': 'Hardcoded Secrets',
        'description': 'Passwords, API keys, or tokens stored in source code',
        'recommendation': 'Use environment variables or a secrets manager',
        'example_fix': "api_key = os.environ.get('API_KEY')",
        'cwe': 'CWE-798',
        'owasp': 'A07:2021 Auth Failures'
    },
    'xss_risk': {
        'severity': 'HIGH',
        'name': 'XSS Risk',
        'description': 'Unsafe HTML injection via innerHTML or dangerouslySetInnerHTML',
        'recommendation': 'Sanitize input or use safe DOM methods like textContent',
        'example_fix': "element.textContent = userInput  // instead of innerHTML",
        'cwe': 'CWE-79',
        'owasp': 'A03:2021 Injection'
    },
    'buffer_overflow': {
        'severity': 'CRITICAL',
        'name': 'Buffer Overflow Risk',
        'description': 'Use of unsafe C functions like strcpy, gets, sprintf',
        'recommendation': 'Use safe alternatives: strncpy, fgets, snprintf',
        'example_fix': "strncpy(dest, src, sizeof(dest) - 1)",
        'cwe': 'CWE-120',
        'owasp': 'A06:2021 Vuln Components'
    },
    'prototype_pollution': {
        'severity': 'HIGH',
        'name': 'Prototype Pollution',
        'description': 'Manipulation of __proto__ or constructor.prototype',
        'recommendation': 'Validate object keys and use Object.create(null) for maps',
        'example_fix': "const safeMap = Object.create(null)",
        'cwe': 'CWE-1321',
        'owasp': 'A03:2021 Injection'
    },
    'unsafe_deserialization': {
        'severity': 'CRITICAL',
        'name': 'Unsafe Deserialization',
        'description': 'Deserializing untrusted data can lead to code execution',
        'recommendation': 'Validate and sanitize serialized data, use safe formats like JSON',
        'example_fix': "Use JSON.parse() instead of eval() or pickle",
        'cwe': 'CWE-502',
        'owasp': 'A08:2021 Integrity Failures'
    },
    'pickle_usage': {
        'severity': 'HIGH',
        'name': 'Pickle Deserialization',
        'description': 'pickle.load can execute arbitrary code from untrusted sources',
        'recommendation': 'Use JSON or implement custom serialization for untrusted data',
        'example_fix': "data = json.loads(json_string)",
        'cwe': 'CWE-502',
        'owasp': 'A08:2021 Integrity Failures'
    },
    'path_traversal': {
        'severity': 'HIGH',
        'name': 'Path Traversal',
        'description': 'File paths constructed with user input without validation',
        'recommendation': 'Validate paths and use os.path.realpath to resolve',
        'example_fix': "safe_path = os.path.realpath(os.path.join(base_dir, filename))",
        'cwe': 'CWE-22',
        'owasp': 'A01:2021 Broken Access'
    },
    'xxe_vulnerability': {
        'severity': 'HIGH',
        'name': 'XXE Vulnerability',
        'description': 'XML parser configured to process external entities',
        'recommendation': 'Disable external entity processing in XML parser',
        'example_fix': "parser.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true)",
        'cwe': 'CWE-611',
        'owasp': 'A05:2021 Misconfig'
    },
    'format_string': {
        'severity': 'MEDIUM',
        'name': 'Format String Vulnerability',
        'description': 'printf-style function called with user-controlled format string',
        'recommendation': 'Always use a format string literal',
        'example_fix': 'printf("%s", user_input)  // instead of printf(user_input)',
        'cwe': 'CWE-134',
        'owasp': 'A03:2021 Injection'
    },
    'memory_leak_risk': {
        'severity': 'MEDIUM',
        'name': 'Memory Leak Risk',
        'description': 'More malloc calls than free calls detected',
        'recommendation': 'Ensure all allocated memory is freed, consider RAII pattern',
        'example_fix': "Use smart pointers in C++ or ensure matching free() calls",
        'cwe': 'CWE-401',
        'owasp': 'N/A'
    }
}

BUG_INFO = {
    'high_complexity': {
        'severity': 'MEDIUM',
        'name': 'High Cyclomatic Complexity',
        'description': 'Function has too many decision paths',
        'recommendation': 'Break down into smaller functions, use early returns, extract complex conditions',
        'threshold': 15,
        'impact': 'Hard to test, maintain, and understand. Increases bug probability.'
    },
    'deep_nesting': {
        'severity': 'MEDIUM',
        'name': 'Deep Nesting',
        'description': 'Code has too many nested levels',
        'recommendation': 'Use guard clauses, extract methods, or flatten logic with early returns',
        'threshold': 4,
        'impact': 'Reduces readability, makes code flow hard to follow.'
    },
    'long_function': {
        'severity': 'LOW',
        'name': 'Long Function',
        'description': 'Function exceeds recommended line count',
        'recommendation': 'Split into smaller, focused functions with single responsibility',
        'threshold': 100,
        'impact': 'Violates single responsibility principle, hard to maintain.'
    }
}


def load_results(filepath):
    """Load analysis results from JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)


def get_severity_color(severity):
    """Get color for severity level"""
    colors = {
        'CRITICAL': 'red bold',
        'HIGH': 'red',
        'MEDIUM': 'yellow',
        'LOW': 'cyan'
    }
    return colors.get(severity, 'white')


def get_severity_emoji(severity):
    """Get emoji for severity level"""
    emojis = {
        'CRITICAL': '🔴',
        'HIGH': '🟠',
        'MEDIUM': '🟡',
        'LOW': '🟢'
    }
    return emojis.get(severity, '⚪')


def analyze_vulnerabilities(results):
    """Group and analyze vulnerability findings"""
    vuln_by_type = defaultdict(list)

    for result in results['file_results']:
        vf = result.get('vulnerability_features', {})
        filepath = result.get('filepath', 'unknown')
        filename = result.get('filename', Path(filepath).name)

        for vuln_key, info in VULNERABILITY_INFO.items():
            count = vf.get(vuln_key, 0)
            if count > 0:
                vuln_by_type[vuln_key].append({
                    'filepath': filepath,
                    'filename': filename,
                    'count': count,
                    'language': result.get('language', 'unknown')
                })

    return vuln_by_type


def analyze_bugs(results):
    """Group and analyze bug/complexity findings"""
    bug_by_type = defaultdict(list)

    for result in results['file_results']:
        bf = result.get('bug_features', {})
        filepath = result.get('filepath', 'unknown')
        filename = result.get('filename', Path(filepath).name)

        # Check complexity
        max_complexity = bf.get('max_complexity', 0)
        if max_complexity > BUG_INFO['high_complexity']['threshold']:
            bug_by_type['high_complexity'].append({
                'filepath': filepath,
                'filename': filename,
                'value': max_complexity,
                'language': result.get('language', 'unknown')
            })

        # Check nesting
        max_nesting = bf.get('max_nesting', 0)
        if max_nesting > BUG_INFO['deep_nesting']['threshold']:
            bug_by_type['deep_nesting'].append({
                'filepath': filepath,
                'filename': filename,
                'value': max_nesting,
                'language': result.get('language', 'unknown')
            })

        # Check function length (if available)
        max_length = bf.get('max_function_length', 0)
        if max_length > BUG_INFO['long_function']['threshold']:
            bug_by_type['long_function'].append({
                'filepath': filepath,
                'filename': filename,
                'value': max_length,
                'language': result.get('language', 'unknown')
            })

    return bug_by_type


def display_executive_summary(results, vuln_by_type, bug_by_type):
    """Display executive summary"""
    stats = results.get('statistics', {})

    # Count critical issues
    critical_count = sum(
        len(files) for vuln_key, files in vuln_by_type.items()
        if VULNERABILITY_INFO.get(vuln_key, {}).get('severity') == 'CRITICAL'
    )
    high_count = sum(
        len(files) for vuln_key, files in vuln_by_type.items()
        if VULNERABILITY_INFO.get(vuln_key, {}).get('severity') == 'HIGH'
    )

    console.print(Panel.fit(
        f"""[bold white]EXECUTIVE SUMMARY[/bold white]

[cyan]Files Analyzed:[/cyan] {stats.get('total_files', 0)}
[green]Pass Rate:[/green] {stats.get('overall_pass_rate', 0):.1f}%

[bold red]🔴 Critical Issues:[/bold red] {critical_count} files
[bold yellow]🟠 High Severity:[/bold yellow] {high_count} files
[bold cyan]🟡 Code Quality:[/bold cyan] {sum(len(f) for f in bug_by_type.values())} files

[dim]Security issues should be fixed before deployment.[/dim]""",
        title="📊 Analysis Report",
        border_style="cyan"
    ))


def display_vulnerability_report(vuln_by_type):
    """Display detailed vulnerability report"""
    console.print("\n")
    console.print(Panel.fit(
        "[bold red]SECURITY VULNERABILITY DETAILS[/bold red]",
        border_style="red"
    ))

    if not vuln_by_type:
        console.print("[green]✓ No security vulnerabilities detected![/green]")
        return

    # Sort by severity
    severity_order = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
    sorted_vulns = sorted(
        vuln_by_type.items(),
        key=lambda x: severity_order.get(VULNERABILITY_INFO.get(x[0], {}).get('severity', 'LOW'), 3)
    )

    for vuln_key, files in sorted_vulns:
        info = VULNERABILITY_INFO.get(vuln_key, {})
        severity = info.get('severity', 'UNKNOWN')
        color = get_severity_color(severity)
        emoji = get_severity_emoji(severity)

        # Create detailed panel for this vulnerability
        tree = Tree(f"{emoji} [{color}]{info.get('name', vuln_key)}[/{color}] [{color}][{severity}][/{color}]")

        # Description branch
        desc_branch = tree.add("[dim]Description[/dim]")
        desc_branch.add(f"{info.get('description', 'No description')}")

        # Standards branch
        if info.get('cwe') or info.get('owasp'):
            standards = tree.add("[dim]Security Standards[/dim]")
            if info.get('cwe'):
                standards.add(f"CWE: {info.get('cwe')}")
            if info.get('owasp'):
                standards.add(f"OWASP: {info.get('owasp')}")

        # Affected files branch
        files_branch = tree.add(f"[yellow]Affected Files ({len(files)})[/yellow]")

        # Group by language
        by_lang = defaultdict(list)
        for f in files:
            by_lang[f['language']].append(f)

        for lang, lang_files in sorted(by_lang.items(), key=lambda x: len(x[1]), reverse=True):
            lang_branch = files_branch.add(f"[cyan]{lang.title()}[/cyan] ({len(lang_files)} files)")
            for f in sorted(lang_files, key=lambda x: x['count'], reverse=True)[:5]:
                occurrence_text = f"{f['count']} occurrence{'s' if f['count'] > 1 else ''}"
                lang_branch.add(f"[white]{f['filename']}[/white] [dim]({occurrence_text})[/dim]")
            if len(lang_files) > 5:
                lang_branch.add(f"[dim]... and {len(lang_files) - 5} more[/dim]")

        # Recommendation branch
        rec_branch = tree.add("[green]How to Fix[/green]")
        rec_branch.add(f"[italic]{info.get('recommendation', 'N/A')}[/italic]")

        if info.get('example_fix'):
            example_branch = rec_branch.add("[cyan]Example[/cyan]")
            example_branch.add(f"[white]{info.get('example_fix')}[/white]")

        console.print(tree)
        console.print()


def display_bug_report(bug_by_type):
    """Display detailed bug/complexity report"""
    console.print("\n")
    console.print(Panel.fit(
        "[bold yellow]CODE QUALITY DETAILS[/bold yellow]",
        border_style="yellow"
    ))

    if not bug_by_type:
        console.print("[green]✓ No code quality issues detected![/green]")
        return

    for bug_key, files in bug_by_type.items():
        info = BUG_INFO.get(bug_key, {})
        severity = info.get('severity', 'UNKNOWN')
        color = get_severity_color(severity)
        emoji = get_severity_emoji(severity)

        tree = Tree(f"{emoji} [{color}]{info.get('name', bug_key)}[/{color}] [{color}][{severity}][/{color}]")

        # Description
        desc_branch = tree.add("[dim]Description[/dim]")
        desc_branch.add(f"{info.get('description')} (threshold: {info.get('threshold')})")

        # Impact
        if info.get('impact'):
            impact_branch = tree.add("[dim]Impact[/dim]")
            impact_branch.add(f"{info.get('impact')}")

        # Worst offenders with values
        files_branch = tree.add(f"[yellow]Worst Offenders ({len(files)} files)[/yellow]")

        # Group by language
        by_lang = defaultdict(list)
        for f in files:
            by_lang[f['language']].append(f)

        for lang, lang_files in sorted(by_lang.items(), key=lambda x: len(x[1]), reverse=True):
            lang_branch = files_branch.add(f"[cyan]{lang.title()}[/cyan] ({len(lang_files)} files)")
            for f in sorted(lang_files, key=lambda x: x['value'], reverse=True)[:5]:
                severity_indicator = "🔴" if f['value'] > info.get('threshold', 0) * 2 else "🟡"
                lang_branch.add(f"{severity_indicator} [white]{f['filename']}[/white] [dim](value: {f['value']}, threshold: {info.get('threshold')})[/dim]")
            if len(lang_files) > 5:
                lang_branch.add(f"[dim]... and {len(lang_files) - 5} more[/dim]")

        # Recommendation
        rec_branch = tree.add("[green]How to Fix[/green]")
        rec_branch.add(f"[italic]{info.get('recommendation', 'N/A')}[/italic]")

        console.print(tree)
        console.print()


def display_priority_action_items(vuln_by_type, bug_by_type):
    """Display prioritized action items"""
    console.print("\n")
    console.print(Panel.fit(
        "[bold magenta]PRIORITY ACTION ITEMS[/bold magenta]",
        border_style="magenta"
    ))

    action_items = []

    # Critical vulnerabilities first
    for vuln_key, files in vuln_by_type.items():
        info = VULNERABILITY_INFO.get(vuln_key, {})
        if info.get('severity') == 'CRITICAL':
            action_items.append({
                'priority': 1,
                'severity': 'CRITICAL',
                'type': 'Security',
                'issue': info.get('name', vuln_key),
                'count': len(files),
                'action': info.get('recommendation', 'Fix immediately'),
                'cwe': info.get('cwe', 'N/A')
            })

    # High severity vulnerabilities
    for vuln_key, files in vuln_by_type.items():
        info = VULNERABILITY_INFO.get(vuln_key, {})
        if info.get('severity') == 'HIGH':
            action_items.append({
                'priority': 2,
                'severity': 'HIGH',
                'type': 'Security',
                'issue': info.get('name', vuln_key),
                'count': len(files),
                'action': info.get('recommendation', 'Fix soon'),
                'cwe': info.get('cwe', 'N/A')
            })

    # Medium vulnerabilities
    for vuln_key, files in vuln_by_type.items():
        info = VULNERABILITY_INFO.get(vuln_key, {})
        if info.get('severity') == 'MEDIUM':
            action_items.append({
                'priority': 3,
                'severity': 'MEDIUM',
                'type': 'Security',
                'issue': info.get('name', vuln_key),
                'count': len(files),
                'action': info.get('recommendation', 'Address when possible'),
                'cwe': info.get('cwe', 'N/A')
            })

    # Bug issues
    for bug_key, files in bug_by_type.items():
        info = BUG_INFO.get(bug_key, {})
        action_items.append({
            'priority': 4,
            'severity': info.get('severity', 'MEDIUM'),
            'type': 'Quality',
            'issue': info.get('name', bug_key),
            'count': len(files),
            'action': info.get('recommendation', 'Refactor when possible'),
            'cwe': 'N/A'
        })

    # Sort by priority
    action_items.sort(key=lambda x: x['priority'])

    # Display table
    table = Table(title="Prioritized Action Items", show_header=True, header_style="bold")
    table.add_column("#", style="dim", width=3)
    table.add_column("Sev", justify="center", width=8)
    table.add_column("Type", width=8)
    table.add_column("Issue", width=22)
    table.add_column("Files", justify="right", width=5)
    table.add_column("CWE", width=8)
    table.add_column("Action", width=35)

    for i, item in enumerate(action_items, 1):
        severity_color = get_severity_color(item['severity'])
        emoji = get_severity_emoji(item['severity'])
        table.add_row(
            str(i),
            f"{emoji} [{severity_color}]{item['severity'][:4]}[/{severity_color}]",
            item['type'],
            item['issue'],
            str(item['count']),
            item['cwe'],
            item['action'][:35]
        )

    console.print(table)

    # Summary counts
    console.print(f"\n[bold]Summary:[/bold]")
    console.print(f"  🔴 Critical: {sum(1 for i in action_items if i['severity'] == 'CRITICAL')} issues")
    console.print(f"  🟠 High: {sum(1 for i in action_items if i['severity'] == 'HIGH')} issues")
    console.print(f"  🟡 Medium: {sum(1 for i in action_items if i['severity'] == 'MEDIUM')} issues")
    console.print(f"  🟢 Low: {sum(1 for i in action_items if i['severity'] == 'LOW')} issues")


def display_language_breakdown(results):
    """Display issues by language with health scores"""
    console.print("\n")
    console.print(Panel.fit(
        "[bold cyan]LANGUAGE HEALTH REPORT[/bold cyan]",
        border_style="cyan"
    ))

    lang_stats = defaultdict(lambda: {
        'total': 0,
        'bug_fails': 0,
        'vuln_fails': 0,
        'critical_vulns': 0,
        'high_vulns': 0
    })

    for result in results['file_results']:
        lang = result.get('language', 'unknown')
        lang_stats[lang]['total'] += 1

        if result.get('bug_gate') == 'FAIL':
            lang_stats[lang]['bug_fails'] += 1

        if result.get('vulnerability_gate') == 'FAIL':
            lang_stats[lang]['vuln_fails'] += 1

            # Count critical and high vulnerabilities
            vf = result.get('vulnerability_features', {})
            for vuln_key in ['sql_injection', 'eval_exec', 'command_injection', 'buffer_overflow', 'unsafe_deserialization']:
                if vf.get(vuln_key, 0) > 0:
                    lang_stats[lang]['critical_vulns'] += 1
                    break
            for vuln_key in ['hardcoded_secrets', 'xss_risk', 'prototype_pollution', 'pickle_usage', 'path_traversal', 'xxe_vulnerability']:
                if vf.get(vuln_key, 0) > 0:
                    lang_stats[lang]['high_vulns'] += 1
                    break

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Language", width=12)
    table.add_column("Files", justify="right", width=6)
    table.add_column("Bug Issues", justify="right", width=10)
    table.add_column("Vuln Issues", justify="right", width=11)
    table.add_column("Critical", justify="right", width=8)
    table.add_column("High", justify="right", width=6)
    table.add_column("Health", justify="right", width=8)
    table.add_column("Grade", justify="center", width=5)

    for lang, stats in sorted(lang_stats.items(), key=lambda x: x[1]['total'], reverse=True):
        total = stats['total']
        bug_pct = (total - stats['bug_fails']) / total * 100 if total > 0 else 100
        vuln_pct = (total - stats['vuln_fails']) / total * 100 if total > 0 else 100
        health = (bug_pct + vuln_pct) / 2

        # Deduct for critical/high issues
        health -= stats['critical_vulns'] * 5
        health -= stats['high_vulns'] * 2
        health = max(0, health)

        health_color = "green" if health >= 80 else "yellow" if health >= 60 else "red"
        crit_color = "red bold" if stats['critical_vulns'] > 0 else "green"
        high_color = "red" if stats['high_vulns'] > 0 else "green"

        # Letter grade
        if health >= 90:
            grade = "[green bold]A[/green bold]"
        elif health >= 80:
            grade = "[green]B[/green]"
        elif health >= 70:
            grade = "[yellow]C[/yellow]"
        elif health >= 60:
            grade = "[yellow]D[/yellow]"
        else:
            grade = "[red]F[/red]"

        table.add_row(
            lang.title(),
            str(total),
            f"[yellow]{stats['bug_fails']}[/yellow] ({100-bug_pct:.0f}%)",
            f"[red]{stats['vuln_fails']}[/red] ({100-vuln_pct:.0f}%)",
            f"[{crit_color}]{stats['critical_vulns']}[/{crit_color}]",
            f"[{high_color}]{stats['high_vulns']}[/{high_color}]",
            f"[{health_color}]{health:.0f}%[/{health_color}]",
            grade
        )

    console.print(table)

    console.print("\n[dim]Health Score = (Bug Pass Rate + Vuln Pass Rate) / 2 - (Critical×5) - (High×2)[/dim]")


def generate_markdown_report(results, vuln_by_type, bug_by_type, output_path):
    """Generate a detailed markdown report"""
    stats = results.get('statistics', {})

    md = []
    md.append("# Code Quality Analysis Report\n")
    md.append(f"**Generated:** {results.get('timestamp', 'Unknown')}")
    md.append(f"**Directory:** `{results.get('directory', 'Unknown')}`")
    md.append("")

    # Executive Summary
    md.append("## Executive Summary\n")
    md.append(f"| Metric | Value |")
    md.append(f"|--------|-------|")
    md.append(f"| Total Files Analyzed | {stats.get('total_files', 0)} |")
    md.append(f"| Overall Pass Rate | {stats.get('overall_pass_rate', 0):.1f}% |")
    md.append(f"| Bug Gate Pass Rate | {stats.get('bug_gate_pass_rate', 0):.1f}% |")
    md.append(f"| Vulnerability Gate Pass Rate | {stats.get('vuln_gate_pass_rate', 0):.1f}% |")
    md.append("")

    # Critical Findings
    md.append("## 🔴 Critical Security Findings\n")
    critical_found = False
    for vuln_key, files in vuln_by_type.items():
        info = VULNERABILITY_INFO.get(vuln_key, {})
        if info.get('severity') == 'CRITICAL':
            critical_found = True
            md.append(f"### {info.get('name', vuln_key)}\n")
            md.append(f"- **Severity:** CRITICAL")
            md.append(f"- **Files Affected:** {len(files)}")
            md.append(f"- **CWE:** {info.get('cwe', 'N/A')}")
            md.append(f"- **OWASP:** {info.get('owasp', 'N/A')}")
            md.append(f"- **Description:** {info.get('description', 'N/A')}")
            md.append(f"- **Recommendation:** {info.get('recommendation', 'N/A')}")
            md.append(f"- **Example Fix:** `{info.get('example_fix', 'N/A')}`")
            md.append("")
            md.append("**Affected Files:**")
            for f in files[:15]:
                md.append(f"- `{f['filepath']}` ({f['count']} occurrences)")
            if len(files) > 15:
                md.append(f"- *... and {len(files) - 15} more files*")
            md.append("")

    if not critical_found:
        md.append("✅ No critical security vulnerabilities found.\n")

    # High Severity Findings
    md.append("## 🟠 High Severity Findings\n")
    high_found = False
    for vuln_key, files in vuln_by_type.items():
        info = VULNERABILITY_INFO.get(vuln_key, {})
        if info.get('severity') == 'HIGH':
            high_found = True
            md.append(f"### {info.get('name', vuln_key)}\n")
            md.append(f"- **Files Affected:** {len(files)}")
            md.append(f"- **CWE:** {info.get('cwe', 'N/A')}")
            md.append(f"- **Recommendation:** {info.get('recommendation', 'N/A')}")
            md.append("")

    if not high_found:
        md.append("✅ No high severity vulnerabilities found.\n")

    # Code Quality Issues
    md.append("## 🟡 Code Quality Issues\n")
    if bug_by_type:
        for bug_key, files in bug_by_type.items():
            info = BUG_INFO.get(bug_key, {})
            md.append(f"### {info.get('name', bug_key)}\n")
            md.append(f"- **Files Affected:** {len(files)}")
            md.append(f"- **Threshold:** {info.get('threshold', 'N/A')}")
            md.append(f"- **Impact:** {info.get('impact', 'N/A')}")
            md.append(f"- **Recommendation:** {info.get('recommendation', 'N/A')}")
            md.append("")
    else:
        md.append("✅ No code quality issues found.\n")

    # Language Breakdown
    md.append("## Language Breakdown\n")
    lang_stats = stats.get('by_language', {})
    if lang_stats:
        md.append("| Language | Total | Passed | Failed | Pass Rate |")
        md.append("|----------|-------|--------|--------|-----------|")
        for lang, data in sorted(lang_stats.items(), key=lambda x: x[1].get('total', 0), reverse=True):
            total = data.get('total', 0)
            passed = data.get('passed', 0)
            failed = data.get('failed', 0)
            rate = passed / total * 100 if total > 0 else 0
            md.append(f"| {lang.title()} | {total} | {passed} | {failed} | {rate:.1f}% |")
    md.append("")

    # Write to file
    with open(output_path, 'w') as f:
        f.write('\n'.join(md))

    console.print(f"\n[green]✓ Markdown report saved to: {output_path}[/green]")


def main():
    parser = argparse.ArgumentParser(
        description='Generate detailed analytics from code quality analysis',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python detailed_report.py data/results/all_languages_analysis.json
  python detailed_report.py results.json --section vulns
  python detailed_report.py results.json --markdown report.md
        """
    )
    parser.add_argument('results_file', help='Path to JSON results file from batch_analyze_all.py')
    parser.add_argument('--markdown', '-m', help='Generate markdown report to this path')
    parser.add_argument('--section', '-s',
                       choices=['summary', 'vulns', 'bugs', 'priority', 'language', 'all'],
                       default='all', help='Which section to display')

    args = parser.parse_args()

    # Load results
    console.print(f"\n[bold cyan]Loading results from:[/bold cyan] {args.results_file}")
    results = load_results(args.results_file)
    console.print(f"[green]✓ Loaded {len(results.get('file_results', []))} file results[/green]\n")

    # Analyze
    vuln_by_type = analyze_vulnerabilities(results)
    bug_by_type = analyze_bugs(results)

    # Display requested sections
    if args.section in ['summary', 'all']:
        display_executive_summary(results, vuln_by_type, bug_by_type)

    if args.section in ['vulns', 'all']:
        display_vulnerability_report(vuln_by_type)

    if args.section in ['bugs', 'all']:
        display_bug_report(bug_by_type)

    if args.section in ['priority', 'all']:
        display_priority_action_items(vuln_by_type, bug_by_type)

    if args.section in ['language', 'all']:
        display_language_breakdown(results)

    # Generate markdown if requested
    if args.markdown:
        generate_markdown_report(results, vuln_by_type, bug_by_type, args.markdown)


if __name__ == "__main__":
    main()
