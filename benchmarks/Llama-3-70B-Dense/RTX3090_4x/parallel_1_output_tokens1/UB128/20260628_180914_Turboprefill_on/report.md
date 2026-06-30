# llama-server PARALLEL-only 1-token response benchmark report

## Test header

- MODEL: `/root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf`
- NGL: `99`
- CTX_SIZE: `107000`
- N_GEN: `1`
- BATCH: `16384`
- UBATCH: `128`
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
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_180914/llama_server.log`

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
./build/bin/llama-server -m /root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 107000 --override-kv llama.context_length=int:107000 -b 16384 -ub 128 -np 1 -ctk f16 -sm layer -ts 18/21/21/21
```

## Group response summary

| File | Active slots | Group prompt tokens* | Group wall time s* | Group response tok/s* |
|---|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 254 | 0.57 | 442.10 |
| ctx_000512.txt | 1 | 510 | 0.85 | 597.42 |
| ctx_001024.txt | 1 | 1022 | 1.27 | 803.12 |
| ctx_002048.txt | 1 | 2046 | 2.21 | 927.25 |
| ctx_004096.txt | 1 | 4094 | 4.09 | 1001.78 |
| ctx_008192.txt | 1 | 8190 | 7.97 | 1027.03 |
| ctx_016384.txt | 1 | 16382 | 16.28 | 1006.01 |
| ctx_032768.txt | 1 | 32767 | 40.41 | 810.90 |
| ctx_065536.txt | 1 | 65534 | 110.65 | 592.24 |
| ctx_100000.txt | 1 | 99998 | 229.03 | 436.62 |

## Per-request server prefill timings

| File | Active slots | Request | Prompt tokens | Server prefill tok/s | Server prefill time s | HTTP wall s |
|---|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 254 | 445.07 | 0.57 | 0.57 |
| ctx_000512.txt | 1 | 1 | 510 | 676.09 | 0.75 | 0.85 |
| ctx_001024.txt | 1 | 1 | 1022 | 945.10 | 1.08 | 1.27 |
| ctx_002048.txt | 1 | 1 | 2046 | 1113.18 | 1.84 | 2.21 |
| ctx_004096.txt | 1 | 1 | 4094 | 1216.65 | 3.36 | 4.09 |
| ctx_008192.txt | 1 | 1 | 8190 | 1249.99 | 6.55 | 7.97 |
| ctx_016384.txt | 1 | 1 | 16382 | 1212.95 | 13.51 | 16.28 |
| ctx_032768.txt | 1 | 1 | 32767 | 951.39 | 34.44 | 40.41 |
| ctx_065536.txt | 1 | 1 | 65534 | 666.54 | 98.32 | 110.65 |
| ctx_100000.txt | 1 | 1 | 99998 | 487.29 | 205.21 | 229.03 |

## GPU load during group response window

### ctx_000256.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 103.7 | 103.7 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 116.5 | 116.5 | 19330 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 109.5 | 109.5 | 19330 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 110.2 | 110.2 | 19698 |

### ctx_000512.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 102.2 | 102.2 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 124.0 | 124.0 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 2.0 | 2.0 | 116.6 | 116.6 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 2.0 | 2.0 | 116.8 | 116.8 | 19706 |

### ctx_001024.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 19.0 | 38.0 | 141.8 | 157.8 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 35.0 | 70.0 | 162.1 | 180.5 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 16.0 | 32.0 | 154.9 | 174.4 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 147.6 | 160.8 | 19706 |

### ctx_002048.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 30.0 | 60.0 | 127.1 | 154.5 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 35.0 | 70.0 | 143.0 | 169.7 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 41.0 | 82.0 | 131.9 | 156.6 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 38.0 | 76.0 | 128.6 | 148.5 | 19706 |

### ctx_004096.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 52.5 | 73.0 | 167.2 | 195.1 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 61.2 | 82.0 | 191.1 | 226.6 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 61.0 | 82.0 | 183.8 | 217.2 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 54.8 | 79.0 | 180.1 | 212.2 | 19706 |

### ctx_008192.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 48.4 | 75.0 | 160.8 | 195.9 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 56.1 | 84.0 | 188.0 | 228.5 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 56.0 | 83.0 | 178.7 | 218.9 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 52.9 | 77.0 | 174.6 | 212.6 | 19706 |

### ctx_016384.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 47.7 | 75.0 | 162.3 | 196.3 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 51.7 | 84.0 | 190.2 | 228.9 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 48.3 | 79.0 | 181.0 | 220.1 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 45.8 | 78.0 | 175.7 | 211.0 | 19706 |

### ctx_032768.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 47.8 | 87.0 | 158.4 | 205.0 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 52.6 | 96.0 | 188.0 | 240.6 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 54.1 | 96.0 | 174.9 | 228.9 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 48.2 | 91.0 | 168.7 | 214.1 | 19706 |

### ctx_065536.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 45.8 | 100.0 | 158.1 | 205.7 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 52.5 | 100.0 | 185.5 | 242.8 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 50.8 | 100.0 | 171.1 | 227.9 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 44.3 | 100.0 | 167.5 | 215.8 | 19706 |

### ctx_100000.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 46.3 | 100.0 | 153.7 | 205.9 | 17128 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 47.9 | 100.0 | 178.7 | 239.7 | 19338 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 48.2 | 100.0 | 165.5 | 224.5 | 19338 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 43.7 | 100.0 | 162.1 | 214.7 | 19706 |


## Notes

- `*` values are computed by the benchmark script, not reported by llama-server.
- `group_wall_ms*` is measured from immediately before releasing the PARALLEL request group to after the last HTTP response in that group is received.
- `group_response_tok_s* = sum(prompt_tokens for all requests in the group) / group_wall_time`.
- Each request is forced to `n_predict=1`, so the group wall time is treated as prefill-dominated server response time with a one-token answer.
- Per-request prefill timing columns are still the server-reported values from each individual HTTP response.
