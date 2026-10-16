"""
AutoDiagnostix-AI Agentic Diagnostic Supervisor
Implements autonomous multi-step reasoning, tool dispatching,
and safety-aware diagnostic tree generation.
"""

import json
import re
from typing import Dict, Any, List
from rag_pipeline import AutoDiagnostixRAG


class DiagnosticAgent:
    def __init__(self, rag_engine: AutoDiagnostixRAG = None):
        self.rag = rag_engine or AutoDiagnostixRAG()

    # --- Tool 1: OBD-II Trouble Code Lookup ---
    def tool_lookup_obd2_code(self, dtc_code: str) -> Dict[str, Any]:
        dtc = dtc_code.strip().upper()
        res = self.rag.query(f"FAULT CODE {dtc}", top_k=2)
        return {
            "tool": "lookup_obd2_code",
            "query": dtc,
            "status": "success" if res["retrieved_chunks"] else "not_found",
            "evidence": res["answer"],
            "citations": res["citations"]
        }

    # --- Tool 2: Torque Specification Finder ---
    def tool_get_torque_spec(self, component: str, vehicle_model: str = "") -> Dict[str, Any]:
        query = f"torque specification for {component} {vehicle_model}"
        res = self.rag.query(query, top_k=2)
        return {
            "tool": "get_torque_spec",
            "component": component,
            "vehicle_model": vehicle_model,
            "status": "success",
            "evidence": res["answer"],
            "citations": res["citations"]
        }

    # --- Tool 3: Wiring & Pinout Extractor ---
    def tool_get_wiring_and_pinout(self, circuit: str) -> Dict[str, Any]:
        query = f"pinout resistance voltage connector wiring {circuit}"
        res = self.rag.query(query, top_k=2)
        return {
            "tool": "get_wiring_and_pinout",
            "circuit": circuit,
            "status": "success",
            "evidence": res["answer"],
            "citations": res["citations"]
        }

    # --- Tool 4: High-Voltage Safety Verification ---
    def tool_verify_hv_safety_protocol(self, operation: str) -> Dict[str, Any]:
        res = self.rag.query("EV 4-Step Zero-Voltage Safety Verification Protocol MSD", top_k=1)
        return {
            "tool": "verify_hv_safety_protocol",
            "operation": operation,
            "safety_level": "MANDATORY HIGH VOLTAGE LOCKOUT",
            "protocol_summary": "1. 2m cordon -> 2. Key fob 5m away -> 3. 12V disconnect -> 4. Pull MSD -> 5. 10min capacitor discharge -> 6. Measure <10.0V DC.",
            "citations": res["citations"]
        }

    # --- Autonomous Supervisor Reasoning Loop ---
    def run_diagnostic_workflow(self, technician_input: str) -> Dict[str, Any]:
        """
        Agentic execution plan:
        1. Extract entities (DTCs, torque requests, safety requirements).
        2. Execute appropriate tools.
        3. Synthesize structured diagnostic action plan with full citations.
        """
        action_trace = []
        dtc_pattern = r'\b([P|C|B|U][0-9][0-9A-F]{3})\b'
        found_dtcs = re.findall(dtc_pattern, technician_input.upper())

        is_ev_query = any(w in technician_input.lower() for w in ["ev", "electric", "battery", "bms", "inverter", "hvil", "p0a0c", "p0a80", "high voltage", "msd"])
        is_torque_query = any(w in technician_input.lower() for w in ["torque", "tightening", "nm", "fastener", "bolt"])

        # Step 1: Safety Check
        if is_ev_query:
            action_trace.append({
                "step": 1,
                "action": "Autonomous Safety Interlock Triggered",
                "tool_called": "verify_hv_safety_protocol",
                "result": self.tool_verify_hv_safety_protocol(technician_input)
            })

        # Step 2: DTC Lookups
        for dtc in set(found_dtcs):
            action_trace.append({
                "step": len(action_trace) + 1,
                "action": f"Querying OEM DTC Database for {dtc}",
                "tool_called": "lookup_obd2_code",
                "result": self.tool_lookup_obd2_code(dtc)
            })

        # Step 3: Torque Spec Lookups
        if is_torque_query:
            action_trace.append({
                "step": len(action_trace) + 1,
                "action": "Retrieving Authorized Fastener Torque Tables",
                "tool_called": "get_torque_spec",
                "result": self.tool_get_torque_spec(technician_input)
            })

        # Step 4: General RAG Query if no specific tool matched
        if not action_trace:
            rag_res = self.rag.query(technician_input, top_k=3)
            action_trace.append({
                "step": 1,
                "action": "Direct Hybrid Semantic Search",
                "tool_called": "hybrid_retriever",
                "result": rag_res
            })

        # Compile Consolidated Diagnostic Report
        all_citations = []
        for act in action_trace:
            if "result" in act and "citations" in act["result"]:
                all_citations.extend(act["result"]["citations"])

        # Deduplicate citations
        unique_citations = []
        seen = set()
        for c in all_citations:
            k = (c["document_title"], c["page_number"])
            if k not in seen:
                seen.add(k)
                unique_citations.append(c)

        return {
            "technician_input": technician_input,
            "detected_dtcs": list(set(found_dtcs)),
            "safety_critical": is_ev_query,
            "agent_action_trace": action_trace,
            "consolidated_citations": unique_citations,
            "final_diagnostic_summary": self._generate_agent_summary(technician_input, action_trace, unique_citations)
        }

    def _generate_agent_summary(self, query: str, trace: List[Dict[str, Any]], citations: List[Dict[str, Any]]) -> str:
        lines = [
            "### 🤖 AutoDiagnostix Agentic Supervisory Diagnosis",
            f"**Query Analyzed:** \"{query}\"",
            f"**Tools Executed:** {len(trace)} specialized diagnostic actions\n"
        ]

        for step in trace:
            lines.append(f"#### Step {step['step']}: {step['action']}")
            res = step["result"]
            if "evidence" in res:
                lines.append(res["evidence"])
            elif "protocol_summary" in res:
                lines.append(f"**Safety Protocol:** {res['protocol_summary']}")
            elif "answer" in res:
                lines.append(res["answer"])
            lines.append("")

        lines.append("#### 📌 Authoritative Source Citations:")
        for c in citations:
            lines.append(f"- **{c['document_title']}** (Section: {c['section']}, Page: {c['page_number']})")

        return "\n".join(lines)
