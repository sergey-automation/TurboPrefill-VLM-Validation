# TurboPrefill benchmark configuration for llama-server.
# Edit MODEL, CONTEXTS_DIR, OUTPUT_DIR and TENSOR_SPLIT for your machine.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# MODEL="/home/serg/workspace/models/gpt-oss-20b-Q4_K_M.gguf"
# MODEL="/home/serg/workspace/models/Llama-3-70B/meta-llama-3-70b-instruct.Q4_K_M.gguf"
MODEL = "/root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf"

# CONTEXTS_DIR="$SCRIPT_DIR/contexts_gpt_tokenizer"

CONTEXTS_DIR="$SCRIPT_DIR/contexts_llama3_70b"

OUTPUT_DIR="$SCRIPT_DIR/bench_reports_Llama3_70B"

# For 4 identical GPUs use: 1/1/1/1
# For 10 P104-100 GPUs used in early tests: 2/4/4/4/4/4/4/4/3/3
# TENSOR_SPLIT="1/1/1/1/1/1/1/1/1/1"
# TENSOR_SPLIT="5/8/9/9/9/9/9/9/8/6"
# TENSOR_SPLIT="5/7/7/7/7/7/7/7/7/7/7/6"
 TENSOR_SPLIT="18/21/21/21"
# TENSOR_SPLIT="1/1/1/1"


HOST="0.0.0.0"
PORT=8081

NGL=99
CTX_SIZE=107000
# CTX_SIZE=131070
# CTX_SIZE=131070

N_GEN=1

BATCH=16384


UBATCH=1024
PARALLEL=1

CTK=f16
SPLIT_MODE=layer
# SPLIT_MODE=tensor

TEMPERATURE=0.0
MONITOR_INTERVAL=1

# Debug environment passed to llama-server.
# Keep GGML_SCHED_DEBUG=0 for public benchmark runs unless you need scheduler diagnostics.
GGML_SCHED_DEBUG=1
GGML_CUDA_DEBUG=1

