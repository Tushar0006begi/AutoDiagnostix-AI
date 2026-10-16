# VIDEO RECORDING CHECKLIST & BEST PRACTICES

Use this checklist before recording your **5 to 10-minute demonstration video**:

---

## 1. Environment & Setup Checklist
- [ ] Screen resolution set to 1080p (1920x1080) for crisp code and UI readability.
- [ ] Clear desktop of extraneous tabs, personal bookmarks, or personal messaging apps.
- [ ] Good quality microphone (external headset or USB mic preferred) in a quiet room.
- [ ] Audio levels checked: Voice clearly audible without echo or clipping.

## 2. Technical Preparation Checklist
- [ ] Terminal open to `PCCOE_StudentName_PRN_CSx_AIML/Code/`.
- [ ] Web GUI server running: `python3 app_web_gui.py 8080`.
- [ ] Browser window open to `http://localhost:8080` with clean zoom (100% or 110%).
- [ ] Have the 12-slide presentation deck open and ready in fullscreen mode.
- [ ] Have `run_evaluation.py` ready to execute live in a clean terminal window.

## 3. Mandatory Demonstration Content (As per Tata TechPulse Guidelines)
- [ ] **Input Data / Knowledge Base:** Show JSON files in `Input_Data/` with metadata (Doc, Page, Diagram ID).
- [ ] **Model / RAG / Agent Pipeline:** Show architecture diagram and explain hybrid BM25 + dense search.
- [ ] **Sample Interactions:** Click live on Web GUI (P0A0C EV HVIL, P0300 Misfire, ADAS Radar Alignment).
- [ ] **Grounded Responses with Citations:** Show explicit page citations `[Source: ..., Page: ..., Section: ...]`.
- [ ] **Results & Evaluation:** Show terminal execution of `python3 run_evaluation.py` and `evaluation_metrics_summary.md`.
- [ ] **Working Behaviour & Safety Interlocks:** Highlight the red High-Voltage Safety Warning banner when querying EV components.

## 4. Final Verification
- [ ] Video duration is strictly between 5 and 10 minutes (target 7:30 to 8:30).
- [ ] Video file saved in MP4 format (e.g., `Video/AutoDiagnostix_Demonstration_Video.mp4`) and copied to the `Video/` folder before final ZIP archiving.
