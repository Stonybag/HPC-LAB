# Project 2: GenAI Inference Stack — As-Built Results

## Environment
- Cloud: Vast.ai
- GPU: NVIDIA GeForce RTX 5090, 32GB VRAM
- CUDA: 13.0 | Driver: 580.159.03
- OS: Ubuntu 24.04.4 LTS

## Stack
- vLLM: 0.24.0
- PyTorch: 2.11.0
- Model: mistralai/Mistral-7B-Instruct-v0.2 (float16)
- DCGM: 3.3.9

## Benchmark Results
- Inference throughput: 101 tokens/sec
- Test: 150 completion tokens, 1.486s elapsed
- Prompt: "Explain GPU acceleration in HPC"

## DCGM Metrics (idle)
- SM Clock: 195 MHz
- GPU Temp: 43C
- Power: 11.9W
- Fan: 0%

## Notes
- vLLM deployed via pip (no Docker — container kernel restrictions)
- OpenAI-compatible API on port 8000
- DCGM host engine on port 5555
