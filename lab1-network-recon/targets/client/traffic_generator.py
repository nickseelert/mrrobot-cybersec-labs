#!/usr/bin/env python3
"""
Traffic generator to simulate coffee shop customer activity
Creates realistic network traffic for packet capture exercises
"""

import time
import random
import requests
import ftplib
import os
from datetime import datetime

# Configuration
WEB_SERVER = "http://coffee-shop-web"
FTP_SERVER = "coffee-shop-ftp"
TRAFFIC_INTERVAL = int(os.environ.get('TRAFFIC_INTERVAL', 30))

# Simulated user credentials (intentionally weak)
users = [
    {"username": "john_doe", "password": "password123", "cc": "4532-1234-5678-9012"},
    {"username": "jane_smith", "password": "qwerty", "cc": "5412-7534-9821-4567"},
    {"username": "ron", "password": "coffee123", "cc": "4916-2234-5678-9012"},
    {"username": "admin", "password": "admin123", "cc": "4024-0071-2345-6789"}
]

def generate_web_traffic():
    """Simulate various HTTP requests"""
    print(f"[{datetime.now()}] Generating web traffic...")
    
    # Browse main page
    try:
        response = requests.get(WEB_SERVER)
        print(f"  - Browsed main page: {response.status_code}")
    except Exception as e:
        print(f"  - Web error: {e}")
    
    # Attempt login with random user
    user = random.choice(users)
    try:
        login_data = {
            "username": user["username"],
            "password": user["password"]
        }
        response = requests.post(f"{WEB_SERVER}/login.php", data=login_data)
        print(f"  - Login attempt for {user['username']}: {response.status_code}")
    except Exception as e:
        print(f"  - Login error: {e}")
    
    # Simulate credit card form submission (unencrypted)
    try:
        payment_data = {
            "card_number": user["cc"],
            "cvv": "123",
            "amount": "4.50"
        }
        response = requests.post(f"{WEB_SERVER}/payment.php", data=payment_data)
        print(f"  - Payment submission: {response.status_code}")
    except Exception as e:
        print(f"  - Payment error: {e}")

def generate_ftp_traffic():
    """Simulate FTP activity"""
    print(f"[{datetime.now()}] Generating FTP traffic...")
    
    try:
        # Connect to FTP server
        ftp = ftplib.FTP()
        ftp.connect(FTP_SERVER, 21)
        ftp.login("ron", "coffee123")
        
        # List files
        files = []
        ftp.dir(files.append)
        print(f"  - FTP connected, found {len(files)} files")
        
        # Try to upload a file
        test_content = f"Sales report - {datetime.now()}\nTotal: $1,234.56"
        filename = f"sales_{datetime.now().strftime('%Y%m%d')}.txt"
        
        # Create temporary file
        with open(f"/tmp/{filename}", "w") as f:
            f.write(test_content)
        
        # Upload file
        with open(f"/tmp/{filename}", "rb") as f:
            ftp.storbinary(f"STOR {filename}", f)
        print(f"  - Uploaded file: {filename}")
        
        ftp.quit()
    except Exception as e:
        print(f"  - FTP error: {e}")

def generate_telnet_traffic():
    """Simulate telnet activity to router"""
    print(f"[{datetime.now()}] Generating telnet traffic...")
    # Note: Actual telnet implementation would require pexpect or telnetlib
    print("  - Telnet simulation (would connect to router)")

def main():
    """Main traffic generation loop"""
    print("Starting coffee shop traffic simulator...")
    print(f"Generating traffic every {TRAFFIC_INTERVAL} seconds")
    
    while True:
        try:
            # Randomly select traffic types
            traffic_types = [generate_web_traffic, generate_ftp_traffic]
            
            # Generate 1-3 types of traffic
            num_actions = random.randint(1, 3)
            for _ in range(num_actions):
                traffic_func = random.choice(traffic_types)
                traffic_func()
                time.sleep(random.randint(2, 5))
            
            # Wait before next cycle
            time.sleep(TRAFFIC_INTERVAL)
            
        except KeyboardInterrupt:
            print("\nTraffic generator stopped")
            break
        except Exception as e:
            print(f"Error in main loop: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()