# PROJECT SYNOPSIS

**Project Title:** AutoDiagnostix-AI: Intelligent RAG & Agentic Diagnostic System for Automotive Workshop Manuals and OBD-II Telemetry with Grounded Source Citations  
**Department:** Department of Computer Science (AI & ML)  
**Institution:** Pimpri Chinchwad College of Engineering (PCCOE), Pune  
**Industry Partner / Event:** Tata TechPulse & Applied AI Project Showcase  
**Academic Year:** 2025–2026  

---

## 1. Project Information

| Field | Details |
| :--- | :--- |
| **Student Name** | [Student Name] |
| **Permanent Registration No. (PRN)** | 123B1F001 |
| **Class & Division** | B.Tech Computer Engineering (CS-AIML) |
| **Project Guide (Faculty)** | Prof. Dr. [Faculty Guide Name] |
| **Domain** | Generative AI, Retrieval-Augmented Generation (RAG), Automotive AI |
| **Target Application** | Automotive Workshop Troubleshooting, Field Service Diagnostics, OBD-II Fault Isolation |

---

## 2. Abstract
Modern automotive vehicles—ranging from Internal Combustion Engine (ICE) platforms (e.g., 2.0L Turbo Diesel) to modern Electric Vehicles (EVs) and Advanced Driver Assistance Systems (ADAS Level 2)—contain complex electro-mechanical interactions and hundreds of Diagnostic Trouble Codes (DTCs). Workshop technicians and service engineers face immense cognitive load navigating thousands of pages of Technical Service Bulletins (TSBs), workshop manuals, wiring schematics, and torque specifications. Conventional search mechanisms fail to synthesize multi-step troubleshooting procedures, while general-purpose Large Language Models (LLMs) suffer from dangerous domain hallucinations and lack strict source attribution.

This project proposes **AutoDiagnostix-AI**, a robust Retrieval-Augmented Generation (RAG) and Agentic diagnostic system. The system ingests structured automotive knowledge bases (OEM workshop manuals, OBD-II diagnostic trees, CAN-bus telemetry guides, and safety SOPs). It leverages hybrid semantic-lexical retrieval (Dense embeddings + BM25) coupled with cross-encoder re-ranking and an Agentic Diagnostic Supervisor. Crucially, the system enforces **strict grounded citation generation**, where every diagnostic step, torque value, and pinout probe instruction is accompanied by exact document name, chapter, section, and page citations. The system is evaluated using the RAGAS framework (Faithfulness, Answer Relevance, Context Precision, and Citation Accuracy) against a ground-truth benchmark of 30+ diagnostic scenarios.

---

## 3. Problem Statement
Automotive technicians encounter complex vehicle fault codes (e.g., P0300 Random Misfire, P0A80 Hybrid/EV Battery Degradation, C1A12 ADAS Radar Misalignment) that require exact step-by-step diagnostic trees, safety protocols, and component pinout verification. Existing challenges include:
1. **Manual Navigation Overhead:** OEM service manuals often span 1,500+ pages per vehicle model, causing high Mean Time To Repair (MTTR).
2. **LLM Hallucinations in Safety-Critical Scenarios:** Standard GenAI tools produce plausible-sounding but erroneous torque specifications, incorrect wiring pinouts, or bypass dangerous high-voltage (HV) safety isolation steps.
3. **Absence of Verifiable Citations:** Field engineers cannot trust automated suggestions without verifiable references back to approved OEM workshop bulletins.

---

## 4. Objectives
1. **Curate and Preprocess Structured Automotive Knowledge Base:** Parse and index OEM service manuals, OBD-II diagnostic flowcharts, EV battery management protocols, and ADAS calibration manuals with metadata preservation (Document, Chapter, Section, Page, Diagram ID).
2. **Build a Hybrid Retrieval Engine:** Combine BM25 lexical keyword matching with dense vector embeddings to ensure precise retrieval of specific alpha-numeric part numbers, DTCs, and semantic symptom descriptions.
3. **Develop an Agentic Diagnostic Supervisor:** Implement multi-step reasoning tools (OBD-II Code Lookup, Torque Spec Finder, Wiring Diagram Locator, and HV Safety Pre-check Tool).
4. **Enforce Grounded Citation & Hallucination Guardrails:** Design prompt engineering and output parsing layers that reject ungrounded assertions and mandate exact markdown citations `[Doc: X, Page: Y, Section: Z]`.
5. **Comprehensive Quantitative Evaluation:** Benchmark system accuracy using RAGAS metrics (Faithfulness > 95%, Context Precision > 90%, Citation Accuracy 100%) against a peer-reviewed ground-truth test suite.
6. **Deploy an Interactive User Interface:** Deliver a responsive, field-ready Web and CLI interface showing real-time query answers, retrieved source context chunks, and clickable citations.

---

## 5. System Architecture & Methodology

```
+-------------------------------------------------------------------------+
|                         AUTODIAGNOSTIX-AI PIPELINE                      |
+-------------------------------------------------------------------------+
                                     |
               +---------------------+---------------------+
               |                                           |
    [Automotive Knowledge Base]                   [Technician Query]
  - EV Battery & Inverter Manuals              "P0300 misfire with rough
  - ICE 2.0L & 1.2L Engine TSBs                 idling on cold start"
  - ADAS Radar/Camera Calibration                          |
  - OBD-II DTC Trouble Trees                               v
               |                              +-------------------------+
               v                              | Query Reformulator &    |
    [Document Parser & Chunker]               | Entity Extractor (DTCs) |
  - Recursive Character Splitter              +-------------------------+
  - Metadata Tagging (Page/Section/ID)                     |
               |                                           v
               v                              +-------------------------+
     [Hybrid Vector Store]                    | Hybrid Retrieval Engine |
  - Dense Embeddings (Semantic) <------------>| - BM25 Lexical Search   |
  - BM25 Inverted Index (Exact DTC)           | - Dense Cosine Sim      |
               |                              +-------------------------+
               +-------------------------------------------|
                                                           v
                                              +-------------------------+
                                              | Cross-Encoder Reranker  |
                                              | Top-K Relevant Passages |
                                              +-------------------------+
                                                           |
                                                           v
                                              +-------------------------+
                                              | Agentic Diagnostic      |
                                              | Reasoning & Tool Engine |
                                              +-------------------------+
                                                           |
                                                           v
                                              +-------------------------+
                                              | Grounded Response Gen   |
                                              | with Strict Citations   |
                                              +-------------------------+
                                                           |
                                                           v
                                              +-------------------------+
                                              | Hallucination Guard &   |
                                              | Citation Verifier       |
                                              +-------------------------+
                                                           |
                                                           v
                                              [Technician Web / CLI UI]
```

---

## 6. Hardware & Software Requirements

### Software Environment
* **Language:** Python 3.10+ / 3.13
* **Vector Store & Indexing:** In-memory Vector Store with Cosine Similarity, BM25 Lexical Index (ChromaDB / FAISS compatible)
* **LLM Engine / API:** Google Gemini 1.5 Pro / Flash or Local HuggingFace / Llama-3 (Fallback rule-based synthesizer included for offline evaluation)
* **Evaluation Framework:** RAGAS Evaluation Suite (Faithfulness, Answer Relevance, Context Precision, Citation Coverage)
* **Frontend UI:** Interactive Responsive Web Dashboard (HTML5/Modern CSS/Vanilla JS) & Rich CLI Console

### Hardware Specifications
* **CPU:** Multi-core Intel Core i5/i7 or Apple Silicon (M1/M2/M3)
* **RAM:** Minimum 8 GB (16 GB recommended)
* **Storage:** 2 GB free disk space

---

## 7. Project Milestones & Timeline

| Phase | Milestone Description | Status |
| :--- | :--- | :--- |
| **Phase 1** | Requirement analysis, domain scoping & synopsis finalization | Completed |
| **Phase 2** | Knowledge base curation (Tata EV, ICE, ADAS, OBD-II manuals) | Completed |
| **Phase 3** | Chunking, metadata extraction & Hybrid retrieval engine build | Completed |
| **Phase 4** | Prompt engineering, Agent tool calling & Citation enforcement | Completed |
| **Phase 5** | RAGAS benchmark evaluation with ground-truth test suite | Completed |
| **Phase 6** | UI development, Technical Report, and Demonstration video prep | Completed |

---

## 8. Expected Outcomes & Deliverables
1. Production-grade codebase with modular architecture (`vector_store.py`, `retriever.py`, `rag_pipeline.py`, `agent_diagnostic_logic.py`, `evaluation_metrics.py`).
2. Curated Knowledge Base containing 4 specialized automotive manuals with full provenance.
3. 25-Question Ground-Truth evaluation benchmark demonstrating >95% groundedness.
4. Comprehensive Technical Report formatted to academic & Tata TechPulse specifications.
5. End-to-end Demonstration Video guide and execution script.
