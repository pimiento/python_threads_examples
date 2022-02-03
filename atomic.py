#!/usr/bin/env python2
# encoding: utf-8
from dis import dis

lst = [4, 1, 3, 2]


def foo():
    lst.sort()

print(dis(foo))
