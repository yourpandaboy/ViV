# write some code to build your image
FROM python:3.8.13-buster

COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY api.py /api.py
COPY ViV_backend /ViV_backend
COPY models /models
COPY data /data

CMD uvicorn api:app --host 0.0.0.0 --port 8080
