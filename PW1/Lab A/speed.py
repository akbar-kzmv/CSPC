import time

from decay import simulate, simulate_loop


N0 = 200000
lam = 0.4


start = time.perf_counter()
simulate_loop(N0, lam)
end = time.perf_counter()

loop_time = end - start


start = time.perf_counter()
simulate(N0, lam)
end = time.perf_counter()

numpy_time = end - start


speedup = loop_time / numpy_time


print(f"Loop time: {loop_time:.6f} s")
print(f"NumPy time: {numpy_time:.6f} s")
print(f"NumPy is {speedup:.2f}x faster")