FROM python:3.11.1-slim-bullseye

ADD ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ADD ./main.py /main.py

EXPOSE 8001

CMD uvicorn main:app --host 0.0.0.0 --port 8001
