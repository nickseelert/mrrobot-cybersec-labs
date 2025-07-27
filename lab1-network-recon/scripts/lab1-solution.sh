#!/bin/bash
# Lab 1 Solution Guide - Network Reconnaissance
# This script demonstrates the solution steps

echo "=== Lab 1 Solution Walkthrough ==="
echo "This script shows the commands used to complete the lab"
echo

# Task 1: Network Discovery
echo "Task 1: Network Discovery"
echo "------------------------"
echo "Command: nmap -sn 172.20.0.0/24"
echo "This performs a ping sweep to find live hosts"
echo

# Task 2: Service Enumeration
echo "Task 2: Service Enumeration"
echo "--------------------------"
echo "Command: nmap -sV -sC -A 172.20.0.20"
echo "This performs aggressive service detection on the web server"
echo
echo "Command: nmap -sV -p- 172.20.0.1"
echo "This scans all ports on the router"
echo

# Task 3: Traffic Capture
echo "Task 3: Traffic Capture"
echo "----------------------"
echo "Command: tcpdump -i eth0 -w capture.pcap"
echo "This captures all traffic on the network interface"
echo
echo "Command: tcpdump -i eth0 'tcp port 80' -A"
echo "This captures and displays HTTP traffic in ASCII"
echo

# Task 4: Vulnerability Assessment
echo "Task 4: Vulnerability Assessment"
echo "-------------------------------"
echo "Vulnerabilities found:"
echo "1. Unencrypted HTTP traffic exposing credentials"
echo "2. Default router credentials (admin/admin)"
echo "3. FTP with weak credentials (ron/coffee123)"
echo "4. MySQL accessible with weak passwords"
echo "5. SNMP with default community string 'public'"
echo "6. Exposed backup files on web server"
echo

# Task 5: Exploitation Demo
echo "Task 5: Exploitation Demo"
echo "------------------------"
echo "SQL Injection:"
echo "username: admin' OR '1'='1"
echo "password: anything"
echo
echo "This bypasses authentication due to vulnerable SQL query"
echo

# Additional findings
echo "Additional Findings:"
echo "------------------"
echo "- Credit card numbers transmitted in plain text"
echo "- Server information disclosure via HTTP headers"
echo "- Directory listing enabled on web server"
echo "- Telnet service running on router (port 23)"
echo "- SSH with password authentication enabled"

echo
echo "=== Solution Complete ==="