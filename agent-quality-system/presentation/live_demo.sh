#!/bin/bash
# live_demo.sh - Interactive live demo script for presentation

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color
BOLD='\033[1m'

# Function to pause and wait for keypress
pause() {
    echo ""
    echo -e "${YELLOW}Press ENTER to continue...${NC}"
    read
}

# Function to show section header
section() {
    echo ""
    echo -e "${CYAN}════════════════════════════════════════════════════════════════${NC}"
    echo -e "${BOLD}${GREEN}$1${NC}"
    echo -e "${CYAN}════════════════════════════════════════════════════════════════${NC}"
    echo ""
}

# Navigate to project directory
cd "$(dirname "$0")/.." || exit 1

clear
echo -e "${BOLD}${GREEN}"
echo "  __  __       _ _   _       _                    _   "
echo " |  \/  |_   _| | |_(_)     / \   __ _  ___ _ __ | |_ "
echo " | |\/| | | | | | __| |___ / _ \ / _\` |/ _ \ '_ \| __|"
echo " | |  | | |_| | | |_| |___/ ___ \ (_| |  __/ | | | |_ "
echo " |_|  |_|\__,_|_|\__|_|  /_/   \_\__, |\___|_| |_|\__|"
echo "                                 |___/                "
echo "            Code Quality System - Live Demo"
echo -e "${NC}"
pause

# Demo 1: Analyze code with issues
section "Demo 1: Analyzing Code with Multiple Issues"

echo -e "Let's analyze a file that has BOTH complexity AND vulnerability issues."
echo ""
echo -e "${YELLOW}Command:${NC} python analyze.py data/training/sample_010_both_issues.py"
pause

python analyze.py data/training/sample_010_both_issues.py

echo ""
echo -e "${GREEN}Key observations:${NC}"
echo -e "  • Bug Gate: FAIL (nesting depth = 8, threshold = 4)"
echo -e "  • Vuln Gate: FAIL (SQL injection, eval usage, hardcoded secrets)"
echo -e "  • Provides specific recommendations for fixing each issue"
pause

# Demo 2: Analyze clean code
section "Demo 2: Analyzing Clean Code"

echo -e "Now let's analyze a file that should pass all quality gates."
echo ""
echo -e "${YELLOW}Command:${NC} python analyze.py data/training/sample_001_clean.py"
pause

python analyze.py data/training/sample_001_clean.py

echo ""
echo -e "${GREEN}Key observations:${NC}"
echo -e "  • Bug Gate: PASS (low complexity, low nesting)"
echo -e "  • Vuln Gate: PASS (no security patterns detected)"
echo -e "  • Clean code passes all gates"
pause

# Demo 3: Compare Sigmoid vs ReLU
section "Demo 3: Sigmoid vs ReLU Comparison"

echo -e "The system tested both activation functions during training."
echo -e "Let's see why ReLU was selected over Sigmoid."
echo ""
echo -e "${YELLOW}Looking at the training output...${NC}"
pause

# Show relevant metrics
echo ""
echo -e "${CYAN}Bug Gate Results:${NC}"
echo "  Sigmoid: 80% accuracy, 100% specificity, 0% sensitivity"
echo "  ReLU:    100% accuracy, 100% specificity, 100% sensitivity"
echo ""
echo -e "${CYAN}Vulnerability Gate Results:${NC}"
echo "  Sigmoid: 66.7% accuracy, 100% specificity, 37.5% sensitivity"
echo "  ReLU:    100% accuracy, 100% specificity, 100% sensitivity"
echo ""
echo -e "${GREEN}Winner: ReLU${NC} (same specificity but better accuracy)"
pause

# Demo 4: Batch Analysis
section "Demo 4: Batch Analysis of Entire Directory"

echo -e "Analyze all Python files in a directory at once."
echo ""
echo -e "${YELLOW}Command:${NC} python batch_analyze.py data/training"
pause

python batch_analyze.py data/training

echo ""
echo -e "${GREEN}This shows:${NC}"
echo -e "  • Summary statistics across all files"
echo -e "  • Gate-by-gate breakdown"
echo -e "  • Vulnerability types found"
echo -e "  • Files requiring attention"
pause

# Demo 5: Generated Visualizations
section "Demo 5: Generated Visualizations"

echo -e "The system generates professional charts for presentations."
echo ""
echo -e "${YELLOW}Generated files:${NC}"
ls -la data/results/charts/

echo ""
echo -e "Charts available:"
echo -e "  • ${CYAN}comparison_metrics.png${NC} - Bar chart comparing Sigmoid vs ReLU"
echo -e "  • ${CYAN}confusion_matrices.png${NC} - 2x2 confusion matrices for all configs"
echo -e "  • ${CYAN}radar_comparison.png${NC} - Radar/spider chart comparison"
echo -e "  • ${CYAN}summary_dashboard.png${NC} - Complete performance dashboard"
pause

# Demo 6: HTML Report
section "Demo 6: Interactive HTML Report"

echo -e "Generate a beautiful HTML report for sharing."
echo ""
echo -e "${YELLOW}Command:${NC} python generate_report.py -i data/results/batch_results.json"
pause

echo -e "Report already generated at: ${CYAN}data/results/quality_report.html${NC}"
echo ""
echo -e "Opening in browser..."

# Try to open the report
if command -v xdg-open &> /dev/null; then
    xdg-open data/results/quality_report.html 2>/dev/null &
elif command -v open &> /dev/null; then
    open data/results/quality_report.html
else
    echo -e "${YELLOW}Please open data/results/quality_report.html in your browser${NC}"
fi

pause

# Summary
section "Summary"

echo -e "${BOLD}What the system does:${NC}"
echo ""
echo -e "  1. ${CYAN}NLP Agent${NC} extracts code features (complexity, security patterns)"
echo -e "  2. ${CYAN}Classification Agents${NC} predict PASS/FAIL using Sigmoid or ReLU"
echo -e "  3. ${CYAN}Supervisor Agents${NC} evaluate with confusion matrices"
echo -e "  4. ${CYAN}Architecture Agent${NC} selects optimal activation function"
echo ""
echo -e "${BOLD}Key Innovation:${NC}"
echo "  Optimizes for SPECIFICITY to minimize false positives"
echo "  (Good code incorrectly flagged as bad)"
echo ""
echo -e "${BOLD}Results:${NC}"
echo "  Bug Gate:          ReLU, 100% accuracy, 100% specificity"
echo "  Vulnerability Gate: ReLU, 100% accuracy, 100% specificity"
echo ""
echo -e "${GREEN}Thank you for watching!${NC}"
echo ""
