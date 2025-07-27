# Lab 1: Network Reconnaissance & Scanning

## Mr. Robot Reference
In Season 1, Episode 1, Elliot exposes Ron's (coffee shop owner) illegal activities by intercepting unencrypted WiFi traffic. This lab recreates that scenario, teaching you network reconnaissance and packet analysis.

## Learning Objectives

By completing this lab, you will:
- Perform network discovery and mapping
- Capture and analyze network traffic
- Identify vulnerabilities in network configurations
- Extract sensitive information from packet captures
- Understand the importance of encryption

## Lab Scenario

You are a security consultant hired by "Ron's Coffee Shop" to test their network security. The shop offers free WiFi to customers and processes credit card transactions. Your mission is to identify security vulnerabilities in their network setup.

## Prerequisites

- Basic understanding of TCP/IP
- Familiarity with Linux command line
- Docker and Docker Compose installed

## Lab Architecture

The lab consists of:
- **Target Network**: Simulated coffee shop network with multiple services
- **Attacker Machine**: Kali Linux container with security tools
- **Vulnerable Services**: Web server, FTP server, database
- **Client Simulator**: Generates realistic network traffic

## Getting Started

1. Start the lab environment:
   ```bash
   docker-compose up -d
   ```

2. Access the Kali container:
   ```bash
   docker exec -it kali-attacker /bin/bash
   ```

3. Verify network connectivity:
   ```bash
   ping target-web
   ```

## Tasks

### Task 1: Network Discovery (20 points)
Identify all hosts and services on the coffee shop network.

**Tools**: nmap, arp-scan
**Deliverable**: Network map with all discovered hosts and services

### Task 2: Service Enumeration (20 points)
Gather detailed information about running services.

**Tools**: nmap service detection, banner grabbing
**Deliverable**: Service versions and potential vulnerabilities

### Task 3: Traffic Capture (25 points)
Capture and analyze network traffic to find sensitive information.

**Tools**: tcpdump, Wireshark
**Deliverable**: Captured credentials or sensitive data

### Task 4: Vulnerability Assessment (25 points)
Identify security misconfigurations and vulnerabilities.

**Tools**: nmap scripts, manual analysis
**Deliverable**: Vulnerability report with severity ratings

### Task 5: Exploitation Demo (10 points)
Demonstrate one vulnerability exploitation (educational purposes only).

**Tools**: Various depending on vulnerability
**Deliverable**: Proof of concept with screenshots

## Hints

<details>
<summary>Hint 1: Network Discovery</summary>

Start with a ping sweep to identify live hosts:
```bash
nmap -sn 172.20.0.0/24
```
</details>

<details>
<summary>Hint 2: Service Scanning</summary>

Use aggressive service detection:
```bash
nmap -sV -sC -A [target-ip]
```
</details>

<details>
<summary>Hint 3: Traffic Analysis</summary>

Look for unencrypted protocols like HTTP, FTP, Telnet. Filter Wireshark by protocol.
</details>

## Assessment Criteria

- **Technical Accuracy** (40%): Correct use of tools and techniques
- **Documentation** (30%): Clear reporting of findings
- **Critical Thinking** (20%): Analysis of security implications
- **Ethics** (10%): Proper handling of discovered information

## Submission Requirements

1. Network diagram showing all discovered hosts
2. Service enumeration report
3. Screenshot evidence of captured credentials
4. Vulnerability assessment report (2-3 pages)
5. Remediation recommendations

## Defensive Measures

After completing the lab, consider these defenses:
- Implement WPA3 encryption
- Use VPN for sensitive transactions
- Enable HTTPS on all web services
- Implement network segmentation
- Regular security audits

## Real-World Context

This lab demonstrates why public WiFi is dangerous:
- 2017: Krack Attack affected WPA2
- 2019: Over 25% of public WiFi hotspots lack encryption
- 2020: FBI warning about hotel WiFi vulnerabilities

## Clean Up

```bash
docker-compose down
docker system prune -a
```

## Additional Resources

- [Wireshark User Guide](https://www.wireshark.org/docs/wsug_html/)
- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)

## Next Lab Preview

Lab 2 will explore social engineering techniques used in the Steel Mountain episode, including OSINT gathering and phishing attacks.