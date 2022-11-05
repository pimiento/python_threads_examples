#!/usr/bin/env python3
# multi_threaded.py
import time
from threading import Thread

cdef int COUNT = int(5e8)


cdef countdown(n: int):
    """Countdown"""
    while n > 0:
        n -= 1

t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))

start: float = time.process_time()
t1.start()
t2.start()
t1.join()
t2.join()
end: float = time.process_time()
print(f"Time taken in seconds: {end - start:.2f}")
