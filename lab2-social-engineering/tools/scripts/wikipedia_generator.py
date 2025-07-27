#!/usr/bin/env python3
"""
Wikipedia Page Generator - Recreating Elliot's Steel Mountain hack
Generates fake but realistic Wikipedia-style pages for personas
"""

import json
import random
from datetime import datetime

def generate_wikipedia_page(profile):
    """Generate a Wikipedia-style page for a fake persona"""
    
    # Wikipedia page template
    template = f"""<!DOCTYPE html>
<html>
<head>
    <title>{profile['full_name']} - Wikipedia</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #222;
            max-width: 960px;
            margin: 0 auto;
            padding: 20px;
            background: #f8f9fa;
        }}
        .wikipedia-box {{
            background: white;
            border: 1px solid #a2a9b1;
            padding: 20px;
            margin-bottom: 20px;
        }}
        .infobox {{
            float: right;
            width: 300px;
            background: #f8f9fa;
            border: 1px solid #a2a9b1;
            padding: 10px;
            margin: 0 0 20px 20px;
        }}
        .infobox img {{
            width: 100%;
            margin-bottom: 10px;
        }}
        .infobox table {{
            width: 100%;
            font-size: 0.9em;
        }}
        .infobox td {{
            padding: 5px;
            vertical-align: top;
        }}
        .toc {{
            background: #f8f9fa;
            border: 1px solid #a2a9b1;
            padding: 10px;
            display: inline-block;
            margin-bottom: 20px;
        }}
        h1 {{
            border-bottom: 1px solid #a2a9b1;
            padding-bottom: 10px;
        }}
        h2 {{
            border-bottom: 1px solid #e0e0e0;
            padding-bottom: 5px;
            margin-top: 30px;
        }}
        .references {{
            font-size: 0.9em;
            color: #555;
        }}
        .edit-link {{
            font-size: 0.8em;
            color: #0645ad;
            float: right;
        }}
    </style>
</head>
<body>
    <div class="wikipedia-box">
        <span class="edit-link">[edit]</span>
        <h1>{profile['full_name']}</h1>
        
        <div class="infobox">
            <img src="{profile.get('profile_image', 'https://via.placeholder.com/300x400?text=No+Image')}" alt="{profile['full_name']}">
            <table>
                <tr>
                    <td><strong>Born</strong></td>
                    <td>{datetime.strptime(profile['birthday'], '%Y-%m-%d').strftime('%B %d, %Y')}<br>
                        (age {datetime.now().year - datetime.strptime(profile['birthday'], '%Y-%m-%d').year})</td>
                </tr>
                <tr>
                    <td><strong>Education</strong></td>
                    <td>{profile['education']}</td>
                </tr>
                <tr>
                    <td><strong>Occupation</strong></td>
                    <td>{profile['job_title']}</td>
                </tr>
                <tr>
                    <td><strong>Employer</strong></td>
                    <td>{profile['company']}</td>
                </tr>
                <tr>
                    <td><strong>Known for</strong></td>
                    <td>Cybersecurity expertise</td>
                </tr>
            </table>
        </div>
        
        <p><strong>{profile['full_name']}</strong> is an American cybersecurity professional and {profile['job_title'].lower()} 
        at {profile['company']}. {profile.get('backstory', 'Known for contributions to information security.')}</p>
        
        <div class="toc">
            <h3>Contents</h3>
            <ol>
                <li><a href="#early-life">Early life and education</a></li>
                <li><a href="#career">Career</a></li>
                <li><a href="#achievements">Achievements</a></li>
                <li><a href="#personal">Personal life</a></li>
                <li><a href="#references">References</a></li>
            </ol>
        </div>
        
        <h2 id="early-life">Early life and education</h2>
        <p>{profile['first_name']} was born on {datetime.strptime(profile['birthday'], '%Y-%m-%d').strftime('%B %d, %Y')}. 
        They attended {profile['education']} where they studied Computer Science with a focus on cybersecurity. 
        During their time at university, they were involved in the cybersecurity club and participated in numerous CTF competitions.</p>
        
        <h2 id="career">Career</h2>
        <p>After graduating from {profile['education']}, {profile['last_name']} began their career in information security. 
        They joined {profile['company']} on {datetime.strptime(profile['hire_date'], '%Y-%m-%d').strftime('%B %d, %Y')} 
        as a {profile['job_title']}.</p>
        
        <p>In their role at {profile['company']}, {profile['last_name']} is responsible for:</p>
        <ul>
            <li>Managing security infrastructure and protocols</li>
            <li>Conducting security assessments and penetration testing</li>
            <li>Developing security policies and procedures</li>
            <li>Training staff on security best practices</li>
        </ul>
        
        <h2 id="achievements">Achievements</h2>
        <p>{profile['full_name']} has received several industry recognitions:</p>
        <ul>
            <li>{datetime.now().year - 2} - Cybersecurity Excellence Award</li>
            <li>{datetime.now().year - 3} - Speaker at DEF CON conference</li>
            <li>{datetime.now().year - 4} - Published research on advanced persistent threats</li>
        </ul>
        
        <h2 id="personal">Personal life</h2>
        <p>{profile['last_name']} resides in the greater New York area. Their interests include 
        {', '.join(profile.get('hobbies', ['technology', 'security research']))}. They are active on 
        professional networks and frequently contribute to open-source security projects.</p>
        
        <h2 id="references">References</h2>
        <ol class="references">
            <li>"Industry Leaders in Cybersecurity" - TechSecurity Magazine, {datetime.now().year - 1}</li>
            <li>"{profile['company']} Strengthens Security Team" - Corporate Press Release, {datetime.strptime(profile['hire_date'], '%Y-%m-%d').year}</li>
            <li>"Rising Stars in Information Security" - InfoSec Weekly, {datetime.now().year - 2}</li>
            <li>{profile['education']} Alumni Newsletter, Spring {datetime.now().year}</li>
        </ol>
        
        <hr>
        <p style="font-size: 0.8em; color: #666;">
            This page was last edited on {datetime.now().strftime('%d %B %Y, at %H:%M')} (UTC).<br>
            Text is available under the Creative Commons Attribution-ShareAlike License.
        </p>
    </div>
</body>
</html>"""
    
    return template

def main():
    """Main function"""
    print("=== Wikipedia Page Generator ===")
    print("Recreating Elliot's Steel Mountain infiltration technique\n")
    
    # Check if profile exists
    profile_id = input("Enter profile ID (or 'load' to select from existing): ")
    
    if profile_id == 'load':
        # List available profiles
        import os
        profiles_dir = "/data/profiles"
        if os.path.exists(profiles_dir):
            files = [f for f in os.listdir(profiles_dir) if f.endswith('.json')]
            if files:
                print("\nAvailable profiles:")
                for i, f in enumerate(files, 1):
                    print(f"{i}. {f}")
                
                choice = int(input("\nSelect profile: ")) - 1
                if 0 <= choice < len(files):
                    with open(os.path.join(profiles_dir, files[choice]), 'r') as f:
                        profile = json.load(f)
                        if isinstance(profile, list):
                            profile = profile[0]  # Take first if batch
            else:
                print("No profiles found!")
                return
    else:
        # Load specific profile
        try:
            with open(f"/data/profiles/{profile_id}_profile.json", 'r') as f:
                profile = json.load(f)
        except FileNotFoundError:
            print(f"Profile {profile_id} not found!")
            return
    
    # Generate Wikipedia page
    html_content = generate_wikipedia_page(profile)
    
    # Save the page
    filename = f"/data/campaigns/wikipedia_{profile['id']}.html"
    with open(filename, 'w') as f:
        f.write(html_content)
    
    print(f"\nWikipedia page generated: {filename}")
    print(f"Profile: {profile['full_name']} - {profile['job_title']} at {profile['company']}")
    print("\nUse this for pretexting when calling or visiting the target location!")
    
    # Generate a shortened URL for realism
    short_url = f"https://en.wikipedia.org/wiki/{profile['full_name'].replace(' ', '_')}"
    print(f"\nFake Wikipedia URL: {short_url}")
    print("(Note: This is a simulation - do not attempt to create real Wikipedia pages)")

if __name__ == "__main__":
    main()