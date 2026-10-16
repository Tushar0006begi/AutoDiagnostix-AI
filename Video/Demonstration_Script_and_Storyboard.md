# 8-MINUTE VIDEO DEMONSTRATION SCRIPT & STORYBOARD

**Project Title:** AutoDiagnostix-AI: Intelligent RAG & Agentic Diagnostic System for Automotive Workshop Manuals with Grounded Source Citations  
**Event:** Tata TechPulse & PCCOE CS-AIML Final Evaluation  
**Target Video Duration:** 7:30 to 8:30 Minutes (Permitted window: 5 to 10 minutes)  

---

### Segment 1: Introduction & Domain Relevance (0:00 – 1:15)
* **Visual on Screen:** Title slide showing Student Name, PRN, PCCOE logo, and Tata TechPulse banner, transitioning to live terminal showing project directory structure.
* **Speaker Narration:**
  > "Respected evaluators and faculty members, I am [Student Name], final-year Computer Engineering AI/ML student at PCCOE Pune. Today, I am proud to present **AutoDiagnostix-AI**, an intelligent RAG and Agentic Diagnostic System designed for automotive workshop manuals and OBD-II telemetry with strictly grounded citations.
  > Modern vehicles like the Tata Harrier, Safari, and Nexon EV combine 400-volt high-voltage drivetrains, ADAS radars, and turbocharged ICE powertrains. When an error manifests, workshop technicians face thousands of pages of service manuals. General LLMs fail in these safety-critical scenarios due to hallucinations of fastener torque values and electrical pinouts. AutoDiagnostix-AI bridges this gap with verifiable citations and autonomous safety interlocks."

---

### Segment 2: Automotive Knowledge Base & Data Provenance (1:15 – 2:30)
* **Visual on Screen:** Open `Input_Data/` directory. Show `tata_ev_powertrain_troubleshooting_manual.json` and `knowledge_base_metadata.json`. Highlight metadata fields (Document Title, Page, Diagram ID).
* **Speaker Narration:**
  > "Let us look at our input data and knowledge base. Under `Input_Data/`, we have curated four technical workshop manuals covering:
  > 1. Tata EV Powertrains and High-Voltage BMS fault isolation.
  > 2. Tata Kryotec 2.0L Diesel and Revotron 1.2L Turbo Petrol OBD-II diagnostic trees.
  > 3. Level-2 ADAS camera and 77GHz radar calibration procedures.
  > 4. Workshop High-Voltage Zero-Voltage verification protocols and torque ratings.
  > Notice that every single chunk preserves rich metadata: exact document ID, chapter, section name, page number, and diagram ID. This ensures total provenance tracking for every piece of information."

---

### Segment 3: Pipeline Architecture & Hybrid Retrieval (2:30 – 3:45)
* **Visual on Screen:** Display `Documentation/Architecture_Diagram.md` showing Mermaid flowchart. Explain dense-sparse fusion.
* **Speaker Narration:**
  > "Now, turning to our architectural pipeline: automotive diagnostics presents a unique challenge—standard dense vector embeddings often fail on rare alphanumeric trouble codes like `P0A0C` or `C1A12`.
  > To solve this, AutoDiagnostix-AI implements a **Hybrid Retrieval Engine** combining Okapi BM25 lexical search with dense vector cosine similarity. We use linear score fusion with weights of 0.45 for lexical and 0.55 for dense similarity.
  > Furthermore, we have an **Agentic Diagnostic Supervisor** that inspects incoming queries and dynamically calls four specialized tools: OBD-II Code Lookup, Torque Spec Finder, Wiring Pinout Tool, and a mandatory High-Voltage Safety Protocol Tool."

---

### Segment 4: Live System Demonstration & Grounded Citations (3:45 – 5:45)
* **Visual on Screen:** Open Web browser at `http://localhost:8080`.
* **Action 1:** Click on *"⚡ P0A0C: EV HVIL Open Circuit"*.
* **Speaker Narration:**
  > "Let's demonstrate the live working system on our Web Dashboard at `http://localhost:8080`.
  > Notice what happens immediately: The Autonomous Agent detects a High-Voltage query and fires a prominent red **Safety Warning**: Class 0 1000V PPE and Zero-Voltage Verification are mandatory before any physical contact.
  > In the execution trace, we see Step 1: Safety Interlock activated; Step 2: OEM DTC lookup.
  > Look at the synthesized diagnostic workflow: It gives the exact 5-step procedure—waiting 10 minutes for capacitor discharge, removing the Manual Service Disconnect (MSD), probing connector PDU-X02 pins 3 and 7 with a 1000V DMM, and checking for 0.5 to 1.8 Ohms.
  > Most importantly, at the bottom, notice the **verifiable citation**: `Tata Electric Vehicle Powertrain Manual, Page 48, Section 4.2`. There is zero hallucination."
* **Action 2:** Test a mechanical query: *"What is the torque specification for the spark plugs on Revotron 1.2L and wheel lug nuts on Harrier?"*
* **Speaker Narration:**
  > "Now, testing a mechanical query with multiple torque specifications. The agent retrieves from both the engine manual and the chassis maintenance SOP. It accurately outputs 22 Nm for the spark plug, 9 Nm for the pencil coil, and 120 Nm for the Harrier wheel lug nuts, citing Page 34 and Page 19 respectively."

---

### Segment 5: Quantitative RAGAS Evaluation Results (5:45 – 7:00)
* **Visual on Screen:** Switch to terminal, run `python3 run_evaluation.py`. Show terminal output and open `Evaluation_Results/evaluation_metrics_summary.md`.
* **Speaker Narration:**
  > "Let us evaluate empirical performance. I am now executing our automated benchmark suite containing 12 ground-truth scenarios covering EV, ICE, ADAS, and workshop safety protocols.
  > In just milliseconds, our evaluation suite completes:
  > - **Grounded Faithfulness:** Achieved **86.4%**, well above the 85% rubric threshold.
  > - **Answer Relevancy:** Achieved **89.8%**.
  > - **Context Precision:** Achieved **89.4%**.
  > - **Citation Accuracy:** A perfect **100%**, matching the ground-truth document and page numbers.
  > - **Average Latency:** An astounding **0.4 milliseconds** per query locally, guaranteeing sub-second responsiveness on field tablets."

---

### Segment 6: Decisions, Limitations & Conclusion (7:00 – 8:00)
* **Visual on Screen:** Return to camera / presentation summary slide showing Student Details, Rubric Scorecard, and Submission Checklist.
* **Speaker Narration:**
  > "To summarize our implementation decisions: We prioritized a hybrid dense-sparse retrieval model over dense-only search to guarantee 100% recall on alphanumeric fault codes. We designed a zero-dependency architecture so this project executes reliably on any evaluation machine without external API failures.
  > Current limitations include indexing four core manuals, with future scope expanding to live OBD-II CAN telemetry and multi-modal wiring schematic images.
  > The entire project is organized into the prescribed folder structure `PCCOE_StudentName_PRN_CSx_AIML/` and is ready for final submission. Thank you!"
