# Multi-Agent Code Quality System
## Presentation Outline

---

## Slide 1: Title

**Multi-Agent Code Quality System**
*Deep Learning-Inspired Architecture for SonarQube Prediction*

- Your Name
- Course: [Your Course]
- Date: [Date]

---

## Slide 2: The Problem

### Why This Matters

- SonarQube runs in CI/CD (slow feedback - minutes to hours)
- Developers commit code → wait → find out it fails → fix → repeat
- Need **real-time prediction** before committing
- Want analysis **personalized to MY coding patterns**

### The Goal

> Build a system that predicts SonarQube quality gate failures **instantly**, 
> before code leaves the developer's machine.

---

## Slide 3: Solution Overview

### Multi-Agent Architecture

```
Source Code
     ↓
┌─────────────────────────────────┐
│   ENHANCED FEATURE EXTRACTOR    │  ← NLP-style analysis
└─────────────────────────────────┘
     ↓
┌─────────────────────────────────┐
│   8 QUALITY GATE CLASSIFIERS    │  ← Each with Sigmoid/ReLU
└─────────────────────────────────┘
     ↓
┌─────────────────────────────────┐
│   SUPERVISOR AGENTS             │  ← Confusion matrix evaluation
└─────────────────────────────────┘
     ↓
┌─────────────────────────────────┐
│   ARCHITECTURE AGENT            │  ← Selects optimal activation
└─────────────────────────────────┘
```

---

## Slide 4: The 8 Quality Gates

| Gate | What It Detects | Detection Method |
|------|-----------------|------------------|
| **Bug** | Code defects | Complexity, nesting |
| **Vulnerability** | Security flaws | SQL injection, eval, secrets |
| **Security Hotspot** | Needs review | Crypto, file ops, network |
| **Reliability** | Stability issues | Error handling |
| **Security** | Security rating | Critical vulnerability severity |
| **Maintainability** | Tech debt | Code smells |
| **Coverage** | Test gaps | Test file presence |
| **Duplication** | Copy-paste | Duplicate detection |

*Same gates as SonarQube!*

---

## Slide 5: Key Innovation - Adaptive Activation

### Why Sigmoid vs ReLU?

| Sigmoid | ReLU |
|---------|------|
| Soft thresholds | Hard cutoffs |
| Gradual transitions | Binary decisions |
| Better for nuanced cases | Zero-tolerance policies |

### The System Automatically Selects

- Trains both activations per gate
- Evaluates using confusion matrices
- Picks the one that **maximizes specificity**

---

## Slide 6: Training with Real SonarQube Data

### Ground Truth from Actual Scans

1. Started SonarQube via Docker
2. Scanned all my course repositories
3. Extracted metrics for all 8 gates
4. Used as training labels

### Results

| Project | Bugs | Vulns | Hotspots | Status |
|---------|------|-------|----------|--------|
| CST-180-Python | 215 | 1 | 22 | FAIL |
| CST-391-Web_dev | 9 | 0 | 17 | FAIL |
| agent-quality-system | 0 | 0 | 12 | PASS |
| *... 6 more projects* | | | | |

---

## Slide 7: Iterative Feedforward Pipeline

### Multiple Passes Until Convergence

```
Iteration 1: bug_gate PASS (conf=39%), security_gate FAIL (conf=100%)
Iteration 2: bug_gate PASS (conf=39%), security_gate FAIL (conf=100%)
→ Converged!
```

### Confidence Scoring

| Level | Confidence | Meaning |
|-------|------------|---------|
| HIGH | >90% | Very certain |
| MEDIUM | 70-90% | Reasonably certain |
| LOW | 50-70% | Less certain |
| UNCERTAIN | <50% | Need more data |

---

## Slide 8: Real-Time Integration

### Pre-commit Hook

```bash
$ git commit -m "Add new feature"

╭──────────────────────────────────────────╮
│  Multi-Agent Code Quality Gate Check     │
╰──────────────────────────────────────────╯
Analyzing 3 staged file(s)...
✓ All quality gates passed!
```

### CI/CD with GitHub Actions

- Runs on every push/PR
- Analyzes changed files only
- Comments results on PRs

---

## Slide 9: Live Demo

### Demo 1: Single File Analysis
```bash
python demo_all_gates.py vulnerable_code.py
```

### Demo 2: Project Analysis
```bash
python demo_all_gates.py /path/to/project
```

### Demo 3: Iterative Pipeline with Confidence
```bash
python demo_iterative.py complex_code.py
```

### Demo 4: Pre-commit Hook
```bash
git add buggy_file.py
git commit -m "Test commit"
# Watch the quality gate check run!
```

---

## Slide 10: Comparison with SonarQube

| Aspect | Our System | SonarQube |
|--------|------------|-----------|
| **Speed** | ~1 second | Minutes |
| **When** | Pre-commit | CI/CD |
| **Training** | Customizable | Fixed rules |
| **Integration** | Git hook | Server-based |

### Agreement with SonarQube

- Security Hotspot Gate: **66.7%** accuracy
- Bug Gate: **55.6%** accuracy (more aggressive)
- Coverage Gate: **100%** accuracy (both agree: no tests!)

---

## Slide 11: Technical Highlights

### Languages Supported
- Python, Java, C#, JavaScript/TypeScript, C/C++

### Features Extracted
- Cyclomatic complexity (radon)
- Nesting depth
- SQL injection patterns
- Hardcoded secrets (API keys)
- XSS vulnerabilities
- Command injection
- Code duplication

### Optimization Target
- **Specificity** (minimize false positives)
- Developers hate false alarms!

---

## Slide 12: Architecture Summary

```
┌─────────────────────────────────────────────────────────────────┐
│                         SOURCE CODE                              │
│                 (Python, Java, C#, JS, C++)                      │
└─────────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
        ┌──────────┐   ┌──────────┐   ┌──────────┐
        │   Bug    │   │   Vuln   │   │ Project  │
        │ Features │   │ Features │   │ Features │
        └────┬─────┘   └────┬─────┘   └────┬─────┘
              │              │              │
              ▼              ▼              ▼
    ┌─────────────────────────────────────────────────┐
    │           8 QUALITY GATE CLASSIFIERS             │
    │    (Each with optimized Sigmoid or ReLU)         │
    └─────────────────────────────────────────────────┘
                              │
                              ▼
    ┌─────────────────────────────────────────────────┐
    │              ITERATIVE PIPELINE                  │
    │        (Multiple passes until convergence)       │
    └─────────────────────────────────────────────────┘
                              │
                              ▼
                    PASS/FAIL + Confidence
```

---

## Slide 13: What I Learned

1. **Multi-agent systems** can decompose complex problems
2. **Activation functions** matter for classification behavior
3. **Confusion matrices** enable objective optimization
4. **Real ground truth** (SonarQube) validates the approach
5. **Developer experience** (speed, integration) is crucial

---

## Slide 14: Future Work

1. **More training data** - Scan more repositories
2. **Better accuracy** - Tune thresholds to match SonarQube
3. **IDE integration** - VS Code extension for real-time feedback
4. **Deep learning** - Use actual neural networks
5. **Semantic analysis** - Beyond pattern matching

---

## Slide 15: Questions?

### Quick Reference

```bash
# Install
pip install -r requirements.txt

# Train
python train_all_gates.py

# Analyze
python demo_all_gates.py your_file.py

# Install hook
python install_hook.py /your/repo
```

### Repository
[Your GitHub URL]

---

## Professor Q&A Prep

### Q: "How is this different from just running SonarQube?"
**A:** Speed and integration. SonarQube takes minutes and runs in CI. This runs in <1 second as a pre-commit hook. Developers get feedback before code ever leaves their machine.

### Q: "Why not just use a neural network?"
**A:** This IS neural network-inspired. We use sigmoid/ReLU activations, train on labeled data, and optimize via metrics. The difference is interpretability - we can explain every decision.

### Q: "What's the accuracy?"
**A:** Against SonarQube ground truth: 55-100% depending on the gate. But our goal is specificity (avoiding false positives), not accuracy. A false positive wastes developer time.

### Q: "How did you get training data?"
**A:** Real SonarQube scans! I ran SonarQube in Docker, scanned all my course repos, and used those results as ground truth labels.

### Q: "Can this replace SonarQube?"
**A:** No, it complements it. This catches issues early (pre-commit). SonarQube does deeper analysis in CI. They work together.

---

## Demo Script

### 1. Show the system (30 seconds)
```bash
ls agents/
cat README.md | head -50
```

### 2. Analyze a file (1 minute)
```bash
python demo_all_gates.py demo_code.py
```

### 3. Show iterative pipeline (30 seconds)
```bash
python demo_iterative.py
```

### 4. Show pre-commit hook (1 minute)
```bash
echo "eval(input())" > test_vuln.py
git add test_vuln.py
git commit -m "Test"
# Show it fails!
rm test_vuln.py
```

### 5. Show SonarQube comparison (30 seconds)
```bash
cat data/results/sonar_comprehensive_metrics.json | python -m json.tool | head -30
```

---

## File Checklist

- [x] `agents/all_gate_classifiers.py` - All 8 gates
- [x] `agents/enhanced_feature_extractor.py` - Feature extraction
- [x] `agents/iterative_pipeline.py` - Feedforward iteration
- [x] `train_all_gates.py` - Training script
- [x] `demo_all_gates.py` - Demo script
- [x] `demo_iterative.py` - Iterative demo
- [x] `install_hook.py` - Pre-commit installation
- [x] `.github/workflows/quality-gate.yml` - CI/CD
- [x] `data/results/all_gates_optimal_config.json` - Trained config
- [x] `data/results/sonar_comprehensive_metrics.json` - Ground truth
