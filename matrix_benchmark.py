import torch
import time
import platform

print(f"Host: {platform.node()}")
print(f"PyTorch: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Running on: {device}\n")

sizes = [1024, 2048, 4096]
for n in sizes:
    A = torch.randn(n, n, device=device)
    B = torch.randn(n, n, device=device)
    start = time.time()
    for _ in range(10):
        C = torch.matmul(A, B)
    elapsed = (time.time() - start) / 10
    gflops = (2 * n**3) / (elapsed * 1e9)
    print(f"Matrix {n}x{n}: {elapsed*1000:.1f} ms/iter | {gflops:.1f} GFLOPS")

print("\nBenchmark complete.")
