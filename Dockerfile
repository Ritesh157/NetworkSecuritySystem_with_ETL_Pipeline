FROM python:3.10-slim

WORKDIR /app

# Copy requirements first (better layer caching)
COPY requirements.txt .

# Install system dependencies + awscli properly
RUN apt-get update -qq && \
    apt-get install -y --no-install-recommends \
    awscli \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

CMD ["python3", "app.py"]