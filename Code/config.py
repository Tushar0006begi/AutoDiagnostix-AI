"""
AutoDiagnostix-AI Configuration Module
Defines absolute and relative paths, model hyperparameters, and retrieval settings.
"""

import os
from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DATA_DIR = BASE_DIR / "Input_Data"
EVALUATION_DIR = BASE_DIR / "Evaluation_Results"
PROMPTS_CONFIG_DIR = BASE_DIR / "Model_Prompts_Config"
DOCUMENTATION_DIR = BASE_DIR / "Documentation"

# Knowledge Base Files
KB_FILES = [
    INPUT_DATA_DIR / "tata_ev_powertrain_troubleshooting_manual.json",
    INPUT_DATA_DIR / "tata_ice_engine_obd2_diagnostic_codes.json",
    INPUT_DATA_DIR / "tata_adas_and_telematics_service_manual.json",
    INPUT_DATA_DIR / "vehicle_maintenance_schedule_sops.json",
]

# Retrieval Hyperparameters
BM25_ALPHA = 0.45       # Weight for lexical search
DENSE_BETA = 0.55       # Weight for dense semantic search
DEFAULT_TOP_K = 3       # Top passages to feed to generation context
MIN_SIMILARITY_SCORE = 0.15

# Model Settings
LLM_PROVIDER = "Google Gemini / Fallback Grounded Synthesizer"
PRIMARY_MODEL = "gemini-1.5-pro"
FALLBACK_MODEL = "gemini-1.5-flash"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
TEMPERATURE = 0.1
MAX_OUTPUT_TOKENS = 1200

# Evaluation Benchmarks
GROUND_TRUTH_BENCHMARK_FILE = EVALUATION_DIR / "test_ground_truth_qa_pairs.json"
EVAL_REPORT_OUTPUT = EVALUATION_DIR / "evaluation_report.json"
EVAL_SUMMARY_OUTPUT = EVALUATION_DIR / "evaluation_metrics_summary.md"
