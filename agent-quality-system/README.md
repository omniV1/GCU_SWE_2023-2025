# Experimental Code Quality Heuristics

A developer-tooling prototype that extracts static-analysis signals and applies
configurable, deterministic heuristics inspired by SonarQube quality gates. It
is not a deep-learning system, a SonarQube replacement, or a security scanner.
The included experimental configuration was evaluated against a small set of
SonarQube results; the metrics below are not strong enough for production use.

## 🎯 Key Features

- **Eight experimental signals** - Bug, vulnerability, security, reliability, maintainability, test presence, duplication, and security hotspots
- **Fast local feedback** - Runs deterministic source-pattern checks before commit
- **Multi-Language Support** - Python, Java, C#, JavaScript/TypeScript, C/C++
- **Configurable thresholds** - Compares sigmoid-style scoring with hard thresholds
- **SonarQube comparison data** - Includes a small experimental evaluation dataset
- **Offline unit tests** - Core extraction and classification tests need no network or SonarQube server

## 📊 Quality Gates

| Gate | What It Detects | Detection Method |
|------|-----------------|------------------|
| **Bug Gate** | Code defects | Complexity, nesting depth |
| **Vulnerability Gate** | Security flaws | SQL injection, eval, XSS |
| **Security Hotspot Gate** | Needs review | Crypto, file ops, network |
| **Reliability Gate** | Code stability | Error handling score |
| **Security Gate** | Security rating | Critical vulnerability severity |
| **Maintainability Gate** | Technical debt | Code smells, function length |
| **Coverage Gate** | Test coverage | Test file presence |
| **Duplication Gate** | Copy-paste code | Duplicate line detection |

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    SOURCE CODE INPUT                             │
│              (Python, Java, C#, JS/TS, C/C++)                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                 ENHANCED FEATURE EXTRACTOR                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐   │
│  │ Bug Features │  │ Vuln Features│  │ Project Features     │   │
│  │ • Complexity │  │ • SQL Inject │  │ • Test file ratio    │   │
│  │ • Nesting    │  │ • Eval/Exec  │  │ • Duplication ratio  │   │
│  │ • Length     │  │ • Secrets    │  │ • Error handling     │   │
│  └──────────────┘  └──────────────┘  └──────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              ALL GATES CLASSIFICATION PIPELINE                   │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐   │
│  │   Bug   │ │  Vuln   │ │ Hotspot │ │Reliabil │ │Security │   │
│  │  Gate   │ │  Gate   │ │  Gate   │ │  Gate   │ │  Gate   │   │
│  │(SIGMOID)│ │(SIGMOID)│ │(SIGMOID)│ │(SIGMOID)│ │(SIGMOID)│   │
│  └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘   │
│       │          │          │          │          │            │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐                           │
│  │ Maint.  │ │Coverage │ │  Dup.   │                           │
│  │  Gate   │ │  Gate   │ │  Gate   │                           │
│  │(SIGMOID)│ │(SIGMOID)│ │(SIGMOID)│                           │
│  └────┬────┘ └────┬────┘ └────┬────┘                           │
└───────┴──────────┴──────────┴───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    SUPERVISOR AGENTS                             │
│           Confusion Matrix Evaluation per Gate                   │
│     Metrics: Accuracy, Specificity, Sensitivity, Precision      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   ARCHITECTURE AGENT                             │
│         Select Optimal Activation (Sigmoid vs ReLU)              │
│              Optimize for: SPECIFICITY                           │
└─────────────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

```bash
# Install runtime dependencies
python -m pip install -r requirements.txt

# Install development dependencies and run offline tests
python -m pip install -r requirements-dev.txt
python -m pytest -q

# Re-evaluate heuristic configurations using existing SonarQube labels
python train_all_gates.py

# Analyze a file
python demo_all_gates.py your_file.py

# Analyze a project
python demo_all_gates.py /path/to/project

# Install pre-commit hook
python install_hook.py /path/to/your/repo
```

## 📦 Installation

### 1. Clone/Setup
```bash
cd agent-quality-system
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

### 2. Train with SonarQube Data
```bash
# Start SonarQube (requires Docker)
python sonarqube_batch_scan.py /path/to/repos

# Fetch metrics
python fetch_sonar_metrics.py

# Train all gates
python train_all_gates.py
```

### 3. Install Pre-commit Hook
```bash
# Install to any git repository
python install_hook.py /path/to/your/repo

# Uninstall
python install_hook.py --uninstall /path/to/your/repo
```

## 📖 Usage

### Single File Analysis
```bash
python demo_all_gates.py path/to/file.py
```

### Project Analysis
```bash
python demo_all_gates.py /path/to/project
```

### Batch Analysis (All Languages)
```bash
python batch_analyze_all.py /path/to/codebase -o results.json
```

### Pre-commit Hook
Once installed, the hook automatically runs on `git commit`:
```bash
git add myfile.py
git commit -m "My changes"
# ╭──────────────────────────────────────────╮
# │  Multi-Agent Code Quality Gate Check     │
# ╰──────────────────────────────────────────╯
# Analyzing 1 staged file(s)...
# ✓ All quality gates passed!
```

To skip the check:
```bash
git commit --no-verify -m "Skip check"
```

## 📊 Training Results

These historical results come from only nine projects and show weak,
inconsistent performance. Several gates have 0% specificity or sensitivity,
so the classifiers should be treated as experimental static-analysis
heuristics—not validated predictors. The 100% coverage-gate accuracy is
especially misleading because this prototype estimates test presence rather
than measuring executed line or branch coverage.

| Quality Gate | Activation | Specificity | Accuracy | Sensitivity |
|--------------|------------|-------------|----------|-------------|
| Bug Gate | SIGMOID | 20.0% | 55.6% | 100.0% |
| Vulnerability Gate | SIGMOID | 37.5% | 33.3% | 0.0% |
| Security Hotspot Gate | SIGMOID | 50.0% | 66.7% | 80.0% |
| Reliability Gate | SIGMOID | 0.0% | 11.1% | 100.0% |
| Security Gate | SIGMOID | 50.0% | 55.6% | 100.0% |
| Maintainability Gate | SIGMOID | 11.1% | 11.1% | 0.0% |
| Coverage Gate | SIGMOID | 0.0% | 100.0% | 100.0% |
| Duplication Gate | SIGMOID | 50.0% | 55.6% | 66.7% |

## 📁 Project Structure

```
agent-quality-system/
├── agents/
│   ├── all_gate_classifiers.py      # All 8 quality gate classifiers
│   ├── enhanced_feature_extractor.py # Comprehensive feature extraction
│   ├── nlp_agent.py                  # Python-specific NLP features
│   ├── multi_lang_agent.py           # Multi-language support
│   ├── supervisor.py                 # Confusion matrix evaluation
│   └── architecture_agent.py         # Activation selection
│
├── data/
│   ├── results/
│   │   ├── all_gates_optimal_config.json  # Trained config (all 8 gates)
│   │   ├── sonar_comprehensive_metrics.json
│   │   ├── sonar_all_gates_labels.json    # Ground truth labels
│   │   └── charts/                        # Visualizations
│   └── training/                          # Training samples
│
├── hooks/
│   └── pre-commit                    # Pre-commit hook template
│
├── train_all_gates.py               # Train all 8 gates
├── demo_all_gates.py                # Demo with all gates
├── batch_analyze_all.py             # Batch analysis (multi-lang)
├── install_hook.py                  # Install pre-commit hook
├── sonarqube_batch_scan.py          # Scan repos with SonarQube
├── fetch_sonar_metrics.py           # Fetch SonarQube metrics
├── compare_with_sonarqube.py        # Compare predictions vs SonarQube
└── requirements.txt
```

## 🔬 How It Works

### 1. Feature Extraction

The system extracts features across multiple dimensions:

**Bug Features:**
- Cyclomatic complexity (using radon)
- Maximum nesting depth
- Function lengths
- Error handling coverage

**Vulnerability Features:**
- SQL injection patterns
- Command injection (os.system, subprocess)
- Dangerous functions (eval, exec, pickle)
- Hardcoded secrets (API keys, passwords)
- XSS risks (innerHTML, dangerouslySetInnerHTML)

**Security Hotspot Features:**
- Cryptographic operations
- File system operations
- Network operations
- Weak random number generation

**Project Features:**
- Test file ratio
- Code duplication ratio
- Test framework presence

### 2. Adaptive Classification

Each gate uses either **Sigmoid** or **ReLU** activation, selected during training:

| Activation | Behavior | Best For |
|------------|----------|----------|
| **Sigmoid** | Soft thresholds, weighted scores | Nuanced decisions |
| **ReLU** | Hard cutoffs, binary decisions | Zero-tolerance rules |

### 3. Optimization Target

The system optimizes for **Specificity** (minimizing false positives):
- False positives frustrate developers
- Too many false alarms = tool gets ignored
- Better to miss some issues than cry wolf


## 📈 Comparison with SonarQube

| Aspect | Our System | SonarQube |
|--------|------------|-----------|
| **Analysis Type** | Pattern-based | Semantic + Dataflow |
| **Speed** | Local pattern matching; benchmark for your project | Depends on project and server |
| **Scope** | Source files | Everything (notebooks, configs) |
| **Integration** | Pre-commit hook | CI/CD |
| **Training** | Customizable per-project | Fixed rules |

## 🛠️ Dependencies

```
radon>=6.0.1        # Complexity analysis
numpy>=1.26.0       # Numerical operations
pandas>=2.1.0       # Data manipulation
rich>=13.7.0        # Terminal formatting
matplotlib>=3.8.0   # Visualizations
requests>=2.31.0    # SonarQube API
```

Development and CI dependencies are defined in `requirements-dev.txt`.
GitHub Actions runs the offline pytest suite on Python 3.10, 3.11, and 3.12.

## License

MIT License
