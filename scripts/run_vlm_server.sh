#!/bin/bash
set -e

CTX_SIZE="${CTX_SIZE:-16384}"
BATCH_SIZE="${BATCH_SIZE:-16384}"
UBATCH_SIZE="${UBATCH_SIZE:-64}"
N_PREDICT="${N_PREDICT:-128}"
N_PARALLEL="${N_PARALLEL:-1}"

N_GPU_LAYERS="${N_GPU_LAYERS:-99}"
SPLIT_MODE="${SPLIT_MODE:-layer}"
#TENSOR_SPLIT="${TENSOR_SPLIT:-"5/9/9/9/9/9/9/8/8/7"}"

#GPU0 assigned a smaller model fraction due to higher observed utilization during the VLM image-processing stage.
TENSOR_SPLIT="${TENSOR_SPLIT:-"1/9/9/9/9/9/9/9/9/9"}"

CUDA_DEVICES="${CUDA_DEVICES:-}"
TURBOPREFILL="${TURBOPREFILL:-1}"

FLASH_ATTN="${FLASH_ATTN:-on}"
CACHE_TYPE_K="${CACHE_TYPE_K:-f16}"
CACHE_TYPE_V="${CACHE_TYPE_V:-f16}"

IMAGE_MIN_TOKENS="${IMAGE_MIN_TOKENS:-256}"
IMAGE_MAX_TOKENS="${IMAGE_MAX_TOKENS:-6776}"

HOST="${HOST:-0.0.0.0}"
PORT="${PORT:-8081}"

CACHE_RAM="${CACHE_RAM:-0}"
PROMPT_CACHE="${PROMPT_CACHE:-0}"
METRICS="${METRICS:-1}"
WEBUI="${WEBUI:-1}"
WARMUP="${WARMUP:-1}"
KV_UNIFIED="${KV_UNIFIED:-0}"
OFFLINE="${OFFLINE:-1}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LLAMA_BIN="$SCRIPT_DIR/build/bin/llama-server"

MODEL_FILE="${MODEL_FILE:-$SCRIPT_DIR/../../models/Qwen2.5-VL-72B/Qwen2.5-VL-72B-Instruct-Q4_K_M.gguf}"
MMPROJ_FILE="${MMPROJ_FILE:-$SCRIPT_DIR/../../models/Qwen2.5-VL-72B/mmproj-Qwen2.5-VL-72B-Instruct-Q8_0.gguf}"
MEDIA_PATH="${MEDIA_PATH:-$SCRIPT_DIR/resolution_samples}"

LOG_DIR="$SCRIPT_DIR/logs"
LOG_FILE="$LOG_DIR/vlm_server.log"
mkdir -p "$LOG_DIR"

[ -x "$LLAMA_BIN" ] || { echo "ERROR: llama-server not found: $LLAMA_BIN"; exit 1; }
[ -f "$MODEL_FILE" ] || { echo "ERROR: model not found: $MODEL_FILE"; exit 1; }
[ -f "$MMPROJ_FILE" ] || { echo "ERROR: mmproj not found: $MMPROJ_FILE"; exit 1; }
[ -d "$MEDIA_PATH" ] || { echo "ERROR: media path not found: $MEDIA_PATH"; exit 1; }

ARGS=(
  -m "$MODEL_FILE"
  --mmproj "$MMPROJ_FILE"
  -c "$CTX_SIZE"
  -b "$BATCH_SIZE"
  -ub "$UBATCH_SIZE"
  -n "$N_PREDICT"
  -np "$N_PARALLEL"
  -ngl "$N_GPU_LAYERS"
  -sm "$SPLIT_MODE"
  -fa "$FLASH_ATTN"
  -ctk "$CACHE_TYPE_K"
  -ctv "$CACHE_TYPE_V"
  --image-min-tokens "$IMAGE_MIN_TOKENS"
  --image-max-tokens "$IMAGE_MAX_TOKENS"
  --media-path "$MEDIA_PATH"
  --cache-ram "$CACHE_RAM"
  --host "$HOST"
  --port "$PORT"
  --log-file "$LOG_FILE"
)

[ -n "$TENSOR_SPLIT" ] && ARGS+=(-ts "$TENSOR_SPLIT")
[ "$PROMPT_CACHE" = "0" ] && ARGS+=(--no-cache-prompt)
[ "$METRICS" = "1" ] && ARGS+=(--metrics)
[ "$WEBUI" = "0" ] && ARGS+=(--no-webui)
[ "$WARMUP" = "0" ] && ARGS+=(--no-warmup)
[ "$KV_UNIFIED" = "1" ] && ARGS+=(--kv-unified)
[ "$OFFLINE" = "1" ] && ARGS+=(--offline)

echo "============================================================"
echo "VLM SERVER CONFIG"
echo "============================================================"
echo "LLAMA_BIN         : $LLAMA_BIN"
echo "MODEL_FILE        : $MODEL_FILE"
echo "MMPROJ_FILE       : $MMPROJ_FILE"
echo "MEDIA_PATH        : $MEDIA_PATH"
echo "LOG_FILE          : $LOG_FILE"
echo "CTX_SIZE          : $CTX_SIZE"
echo "BATCH_SIZE        : $BATCH_SIZE"
echo "UBATCH_SIZE       : $UBATCH_SIZE"
echo "N_PREDICT         : $N_PREDICT"
echo "N_PARALLEL        : $N_PARALLEL"
echo "N_GPU_LAYERS      : $N_GPU_LAYERS"
echo "SPLIT_MODE        : $SPLIT_MODE"
echo "TENSOR_SPLIT      : $TENSOR_SPLIT"
echo "FLASH_ATTN        : $FLASH_ATTN"
echo "CACHE_TYPE_K      : $CACHE_TYPE_K"
echo "CACHE_TYPE_V      : $CACHE_TYPE_V"
echo "IMAGE_MIN_TOKENS  : $IMAGE_MIN_TOKENS"
echo "IMAGE_MAX_TOKENS  : $IMAGE_MAX_TOKENS"
echo "TURBOPREFILL      : $TURBOPREFILL"
echo "CUDA_DEVICES      : $CUDA_DEVICES"
echo "CACHE_RAM         : $CACHE_RAM"
echo "PROMPT_CACHE      : $PROMPT_CACHE"
echo "METRICS           : $METRICS"
echo "WEBUI             : $WEBUI"
echo "WARMUP            : $WARMUP"
echo "KV_UNIFIED        : $KV_UNIFIED"
echo "OFFLINE           : $OFFLINE"
echo "HOST              : $HOST"
echo "PORT              : $PORT"
echo "============================================================"

if [ -n "$CUDA_DEVICES" ]; then
  CUDA_VISIBLE_DEVICES="$CUDA_DEVICES" TURBOPREFILL="$TURBOPREFILL" exec "$LLAMA_BIN" "${ARGS[@]}"
else
  TURBOPREFILL="$TURBOPREFILL" exec "$LLAMA_BIN" "${ARGS[@]}"
fi
