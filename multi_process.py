#!/usr/bin/env python3
import time
from multiprocessing import Pool


COUNT = int(5e8)

def countdown(n: int) -> None:
    while n > 0:
        n -= 1

if __name__ == '__main__':
    pool = Pool(processes=2)
    start: float = time.time()
    r1 = pool.apply_async(countdown, [COUNT//2])
    r2 = pool.apply_async(countdown, [COUNT//2])
    pool.close()
    pool.join()
    end: float = time.time()
    print(f"Time taken in seconds: {end - start:.2f}")
