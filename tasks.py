from celery import Celery

app = Celery("tasks", broker="pyamqp://guest@localhost//", backend="rpc://")


@app.task
def countdown(n=int(5e8)):
    assert isinstance(n, int)
    for _ in range(n):
        n -= 1
    return n
