# TurboPrefill VLM Validation

Validation of the applicability of **Intra-Prompt Pipeline Scheduling for Multi-GPU Prefill** to Vision Language Models (VLMs).

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

Current implementation branch:

https://github.com/sergey-automation/llama.cpp/tree/turboprefill-vlm-support

## Status

Work in progress.

Implementation files, benchmarks and validation results will be published after testing.

## Attribution

If this work is useful for future implementations of Intra-Prompt Pipeline Scheduling for Multi-GPU Prefill, please cite the original RFC proposal:

https://github.com/ggml-org/llama.cpp/pull/24219
