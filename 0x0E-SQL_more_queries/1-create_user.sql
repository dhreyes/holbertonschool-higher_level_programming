-- Script to create user in server with privelages
-- Create user with privelages
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant priveleges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- Makes sure priveleges are gucci
FLUSH PRIVILEGES;
