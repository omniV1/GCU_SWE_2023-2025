# Quality Gate MCP Server

An MCP (Model Context Protocol) server that exposes multi-agent code quality analysis as tools for Claude.

## Features

- **analyze_code** - Analyze code snippets for bugs and vulnerabilities
- **analyze_file** - Analyze a file on disk
- **analyze_directory** - Batch analyze all source files in a project
- **get_quality_summary** - Get human-readable explanations of issues

## Supported Languages

- Python
- Java
- C#
- JavaScript/TypeScript
- C/C++

## Installation

### From source (development)

```bash
cd mcp_server
pip install -e .
```

### Using uvx (recommended for Claude Desktop)

```bash
uvx quality-gate-mcp
```

## Configuration

### Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "quality-gate": {
      "command": "python",
      "args": ["-m", "quality_gate_mcp.server"],
      "cwd": "/path/to/agent-quality-system/mcp_server/src"
    }
  }
}
```

Or if installed via pip:

```json
{
  "mcpServers": {
    "quality-gate": {
      "command": "quality-gate-mcp"
    }
  }
}
```

### Claude Code

Add to your project's `.claude/settings.json`:

```json
{
  "mcpServers": {
    "quality-gate": {
      "command": "quality-gate-mcp"
    }
  }
}
```

## Usage Examples

Once configured, Claude can use the quality gate tools:

**Analyze a code snippet:**
```
Can you analyze this code for quality issues?

def process(data):
    if data:
        if data.get('items'):
            for item in data['items']:
                if item.get('valid'):
                    query = "SELECT * FROM users WHERE id = " + item['id']
                    eval(item['expression'])
```

**Analyze a project:**
```
Analyze the code quality of my project at /path/to/project
```

## Quality Gates

The server checks code against two quality gates:

### Bug Gate
- Cyclomatic complexity (threshold: 15)
- Nesting depth (threshold: 4)
- Function length (threshold: 100 lines)

### Vulnerability Gate
- SQL injection patterns
- eval/exec usage
- Command injection
- Hardcoded secrets
- XSS risks

## Architecture

This MCP server wraps the Multi-Agent Quality Gate System:

```
[Claude] → [MCP Server] → [NLP Agent] → [Feature Extraction]
                              ↓
                      [Classification Agents]
                              ↓
                      [Bug Gate] [Vuln Gate]
                              ↓
                      [Results to Claude]
```

## License

MIT
