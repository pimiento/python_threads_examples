#!/usr/bin/env python3
# single_threaded.py
import time

cdef int COUNT = int(5e8)


cdef void countdown(n: int):
    """Countdown"""
    while n > 0:
        n -= 1


start : float = time.time()
countdown(COUNT)
end : float = time.time()
print(f"Time taken in seconds: {end - start:.2f}")
