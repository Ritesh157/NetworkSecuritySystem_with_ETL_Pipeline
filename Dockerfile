FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update -qq && \
    apt-get install -y --no-install-recommends \
    awscli \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "app.py"]