<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Steel Mountain Data Security - Protecting Your Digital Assets</title>
    <meta name="description" content="Steel Mountain is the leader in secure data storage and disaster recovery solutions">
    <meta name="keywords" content="data security, disaster recovery, secure storage, compliance">
    <meta name="author" content="Steel Mountain IT Department">
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            color: #333;
        }
        
        header {
            background-color: #1a1a1a;
            color: white;
            padding: 20px 0;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        nav {
            background-color: #333;
            padding: 10px 0;
        }
        
        nav ul {
            list-style: none;
            display: flex;
        }
        
        nav li {
            margin-right: 20px;
        }
        
        nav a {
            color: white;
            text-decoration: none;
            padding: 5px 10px;
        }
        
        nav a:hover {
            background-color: #555;
        }
        
        .hero {
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('images/datacenter.jpg');
            background-size: cover;
            color: white;
            padding: 100px 0;
            text-align: center;
        }
        
        .hero h1 {
            font-size: 48px;
            margin-bottom: 20px;
        }
        
        .content {
            background: white;
            padding: 40px 0;
            margin: 20px 0;
        }
        
        .team-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 30px;
        }
        
        .team-member {
            background: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }
        
        .team-member img {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            margin-bottom: 15px;
        }
        
        footer {
            background-color: #1a1a1a;
            color: white;
            padding: 30px 0;
            text-align: center;
        }
        
        .news-ticker {
            background: #ff0000;
            color: white;
            padding: 10px;
            overflow: hidden;
        }
        
        .news-ticker span {
            display: inline-block;
            padding-left: 100%;
            animation: scroll 20s linear infinite;
        }
        
        @keyframes scroll {
            0% { transform: translateX(0); }
            100% { transform: translateX(-100%); }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>STEEL MOUNTAIN</h1>
            <p>Secure Data Storage Solutions Since 1998</p>
        </div>
    </header>
    
    <nav>
        <div class="container">
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/about.php">About Us</a></li>
                <li><a href="/services.php">Services</a></li>
                <li><a href="/team.php">Our Team</a></li>
                <li><a href="/careers.php">Careers</a></li>
                <li><a href="/contact.php">Contact</a></li>
                <li><a href="/login.php">Employee Portal</a></li>
            </ul>
        </div>
    </nav>
    
    <div class="news-ticker">
        <span>BREAKING: Steel Mountain achieves SOC 2 Type II certification • Now serving over 500 Fortune 1000 companies • 99.999% uptime guaranteed • State-of-the-art facilities in NY, VA, and CA</span>
    </div>
    
    <section class="hero">
        <div class="container">
            <h1>Your Data. Our Fortress.</h1>
            <p>Industry-leading secure data storage and disaster recovery solutions</p>
        </div>
    </section>
    
    <section class="content">
        <div class="container">
            <h2>Why Choose Steel Mountain?</h2>
            <p>With over 25 years of experience, Steel Mountain is the trusted name in secure data storage. Our state-of-the-art facilities feature:</p>
            <ul style="margin: 20px 0; padding-left: 40px;">
                <li>Military-grade physical security</li>
                <li>24/7 monitoring and surveillance</li>
                <li>Redundant power and cooling systems</li>
                <li>Compliance with HIPAA, SOX, and PCI-DSS</li>
                <li>Biometric access controls</li>
            </ul>
            
            <h2 style="margin-top: 40px;">Leadership Team</h2>
            <div class="team-grid">
                <div class="team-member">
                    <img src="https://thispersondoesnotexist.com/image?1" alt="James Plouffe">
                    <h3>James Plouffe</h3>
                    <p>Chief Security Officer</p>
                    <p>jplouffe@steelmountain.com</p>
                    <p>Ext: 2001</p>
                </div>
                
                <div class="team-member">
                    <img src="https://thispersondoesnotexist.com/image?2" alt="Bill Harper">
                    <h3>Bill Harper</h3>
                    <p>VP of Operations</p>
                    <p>bharper@steelmountain.com</p>
                    <p>Ext: 2002</p>
                </div>
                
                <div class="team-member">
                    <img src="https://thispersondoesnotexist.com/image?3" alt="Sarah Chen">
                    <h3>Sarah Chen</h3>
                    <p>IT Director</p>
                    <p>schen@steelmountain.com</p>
                    <p>Ext: 2003</p>
                </div>
            </div>
            
            <!-- Hidden comment for OSINT practice -->
            <!-- TODO: Remove before production
                 Admin panel: /admin/dashboard.php
                 Test credentials: admin:TempPass123!
                 Employee directory: /staff/directory.php
                 Internal wiki: http://wiki.steelmountain.local
            -->
        </div>
    </section>
    
    <footer>
        <div class="container">
            <p>&copy; <?php echo date('Y'); ?> Steel Mountain Data Security. All rights reserved.</p>
            <p>Corporate HQ: 123 Security Blvd, New York, NY 10001 | Phone: (212) 555-0100</p>
            <p><small>Site last updated: <?php echo date('F j, Y'); ?></small></p>
        </div>
    </footer>
    
    <?php
    // Intentionally vulnerable - exposes server information
    if (isset($_GET['debug'])) {
        echo "<!-- Debug Info: " . php_uname() . " -->";
    }
    ?>
</body>
</html>