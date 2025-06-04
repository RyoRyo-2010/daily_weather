FROM python:3.11-slim

RUN apt-get update && apt-get install -y tzdata python3-pip
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app

ENV TZ=Asia/Tokyo
