#!/usr/bin/env python3
"""
Quality Gate MCP Server

Exposes multi-agent code quality analysis as MCP tools for Claude.

Tools:
- analyze_code: Analyze a code snippet for bugs and vulnerabilities
- analyze_file: Analyze a file on disk
- analyze_directory: Batch analyze all source files in a directory
- get_quality_report: Generate a detailed quality report
"""

import os
import sys
import json
from pathlib import Path
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Add parent paths to find the agents module
# From: mcp_server/src/quality_gate_mcp/server.py
# To:   agent-quality-system/
SCRIPT_DIR = Path(__file__).parent.resolve()
AGENT_SYSTEM_PATH = SCRIPT_DIR.parent.parent.parent  # quality_gate_mcp → src → mcp_server → agent-quality-system
sys.path.insert(0, str(AGENT_SYSTEM_PATH))

# Import the quality gate components
try:
    from agents.multi_lang_agent import MultiLanguageAgent, calculate_total_signals
    from agents.classifiers import BugGateClassifier, VulnerabilityGateClassifier
    from agents.architecture_agent import ArchitectureAgent
    AGENTS_AVAILABLE = True
except ImportError as e:
    AGENTS_AVAILABLE = False
    IMPORT_ERROR = str(e)

# Try to load enhanced feature extractor if available
try:
    from agents.enhanced_feature_extractor import EnhancedFeatureExtractor
    from agents.all_gate_classifiers import AllGatesClassificationPipeline
    ENHANCED_AVAILABLE = True
except ImportError:
    ENHANCED_AVAILABLE = False

# Create server instance
server = Server("quality-gate-mcp")

# Initialize agents (lazy loading)
_nlp_agent = None
_bug_classifier = None
_vuln_classifier = None
_enhanced_extractor = None
_all_gates_pipeline = None


def get_nlp_agent():
    """Lazy load NLP agent"""
    global _nlp_agent
    if _nlp_agent is None and AGENTS_AVAILABLE:
        _nlp_agent = MultiLanguageAgent()
    return _nlp_agent


def get_classifiers():
    """Lazy load classifiers"""
    global _bug_classifier, _vuln_classifier
    if _bug_classifier is None and AGENTS_AVAILABLE:
        _bug_classifier = BugGateClassifier(verbose=False)
        _vuln_classifier = VulnerabilityGateClassifier(verbose=False)
    return _bug_classifier, _vuln_classifier


def get_enhanced_pipeline():
    """Lazy load enhanced pipeline if available"""
    global _enhanced_extractor, _all_gates_pipeline
    if _enhanced_extractor is None and ENHANCED_AVAILABLE:
        _enhanced_extractor = EnhancedFeatureExtractor()
        # Load config if exists
        config_path = AGENT_SYSTEM_PATH / "data" / "results" / "all_gates_optimal_config.json"
        pipeline_config = {}
        if config_path.exists():
            try:
                with open(config_path) as f:
                    config = json.load(f)
                pipeline_config = {g: {'activation': c.get('activation', 'sigmoid')}
                                   for g, c in config.get('gates', {}).items()}
            except Exception:
                pass
        _all_gates_pipeline = AllGatesClassificationPipeline(pipeline_config)
    return _enhanced_extractor, _all_gates_pipeline


def detect_language(filename: str, code: str) -> str:
    """Detect programming language from filename or content"""
    ext_map = {
        '.py': 'Python', '.java': 'Java', '.cs': 'C#',
        '.js': 'JavaScript', '.ts': 'TypeScript',
        '.c': 'C', '.cpp': 'C++', '.h': 'C/C++ Header'
    }
    ext = Path(filename).suffix.lower() if filename else ''
    return ext_map.get(ext, 'Unknown')


def analyze_code_internal(code: str, filename: str = "snippet.py") -> dict:
    """Internal function to analyze code"""
    if not AGENTS_AVAILABLE:
        return {"error": f"Agent system not available: {IMPORT_ERROR}"}

    nlp_agent = get_nlp_agent()
    bug_classifier, vuln_classifier = get_classifiers()

    # Extract features
    features = nlp_agent.extract_features(code, filename)
    calculate_total_signals(features['vulnerability_features'])

    # Map NLP agent feature names to classifier expected names
    vuln_features = features['vulnerability_features']
    classifier_vuln_features = {
        'total_vulnerability_signals': vuln_features.get('total_signals', 0),
        'eval_usage': vuln_features.get('eval_exec', 0),
        'sql_concat': vuln_features.get('sql_injection', 0),
        'hardcoded_secrets': vuln_features.get('hardcoded_secrets', 0),
    }

    # Classify
    bug_result = bug_classifier.classify(features['bug_features'], activation='relu')
    vuln_result = vuln_classifier.classify(classifier_vuln_features, activation='relu')

    overall = 'PASS' if (bug_result == 'PASS' and vuln_result == 'PASS') else 'FAIL'

    return {
        'filename': filename,
        'language': features.get('language', detect_language(filename, code)),
        'overall': overall,
        'bug_gate': bug_result,
        'vulnerability_gate': vuln_result,
        'metrics': {
            'complexity': features['bug_features'].get('max_complexity', 0),
            'nesting_depth': features['bug_features'].get('max_nesting', 0),
            'function_length': features['bug_features'].get('max_function_length', 0),
        },
        'vulnerabilities': {
            'sql_injection': features['vulnerability_features'].get('sql_injection', 0),
            'eval_exec': features['vulnerability_features'].get('eval_exec', 0),
            'command_injection': features['vulnerability_features'].get('command_injection', 0),
            'hardcoded_secrets': features['vulnerability_features'].get('hardcoded_secrets', 0),
            'xss_risk': features['vulnerability_features'].get('xss_risk', 0),
        }
    }


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available quality gate tools"""
    tools = [
        Tool(
            name="analyze_code",
            description="Analyze a code snippet for bugs, vulnerabilities, and code quality issues. "
                       "Returns pass/fail status for bug gate and vulnerability gate, along with detailed metrics.",
            inputSchema={
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string",
                        "description": "The source code to analyze"
                    },
                    "filename": {
                        "type": "string",
                        "description": "Optional filename (used to detect language). Default: snippet.py",
                        "default": "snippet.py"
                    }
                },
                "required": ["code"]
            }
        ),
        Tool(
            name="analyze_file",
            description="Analyze a source code file on disk for bugs and vulnerabilities.",
            inputSchema={
                "type": "object",
                "properties": {
                    "filepath": {
                        "type": "string",
                        "description": "Path to the source file to analyze"
                    }
                },
                "required": ["filepath"]
            }
        ),
        Tool(
            name="analyze_directory",
            description="Batch analyze all source files in a directory. "
                       "Supports Python, Java, C#, JavaScript, TypeScript, C/C++.",
            inputSchema={
                "type": "object",
                "properties": {
                    "directory": {
                        "type": "string",
                        "description": "Path to the directory to analyze"
                    },
                    "max_files": {
                        "type": "integer",
                        "description": "Maximum number of files to analyze (default: 50)",
                        "default": 50
                    }
                },
                "required": ["directory"]
            }
        ),
        Tool(
            name="get_quality_summary",
            description="Get a summary explanation of quality gate results, "
                       "explaining what the metrics mean and how to fix issues.",
            inputSchema={
                "type": "object",
                "properties": {
                    "results": {
                        "type": "object",
                        "description": "Results from analyze_code or analyze_file"
                    }
                },
                "required": ["results"]
            }
        )
    ]
    return tools


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle tool calls"""

    if name == "analyze_code":
        code = arguments.get("code", "")
        filename = arguments.get("filename", "snippet.py")

        if not code.strip():
            return [TextContent(type="text", text=json.dumps({"error": "No code provided"}))]

        result = analyze_code_internal(code, filename)
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    elif name == "analyze_file":
        filepath = arguments.get("filepath", "")

        if not filepath:
            return [TextContent(type="text", text=json.dumps({"error": "No filepath provided"}))]

        path = Path(filepath).expanduser().resolve()
        if not path.exists():
            return [TextContent(type="text", text=json.dumps({"error": f"File not found: {filepath}"}))]

        try:
            code = path.read_text(encoding='utf-8', errors='ignore')
            result = analyze_code_internal(code, path.name)
            result['filepath'] = str(path)
            return [TextContent(type="text", text=json.dumps(result, indent=2))]
        except Exception as e:
            return [TextContent(type="text", text=json.dumps({"error": str(e)}))]

    elif name == "analyze_directory":
        directory = arguments.get("directory", "")
        max_files = arguments.get("max_files", 50)

        if not directory:
            return [TextContent(type="text", text=json.dumps({"error": "No directory provided"}))]

        dir_path = Path(directory).expanduser().resolve()
        if not dir_path.exists() or not dir_path.is_dir():
            return [TextContent(type="text", text=json.dumps({"error": f"Directory not found: {directory}"}))]

        # Find source files
        extensions = {'.py', '.java', '.cs', '.js', '.ts', '.jsx', '.tsx', '.c', '.cpp', '.h'}
        skip_patterns = ['node_modules', 'vendor', '.git', '__pycache__', 'venv', '.venv']

        source_files = []
        for ext in extensions:
            for f in dir_path.rglob(f'*{ext}'):
                if not any(p in str(f) for p in skip_patterns):
                    source_files.append(f)
                if len(source_files) >= max_files:
                    break
            if len(source_files) >= max_files:
                break

        results = []
        passed = 0
        failed = 0

        for filepath in source_files[:max_files]:
            try:
                code = filepath.read_text(encoding='utf-8', errors='ignore')
                result = analyze_code_internal(code, filepath.name)
                result['filepath'] = str(filepath.relative_to(dir_path))
                results.append(result)
                if result['overall'] == 'PASS':
                    passed += 1
                else:
                    failed += 1
            except Exception:
                pass

        summary = {
            'directory': str(dir_path),
            'total_files': len(results),
            'passed': passed,
            'failed': failed,
            'pass_rate': f"{(passed/len(results)*100):.1f}%" if results else "N/A",
            'files': results
        }

        return [TextContent(type="text", text=json.dumps(summary, indent=2))]

    elif name == "get_quality_summary":
        results = arguments.get("results", {})

        if not results:
            return [TextContent(type="text", text=json.dumps({"error": "No results provided"}))]

        # Generate human-readable summary
        summary_parts = []

        overall = results.get('overall', 'UNKNOWN')
        bug_gate = results.get('bug_gate', 'UNKNOWN')
        vuln_gate = results.get('vulnerability_gate', 'UNKNOWN')

        if overall == 'PASS':
            summary_parts.append("✓ Code passed all quality gates!")
        else:
            summary_parts.append("✗ Code failed quality gates:")
            if bug_gate == 'FAIL':
                summary_parts.append("  - Bug Gate: FAILED")
                metrics = results.get('metrics', {})
                if metrics.get('complexity', 0) > 15:
                    summary_parts.append(f"    • High complexity ({metrics['complexity']}): Consider breaking into smaller functions")
                if metrics.get('nesting_depth', 0) > 4:
                    summary_parts.append(f"    • Deep nesting ({metrics['nesting_depth']}): Consider early returns or extracting methods")
                if metrics.get('function_length', 0) > 100:
                    summary_parts.append(f"    • Long functions ({metrics['function_length']} lines): Consider splitting")

            if vuln_gate == 'FAIL':
                summary_parts.append("  - Vulnerability Gate: FAILED")
                vulns = results.get('vulnerabilities', {})
                if vulns.get('sql_injection'):
                    summary_parts.append("    • SQL Injection risk: Use parameterized queries")
                if vulns.get('eval_exec'):
                    summary_parts.append("    • eval/exec usage: Avoid dynamic code execution")
                if vulns.get('command_injection'):
                    summary_parts.append("    • Command injection: Use subprocess with shell=False")
                if vulns.get('hardcoded_secrets'):
                    summary_parts.append("    • Hardcoded secrets: Use environment variables")
                if vulns.get('xss_risk'):
                    summary_parts.append("    • XSS risk: Sanitize user input before output")

        summary = "\n".join(summary_parts)
        return [TextContent(type="text", text=summary)]

    else:
        return [TextContent(type="text", text=json.dumps({"error": f"Unknown tool: {name}"}))]


async def main():
    """Run the MCP server"""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


def run():
    """Entry point for the MCP server"""
    import asyncio
    asyncio.run(main())


if __name__ == "__main__":
    run()
