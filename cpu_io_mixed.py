import socket
from threading import Thread


def do_connect(name):
    print(name.upper() + ": Before connect")
    s = socket.socket()
    s.connect(('python.org', 80))  # drop the GIL
    print(name.upper() + ": Connected")

def cpu_bound(n=int(5e8)):
    result = 0
    for i in range(n):
        result += i
    return result


threads = []
threads.append(Thread(target=cpu_bound))
for i in range(2):
    t = Thread(target=do_connect, args=("connection_" + str(i),))
    threads.append(t)


for t in threads:
    t.start()

for t in threads:
    t.join()
