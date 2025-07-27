<?php
// Intentionally vulnerable login script for educational purposes

$username = $_POST['username'] ?? '';
$password = $_POST['password'] ?? '';

// Vulnerable to SQL injection
$connection = new mysqli('coffee-shop-db', 'dbuser', 'dbpass123', 'customers');

if ($connection->connect_error) {
    die("Connection failed: " . $connection->connect_error);
}

// Intentionally vulnerable SQL query
$query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
$result = $connection->query($query);

if ($result && $result->num_rows > 0) {
    $user = $result->fetch_assoc();
    session_start();
    $_SESSION['user'] = $user['username'];
    
    // Vulnerable: Exposing sensitive information
    echo "<h1>Welcome " . $user['username'] . "!</h1>";
    echo "<p>Account Type: " . $user['role'] . "</p>";
    echo "<p>Last Login: " . $user['last_login'] . "</p>";
    echo "<p>Credit Card on File: ****" . substr($user['credit_card'], -4) . "</p>";
    echo '<a href="admin/">Admin Panel</a>';
} else {
    echo "<h1>Login Failed!</h1>";
    echo "<p>Invalid username or password</p>";
    // Vulnerable: Information disclosure
    echo "<!-- Debug: Query was: $query -->";
    echo '<a href="index.php">Try Again</a>';
}

$connection->close();
?>