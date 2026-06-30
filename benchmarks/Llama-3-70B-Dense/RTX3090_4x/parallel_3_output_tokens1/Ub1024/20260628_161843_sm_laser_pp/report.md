# llama-server PARALLEL-only 1-token response benchmark report

## Test header

- MODEL: `/root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf`
- NGL: `99`
- CTX_SIZE: `107000`
- N_GEN: `128`
- BATCH: `16384`
- UBATCH: `1024`
- CTK: `f16`
- SPLIT_MODE: `layer`
- TENSOR_SPLIT: `18/21/21/21`
- PARALLEL: `3`
- TEMPERATURE: `0.0`
- Effective n_predict: `1` forced by benchmark script
- TURBOPREFILL: `0`
- Parallel mode: `active_slots = PARALLEL only`
- Decode metrics: `not written`
- Group metrics marked `*`: `computed by benchmark script`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_161843/llama_server.log`

## Environment

### TURBOPREFILL

```text
0
```

### nvidia_smi

```text
0, NVIDIA GeForce RTX 3090, 580.126.20, 24576 MiB
1, NVIDIA GeForce RTX 3090, 580.126.20, 24576 MiB
2, NVIDIA GeForce RTX 3090, 580.126.20, 24576 MiB
3, NVIDIA GeForce RTX 3090, 580.126.20, 24576 MiB
```

### nvcc

```text
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2025 NVIDIA Corporation
Built on Wed_Aug_20_01:58:59_PM_PDT_2025
Cuda compilation tools, release 13.0, V13.0.88
Build cuda_13.0.r13.0/compiler.36424714_0
```

### cmake

```text
cmake version 3.28.3

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```

## Server command

```bash
./build/bin/llama-server -m /root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 107000 --override-kv llama.context_length=int:107000 -b 16384 -ub 1024 -np 3 -ctk f16 -sm layer -ts 18/21/21/21
```

## Group response summary

| File | Active slots | Group prompt tokens* | Group wall time s* | Group response tok/s* |
|---|---:|---:|---:|---:|
| ctx_000256.txt | 3 | 762 | 1.46 | 521.13 |
| ctx_000512.txt | 3 | 1530 | 3.03 | 505.21 |
| ctx_001024.txt | 3 | 3066 | 6.09 | 503.77 |
| ctx_002048.txt | 3 | 6138 | 12.30 | 498.93 |
| ctx_004096.txt | 3 | 12282 | 25.43 | 482.95 |
| ctx_008192.txt | 3 | 24570 | 53.15 | 462.31 |
| ctx_016384.txt | 3 | 49146 | 114.44 | 429.46 |
| ctx_032768.txt | 3 | 98301 | 262.33 | 374.72 |

## Per-request server prefill timings

| File | Active slots | Request | Prompt tokens | Server prefill tok/s | Server prefill time s | HTTP wall s |
|---|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 3 | 1 | 254 | 174.82 | 1.45 | 1.46 |
| ctx_000256.txt | 3 | 2 | 254 | 174.63 | 1.45 | 1.46 |
| ctx_000256.txt | 3 | 3 | 254 | 174.44 | 1.46 | 1.46 |
| ctx_000512.txt | 3 | 1 | 510 | 174.29 | 2.93 | 3.03 |
| ctx_000512.txt | 3 | 2 | 510 | 174.34 | 2.93 | 3.02 |
| ctx_000512.txt | 3 | 3 | 510 | 174.33 | 2.93 | 3.03 |
| ctx_001024.txt | 3 | 1 | 1022 | 173.55 | 5.89 | 6.08 |
| ctx_001024.txt | 3 | 2 | 1022 | 173.53 | 5.89 | 6.08 |
| ctx_001024.txt | 3 | 3 | 1022 | 173.55 | 5.89 | 6.08 |
| ctx_002048.txt | 3 | 1 | 2046 | 171.53 | 11.93 | 12.30 |
| ctx_002048.txt | 3 | 2 | 2046 | 171.54 | 11.93 | 12.30 |
| ctx_002048.txt | 3 | 3 | 2046 | 171.54 | 11.93 | 12.30 |
| ctx_004096.txt | 3 | 1 | 4094 | 165.75 | 24.70 | 25.43 |
| ctx_004096.txt | 3 | 2 | 4094 | 165.75 | 24.70 | 25.43 |
| ctx_004096.txt | 3 | 3 | 4094 | 165.74 | 24.70 | 25.43 |
| ctx_008192.txt | 3 | 1 | 8190 | 237.65 | 34.46 | 35.89 |
| ctx_008192.txt | 3 | 2 | 8190 | 237.65 | 34.46 | 35.89 |
| ctx_008192.txt | 3 | 3 | 8190 | 158.39 | 51.71 | 53.14 |
| ctx_016384.txt | 3 | 1 | 16382 | 220.28 | 74.37 | 114.43 |
| ctx_016384.txt | 3 | 2 | 16382 | 219.81 | 74.53 | 77.35 |
| ctx_016384.txt | 3 | 3 | 16382 | 439.93 | 37.24 | 40.06 |
| ctx_032768.txt | 3 | 1 | 32767 | 240.19 | 136.42 | 262.33 |
| ctx_032768.txt | 3 | 2 | 32767 | 383.71 | 85.40 | 91.42 |
| ctx_032768.txt | 3 | 3 | 32767 | 240.21 | 136.41 | 176.91 |

## GPU load during group response window

### ctx_000256.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 117.0 | 130.5 | 18066 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 135.8 | 154.8 | 20060 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 2.5 | 5.0 | 125.2 | 145.9 | 20060 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.5 | 47.0 | 113.3 | 117.8 | 20516 |

### ctx_000512.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 19.3 | 58.0 | 127.0 | 160.6 | 18080 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 39.0 | 63.0 | 140.0 | 179.2 | 20074 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 33.3 | 100.0 | 121.7 | 147.4 | 20074 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 126.6 | 154.0 | 20530 |

### ctx_001024.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 26.0 | 100.0 | 125.8 | 156.5 | 18080 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 21.0 | 71.0 | 148.8 | 180.3 | 20074 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.2 | 100.0 | 138.3 | 175.0 | 20074 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 16.7 | 100.0 | 130.7 | 158.5 | 20530 |

### ctx_002048.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 12.1 | 100.0 | 128.1 | 158.5 | 18080 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 29.1 | 100.0 | 147.4 | 182.8 | 20074 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 27.3 | 100.0 | 134.5 | 176.0 | 20074 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.2 | 100.0 | 136.2 | 167.7 | 20530 |

### ctx_004096.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 19.4 | 100.0 | 128.4 | 161.4 | 18080 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 32.3 | 100.0 | 147.0 | 186.9 | 20074 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 20.7 | 100.0 | 138.5 | 180.4 | 20074 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.3 | 100.0 | 138.5 | 173.9 | 20530 |

### ctx_008192.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 29.0 | 100.0 | 129.7 | 171.0 | 18080 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 22.3 | 100.0 | 152.2 | 198.3 | 20074 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 33.4 | 100.0 | 137.9 | 187.1 | 20074 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 15.4 | 100.0 | 134.6 | 172.6 | 20530 |

### ctx_016384.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 25.0 | 100.0 | 129.7 | 177.2 | 18082 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 22.4 | 100.0 | 152.0 | 205.5 | 20076 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 28.8 | 100.0 | 138.2 | 195.2 | 20076 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 21.6 | 100.0 | 135.5 | 187.9 | 20532 |

### ctx_032768.txt | active_slots=3

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 24.9 | 100.0 | 130.6 | 193.6 | 18082 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 27.6 | 100.0 | 151.3 | 228.7 | 20076 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.7 | 100.0 | 136.1 | 215.1 | 20076 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 20.6 | 100.0 | 135.2 | 210.3 | 20532 |


## Notes

- `*` values are computed by the benchmark script, not reported by llama-server.
- `group_wall_ms*` is measured from immediately before releasing the PARALLEL request group to after the last HTTP response in that group is received.
- `group_response_tok_s* = sum(prompt_tokens for all requests in the group) / group_wall_time`.
- Each request is forced to `n_predict=1`, so the group wall time is treated as prefill-dominated server response time with a one-token answer.
- Per-request prefill timing columns are still the server-reported values from each individual HTTP response.
