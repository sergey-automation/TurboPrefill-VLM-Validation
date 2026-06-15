# TurboPrefill VLM Validation

Validation of the applicability of **Intra-Prompt Pipeline Scheduling for Multi-GPU Prefill** to Vision Language Models (VLMs).

## Example Input

![FHD giraffe sample](resolution_samples/giraffe_FHD_1920x1080.jpg)

## Validation Task

Question:

> What is happening in this image? Describe the animals, their approximate number, activity, environment, and colors. Which animal appears to be the leader of the group, and what five visual clues made you reach that conclusion? Use no more than 50 words.

Example answer:

> Eight giraffes are walking across a grassy wetland near a river. The animals are light brown with darker patches. The leading giraffe appears to guide the group. Clues: front position, direction of movement, spacing, head orientation, and group alignment.


## Key Result

Validation on Vision Language Models demonstrates that **Intra-Prompt Pipeline Scheduling for Multi-GPU Prefill** can significantly reduce user waiting time before answer generation without changing model weights, architecture, quantization, prompts, or inference mathematics.

On the tested multi-GPU configuration, the scheduling changes reduced the prefill stage latency by approximately **2.24×**, resulting in approximately **2.12×** lower end-to-end response time for a 1920×1080 image workload.

The observed improvement was achieved solely through changes in execution scheduling during the prefill stage.

## Test Configuration

Model:

- Qwen2.5-VL-72B-Instruct-Q4_K_M.gguf
- mmproj-Qwen2.5-VL-72B-Instruct-Q8_0.gguf

Primary metric:

- TTFT (Time-To-First-Token)

## Background

The original scheduling mechanism was proposed in:

**[RFC][PoC] Intra-Prompt Pipeline Scheduling for Multi-GPU Prefill**

https://github.com/ggml-org/llama.cpp/pull/24219

The original proof-of-concept implementation is available at:

https://github.com/sergey-automation/TurboPrefill

## Purpose

This repository validates the applicability of Intra-Prompt Pipeline Scheduling for Multi-GPU Prefill to Vision Language Models.

The objective is not to introduce a new scheduling mechanism, but to demonstrate that the original mechanism is applicable beyond text-only LLM workloads.


## Validation Implementation

Reference implementation branch:

https://github.com/sergey-automation/llama.cpp/tree/turboprefill-vlm-support

## Scope of the Current Implementation

The original TurboPrefill PoC intentionally used a conservative dispatcher and left some eligible workloads on the standard llama.cpp execution path.

The current validation implementation enables additional workloads that are still within the original concept of **Intra-Prompt Pipeline Scheduling for Multi-GPU Prefill**, but were not enabled in the first PoC.

Additional workloads currently enabled for the TurboPrefill execution path:

- Execution of Text LLM workloads.
- Execution of Vision Language Model (VLM) workloads.
- Execution of multiple concurrent requests in multi-user server mode, provided that requests from different users are not mixed within the same TurboPrefill batch.

## Status

Work in progress.

Implementation files, scripts, input samples, and benchmark logs are published in this repository.

## Repository Structure

- `files/` — modified llama.cpp source files used for the validation branch.
- `scripts/` — scripts used to run the VLM server and resolution tests.
- `resolution_samples/` — input images used for validation.
- `benchmarks/` — raw benchmark reports and server logs.



## Reproducing the Validation

### 1. Obtain the reference implementation

The validation was performed using the following reference implementation branch:

https://github.com/sergey-automation/llama.cpp/tree/turboprefill-vlm-support

```bash
git clone https://github.com/sergey-automation/llama.cpp.git
cd llama.cpp
git checkout turboprefill-vlm-support
```

### 2. Build llama.cpp

Build the reference implementation.

### 3. Baseline measurement

Start the VLM server with TurboPrefill disabled:

```text
TURBOPREFILL=0 ./run_vlm_server.sh
```

 Run the benchmark:

```text
python3 run_vlm_resolution.py
```

### 4. TurboPrefill measurement

Start the VLM server with TurboPrefill enabled:

```text
TURBOPREFILL=1 ./run_vlm_server.sh
```
 Run the benchmark:

```text
python3 run_vlm_resolution.py
```

### 5. Compare results

Input images:

```text
resolution_samples/
```

Reference benchmark reports and logs:

```text
benchmarks/
```

Compare generated reports against the published benchmark logs included in this repository.

  
## Attribution

If this work is useful for future implementations of Intra-Prompt Pipeline Scheduling for Multi-GPU Prefill, please cite the original RFC proposal:

https://github.com/ggml-org/llama.cpp/pull/24219
