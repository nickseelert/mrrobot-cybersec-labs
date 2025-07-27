#!/bin/bash
# Lab 1 Setup Script

echo "Setting up Lab 1: Network Reconnaissance & Scanning"
echo "=================================================="

# Check Docker installation
if ! command -v docker &> /dev/null; then
    echo "Error: Docker is not installed. Please install Docker first."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "Error: Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Create necessary directories
echo "Creating directories..."
mkdir -p captures logs scripts/student

# Set permissions
chmod 755 scripts/*.sh 2>/dev/null
chmod +x targets/router/startup.sh 2>/dev/null

# Pull/build images
echo "Building Docker images..."
docker-compose build

# Install tools in Kali container
echo "Setting up Kali Linux container with tools..."
docker-compose up -d kali-attacker
docker exec kali-attacker apt-get update
docker exec kali-attacker apt-get install -y \
    nmap \
    wireshark \
    tcpdump \
    netcat-traditional \
    dnsutils \
    ftp \
    telnet \
    hydra \
    john \
    sqlmap \
    metasploit-framework

# Start all services
echo "Starting lab environment..."
docker-compose up -d

# Wait for services to be ready
echo "Waiting for services to initialize..."
sleep 10

# Verify services
echo "Verifying services..."
docker-compose ps

echo
echo "Lab 1 Setup Complete!"
echo "===================="
echo
echo "To access the Kali attacker machine:"
echo "  docker exec -it kali-attacker /bin/bash"
echo
echo "Target services:"
echo "  - Web Server: http://localhost:8080"
echo "  - FTP Server: ftp://localhost:2121"
echo "  - Internal network: 172.20.0.0/24"
echo
echo "To stop the lab:"
echo "  docker-compose down"
echo
echo "Happy hacking! Remember to use these skills ethically."