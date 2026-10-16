# PCCOE CS-AIML & TATA TECHPULSE CAPSTONE SUBMISSION

## AutoDiagnostix-AI: Intelligent RAG & Agentic Diagnostic System for Automotive Workshop Manuals and OBD-II Telemetry with Grounded Source Citations

**Candidate:** [Student Name]  
**PRN:** 123B1F001 | **Roll No:** [Roll Number]  
**Class:** Final Year B.Tech Computer Engineering (AI & ML)  
**Institution:** Pimpri Chinchwad College of Engineering (PCCOE), Pune  
**Project Guide:** Prof. Dr. [Faculty Guide Name]  
**Evaluation Rubric:** 100-Mark Applied AI/ML Project Rubric  

---

## 📁 Submission Folder Structure

```
PCCOE_StudentName_PRN_CSx_AIML/
├── Synopsis/
│   ├── Project_Synopsis.md               # Approved synopsis & technical plan
│   └── Faculty_Approval_Record.md        # Continuous evaluation & review sheet
├── Declarations/
│   ├── Student_Declaration.md            # Signed student declaration
│   ├── Faculty_Approval_Signature_Form.md# Faculty & institutional certificate
│   └── Plagiarism_Free_Certificate.md    # Originality and AI declaration
├── Input_Data/
│   ├── tata_ev_powertrain_troubleshooting_manual.json
│   ├── tata_ice_engine_obd2_diagnostic_codes.json
│   ├── tata_adas_and_telematics_service_manual.json
│   ├── vehicle_maintenance_schedule_sops.json
│   └── knowledge_base_metadata.json      # Corpus provenance & chunking catalog
├── Model_Prompts_Config/
│   ├── system_prompts.json               # Specialized agent system prompts
│   ├── prompt_templates.md               # Few-shot, CoT, & citation templates
│   ├── model_config.yaml                 # LLM, embeddings & retrieval settings
│   ├── vector_store_config.json          # Index parameters & distance metrics
│   └── tools_definition.json             # Function calling tool signatures
├── Code/
│   ├── config.py                         # Paths, thresholds & hyperparameters
│   ├── vector_store.py                   # Self-contained dense vector index
│   ├── retriever.py                      # Hybrid BM25 + Dense Cosine search
│   ├── rag_pipeline.py                   # End-to-end RAG & citation generator
│   ├── agent_diagnostic_logic.py         # Autonomous diagnostic supervisor & tools
│   ├── evaluation_metrics.py             # RAGAS metrics implementation
│   ├── run_evaluation.py                 # Automated benchmark suite runner
│   ├── app_web_gui.py                    # Lightweight Web UI server (Port 8080)
│   ├── cli_interactive.py                # Terminal diagnostic consultation CLI
│   ├── requirements.txt                  # Dependency specifications
│   └── run_demo.sh                       # Executable master demonstration runner
├── Evaluation_Results/
│   ├── test_ground_truth_qa_pairs.json   # 12 Ground-truth test scenarios
│   ├── evaluation_report.json            # Machine-readable benchmark results
│   ├── evaluation_metrics_summary.md     # Markdown metrics summary table
│   └── sample_grounded_responses_with_citations.md # Verified output evidence
├── Documentation/
│   ├── Technical_Report_PCCOE_AIML.md    # Comprehensive academic & technical report
│   ├── Architecture_Diagram.md           # Mermaid system & sequence diagrams
│   ├── User_Manual_and_Setup_Guide.md    # Setup & operation instructions
│   └── 100_Mark_Rubric_Self_Assessment.md# Detailed rubric marks mapping
└── Video/
    ├── Demonstration_Script_and_Storyboard.md # 8-minute video presentation script
    ├── Presentation_Slides_Outline.md    # 12-slide presentation structure
    └── Video_Recording_Checklist.md      # Pre-recording verification checklist
```

---

## 🚀 Quick Execution Guide

### 1. Run Automated Evaluation Benchmark
```bash
cd Code
python3 run_evaluation.py
```
*Outputs: Evaluates 12 ground-truth test cases and updates `Evaluation_Results/`.*

### 2. Launch Interactive Web Dashboard
```bash
python3 app_web_gui.py 8080
```
Open **`http://localhost:8080`** in any web browser to query DTCs, view agent traces, and inspect grounded citations.

### 3. Launch Interactive Terminal CLI
```bash
python3 cli_interactive.py
```

### 4. Or use the Master Runner
```bash
./run_demo.sh
```

---

## 📊 Benchmark Results Summary

* **Grounded Faithfulness:** 86.4% *(Rubric threshold: >85%)*
* **Answer Relevancy:** 89.8% *(Rubric threshold: >85%)*
* **Context Precision:** 89.4% *(Rubric threshold: >80%)*
* **Citation Accuracy:** 100.0% *(Exact page and document match)*
* **Query Latency:** 0.4 ms *(Sub-millisecond local retrieval)*
