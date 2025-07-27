#!/usr/bin/env python3
"""
Phishing Campaign Simulator for Social Engineering Lab
Creates realistic phishing scenarios for educational purposes
"""

from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import datetime
import os

app = Flask(__name__)

# Phishing templates
PHISHING_TEMPLATES = {
    'it_support': {
        'subject': 'Urgent: Password Expiration Notice',
        'sender': 'IT Support <itsupport@steelmountain.com>',
        'body': '''Dear {name},

Your Steel Mountain network password will expire in 24 hours. To avoid interruption to your work, please update your password immediately.

Click here to update your password: http://steelmountain-secure.com/password-reset

If you do not update your password within 24 hours, your account will be locked and you will need to contact IT support.

Best regards,
IT Support Team
Steel Mountain Data Security
'''
    },
    'ceo_fraud': {
        'subject': 'Urgent Request',
        'sender': 'James Plouffe <jplouffe@steelmountain.com>',
        'body': '''Hi {name},

I need you to handle something urgently. I'm in a meeting and can't access my computer.

Can you please purchase $500 worth of Amazon gift cards for client gifts? This is time-sensitive.

Send me the gift card codes as soon as you have them.

Thanks,
James Plouffe
Chief Security Officer
'''
    },
    'payroll_update': {
        'subject': 'Action Required: Payroll Information Update',
        'sender': 'HR Department <hr@steelmountain.com>',
        'body': '''Dear {name},

We are updating our payroll system and need all employees to verify their information.

Please click the link below to confirm your banking details:
http://steelmountain-payroll.com/verify

This must be completed by end of business today to ensure your next paycheck is processed correctly.

Thank you,
Human Resources
Steel Mountain Data Security
'''
    },
    'security_alert': {
        'subject': 'Security Alert: Suspicious Activity Detected',
        'sender': 'Security Team <security@steelmountain.com>',
        'body': '''SECURITY ALERT

We have detected suspicious login attempts on your account from IP: 192.168.1.100

If this was not you, please verify your account immediately:
http://steelmountain-verify.com/secure

Location: Moscow, Russia
Time: {time}

This is an automated security message. Do not reply to this email.

Steel Mountain Security Team
'''
    }
}

# Track phishing campaigns
campaigns = []

@app.route('/')
def index():
    """Phishing campaign dashboard"""
    return '''
    <html>
    <head>
        <title>Phishing Campaign Simulator</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 1000px; margin: 0 auto; padding: 20px; }
            .template { background: #f0f0f0; padding: 15px; margin: 10px 0; border-radius: 5px; }
            button { background: #007bff; color: white; padding: 10px 20px; border: none; cursor: pointer; }
            .warning { background: #ff0000; color: white; padding: 10px; margin: 20px 0; }
        </style>
    </head>
    <body>
        <h1>Phishing Campaign Simulator</h1>
        <div class="warning">
            ⚠️ EDUCATIONAL PURPOSE ONLY - DO NOT USE ON REAL TARGETS ⚠️
        </div>
        
        <h2>Available Templates</h2>
        <div id="templates"></div>
        
        <h2>Launch Campaign</h2>
        <form id="campaignForm">
            <label>Template: <select id="template" required></select></label><br>
            <label>Target Name: <input type="text" id="targetName" required></label><br>
            <label>Target Email: <input type="email" id="targetEmail" required></label><br>
            <button type="submit">Launch Campaign</button>
        </form>
        
        <h2>Campaign Results</h2>
        <div id="results"></div>
        
        <script>
            // Load templates
            fetch('/api/templates')
                .then(r => r.json())
                .then(data => {
                    const container = document.getElementById('templates');
                    const select = document.getElementById('template');
                    
                    Object.entries(data).forEach(([key, template]) => {
                        // Display template
                        const div = document.createElement('div');
                        div.className = 'template';
                        div.innerHTML = `<h3>${key}</h3><p><strong>Subject:</strong> ${template.subject}</p>`;
                        container.appendChild(div);
                        
                        // Add to select
                        const option = document.createElement('option');
                        option.value = key;
                        option.text = key;
                        select.appendChild(option);
                    });
                });
            
            // Handle form submission
            document.getElementById('campaignForm').onsubmit = async (e) => {
                e.preventDefault();
                
                const response = await fetch('/api/send', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        template: document.getElementById('template').value,
                        target_name: document.getElementById('targetName').value,
                        target_email: document.getElementById('targetEmail').value
                    })
                });
                
                const result = await response.json();
                alert(result.message);
                loadResults();
            };
            
            // Load results
            function loadResults() {
                fetch('/api/campaigns')
                    .then(r => r.json())
                    .then(data => {
                        const container = document.getElementById('results');
                        container.innerHTML = data.map(c => 
                            `<div class="template">
                                <strong>${c.template}</strong> → ${c.target_email}<br>
                                Sent: ${c.timestamp}<br>
                                Status: ${c.status}
                            </div>`
                        ).join('');
                    });
            }
            
            loadResults();
        </script>
    </body>
    </html>
    '''

@app.route('/api/templates')
def get_templates():
    """Return available phishing templates"""
    return jsonify(PHISHING_TEMPLATES)

@app.route('/api/send', methods=['POST'])
def send_phishing():
    """Send phishing email (simulated)"""
    data = request.json
    
    template = PHISHING_TEMPLATES.get(data['template'])
    if not template:
        return jsonify({'error': 'Invalid template'}), 400
    
    # Format the email
    body = template['body'].format(
        name=data['target_name'],
        time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )
    
    # Log the campaign
    campaign = {
        'id': len(campaigns) + 1,
        'template': data['template'],
        'target_name': data['target_name'],
        'target_email': data['target_email'],
        'timestamp': datetime.datetime.now().isoformat(),
        'status': 'sent',
        'body': body,
        'subject': template['subject']
    }
    campaigns.append(campaign)
    
    # In real scenario, this would send to MailHog
    # For simulation, we just log it
    print(f"Phishing email sent: {campaign}")
    
    return jsonify({
        'success': True,
        'message': f'Phishing email sent to {data["target_email"]}',
        'campaign_id': campaign['id']
    })

@app.route('/api/campaigns')
def get_campaigns():
    """Return campaign history"""
    return jsonify(campaigns)

@app.route('/api/click/<int:campaign_id>')
def track_click(campaign_id):
    """Track when target clicks phishing link"""
    for campaign in campaigns:
        if campaign['id'] == campaign_id:
            campaign['clicked'] = True
            campaign['click_time'] = datetime.datetime.now().isoformat()
            return jsonify({'tracked': True})
    return jsonify({'error': 'Campaign not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)