FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip setuptools

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

ENV FLASK_APP=run.py
ENV FLASK_ENV=development

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
