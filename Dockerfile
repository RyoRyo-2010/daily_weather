FROM python:3.11-slim

WORKDIR /daily_weather

COPY requirements.txt ./requirements.txt
COPY app ./app

RUN apt-get update && apt-get install -y tzdata python3-pip
RUN pip install -r requirements.txt

ENV TZ=Asia/Tokyo

CMD ["python", "/daily_weather/app/main.py"]
