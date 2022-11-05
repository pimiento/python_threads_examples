#!/usr/bin/env python3
# cython_multi_threaded
import time
from cython.parallel import prange

cdef int i
cdef int COUNT = int(5e8)
cdef int n = 0

start : float = time.process_time()
for i in prange(COUNT, nogil=True):
    n -= 1
end : float = time.process_time()
print(f"Time taken in seconds: {end - start:.8f}")
