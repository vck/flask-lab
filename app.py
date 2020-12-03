import time
import redis
from flask import Flask, request
from rq import Queue
from rq.job import Job
from job import background_task


app = Flask(__name__)

r = redis.Redis()
q = Queue(connection=r)

@app.route('/')
def index_page():
    return "hello world! visit <a href='/task?n=1'>task</a>"


@app.route("/results/<job_key>", methods=["GET"])
def get_result(job_key):
    try:
        job = Job.fetch(job_key, connection=r)
    except:
        return "Job not found", 202

    print(job)
    if job.is_finished:
        return str(job.result), 200
    else:
        return "Not finished", 202


@app.route('/task')
def add_task():
    if request.args.get("n"):
        job = q.enqueue(background_task, request.args.get("n"))
        return f"task {job.id} added"
    return "No value for n"

if __name__ == "__main__":
    app.run()

