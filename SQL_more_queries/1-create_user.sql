-- Create user if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- Make sure the password is correct even if the user already existed
ALTER USER 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- Give all privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
