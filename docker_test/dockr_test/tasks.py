from docker_test.celery import app


@app.task
def add(x, y):
    return x + y