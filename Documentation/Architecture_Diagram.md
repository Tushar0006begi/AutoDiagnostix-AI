# AUTODIAGNOSTIX-AI: ARCHITECTURE DIAGRAMS & DATA FLOWS

This document visualizes the complete end-to-end architecture, hybrid retrieval fusion, and agentic decision tree of **AutoDiagnostix-AI**.

---

## 1. End-to-End System Architecture

```mermaid
flowchart TD
    subgraph KB ["Automotive Knowledge Base (OEM Manuals)"]
        D1["Tata EV Powertrain & BMS Manual"]
        D2["Tata Kryotec 2.0L & Revotron 1.2L ICE Manual"]
        D3["Tata ADAS L2 & Telematics Manual"]
        D4["Workshop Safety & Torque SOPs"]
    end

    subgraph INGEST ["Ingestion & Chunking Pipeline"]
        CP["Hierarchy & Section Parser"]
        CH["Metadata Enrichment (Doc, Section, Page, Diagram)"]
    end

    subgraph VSTORE ["Hybrid Vector Index"]
        DENSE["Dense TF-IDF Vector Space (Cosine Sim)"]
        SPARSE["BM25 Inverted Lexical Index"]
    end

    subgraph QUERY_LAYER ["User & Workshop Interface"]
        USER(["Technician / Service Engineer"])
        UI["Web GUI Dashboard / CLI Console"]
    end

    subgraph AGENT ["Agentic Diagnostic Supervisor"]
        DET["Intent & Entity Parser (DTCs, Symptoms)"]
        SAFETY{"Is EV / High-Voltage?"}
        S_TOOL["Tool: verify_hv_safety_protocol"]
        DTC_TOOL["Tool: lookup_obd2_code"]
        TORQ_TOOL["Tool: get_torque_spec"]
        PIN_TOOL["Tool: get_wiring_and_pinout"]
    end

    subgraph RETRIEVAL ["Hybrid Retrieval Engine"]
        FUSION["Linear Score Fusion (alpha*BM25 + beta*Dense)"]
        RANK["Top-K Candidate Reranking"]
    end

    subgraph GENERATION ["Grounded Generation & Citation Engine"]
        PROMPT["Context Assembly + Citation Rules"]
        SYNTH["Grounded Diagnostic Response Generator"]
        GUARD["Citation Verifier & Hallucination Guard"]
    end

    KB --> CP --> CH --> VSTORE
    USER --> UI --> DET
    DET --> SAFETY
    SAFETY -- Yes --> S_TOOL
    SAFETY -- No / Continue --> DTC_TOOL & TORQ_TOOL & PIN_TOOL
    DTC_TOOL & TORQ_TOOL & PIN_TOOL --> RETRIEVAL
    VSTORE <--> RETRIEVAL
    RETRIEVAL --> FUSION --> RANK --> PROMPT
    S_TOOL --> PROMPT
    PROMPT --> SYNTH --> GUARD --> UI
```

---

## 2. Hybrid Retrieval & Score Fusion Flow

```mermaid
flowchart LR
    Q["Technician Query (e.g., 'P0A0C HVIL Open')"]
    
    subgraph Lexical ["Lexical Branch"]
        T1["Tokenize Alphanumeric DTCs"]
        B1["Okapi BM25 Index Lookup"]
        S1["Raw BM25 Scores"]
        N1["Min-Max Normalization (Score / Max)"]
    end

    subgraph Dense ["Dense Semantic Branch"]
        T2["Compute Query TF-IDF Vector"]
        B2["Cosine Similarity Matrix"]
        S2["Raw Cosine Scores"]
        N2["Min-Max Normalization (Score / Max)"]
    end

    Q --> T1 --> B1 --> S1 --> N1
    Q --> T2 --> B2 --> S2 --> N2

    N1 --> FUSE["Hybrid Score = (0.45 * BM25_norm) + (0.55 * Dense_norm)"]
    N2 --> FUSE
    FUSE --> TOP["Top-K Passage Selection (Top 3)"]
```

---

## 3. High-Voltage Safety Interlock Decision Sequence

```mermaid
sequenceDiagram
    autonumber
    actor Tech as Workshop Technician
    participant Agent as Diagnostic Supervisor
    participant SafeTool as Safety Protocol Tool
    participant RAG as Hybrid RAG Engine
    participant KB as OEM Manuals Store

    Tech->>Agent: Query: "Replace traction battery module for code P0A80"
    Agent->>Agent: Detect EV / High-Voltage Intent (P0A80, Battery)
    Agent->>SafeTool: Trigger Mandatory HV Pre-check
    SafeTool->>RAG: Fetch Zero-Voltage Safety SOP (Doc 004, Page 8)
    RAG->>KB: Retrieve Section 1.1: 4-Step Zero-Voltage SOP
    KB-->>SafeTool: Return PPE Class 0 & MSD steps
    SafeTool-->>Agent: Safety Interlock Activated (WARNING Banner)
    Agent->>RAG: Fetch Diagnostic Flow for P0A80 (Doc 001, Page 62)
    RAG-->>Agent: Return Balancing steps, Cell delta V < 30mV
    Agent->>Tech: Output Safety Warning + Diagnostic Steps + Exact Citations
```
