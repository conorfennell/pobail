FROM python:3.8.6-buster

ENV PYTHONUNBUFFER=0
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

RUN python -m pytest tests/
RUN pylint -j 4 /app/gunicorn /app/api

RUN mkdir -p /app/metrics
ENV prometheus_multiproc_dir /app/metrics


ENTRYPOINT [ "gunicorn", "-c/app/gunicorn/gunicorn_config.py", "-b", "0.0.0.0:5000", "run:app", "--workers=4", "--threads=1", "--worker-class=gevent", "--log-config=gunicorn_logging.conf"]
