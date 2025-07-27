# Mr. Robot Cybersecurity Labs

A comprehensive cybersecurity course inspired by the technical accuracy of Mr. Robot, designed for university students to learn real-world hacking techniques in a safe, containerized environment.

## Course Overview

This course provides hands-on experience with cybersecurity concepts through Docker-based labs that recreate scenarios from Mr. Robot. Each lab is designed to teach specific security principles while maintaining realism and technical accuracy.

## Prerequisites

- Basic Linux command line knowledge
- Docker and Docker Compose installed
- Understanding of networking fundamentals
- A computer with at least 8GB RAM

## Lab Modules

### Lab 1: Network Reconnaissance & Scanning
Recreate Elliot's WiFi cafe hack. Learn packet sniffing, network mapping, and traffic analysis.

### Lab 2: Social Engineering & OSINT
Master the art of information gathering and social engineering, inspired by the Steel Mountain infiltration.

### Lab 3: Web Application Exploitation
Target vulnerable web applications like E Corp's servers using SQL injection, XSS, and more.

### Lab 4: Wireless Network Security
Understand WiFi vulnerabilities, WPA2 cracking, and evil twin attacks.

### Lab 5: Privilege Escalation & Persistence
Learn post-exploitation techniques, backdoor creation, and maintaining access.

### Lab 6: Cryptography & Steganography
Hide data in plain sight and understand encryption, inspired by Elliot's audio file techniques.

### Lab 7: Physical Security & Hardware Hacking
Explore USB attacks, RFID cloning, and Raspberry Pi hacks from the show.

## Getting Started

1. Clone this repository
2. Navigate to the desired lab directory
3. Run `docker-compose up -d` to start the lab environment
4. Follow the lab instructions in each module's README

## Safety & Ethics

These labs are for educational purposes only. Always:
- Use these techniques only in authorized environments
- Respect privacy and legal boundaries
- Follow responsible disclosure practices
- Remember: with great power comes great responsibility

## Technical Architecture

All labs use Docker containers to provide:
- Isolated, safe environments
- Consistent experiences across different systems
- Easy reset and cleanup
- Resource-efficient virtualization

## Assessment

Each lab includes:
- Clear learning objectives
- Step-by-step tutorials
- Challenge exercises
- Automated scoring where applicable
- Solution walkthroughs