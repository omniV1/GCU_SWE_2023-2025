#!/usr/bin/env python3
"""
Install pre-commit hook for Multi-Agent Code Quality System
Usage: python install_hook.py [target_repo_path]
"""

import os
import sys
import stat
import shutil
from pathlib import Path

HOOK_SCRIPT = '''#!/usr/bin/env python3
"""Pre-commit hook - Multi-Agent Code Quality Gate Check"""

import os
import sys
import subprocess
import json
from pathlib import Path

# Configuration
AGENT_SYSTEM_PATH = "{agent_system_path}"
SKIP_GATES = ["coverage_gate"]  # Gates to skip (coverage needs test framework)
BLOCK_ON_FAIL = True  # Set to False to warn only

def get_staged_files():
    """Get list of staged source files"""
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
        capture_output=True, text=True
    )
    
    extensions = {{'.py', '.java', '.cs', '.js', '.ts', '.jsx', '.tsx', '.c', '.cpp', '.h'}}
    files = []
    
    for line in result.stdout.strip().split('\\n'):
        if line and Path(line).suffix.lower() in extensions:
            files.append(line)
    
    return files


def analyze_files(files):
    """Analyze files using the quality gate system"""
    sys.path.insert(0, AGENT_SYSTEM_PATH)
    
    try:
        from agents.enhanced_feature_extractor import EnhancedFeatureExtractor
        from agents.all_gate_classifiers import AllGatesClassificationPipeline
    except ImportError as e:
        print(f"\\033[33mWarning: Could not load agent system: {{e}}\\033[0m")
        return True, []
    
    # Load config
    config_path = Path(AGENT_SYSTEM_PATH) / "data/results/all_gates_optimal_config.json"
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        pipeline_config = {{g: {{'activation': c.get('activation', 'sigmoid')}} 
                           for g, c in config.get('gates', {{}}).items()}}
    except:
        pipeline_config = {{}}
    
    extractor = EnhancedFeatureExtractor()
    pipeline = AllGatesClassificationPipeline(pipeline_config)
    
    failed_files = []
    
    for filepath in files:
        if not os.path.exists(filepath):
            continue
        
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                code = f.read()
            
            features = extractor.extract_all_features(code, filepath)
            results = pipeline.classify(
                features['bug_features'],
                features['vulnerability_features'],
                features['project_features']
            )
            
            # Check for failures (excluding skipped gates)
            failed_gates = [
                g for g, v in results.items() 
                if v == 'FAIL' and g != 'overall' and g not in SKIP_GATES
            ]
            
            if failed_gates:
                failed_files.append({{'file': filepath, 'gates': failed_gates}})
                
        except Exception as e:
            pass  # Skip files that can't be analyzed
    
    return len(failed_files) == 0, failed_files


def main():
    print("\\033[36m╭──────────────────────────────────────────╮\\033[0m")
    print("\\033[36m│  Multi-Agent Code Quality Gate Check     │\\033[0m")
    print("\\033[36m╰──────────────────────────────────────────╯\\033[0m")
    
    files = get_staged_files()
    
    if not files:
        print("\\033[32m✓ No source files staged\\033[0m")
        sys.exit(0)
    
    print(f"\\033[33mAnalyzing {{len(files)}} staged file(s)...\\033[0m")
    
    passed, failures = analyze_files(files)
    
    if passed:
        print("\\033[32m╭──────────────────────────────────────────╮\\033[0m")
        print("\\033[32m│  ✓ All quality gates passed!             │\\033[0m")
        print("\\033[32m╰──────────────────────────────────────────╯\\033[0m")
        sys.exit(0)
    else:
        print("\\033[31m╭──────────────────────────────────────────╮\\033[0m")
        print("\\033[31m│  ✗ Quality gate check failed!            │\\033[0m")
        print("\\033[31m╰──────────────────────────────────────────╯\\033[0m")
        print()
        print("\\033[33mIssues found:\\033[0m")
        for ff in failures[:10]:
            gates = ', '.join(g.replace('_gate', '').replace('_', ' ') for g in ff['gates'])
            print(f"  \\033[31m✗\\033[0m {{ff['file']}}")
            print(f"    Failed: {{gates}}")
        
        if len(failures) > 10:
            print(f"  ... and {{len(failures) - 10}} more files")
        
        print()
        if BLOCK_ON_FAIL:
            print("\\033[33mTo commit anyway: git commit --no-verify\\033[0m")
            sys.exit(1)
        else:
            print("\\033[33mWarning only - commit will proceed\\033[0m")
            sys.exit(0)


if __name__ == "__main__":
    main()
'''


def install_hook(target_repo=None):
    """Install the pre-commit hook"""
    agent_system_path = Path(__file__).parent.resolve()
    
    # Determine target repository
    if target_repo:
        repo_path = Path(target_repo).resolve()
    else:
        # Default to parent directory (the main GCU directory)
        repo_path = agent_system_path.parent
    
    # Find .git directory
    git_dir = repo_path / ".git"
    if not git_dir.exists():
        print(f"Error: {repo_path} is not a git repository")
        print("Usage: python install_hook.py [path_to_repo]")
        sys.exit(1)
    
    hooks_dir = git_dir / "hooks"
    hooks_dir.mkdir(exist_ok=True)
    
    hook_path = hooks_dir / "pre-commit"
    
    # Check for existing hook
    if hook_path.exists():
        backup = hook_path.with_suffix('.backup')
        print(f"Backing up existing hook to {backup}")
        shutil.copy(hook_path, backup)
    
    # Write hook
    hook_content = HOOK_SCRIPT.format(agent_system_path=str(agent_system_path))
    
    with open(hook_path, 'w') as f:
        f.write(hook_content)
    
    # Make executable
    hook_path.chmod(hook_path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    
    print(f"✓ Pre-commit hook installed to: {hook_path}")
    print()
    print("The hook will analyze staged files before each commit.")
    print("To skip the check: git commit --no-verify")
    print()
    print("Configuration:")
    print(f"  Agent System: {agent_system_path}")
    print(f"  Target Repo:  {repo_path}")


def uninstall_hook(target_repo=None):
    """Uninstall the pre-commit hook"""
    if target_repo:
        repo_path = Path(target_repo).resolve()
    else:
        repo_path = Path(__file__).parent.parent.resolve()
    
    hook_path = repo_path / ".git" / "hooks" / "pre-commit"
    
    if hook_path.exists():
        hook_path.unlink()
        print(f"✓ Pre-commit hook removed from: {hook_path}")
        
        # Restore backup if exists
        backup = hook_path.with_suffix('.backup')
        if backup.exists():
            shutil.copy(backup, hook_path)
            print(f"✓ Restored backup hook")
    else:
        print("No pre-commit hook found")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--uninstall":
        target = sys.argv[2] if len(sys.argv) > 2 else None
        uninstall_hook(target)
    else:
        target = sys.argv[1] if len(sys.argv) > 1 else None
        install_hook(target)
