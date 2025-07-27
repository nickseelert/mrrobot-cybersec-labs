#!/usr/bin/env python3
"""
Fake Profile Generator for Social Engineering Lab
Generates believable personas with consistent details
"""

import random
import json
from datetime import datetime, timedelta
import hashlib

# Data sets for profile generation
first_names = {
    'male': ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles'],
    'female': ['Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Jessica', 'Sarah', 'Karen']
}

last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']

companies = ['Steel Mountain', 'E Corp', 'Allsafe Security', 'Dark Army Corp', 'White Rose Industries']

job_titles = [
    'Security Analyst', 'Network Administrator', 'IT Manager', 'Help Desk Technician',
    'Database Administrator', 'System Administrator', 'Security Engineer', 'DevOps Engineer',
    'Cloud Architect', 'Compliance Officer'
]

hobbies = [
    'hiking', 'photography', 'cooking', 'gaming', 'reading', 'traveling',
    'cycling', 'yoga', 'painting', 'gardening', 'chess', 'running'
]

universities = [
    'MIT', 'Stanford University', 'Carnegie Mellon', 'UC Berkeley',
    'Georgia Tech', 'University of Washington', 'NYU', 'UCLA'
]

def generate_email(first_name, last_name, company):
    """Generate work email address"""
    company_domain = company.lower().replace(' ', '-') + '.com'
    formats = [
        f"{first_name.lower()}.{last_name.lower()}@{company_domain}",
        f"{first_name[0].lower()}{last_name.lower()}@{company_domain}",
        f"{first_name.lower()}{last_name[0].lower()}@{company_domain}",
        f"{first_name.lower()}_{last_name.lower()}@{company_domain}"
    ]
    return random.choice(formats)

def generate_phone():
    """Generate phone number"""
    area_codes = ['212', '415', '310', '312', '202', '617', '404', '206']
    return f"({random.choice(area_codes)}) {random.randint(100,999)}-{random.randint(1000,9999)}"

def generate_birthday():
    """Generate birthday making person 25-45 years old"""
    today = datetime.now()
    age = random.randint(25, 45)
    birth_year = today.year - age
    birth_month = random.randint(1, 12)
    birth_day = random.randint(1, 28)
    return datetime(birth_year, birth_month, birth_day)

def generate_social_media(first_name, last_name):
    """Generate social media handles"""
    handles = []
    base = f"{first_name.lower()}{last_name.lower()}"
    
    # LinkedIn
    handles.append({
        'platform': 'LinkedIn',
        'handle': f"/in/{base}{random.randint(1,99)}"
    })
    
    # Twitter
    handles.append({
        'platform': 'Twitter',
        'handle': f"@{base[:15]}{random.randint(1,999)}"
    })
    
    # GitHub (for tech people)
    if random.random() > 0.5:
        handles.append({
            'platform': 'GitHub',
            'handle': f"{base}-dev"
        })
    
    return handles

def generate_backstory(profile):
    """Generate believable backstory"""
    templates = [
        f"Started at {profile['company']} after graduating from {profile['education']}. "
        f"Passionate about cybersecurity and {random.choice(profile['hobbies'])}. "
        f"Recently completed {random.choice(['CISSP', 'CEH', 'Security+', 'CCNA Security'])} certification.",
        
        f"Joined {profile['company']} {random.randint(1,5)} years ago as {profile['job_title']}. "
        f"Previously worked at {random.choice(['Microsoft', 'Google', 'Amazon', 'IBM'])}. "
        f"Enjoys {random.choice(profile['hobbies'])} and {random.choice(profile['hobbies'])} on weekends.",
        
        f"Security professional with {random.randint(5,15)} years experience. "
        f"Graduated from {profile['education']} with Computer Science degree. "
        f"Active in the {random.choice(['infosec', 'cybersecurity', 'netsec'])} community."
    ]
    
    return random.choice(templates)

def generate_profile():
    """Generate complete fake profile"""
    gender = random.choice(['male', 'female'])
    first_name = random.choice(first_names[gender])
    last_name = random.choice(last_names)
    company = random.choice(companies)
    
    profile = {
        'id': hashlib.md5(f"{first_name}{last_name}{datetime.now()}".encode()).hexdigest()[:8],
        'first_name': first_name,
        'last_name': last_name,
        'full_name': f"{first_name} {last_name}",
        'gender': gender,
        'email': generate_email(first_name, last_name, company),
        'phone': generate_phone(),
        'company': company,
        'job_title': random.choice(job_titles),
        'department': random.choice(['IT Security', 'Network Operations', 'Information Security', 'IT Infrastructure']),
        'birthday': generate_birthday().strftime('%Y-%m-%d'),
        'hire_date': (datetime.now() - timedelta(days=random.randint(180, 1825))).strftime('%Y-%m-%d'),
        'education': random.choice(universities),
        'hobbies': random.sample(hobbies, 3),
        'social_media': generate_social_media(first_name, last_name),
        'profile_image': f"https://thispersondoesnotexist.com/image?{random.randint(1,99999)}",
        'security_clearance': random.choice(['None', 'Secret', 'Top Secret']) if company == 'Steel Mountain' else 'None'
    }
    
    profile['backstory'] = generate_backstory(profile)
    
    # Add some vulnerabilities for social engineering
    vulnerabilities = []
    if random.random() > 0.5:
        vulnerabilities.append("Posts personal information on social media")
    if random.random() > 0.6:
        vulnerabilities.append("Uses birthdate in passwords")
    if random.random() > 0.7:
        vulnerabilities.append("Shares too much on LinkedIn")
    if random.random() > 0.4:
        vulnerabilities.append("Responds to authority figures without verification")
    
    profile['vulnerabilities'] = vulnerabilities
    
    return profile

def main():
    """Main function"""
    print("=== Fake Profile Generator ===")
    print("1. Generate single profile")
    print("2. Generate multiple profiles")
    print("3. Generate profile with specific company")
    
    choice = input("\nSelect option: ")
    
    if choice == '1':
        profile = generate_profile()
        print("\n" + json.dumps(profile, indent=2))
        
        # Save to file
        filename = f"/data/profiles/{profile['id']}_profile.json"
        with open(filename, 'w') as f:
            json.dump(profile, f, indent=2)
        print(f"\nProfile saved to: {filename}")
        
    elif choice == '2':
        count = int(input("How many profiles? "))
        profiles = []
        for i in range(count):
            profile = generate_profile()
            profiles.append(profile)
            print(f"Generated: {profile['full_name']} - {profile['job_title']}")
        
        # Save all profiles
        filename = f"/data/profiles/batch_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(profiles, f, indent=2)
        print(f"\n{count} profiles saved to: {filename}")
        
    elif choice == '3':
        print("\nAvailable companies:")
        for i, company in enumerate(companies, 1):
            print(f"{i}. {company}")
        
        company_choice = int(input("Select company: ")) - 1
        if 0 <= company_choice < len(companies):
            # Generate profile with specific company
            profile = generate_profile()
            profile['company'] = companies[company_choice]
            profile['email'] = generate_email(profile['first_name'], profile['last_name'], companies[company_choice])
            
            print("\n" + json.dumps(profile, indent=2))
            
            filename = f"/data/profiles/{profile['id']}_profile.json"
            with open(filename, 'w') as f:
                json.dump(profile, f, indent=2)
            print(f"\nProfile saved to: {filename}")

if __name__ == "__main__":
    main()