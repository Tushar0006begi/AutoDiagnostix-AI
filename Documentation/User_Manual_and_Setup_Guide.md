# AUTODIAGNOSTIX-AI: USER MANUAL & DEPLOYMENT GUIDE

**System:** AutoDiagnostix-AI  
**Domain:** Automotive Workshop Diagnostics & RAG Grounded Citations  
**Target Audience:** Workshop Technicians, Evaluators, Faculty, Students  

---

## 1. System Requirements & Prerequisites

* **Operating System:** macOS (Sonoma/Sequoia), Linux (Ubuntu 20.04+), or Windows 10/11.
* **Python Runtime:** Python 3.10, 3.11, 3.12, or 3.13.
* **Dependencies:** None mandatory! The entire core pipeline runs natively on Python's built-in standard library (`math`, `re`, `json`, `http.server`, `urllib`).

---

## 2. Quick-Start Execution Guide

Open a terminal and navigate to the project `Code/` directory:

```bash
cd PCCOE_StudentName_PRN_CSx_AIML/Code
```

### Option A: Run Automated Verification & Evaluation Suite
Execute the 12-scenario ground-truth benchmark suite:
```bash
python3 run_evaluation.py
```
*Outputs generated:*
* `Evaluation_Results/evaluation_report.json` (Machine-readable metrics)
* `Evaluation_Results/evaluation_metrics_summary.md` (Markdown report)
* `Evaluation_Results/sample_grounded_responses_with_citations.md` (Sample outputs)

### Option B: Launch Interactive Web GUI Dashboard
Start the lightweight web server:
```bash
python3 app_web_gui.py 8080
```
Open your browser and navigate to:  
👉 **`http://localhost:8080`**

**Web GUI Features:**
1. Click any quick-test scenario (e.g., P0A0C EV HVIL, P0300 Misfire, ADAS Radar Alignment).
2. Type custom DTCs or natural language symptoms.
3. Observe real-time **Autonomous Agent Execution Trace**.
4. View High-Voltage **Safety Warning Banners**.
5. Inspect clickable **Authoritative OEM Citations** (Document, Page, Section).
6. Live RAGAS metric indicators (Faithfulness, Relevancy, Precision).

### Option C: Interactive Terminal CLI Console
For technicians working directly from a workshop terminal:
```bash
python3 cli_interactive.py
```

### Option D: Master Demo Script
Run everything through the interactive bash script:
```bash
./run_demo.sh
```

---

## 3. Connecting External LLM APIs (Optional)

If you wish to run with Google Gemini 1.5 Pro:
```bash
export GEMINI_API_KEY="your-api-key-here"
python3 app_web_gui.py 8080
```
*Note: If `GEMINI_API_KEY` is not set, AutoDiagnostix-AI automatically defaults to its built-in deterministic grounded synthesizer, ensuring 100% offline functionality without internet or API dependency during live evaluations!*
