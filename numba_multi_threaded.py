#!/usr/bin/env python3
# numba_multi_threaded
import time
from numba import jit, prange

COUNT = int(5e8)

@jit(nopython=True, nogil=True)
def parallel_count(n):
    sum = n
    for i in prange(n):
        sum -= i
    return sum


start = time.process_time()
parallel_count(COUNT)
end = time.process_time()
print(f"Time taken in seconds: {end - start:.8f}")
