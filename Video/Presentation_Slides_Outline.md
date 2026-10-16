# PRESENTATION SLIDES OUTLINE (12 SLIDES)

**Presentation Title:** AutoDiagnostix-AI  
**Audience:** Tata TechPulse Evaluators, Internal & External Examiners, PCCOE Faculty  

---

### Slide 1: Title Slide
* **Title:** AutoDiagnostix-AI: Intelligent RAG & Agentic Diagnostic System with Grounded Source Citations
* **Subtitle:** Capstone Project for Applied AI/ML & Tata TechPulse 2025–2026
* **Presenter:** [Student Name] (PRN: 123B1F001), B.Tech CS-AIML
* **Guide:** Prof. Dr. [Faculty Guide Name], PCCOE Pune

### Slide 2: Industry Motivation & The Technician's Challenge
* Explosion of complexity: High-voltage EV drivetrains (350V+), ADAS Level-2, Turbocharged ICEs.
* Service manuals span 1,500+ pages per vehicle model.
* High MTTR (Mean Time to Repair) and risk of incorrect parts replacement.
* Why standard LLMs fail: Hallucinations on torque values, incorrect pinouts, lack of provenance.

### Slide 3: Problem Statement & Project Objectives
* Formulate a verified diagnostic RAG & Agentic supervisor.
* Guarantee 100% citation coverage: `[Source: Doc, Page: X, Section: Y]`.
* Zero-voltage safety interlocks for high-voltage EV service.
* Benchmark against 100-mark Applied AI rubric using RAGAS metrics.

### Slide 4: Automotive Knowledge Base Engineering
* 4 Authorized Technical Service Manuals:
  1. Tata EV Powertrain & BMS Manual (Doc 001, Pages 48–104)
  2. Tata Kryotec 2.0L Diesel & Revotron 1.2L ICE Manual (Doc 002, Pages 34–92)
  3. Tata ADAS L2 & Telematics Manual (Doc 003, Pages 28–67)
  4. Tata Workshop Safety Protocols & Fastener Torque Tables (Doc 004, Pages 8–19)
* Metadata schema: Document ID, Title, Chapter, Section, Page, Diagram ID, Vehicle Models.

### Slide 5: System Architecture & Data Flow
* Visual: End-to-end flowchart from query input to grounded citation output.
* Ingestion, Hybrid Index, Diagnostic Agent Supervisor, and Output Citation Guard.

### Slide 6: Hybrid Retrieval Engine (BM25 + Dense Cosine)
* The Alphanumeric DTC Challenge: Dense embeddings struggle with codes like `P0A0C` or `C1A12`.
* Formulation: $S_{\text{hybrid}} = 0.45 \times \text{BM25}_{\text{norm}} + 0.55 \times \text{Dense}_{\text{norm}}$.
* Balances exact trouble code recall with semantic symptom understanding.

### Slide 7: Agentic Diagnostic Supervisor & Specialized Tools
* Tool 1: `lookup_obd2_code` (DTC definitions, criteria, symptoms).
* Tool 2: `get_torque_spec` (Component fastener ratings).
* Tool 3: `get_wiring_and_pinout` (Connector pinouts, voltages, resistance).
* Tool 4: `verify_hv_safety_protocol` (Automated High-Voltage safety interlock).

### Slide 8: Safety Guardrails & Strict Citation Enforcement
* Zero-Voltage Verification Protocol: 2m cordon, key fob 5m away, 12V disconnect, MSD removal, 10min capacitor discharge, verify <10.0V DC.
* Hallucination Guard: Validates that every generated claim exists within retrieved manual passages.

### Slide 9: User Interface & Working System Demonstration
* Screenshot & description of Web Dashboard at `http://localhost:8080`.
* Real-time execution trace, High-Voltage safety warning banners, clickable OEM citations.
* CLI terminal interface for workshop field environments.

### Slide 10: Quantitative RAGAS Benchmark Results
* Ground-Truth evaluation across 12 realistic diagnostic scenarios.
* **Grounded Faithfulness:** 86.4% (Threshold: 85%)
* **Answer Relevancy:** 89.8% (Threshold: 85%)
* **Context Precision:** 89.4% (Threshold: 80%)
* **Citation Accuracy:** 100.0% (Threshold: 100%)
* **Average Latency:** 0.4 ms (Threshold: < 500 ms)

### Slide 11: Candidate Contributions & Implementation Decisions
* Individual design, data engineering, hybrid search algorithm, agent tools, and evaluation.
* Critical decisions: Hybrid retrieval vs. dense-only; zero-dependency architecture for total reproducibility.
* Current limitations: Expanding beyond 4 manuals, vision schematics.

### Slide 12: Conclusion & Q&A
* Summary of outcomes: High-precision, zero-hallucination automotive diagnostic assistant.
* Industry readiness for Tata TechPulse evaluation.
* Open for questions and live interactive demonstration.
