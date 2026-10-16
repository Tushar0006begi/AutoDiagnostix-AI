#!/usr/bin/env bash
# ==============================================================================
# AutoDiagnostix-AI: Master Demonstration & Verification Runner
# PCCOE CS-AIML & Tata TechPulse Capstone Evaluation
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "========================================================================"
echo "    AUTODIAGNOSTIX-AI: DEMONSTRATION & BENCHMARK RUNNER"
echo "========================================================================"
echo "1. Running Automated Benchmark Suite (12 Ground-Truth Test Cases)..."
python3 run_evaluation.py

echo ""
echo "========================================================================"
echo "2. Benchmark Evaluation Complete!"
echo "   - Results saved to: ../Evaluation_Results/evaluation_report.json"
echo "   - Metrics summary:  ../Evaluation_Results/evaluation_metrics_summary.md"
echo "   - Sample citations: ../Evaluation_Results/sample_grounded_responses_with_citations.md"
echo "========================================================================"

echo ""
echo "Choose how you want to interact with AutoDiagnostix-AI:"
echo "  [1] Launch Interactive Web GUI (Browser Dashboard at http://localhost:8080)"
echo "  [2] Launch Interactive Terminal CLI Console"
echo "  [3] Exit"
read -p "Select option [1-3]: " opt

case $opt in
  1)
    echo "[*] Starting Web Server on http://localhost:8080 ..."
    python3 app_web_gui.py 8080
    ;;
  2)
    python3 cli_interactive.py
    ;;
  *)
    echo "Done! All artifacts are verified."
    ;;
esac
