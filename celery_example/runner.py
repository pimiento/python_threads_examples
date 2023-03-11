#!/usr/bin/env python3
import time
import docker
from celery import chain, group, chord
from tasks import worker, main_reload


client = docker.from_env()
containers = [c for c in client.containers.list() if c.attrs["Name"].startswith("/octopus")]


if __name__ == "__main__":

    # DSL — Domain Specific Language
    res = chord(
        (worker.s(i,) for i in range(20)),
        main_reload.si()
    )()
    with open("/tmp/res.dot", "w") as fh:
        res.graph.to_dot(fh)
