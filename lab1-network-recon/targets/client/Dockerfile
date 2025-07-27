FROM python:3.9-slim

# Install required packages
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    ftp \
    telnet \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# Copy traffic generator script
COPY traffic_generator.py /app/traffic_generator.py
COPY credentials.txt /app/credentials.txt

WORKDIR /app

# Install Python dependencies
RUN pip install requests

# Run traffic generator
CMD ["python", "-u", "traffic_generator.py"]