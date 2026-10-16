# 100-MARK APPLIED AI/ML RUBRIC COMPLIANCE & SELF-ASSESSMENT

**Candidate Name:** [Student Name]  
**PRN:** 123B1F001  
**Institution:** PCCOE, Pune  
**Project:** AutoDiagnostix-AI (Automotive Workshop RAG & Agentic Diagnostic System)  

---

| Rubric Component | Max Marks | Claimed Marks | Artifact Evidence & Location in Submission |
| :--- | :--- | :--- | :--- |
| **1. Problem Formulation & Domain Relevance**<br>Clarity of objective, industry alignment (Tata Motors/TechPulse), safety-critical requirements. | 15 | **15** | `Synopsis/Project_Synopsis.md`<br>`Documentation/Technical_Report_PCCOE_AIML.md` (Chapters 1 & 2) |
| **2. Data Engineering & Knowledge Base**<br>Corpus depth, provenance, metadata indexing, JSON/vector structuring across EV/ICE/ADAS/SOP. | 15 | **15** | `Input_Data/` (4 OEM Manuals + Metadata JSON)<br>`Documentation/Technical_Report_PCCOE_AIML.md` (Chapter 4) |
| **3. Model, RAG Pipeline & Agent Architecture**<br>Hybrid retrieval (BM25 + Dense Cosine), multi-step agent tools, prompt engineering, zero-voltage safety interlocks. | 25 | **25** | `Code/vector_store.py`<br>`Code/retriever.py`<br>`Code/rag_pipeline.py`<br>`Code/agent_diagnostic_logic.py`<br>`Model_Prompts_Config/` |
| **4. Groundedness & Source Citation Verification**<br>Mandatory document title, section, page citations; absence of hallucinations; citation validator. | 15 | **15** | `Evaluation_Results/sample_grounded_responses_with_citations.md`<br>`Code/evaluation_metrics.py` (Citation Accuracy: 100%) |
| **5. Empirical Evaluation & RAGAS Benchmarking**<br>12-question ground truth dataset, Faithfulness (86.4%), Relevancy (89.8%), Context Precision (89.4%), latency tracking. | 15 | **15** | `Evaluation_Results/test_ground_truth_qa_pairs.json`<br>`Evaluation_Results/evaluation_report.json`<br>`Evaluation_Results/evaluation_metrics_summary.md` |
| **6. User Interface, Working Behaviour & Deployment**<br>Interactive Web GUI, CLI console, zero-dependency deployment, sub-millisecond execution. | 10 | **10** | `Code/app_web_gui.py`<br>`Code/cli_interactive.py`<br>`Code/run_demo.sh` |
| **7. Documentation, Video Script & Compliance**<br>Complete PDF/MD technical report, signed approval records, student declarations, 8-minute demonstration script. | 5 | **5** | `Documentation/Technical_Report_PCCOE_AIML.md`<br>`Declarations/`<br>`Video/Demonstration_Script_and_Storyboard.md` |
| **TOTAL** | **100** | **100** | **Comprehensive Full-Marks Submission Package** |
