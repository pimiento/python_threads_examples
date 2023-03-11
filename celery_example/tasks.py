import io
import re
import tarfile
import docker
from celery import Celery

app = Celery('hello', broker='redis://localhost:6379/0')
app.conf.result_backend = 'redis://localhost:6379/0'

client = docker.from_env()
containers = [c for c in client.containers.list() if re.match(r"^\/u\d{1,2}$", c.attrs["Name"])]

@app.task
def worker(server_num):
    nginx_fio = io.BytesIO()
    tf = tarfile.TarFile("nginx.tar", "w", fileobj=nginx_fio)
    tf.add("default.conf")
    nginx_fio.seek(0)

    html_fio = io.BytesIO()
    tf = tarfile.TarFile("index.tar", "w", fileobj=html_fio)
    tf.add("index.html")
    html_fio.seek(0)

    cc = containers[server_num]
    cc.exec_run("mkdir /tmp/ver3")
    cc.put_archive("/tmp/ver3", html_fio)
    cc.put_archive("/etc/nginx/conf.d/", nginx_fio)
    cc.exec_run("nginx -s reload")

    with open(f"/tmp/worker_{server_num}.txt", "w") as fd:
        fd.write(str(server_num))
        fd.write("\n")

    return f"WORKER {server_num} DONE"

@app.task
def main_reload():
    cc = containers[0]
    result = cc.exec_run("date")
    return f"MAIN RELOAD DONE: {result}"
