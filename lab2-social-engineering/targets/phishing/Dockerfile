FROM python:3.9-slim

# Install MailHog for email capture
RUN apt-get update && apt-get install -y \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Download and install MailHog
RUN wget -O /usr/local/bin/mailhog https://github.com/mailhog/MailHog/releases/download/v1.0.1/MailHog_linux_amd64 \
    && chmod +x /usr/local/bin/mailhog

# Install Python dependencies for phishing simulation
RUN pip install flask flask-mail

# Copy phishing templates and server
COPY phishing_server.py /app/phishing_server.py
COPY templates /app/templates

WORKDIR /app

# Expose ports
EXPOSE 8025 1025

# Start both MailHog and phishing server
CMD mailhog & python phishing_server.py