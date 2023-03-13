#!/usr/bin/env python3
import time
from multiprocessing import Pool


COUNT = int(5e8)

def countdown(n: int) -> None:
    while n > 0:
        n -= 1

if __name__ == '__main__':
    p_count = 4
    pool = Pool(processes=p_count)
    for n in range(1, p_count+1):
        pool.apply_async(countdown, [(COUNT//p_count) * n])
    pool.close()
    pool.join()
