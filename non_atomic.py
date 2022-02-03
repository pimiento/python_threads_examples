#!/usr/bin/env python2
# encoding: utf-8
from dis import dis
from threading import Thread

N = 0


def foo():
    global N
    N += 1


print(dis(foo))

threads = []
for i in range(100):
    t = Thread(target=foo)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print(N)
"""
pimiento@e470:~/yap/threads_webinar (main%=) % python2 ./atomic.py
 11           0 LOAD_GLOBAL              0 (N)
              3 LOAD_CONST               1 (1)
              6 INPLACE_ADD
              7 STORE_GLOBAL             0 (N)
             10 LOAD_CONST               0 (None)
             13 RETURN_VALUE
None
100
pimiento@e470:~/yap/threads_webinar (main%=) % python2 ./atomic.py
 11           0 LOAD_GLOBAL              0 (N)
              3 LOAD_CONST               1 (1)
              6 INPLACE_ADD
              7 STORE_GLOBAL             0 (N)
             10 LOAD_CONST               0 (None)
             13 RETURN_VALUE
None
99
pimiento@e470:~/yap/threads_webinar (main%=) % python2 ./atomic.py
 11           0 LOAD_GLOBAL              0 (N)
              3 LOAD_CONST               1 (1)
              6 INPLACE_ADD
              7 STORE_GLOBAL             0 (N)
             10 LOAD_CONST               0 (None)
             13 RETURN_VALUE
None
100
"""
