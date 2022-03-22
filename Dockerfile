from python:3.10.3-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python3", "tracking_seras.py"]
