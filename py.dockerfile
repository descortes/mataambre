FROM python:3.6.4
WORKDIR /home/py
RUN pip install flask gunicorn