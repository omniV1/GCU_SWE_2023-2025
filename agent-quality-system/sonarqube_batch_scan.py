#!/usr/bin/env python3
"""
SonarQube Batch Scanner - Automated scanning of multiple repositories
Exports results for training the multi-agent quality gate system.

Usage:
    python sonarqube_batch_scan.py /path/to/repos --output sonar_results.json

Requirements:
    - Docker installed and running
    - sonar-scanner CLI (will be installed via Docker if not present)
"""

import os
import sys
import json
import time
import argparse
import subprocess
import requests
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# SonarQube Docker configuration
SONAR_IMAGE = "sonarqube:community"
SONAR_CONTAINER = "sonar-batch-scanner"
SONAR_PORT = 9000
SONAR_URL = f"http://localhost:{SONAR_PORT}"
SONAR_USER = "admin"
SONAR_PASS = "admin"  # Default password, will be changed on first run

# Scanner Docker image
SCANNER_IMAGE = "sonarsource/sonar-scanner-cli:latest"

# Supported project types
PROJECT_MARKERS = {
    'java': ['pom.xml', 'build.gradle', 'build.gradle.kts', '*.java'],
    'python': ['setup.py', 'pyproject.toml', 'requirements.txt', '*.py'],
    'javascript': ['package.json', '*.js', '*.ts'],
    'csharp': ['*.csproj', '*.sln', '*.cs'],
    'c': ['Makefile', 'CMakeLists.txt', '*.c', '*.h'],
}


def run_command(cmd, capture=True, check=True, timeout=300):
    """Run a shell command and return output"""
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=capture,
            text=True, check=check, timeout=timeout
        )
        return result.stdout.strip() if capture else None
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {cmd}")
        print(f"Error: {e.stderr}")
        return None
    except subprocess.TimeoutExpired:
        print(f"Command timed out: {cmd}")
        return None


def is_docker_running():
    """Check if Docker daemon is running"""
    result = run_command("docker info", check=False)
    return result is not None


def start_sonarqube():
    """Start SonarQube container"""
    print("\n[1/5] Starting SonarQube...")

    # Check if container already exists
    existing = run_command(f"docker ps -a --filter name={SONAR_CONTAINER} --format '{{{{.Names}}}}'", check=False)

    if existing and SONAR_CONTAINER in existing:
        # Check if running
        running = run_command(f"docker ps --filter name={SONAR_CONTAINER} --format '{{{{.Names}}}}'", check=False)
        if running and SONAR_CONTAINER in running:
            print(f"  ✓ SonarQube already running")
            return True
        else:
            print(f"  → Starting existing container...")
            run_command(f"docker start {SONAR_CONTAINER}", check=False)
    else:
        print(f"  → Creating new SonarQube container...")
        # Create with increased memory for Java analysis
        cmd = f"""docker run -d --name {SONAR_CONTAINER} \
            -p {SONAR_PORT}:{SONAR_PORT} \
            -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true \
            {SONAR_IMAGE}"""
        run_command(cmd, check=False)

    return True


def wait_for_sonarqube(timeout=180):
    """Wait for SonarQube to be ready"""
    print("\n[2/5] Waiting for SonarQube to start...")
    print(f"      (This may take 1-2 minutes on first run)")

    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(f"{SONAR_URL}/api/system/status", timeout=5)
            if response.status_code == 200:
                status = response.json().get('status')
                if status == 'UP':
                    print(f"  ✓ SonarQube is ready!")
                    return True
                else:
                    print(f"  ... Status: {status}")
        except requests.exceptions.RequestException:
            pass

        elapsed = int(time.time() - start_time)
        print(f"  ... Waiting ({elapsed}s)", end='\r')
        time.sleep(5)

    print(f"\n  ✗ Timeout waiting for SonarQube")
    return False


def get_sonar_token():
    """Get or create a SonarQube user token"""
    # Try to create a token
    try:
        response = requests.post(
            f"{SONAR_URL}/api/user_tokens/generate",
            auth=(SONAR_USER, SONAR_PASS),
            data={'name': f'batch-scanner-{int(time.time())}'},
            timeout=10
        )
        if response.status_code == 200:
            return response.json().get('token')
    except Exception as e:
        print(f"  Warning: Could not create token: {e}")

    return None


def detect_project_language(project_dir):
    """Detect primary language of a project"""
    project_path = Path(project_dir)

    # Count files by extension
    ext_counts = defaultdict(int)
    for ext in ['.py', '.java', '.cs', '.js', '.ts', '.c', '.cpp', '.h']:
        ext_counts[ext] = len(list(project_path.rglob(f'*{ext}')))

    # Determine primary language
    if ext_counts['.java'] > 0:
        return 'java'
    elif ext_counts['.cs'] > 0:
        return 'cs'
    elif ext_counts['.py'] > 0:
        return 'python'
    elif ext_counts['.ts'] > 0 or ext_counts['.js'] > 0:
        return 'js'
    elif ext_counts['.c'] > 0 or ext_counts['.cpp'] > 0:
        return 'c'

    return 'unknown'


def create_sonar_properties(project_dir, project_key, language):
    """Create sonar-project.properties file"""
    props_path = Path(project_dir) / 'sonar-project.properties'

    # Language-specific source patterns
    sources = '.'
    exclusions = '**/node_modules/**,**/vendor/**,**/.git/**,**/bin/**,**/obj/**,**/target/**,**/__pycache__/**,**/venv/**'

    props_content = f"""sonar.projectKey={project_key}
sonar.projectName={project_key}
sonar.sources={sources}
sonar.exclusions={exclusions}
sonar.sourceEncoding=UTF-8
"""

    # Add language-specific settings
    if language == 'python':
        props_content += "sonar.python.version=3\n"
    elif language == 'java':
        props_content += "sonar.java.binaries=.\n"

    with open(props_path, 'w') as f:
        f.write(props_content)

    return props_path


def scan_project(project_dir, project_key, token):
    """Run SonarQube scanner on a project"""
    project_path = Path(project_dir).resolve()

    # Use Docker-based scanner for portability
    cmd = f"""docker run --rm \
        --network=host \
        -v "{project_path}:/usr/src" \
        {SCANNER_IMAGE} \
        -Dsonar.host.url={SONAR_URL} \
        -Dsonar.token={token} \
        -Dsonar.projectKey={project_key} \
        -Dsonar.sources=/usr/src \
        -Dsonar.exclusions="**/node_modules/**,**/vendor/**,**/.git/**,**/bin/**,**/obj/**,**/target/**,**/__pycache__/**,**/venv/**" \
        2>&1"""

    result = run_command(cmd, check=False, timeout=120)
    return result is not None and "EXECUTION SUCCESS" in (result or "")


def wait_for_analysis(project_key, timeout=60):
    """Wait for analysis to complete on server"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(
                f"{SONAR_URL}/api/ce/component",
                params={'component': project_key},
                auth=(SONAR_USER, SONAR_PASS),
                timeout=10
            )
            if response.status_code == 200:
                data = response.json()
                current = data.get('current', {})
                status = current.get('status', 'PENDING')
                if status == 'SUCCESS':
                    return True
                elif status in ['FAILED', 'CANCELED']:
                    return False
        except Exception:
            pass
        time.sleep(2)
    return False


def get_project_issues(project_key):
    """Get all issues for a project"""
    issues = []
    page = 1
    page_size = 500

    while True:
        try:
            response = requests.get(
                f"{SONAR_URL}/api/issues/search",
                params={
                    'componentKeys': project_key,
                    'ps': page_size,
                    'p': page,
                    'resolved': 'false'
                },
                auth=(SONAR_USER, SONAR_PASS),
                timeout=30
            )

            if response.status_code != 200:
                break

            data = response.json()
            issues.extend(data.get('issues', []))

            total = data.get('total', 0)
            if page * page_size >= total:
                break
            page += 1

        except Exception as e:
            print(f"  Warning: Could not fetch issues: {e}")
            break

    return issues


def get_quality_gate_status(project_key):
    """Get quality gate status for a project"""
    try:
        response = requests.get(
            f"{SONAR_URL}/api/qualitygates/project_status",
            params={'projectKey': project_key},
            auth=(SONAR_USER, SONAR_PASS),
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()
            return data.get('projectStatus', {})
    except Exception as e:
        print(f"  Warning: Could not get quality gate: {e}")

    return {}


def categorize_issues(issues):
    """Categorize issues into bug and vulnerability types"""
    bug_issues = []
    vuln_issues = []
    code_smells = []

    for issue in issues:
        issue_type = issue.get('type', 'CODE_SMELL')
        if issue_type == 'BUG':
            bug_issues.append(issue)
        elif issue_type == 'VULNERABILITY':
            vuln_issues.append(issue)
        else:
            code_smells.append(issue)

    return {
        'bugs': bug_issues,
        'vulnerabilities': vuln_issues,
        'code_smells': code_smells
    }


def determine_gate_status(categorized_issues, qg_status):
    """Determine PASS/FAIL for bug and vulnerability gates"""
    # Use SonarQube's quality gate if available
    qg_result = qg_status.get('status', 'OK')

    # Bug gate: FAIL if any bugs
    bug_gate = 'FAIL' if len(categorized_issues['bugs']) > 0 else 'PASS'

    # Vulnerability gate: FAIL if any vulnerabilities
    vuln_gate = 'FAIL' if len(categorized_issues['vulnerabilities']) > 0 else 'PASS'

    return {
        'sonarqube_status': qg_result,
        'bug_gate': bug_gate,
        'vulnerability_gate': vuln_gate,
        'overall': 'FAIL' if (bug_gate == 'FAIL' or vuln_gate == 'FAIL') else 'PASS'
    }


def find_projects(base_dir):
    """Find all project directories"""
    projects = []
    base_path = Path(base_dir).resolve()

    # Skip these directories
    skip_patterns = [
        'node_modules', 'vendor', '.git', 'bin', 'obj',
        'target', '__pycache__', 'venv', '.venv', 'photos'
    ]

    for item in base_path.iterdir():
        if not item.is_dir():
            continue

        # Skip certain directories
        if item.name.startswith('.') or item.name in skip_patterns:
            continue

        # Check if it's a code project
        language = detect_project_language(item)
        if language != 'unknown':
            projects.append({
                'path': str(item),
                'name': item.name,
                'language': language
            })

    return projects


def export_for_training(results, output_path):
    """Export results in format suitable for training"""
    # Create labels.json format
    labels = {}

    for result in results:
        if 'error' in result:
            continue

        # Create a label entry for each file analyzed
        project_name = result['project_name']
        gate_status = result.get('gate_status', {})

        labels[f"{project_name}_project.py"] = {
            'bug_gate': gate_status.get('bug_gate', 'PASS'),
            'vulnerability_gate': gate_status.get('vulnerability_gate', 'PASS')
        }

    # Save labels
    labels_path = Path(output_path).parent / 'sonar_labels.json'
    with open(labels_path, 'w') as f:
        json.dump(labels, f, indent=2)

    print(f"\n  Training labels saved to: {labels_path}")
    return labels_path


def main():
    parser = argparse.ArgumentParser(
        description='Batch scan repositories with SonarQube',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python sonarqube_batch_scan.py /path/to/repos
    python sonarqube_batch_scan.py /path/to/repos --output results.json
    python sonarqube_batch_scan.py /path/to/repos --keep-running
        """
    )
    parser.add_argument('directory', help='Directory containing repositories')
    parser.add_argument('-o', '--output', default='sonar_results.json',
                       help='Output JSON file for results')
    parser.add_argument('--keep-running', action='store_true',
                       help='Keep SonarQube running after scan')
    parser.add_argument('--max-projects', type=int, default=50,
                       help='Maximum number of projects to scan')

    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: '{args.directory}' is not a valid directory")
        sys.exit(1)

    print("=" * 60)
    print("SonarQube Batch Scanner")
    print("Multi-Agent Quality Gate Training Data Generator")
    print("=" * 60)

    # Check Docker
    if not is_docker_running():
        print("Error: Docker is not running. Please start Docker first.")
        sys.exit(1)

    # Start SonarQube
    if not start_sonarqube():
        print("Error: Could not start SonarQube")
        sys.exit(1)

    # Wait for SonarQube to be ready
    if not wait_for_sonarqube():
        print("Error: SonarQube did not start in time")
        sys.exit(1)

    # Get authentication token
    print("\n[3/5] Authenticating...")
    token = get_sonar_token()
    if not token:
        print("  Warning: Using basic auth instead of token")
        token = SONAR_PASS  # Fall back to password
    else:
        print("  ✓ Token created")

    # Find projects
    print(f"\n[4/5] Finding projects in {args.directory}...")
    projects = find_projects(args.directory)

    if not projects:
        print("  No projects found!")
        sys.exit(1)

    print(f"  ✓ Found {len(projects)} projects:")
    for p in projects[:10]:
        print(f"    • {p['name']} ({p['language']})")
    if len(projects) > 10:
        print(f"    ... and {len(projects) - 10} more")

    # Limit projects if specified
    if len(projects) > args.max_projects:
        print(f"\n  Limiting to {args.max_projects} projects")
        projects = projects[:args.max_projects]

    # Scan each project
    print(f"\n[5/5] Scanning {len(projects)} projects...")
    results = []

    for i, project in enumerate(projects, 1):
        project_key = project['name'].lower().replace(' ', '-').replace('.', '-')
        print(f"\n  [{i}/{len(projects)}] {project['name']}...")

        try:
            # Run scanner
            success = scan_project(project['path'], project_key, token)

            if not success:
                print(f"    ✗ Scan failed")
                results.append({
                    'project_name': project['name'],
                    'project_path': project['path'],
                    'error': 'Scan failed'
                })
                continue

            # Wait for analysis to complete
            print(f"    → Waiting for analysis...")
            if not wait_for_analysis(project_key):
                print(f"    ✗ Analysis timeout")
                results.append({
                    'project_name': project['name'],
                    'project_path': project['path'],
                    'error': 'Analysis timeout'
                })
                continue

            # Get results
            issues = get_project_issues(project_key)
            qg_status = get_quality_gate_status(project_key)
            categorized = categorize_issues(issues)
            gate_status = determine_gate_status(categorized, qg_status)

            result = {
                'project_name': project['name'],
                'project_path': project['path'],
                'language': project['language'],
                'sonarqube_key': project_key,
                'total_issues': len(issues),
                'bugs': len(categorized['bugs']),
                'vulnerabilities': len(categorized['vulnerabilities']),
                'code_smells': len(categorized['code_smells']),
                'gate_status': gate_status,
                'issues_detail': {
                    'bugs': [{'rule': i['rule'], 'severity': i['severity'], 'message': i['message']}
                             for i in categorized['bugs'][:10]],
                    'vulnerabilities': [{'rule': i['rule'], 'severity': i['severity'], 'message': i['message']}
                                       for i in categorized['vulnerabilities'][:10]]
                }
            }

            results.append(result)

            status_icon = "✓" if gate_status['overall'] == 'PASS' else "✗"
            print(f"    {status_icon} Bugs: {result['bugs']}, Vulns: {result['vulnerabilities']}, "
                  f"Status: {gate_status['overall']}")

        except Exception as e:
            print(f"    ✗ Error: {e}")
            results.append({
                'project_name': project['name'],
                'project_path': project['path'],
                'error': str(e)
            })

    # Save results
    output_data = {
        'timestamp': datetime.now().isoformat(),
        'base_directory': str(args.directory),
        'total_projects': len(projects),
        'successful_scans': len([r for r in results if 'error' not in r]),
        'results': results
    }

    with open(args.output, 'w') as f:
        json.dump(output_data, f, indent=2)

    print(f"\n{'=' * 60}")
    print("SCAN COMPLETE")
    print(f"{'=' * 60}")
    print(f"\nResults saved to: {args.output}")

    # Export for training
    export_for_training(results, args.output)

    # Summary
    successful = [r for r in results if 'error' not in r]
    if successful:
        passed = len([r for r in successful if r['gate_status']['overall'] == 'PASS'])
        failed = len(successful) - passed

        print(f"\nSummary:")
        print(f"  • Scanned: {len(successful)}/{len(projects)} projects")
        print(f"  • Passed: {passed}")
        print(f"  • Failed: {failed}")
        print(f"  • Total bugs found: {sum(r['bugs'] for r in successful)}")
        print(f"  • Total vulnerabilities: {sum(r['vulnerabilities'] for r in successful)}")

    # Cleanup
    if not args.keep_running:
        print(f"\nStopping SonarQube container...")
        run_command(f"docker stop {SONAR_CONTAINER}", check=False)
        print("  ✓ Stopped")
    else:
        print(f"\nSonarQube is still running at: {SONAR_URL}")
        print(f"  Login: admin / admin")
        print(f"  To stop: docker stop {SONAR_CONTAINER}")


if __name__ == "__main__":
    main()
