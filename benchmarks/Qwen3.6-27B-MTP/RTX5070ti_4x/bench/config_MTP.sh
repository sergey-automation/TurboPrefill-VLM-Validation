# TurboPrefill benchmark configuration for llama-server.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD_BIN_DIR="$SCRIPT_DIR/build/bin"

# LLAMA_SERVER_BIN="/home/serg/workspace/versions/TurboPrefill-MTP/build/bin/llama-server"
# LOCAL_LD_LIBRARY_PATH="/home/serg/workspace/versions/TurboPrefill-MTP/build/bin"

LLAMA_SERVER_BIN="$SCRIPT_DIR/build/bin/llama-server"
LOCAL_LD_LIBRARY_PATH="$SCRIPT_DIR/build/bin"

UNSET_LD_PRELOAD=1


# MODEL="/mnt/models/AI/LLM/Qwen3.6-27B/Qwen3.6-27B-MTP-Q8_0.gguf"
# MMPROJ="/mnt/models/AI/LLM/Qwen3.6-27B/mmproj-F16.gguf"
MODEL="/workspace/models/Qwen3.6-27B-MTP/Qwen3.6-27B-Q8_0.gguf"
MMPROJ="/workspace/models/Qwen3.6-27B-MTP/mmproj-F16.gguf"


CONTEXTS_DIR="$SCRIPT_DIR/contexts_llama3_70b"
OUTPUT_DIR="$SCRIPT_DIR/bench_reports_MTP"

# TENSOR_SPLIT="5/8/9/9/9/9/9/9/8/6"
TENSOR_SPLIT="1/1/1/1"
CUDA_VISIBLE_DEVICES="3,2,1,0"

HOST="0.0.0.0"
PORT=8081

NGL=999

CTX_SIZE=67000

N_GEN=512

BATCH=8192


UBATCH=128
PARALLEL=1

SPEC_TYPE=draft-mtp
SPEC_DRAFT_N_MAX=4

CTK=f16
SPLIT_MODE=layer
TEMPERATURE=0.8
MONITOR_INTERVAL=100
TURBOPREFILL="${TURBOPREFILL:-0}"
LOG_LEVEL=4


# Debug environment passed to llama-server.
# Keep GGML_SCHED_DEBUG=0 for public benchmark runs unless you need scheduler diagnostics.
GGML_SCHED_DEBUG=1
GGML_CUDA_DEBUG=1

