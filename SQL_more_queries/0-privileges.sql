-- Create user_0d_1 with full (root-like) privileges
CREATE USER 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Create user_0d_2 with limited privileges on user_2_db
CREATE USER 'user_0d_2'@'localhost';
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

-- Show privileges for both users
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
