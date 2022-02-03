#!/usr/bin/env python3
import socket
from threading import Thread


def do_connect(name):
    print(f"{name.upper()}: Before connect")
    s = socket.socket()
    s.connect(('python.org', 80))  # drop the GIL
    print(f"{name.lower()}: Connected")


for i in range(2):
    t = Thread(target=do_connect, args=(f"connection_{i}",))
    t.start()
