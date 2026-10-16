#!/usr/bin/env python3
"""
AutoDiagnostix-AI Interactive CLI Terminal
Provides real-time interactive automotive workshop diagnostic consultation
with grounded source citations and safety warnings.
"""

import sys
import time
from rag_pipeline import AutoDiagnostixRAG
from agent_diagnostic_logic import DiagnosticAgent


def print_banner():
    banner = """
================================================================================
   🚗  AUTODIAGNOSTIX-AI: WORKSHOP DIAGNOSTIC & RAG CITATION CONSOLE  🚗
        Developed for Tata TechPulse & PCCOE CS-AIML Applied AI Project
================================================================================
* Multi-Modal OEM Knowledge Base: Tata ICE (2.0L/1.2L), EV Powertrains, ADAS L2
* Grounded Answers with Verifiable Chapter, Section, Page & Diagram Citations
================================================================================
    """
    print(banner)


def main():
    print_banner()
    print("[*] Initializing AutoDiagnostix RAG Engine & Diagnostic Agent...")
    rag = AutoDiagnostixRAG()
    agent = DiagnosticAgent(rag)
    print(f"[✓] System Ready! Indexed {rag.total_chunks} OEM manual chunks.\n")

    print("Quick Test Examples:")
    print("  1. 'What is the diagnostic procedure for fault code P0A0C?' (EV HVIL)")
    print("  2. 'Engine is misfiring with DTC P0300 on Revotron 1.2L. What are the spark plug specs?'")
    print("  3. 'How to align the 77GHz mid-range radar sensor under code C1B01?'")
    print("  4. 'What are the mandatory PPE and steps for the EV zero-voltage safety protocol?'")
    print("  5. 'What is the wheel lug nut torque specification for Harrier and Safari?'\n")
    print("Type 'exit' or 'quit' to close.\n" + "-" * 80)

    while True:
        try:
            user_input = input("\n👨‍🔧 [Enter DTC / Vehicle Diagnostic Query] > ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "q"]:
                print("\n[!] Exiting AutoDiagnostix-AI. Drive safe!")
                break

            print("\n🔍 [AutoDiagnostix Supervisor] Analyzing query & retrieving grounded context...")
            t0 = time.time()
            result = agent.run_diagnostic_workflow(user_input)
            latency_ms = (time.time() - t0) * 1000

            print("\n" + "=" * 80)
            print(result["final_diagnostic_summary"])
            print("=" * 80)

            print(f"\n⏱️  Execution Latency: {latency_ms:.2f} ms")
            print(f"🛡️  Safety Critical Alert: {'ACTIVE (High Voltage)' if result['safety_critical'] else 'Normal'}")
            print(f"📚  Verified OEM Citations: {len(result['consolidated_citations'])} source reference(s)\n")
            print("-" * 80)

        except (KeyboardInterrupt, EOFError):
            print("\n\n[!] Session terminated by user.")
            break


if __name__ == "__main__":
    main()
