-- Initialize the coffee shop database
CREATE DATABASE IF NOT EXISTS customers;
USE customers;

-- Users table with intentionally weak security
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,  -- Plain text passwords (bad practice for demo)
    email VARCHAR(100),
    role VARCHAR(20),
    credit_card VARCHAR(20),
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT INTO users (username, password, email, role, credit_card) VALUES
('admin', 'admin123', 'admin@ronscoffee.com', 'administrator', '4532987654321098'),
('ron', 'coffee123', 'ron@ronscoffee.com', 'owner', '4024007123456789'),
('john_doe', 'password123', 'john@email.com', 'customer', '4532123456789012'),
('jane_smith', 'qwerty', 'jane.smith@gmail.com', 'customer', '5412753498214567'),
('employee1', 'emp123', 'emp1@ronscoffee.com', 'employee', '4916123456789012');

-- Orders table
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    item VARCHAR(100),
    price DECIMAL(10,2),
    payment_method VARCHAR(20),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Insert sample orders
INSERT INTO orders (user_id, item, price, payment_method) VALUES
(3, 'Latte', 4.50, 'credit_card'),
(4, 'Cappuccino', 4.00, 'credit_card'),
(3, 'Espresso', 3.00, 'cash'),
(5, 'Americano', 3.50, 'credit_card');

-- API keys table (intentionally exposed)
CREATE TABLE api_keys (
    id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(50),
    api_key VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO api_keys (service_name, api_key) VALUES
('payment_gateway', 'pk_test_4eC39HqLyjWDarjtT1zdp7dc'),
('email_service', 'SG.IKqQXq3mQRy0Eg2L4BPX1g.kHVT_test_key'),
('analytics', 'UA-123456789-1');

-- Grant permissions (overly permissive for demo)
GRANT ALL PRIVILEGES ON customers.* TO 'dbuser'@'%';
FLUSH PRIVILEGES;