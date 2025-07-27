<?php
// Employee directory with intentionally exposed information
$employees = [
    [
        'name' => 'James Plouffe',
        'title' => 'Chief Security Officer',
        'department' => 'Information Security',
        'email' => 'jplouffe@steelmountain.com',
        'phone' => '(212) 555-2001',
        'bio' => 'James has over 20 years of experience in cybersecurity. CISSP certified. Graduate of MIT.',
        'start_date' => '2015-03-15',
        'image' => 'https://thispersondoesnotexist.com/image?1'
    ],
    [
        'name' => 'Bill Harper',
        'title' => 'VP of Operations',
        'department' => 'Operations',
        'email' => 'bharper@steelmountain.com',
        'phone' => '(212) 555-2002',
        'bio' => 'Bill oversees daily operations at all Steel Mountain facilities. Former military. Enjoys golf.',
        'start_date' => '2010-06-20',
        'image' => 'https://thispersondoesnotexist.com/image?2'
    ],
    [
        'name' => 'Sarah Chen',
        'title' => 'IT Director',
        'department' => 'Information Technology',
        'email' => 'schen@steelmountain.com',
        'phone' => '(212) 555-2003',
        'bio' => 'Sarah leads our IT infrastructure team. Stanford graduate. Active in Women in Tech groups.',
        'start_date' => '2018-01-10',
        'image' => 'https://thispersondoesnotexist.com/image?3'
    ],
    [
        'name' => 'Michael Rodriguez',
        'title' => 'Network Administrator',
        'department' => 'IT Infrastructure',
        'email' => 'mrodriguez@steelmountain.com',
        'phone' => '(212) 555-2010',
        'bio' => 'Michael maintains our network infrastructure. CCNA certified. Passionate about network security.',
        'start_date' => '2019-04-05',
        'image' => 'https://thispersondoesnotexist.com/image?4'
    ],
    [
        'name' => 'Jennifer Walsh',
        'title' => 'Security Analyst',
        'department' => 'Information Security',
        'email' => 'jwalsh@steelmountain.com',
        'phone' => '(212) 555-2011',
        'bio' => 'Jennifer specializes in threat analysis and incident response. CEH certified.',
        'start_date' => '2020-07-15',
        'image' => 'https://thispersondoesnotexist.com/image?5'
    ],
    [
        'name' => 'David Park',
        'title' => 'Database Administrator',
        'department' => 'IT Infrastructure',
        'email' => 'dpark@steelmountain.com',
        'phone' => '(212) 555-2012',
        'bio' => 'David manages our database systems. Oracle certified. Enjoys hiking on weekends.',
        'start_date' => '2017-11-30',
        'image' => 'https://thispersondoesnotexist.com/image?6'
    ]
];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Our Team - Steel Mountain Data Security</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        .employee-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
            margin-top: 30px;
        }
        .employee-card {
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .employee-header {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
        }
        .employee-image {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            margin-right: 15px;
        }
        .employee-info h3 {
            margin: 0;
            color: #333;
        }
        .employee-info p {
            margin: 5px 0;
            color: #666;
        }
        .employee-details {
            margin-top: 15px;
            padding-top: 15px;
            border-top: 1px solid #eee;
        }
        .detail-row {
            margin: 8px 0;
        }
        .detail-label {
            font-weight: bold;
            color: #555;
        }
        nav {
            background-color: #333;
            padding: 10px 0;
            margin-bottom: 20px;
        }
        nav a {
            color: white;
            text-decoration: none;
            padding: 10px 20px;
        }
    </style>
</head>
<body>
    <nav>
        <div class="container">
            <a href="/">Home</a>
            <a href="/team.php">Our Team</a>
            <a href="/contact.php">Contact</a>
        </div>
    </nav>
    
    <div class="container">
        <h1>Meet Our Team</h1>
        <p>The dedicated professionals keeping your data secure</p>
        
        <div class="employee-grid">
            <?php foreach ($employees as $employee): ?>
            <div class="employee-card">
                <div class="employee-header">
                    <img src="<?php echo $employee['image']; ?>" alt="<?php echo $employee['name']; ?>" class="employee-image">
                    <div class="employee-info">
                        <h3><?php echo $employee['name']; ?></h3>
                        <p><?php echo $employee['title']; ?></p>
                        <p style="font-size: 0.9em; color: #888;"><?php echo $employee['department']; ?></p>
                    </div>
                </div>
                
                <div class="employee-details">
                    <div class="detail-row">
                        <span class="detail-label">Email:</span> 
                        <a href="mailto:<?php echo $employee['email']; ?>"><?php echo $employee['email']; ?></a>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Phone:</span> <?php echo $employee['phone']; ?>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Start Date:</span> 
                        <?php echo date('F Y', strtotime($employee['start_date'])); ?>
                    </div>
                    <div class="detail-row" style="margin-top: 10px;">
                        <?php echo $employee['bio']; ?>
                    </div>
                </div>
                
                <!-- Intentionally exposed metadata -->
                <div style="display: none;" class="employee-meta">
                    <?php echo json_encode($employee); ?>
                </div>
            </div>
            <?php endforeach; ?>
        </div>
        
        <!-- CSV export link (vulnerable) -->
        <div style="margin-top: 40px; text-align: center;">
            <a href="/export.php?type=employees&format=csv" style="color: #0066cc;">Download Employee Directory (CSV)</a>
        </div>
    </div>
    
    <!-- Vulnerable: Exposes internal information -->
    <!-- Employee VPN: vpn.steelmountain.local -->
    <!-- Helpdesk: helpdesk@steelmountain.com -->
    <!-- IT Support: x2999 -->
</body>
</html>