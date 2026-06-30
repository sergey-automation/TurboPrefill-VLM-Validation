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
- TURBOPREFILL: `0`
- Parallel mode: `active_slots = PARALLEL only`
- Decode metrics: `not written`
- Group metrics marked `*`: `computed by benchmark script`
- llama_server_log: `/workspace/llama.cpp/bench_reports_Llama3_70B/20260628_182731/llama_server.log`

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
./build/bin/llama-server -m /root/workspace/models/Llama-3-70B/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -ngl 99 -c 107000 --override-kv llama.context_length=int:107000 -b 16384 -ub 1024 -np 1 -ctk f16 -sm layer -ts 18/21/21/21
```

## Group response summary

| File | Active slots | Group prompt tokens* | Group wall time s* | Group response tok/s* |
|---|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 254 | 0.55 | 461.47 |
| ctx_000512.txt | 1 | 510 | 1.09 | 469.99 |
| ctx_001024.txt | 1 | 1022 | 2.19 | 467.09 |
| ctx_002048.txt | 1 | 2046 | 4.39 | 466.28 |
| ctx_004096.txt | 1 | 4094 | 8.92 | 458.85 |
| ctx_008192.txt | 1 | 8190 | 18.57 | 441.06 |
| ctx_016384.txt | 1 | 16382 | 39.92 | 410.33 |
| ctx_032768.txt | 1 | 32767 | 90.99 | 360.14 |
| ctx_065536.txt | 1 | 65534 | 230.91 | 283.81 |
| ctx_100000.txt | 1 | 99998 | 447.66 | 223.38 |

## Per-request server prefill timings

| File | Active slots | Request | Prompt tokens | Server prefill tok/s | Server prefill time s | HTTP wall s |
|---|---:|---:|---:|---:|---:|---:|
| ctx_000256.txt | 1 | 1 | 254 | 465.04 | 0.55 | 0.55 |
| ctx_000512.txt | 1 | 1 | 510 | 517.19 | 0.99 | 1.08 |
| ctx_001024.txt | 1 | 1 | 1022 | 512.70 | 1.99 | 2.19 |
| ctx_002048.txt | 1 | 1 | 2046 | 509.25 | 4.02 | 4.39 |
| ctx_004096.txt | 1 | 1 | 4094 | 499.54 | 8.20 | 8.92 |
| ctx_008192.txt | 1 | 1 | 8190 | 477.79 | 17.14 | 18.57 |
| ctx_016384.txt | 1 | 1 | 16382 | 441.82 | 37.08 | 39.92 |
| ctx_032768.txt | 1 | 1 | 32767 | 385.46 | 85.01 | 90.98 |
| ctx_065536.txt | 1 | 1 | 65534 | 299.89 | 218.53 | 230.91 |
| ctx_100000.txt | 1 | 1 | 99998 | 235.95 | 423.81 | 447.66 |

## GPU load during group response window

### ctx_000256.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 15.0 | 15.0 | 102.3 | 102.3 | 19270 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 115.0 | 115.0 | 20554 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 109.5 | 109.5 | 20554 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 110.9 | 110.9 | 21010 |

### ctx_000512.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 111.2 | 111.2 | 19270 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 128.0 | 128.0 | 20566 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 117.2 | 117.2 | 20566 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 118.1 | 118.1 | 21030 |

### ctx_001024.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.0 | 0.0 | 142.7 | 158.0 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 50.0 | 100.0 | 162.6 | 179.6 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 6.5 | 13.0 | 119.0 | 137.5 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 0.0 | 0.0 | 116.8 | 133.0 | 21046 |

### ctx_002048.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 0.2 | 1.0 | 127.7 | 159.1 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 44.0 | 100.0 | 149.0 | 184.5 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 15.0 | 60.0 | 135.8 | 168.3 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 20.2 | 81.0 | 136.3 | 165.7 | 21046 |

### ctx_004096.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 20.4 | 100.0 | 128.6 | 159.9 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.0 | 100.0 | 151.0 | 188.5 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 16.9 | 100.0 | 135.7 | 177.1 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.5 | 100.0 | 131.7 | 162.5 | 21046 |

### ctx_008192.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 14.6 | 100.0 | 125.6 | 166.9 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 29.4 | 100.0 | 147.0 | 188.9 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 17.6 | 100.0 | 141.1 | 187.6 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.6 | 100.0 | 133.3 | 164.8 | 21046 |

### ctx_016384.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 28.9 | 100.0 | 125.7 | 172.5 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 17.8 | 100.0 | 150.4 | 206.6 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 32.8 | 100.0 | 135.2 | 194.6 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 14.7 | 100.0 | 133.3 | 176.1 | 21046 |

### ctx_032768.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 19.9 | 100.0 | 128.9 | 196.8 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.9 | 100.0 | 149.8 | 224.8 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 25.1 | 100.0 | 135.1 | 214.5 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 24.4 | 100.0 | 132.2 | 197.2 | 21046 |

### ctx_065536.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 25.2 | 100.0 | 128.9 | 226.6 | 19294 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.6 | 100.0 | 150.8 | 249.2 | 20590 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 23.0 | 100.0 | 133.4 | 245.5 | 20590 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 22.9 | 100.0 | 132.2 | 241.7 | 21046 |

### ctx_100000.txt | active_slots=1

| GPU | name | PCIe | avg util % | max util % | avg W | max W | max VRAM MiB |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | NVIDIA GeForce RTX 3090 | Gen3 x8 | 24.2 | 100.0 | 127.7 | 244.0 | 19296 |
| 1 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 26.7 | 100.0 | 148.1 | 249.6 | 20592 |
| 2 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 22.9 | 100.0 | 132.1 | 248.3 | 20592 |
| 3 | NVIDIA GeForce RTX 3090 | Gen3 x16 | 21.9 | 100.0 | 131.1 | 244.7 | 21048 |


## Notes

- `*` values are computed by the benchmark script, not reported by llama-server.
- `group_wall_ms*` is measured from immediately before releasing the PARALLEL request group to after the last HTTP response in that group is received.
- `group_response_tok_s* = sum(prompt_tokens for all requests in the group) / group_wall_time`.
- Each request is forced to `n_predict=1`, so the group wall time is treated as prefill-dominated server response time with a one-token answer.
- Per-request prefill timing columns are still the server-reported values from each individual HTTP response.
