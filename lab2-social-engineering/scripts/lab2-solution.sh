#!/bin/bash
# Lab 2 Solution Guide - Social Engineering & OSINT

echo "=== Lab 2 Solution Walkthrough ==="
echo "Social Engineering & OSINT Techniques"
echo

# Task 1: OSINT Reconnaissance
echo "Task 1: OSINT Reconnaissance"
echo "--------------------------"
echo "1. Check company website source code:"
echo "   - View page source for hidden comments"
echo "   - Found: Admin panel at /admin/dashboard.php"
echo "   - Found: Test credentials admin:TempPass123!"
echo "   - Found: Internal wiki at wiki.steelmountain.local"
echo
echo "2. Employee directory analysis:"
echo "   - Visit /team.php for employee listings"
echo "   - Extract emails, phone numbers, departments"
echo "   - Note personal details in bios"
echo
echo "3. Metadata extraction:"
echo "   exiftool downloaded_image.jpg"
echo "   - Can reveal author, creation date, GPS coords"
echo

# Task 2: Create Fake Personas
echo "Task 2: Create Fake Personas"
echo "---------------------------"
echo "Use the profile generator:"
echo "   docker exec -it osint-tools python3 /scripts/profile_generator.py"
echo
echo "Key elements for believable personas:"
echo "- Consistent personal details"
echo "- Professional background"
echo "- Social media presence"
echo "- Realistic profile photos"
echo

# Task 3: Spear Phishing Campaign
echo "Task 3: Spear Phishing Campaign"
echo "------------------------------"
echo "Effective phishing techniques:"
echo "1. Authority (IT Support template)"
echo "2. Urgency (CEO fraud template)"  
echo "3. Fear (Security alert template)"
echo
echo "Personalization increases success:"
echo "- Use target's actual name"
echo "- Reference their department"
echo "- Mention recent company events"
echo

# Task 4: Pretexting Scenarios
echo "Task 4: Pretexting Scenarios"
echo "---------------------------"
echo "Successful pretexts used:"
echo
echo "1. IT Support Call:"
echo "   'Hi, this is Mike from IT. We're doing mandatory'"
echo "   'security updates. I need to verify your login.'"
echo
echo "2. New Employee:"
echo "   'Hi, I'm starting Monday in Sarah Chen's team.'"
echo "   'She said to call about getting building access?'"
echo
echo "3. Vendor Verification:"
echo "   'This is Acme Security. We need to verify your'"
echo "   'employee list for the new badge system.'"
echo

# Task 5: Physical Security Assessment
echo "Task 5: Physical Security Assessment"
echo "----------------------------------"
echo "Infiltration plan based on OSINT:"
echo "1. Target: Lowest security awareness employee"
echo "2. Time: Lunch hours (social engineering opportunity)"
echo "3. Approach: Tailgating with fake badge"
echo "4. Backup: Vendor/interview pretext"
echo

# Defensive Measures
echo
echo "Defensive Measures Discovered:"
echo "-----------------------------"
echo "1. Remove sensitive info from public sites"
echo "2. Implement email authentication (SPF/DKIM/DMARC)"
echo "3. Regular security awareness training"
echo "4. Verify requests through separate channels"
echo "5. Limit information in employee directories"
echo "6. Monitor for fake social media profiles"
echo "7. Implement callback procedures"

echo
echo "=== Key Vulnerabilities Found ==="
echo "1. Too much employee info publicly available"
echo "2. Hidden admin credentials in HTML comments"
echo "3. Predictable email format"
echo "4. No verification for password reset requests"
echo "5. Employees respond to authority without verification"

echo
echo "=== Solution Complete ===