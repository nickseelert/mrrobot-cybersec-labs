<!DOCTYPE html>
<html>
<head>
    <title>Ron's Coffee Shop - Free WiFi</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
        }
        .login-form {
            background: #e9e9e9;
            padding: 20px;
            margin-top: 20px;
            border-radius: 5px;
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
        }
        .warning {
            color: #ff0000;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to Ron's Coffee Shop</h1>
        <p>Enjoy our free WiFi while you enjoy your coffee!</p>
        
        <h2>Today's Specials</h2>
        <ul>
            <li>Latte - $4.50</li>
            <li>Cappuccino - $4.00</li>
            <li>Espresso - $3.00</li>
        </ul>

        <div class="login-form">
            <h3>Staff Login</h3>
            <form method="POST" action="login.php">
                <input type="text" name="username" placeholder="Username">
                <input type="password" name="password" placeholder="Password">
                <button type="submit">Login</button>
            </form>
            <p class="warning">Warning: This is a vulnerable application for educational purposes only!</p>
        </div>

        <div style="margin-top: 30px;">
            <p>WiFi Password: <strong>RonsCoffee2023</strong></p>
            <p><small>Network: CoffeeShop_Guest</small></p>
        </div>

        <!-- Intentionally exposed comment for recon lab -->
        <!-- TODO: Move admin panel from /admin to more secure location -->
        <!-- Database credentials in /backup/config.txt -->
        
        <?php
        // Vulnerable PHP code - displays server info
        if (isset($_GET['debug'])) {
            phpinfo();
        }
        ?>
    </div>
</body>
</html>