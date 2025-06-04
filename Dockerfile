FROM python:3.11-slim

COPY requirements.txt ./requirements.txt
COPY app /app

RUN apt-get update && apt-get install -y tzdata python3-pip
RUN pip install -r requirements.txt

WORKDIR /app

ENV TZ=Asia/Tokyo

CMD ["python", "./app/main.py"]
