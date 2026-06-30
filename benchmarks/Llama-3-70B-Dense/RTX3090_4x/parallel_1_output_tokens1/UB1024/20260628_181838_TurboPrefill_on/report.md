# llama-server PARALLEL-only 1-token response benchmark report

## Test header

- MODEL: `/root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf`
- NGL: `99`
- CTX_SIZE: `107000`
- N_GEN: `1`
- BATCH: `16384`
- UBATCH: `1024`
- CTK: `f16`
- SPLIT_MODE: `layer`
- TENSOR_SPLIT: `18/21/21/21`
- PARALLEL: `1`
- TEMPERATURE: `0.0`
- Effective n_predict: `1` forced by benchmark script
- TURBOPREFILL: `1`
- Parallel mode: `active_slots = PARALLEL only`
- Decode metrics: `not written`
- Group metrics marked `*`: `computed by benchmark script`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_181838/llama_server.log`

## Environment

### TURBOPREFILL

```text
1
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
./build/bin/llama-server -m /root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 107000 --override-kv llama.context_length=int:107000 -b 16384 -ub 1024 -np 1 -ctk f16 -sm layer -ts 18/21/21/21
```

## Group response summary

| File | Active slots | Group prompt tokens* | Group wall time s* | Group response tok/s* |
|---|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 254 | 0.55 | 463.28 |
| ctx_000512.txt | 1 | 510 | 1.08 | 473.46 |
| ctx_001024.txt | 1 | 1022 | 2.18 | 468.96 |
| ctx_002048.txt | 1 | 2046 | 4.35 | 469.86 |
| ctx_004096.txt | 1 | 4094 | 6.50 | 630.13 |
| ctx_008192.txt | 1 | 8190 | 10.58 | 774.01 |
| ctx_016384.txt | 1 | 16382 | 19.73 | 830.32 |
| ctx_032768.txt | 1 | 32767 | 47.04 | 696.64 |
| ctx_065536.txt | 1 | 65534 | 126.96 | 516.18 |
| ctx_100000.txt | 1 | 99998 | 256.82 | 389.37 |

## Per-request server prefill timings

| File | Active slots | Request | Prompt tokens | Server prefill tok/s | Server prefill time s | HTTP wall s |
|---|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 254 | 466.93 | 0.54 | 0.55 |
| ctx_000512.txt | 1 | 1 | 510 | 518.97 | 0.98 | 1.08 |
| ctx_001024.txt | 1 | 1 | 1022 | 515.64 | 1.98 | 2.18 |
| ctx_002048.txt | 1 | 1 | 2046 | 514.12 | 3.98 | 4.35 |
| ctx_004096.txt | 1 | 1 | 4094 | 709.51 | 5.77 | 6.50 |
| ctx_008192.txt | 1 | 1 | 8190 | 893.91 | 9.16 | 10.58 |
| ctx_016384.txt | 1 | 1 | 16382 | 968.46 | 16.92 | 19.73 |
| ctx_032768.txt | 1 | 1 | 32767 | 798.10 | 41.06 | 47.03 |
| ctx_065536.txt | 1 | 1 | 65534 | 571.62 | 114.65 | 126.96 |
| ctx_100000.txt | 1 | 1 | 99998 | 429.20 | 232.99 | 256.82 |

## GPU load during group response window

### ctx_000256.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 6.0 | 6.0 | 99.8 | 99.8 | 19270 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 113.6 | 113.6 | 20554 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 109.1 | 109.1 | 20554 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 109.1 | 109.1 | 21010 |

### ctx_000512.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 110.8 | 110.8 | 19270 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 126.5 | 126.5 | 20566 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 116.5 | 116.5 | 20574 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 116.2 | 116.2 | 21030 |

### ctx_001024.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 141.8 | 157.2 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 50.0 | 100.0 | 160.3 | 176.0 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 117.4 | 136.6 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 115.5 | 132.0 | 21046 |

### ctx_002048.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.2 | 1.0 | 126.4 | 158.3 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.0 | 100.0 | 148.1 | 182.8 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 16.8 | 67.0 | 135.5 | 168.2 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.0 | 100.0 | 133.8 | 162.3 | 21046 |

### ctx_004096.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 50.0 | 100.0 | 132.7 | 205.8 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 16.7 | 100.0 | 162.4 | 220.4 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 50.0 | 100.0 | 150.8 | 215.3 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 16.7 | 100.0 | 136.7 | 205.6 | 21046 |

### ctx_008192.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 21.9 | 100.0 | 143.1 | 213.2 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 50.3 | 100.0 | 169.5 | 235.9 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 27.9 | 100.0 | 157.3 | 219.2 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 40.0 | 100.0 | 154.8 | 222.9 | 21046 |

### ctx_016384.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 36.8 | 100.0 | 150.9 | 211.2 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 53.1 | 100.0 | 177.0 | 237.0 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 40.6 | 100.0 | 162.2 | 213.1 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 33.3 | 100.0 | 157.1 | 209.6 | 21046 |

### ctx_032768.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 34.5 | 100.0 | 148.8 | 219.6 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 47.3 | 100.0 | 177.7 | 236.7 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 39.1 | 100.0 | 159.8 | 227.9 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 36.8 | 100.0 | 157.0 | 225.8 | 21046 |

### ctx_065536.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 42.2 | 100.0 | 147.1 | 217.0 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 43.9 | 100.0 | 173.7 | 249.4 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 39.0 | 100.0 | 158.8 | 241.6 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 39.2 | 100.0 | 155.9 | 237.7 | 21046 |

### ctx_100000.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 39.5 | 100.0 | 144.1 | 244.8 | 19296 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 42.4 | 100.0 | 167.2 | 249.6 | 20592 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 38.1 | 100.0 | 154.1 | 246.2 | 20592 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 36.2 | 100.0 | 151.5 | 248.5 | 21048 |


## Notes

- `*` values are computed by the benchmark script, not reported by llama-server.
- `group_wall_ms*` is measured from immediately before releasing the PARALLEL request group to after the last HTTP response in that group is received.
- `group_response_tok_s* = sum(prompt_tokens for all requests in the group) / group_wall_time`.
- Each request is forced to `n_predict=1`, so the group wall time is treated as prefill-dominated server response time with a one-token answer.
- Per-request prefill timing columns are still the server-reported values from each individual HTTP response.
