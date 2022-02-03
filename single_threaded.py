#!/usr/bin/env python3
# single_threaded.py
import time

COUNT = int(5e8)


def countdown(n):
    """Countdown"""
    while n > 0:
        n -= 1


start = time.time()
countdown(COUNT)
end = time.time()

print(f"Time taken in seconds: {end - start:.2f}")
