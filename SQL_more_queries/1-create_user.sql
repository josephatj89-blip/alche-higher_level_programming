-- creates the MySQL server user user_0d_1 with all privileges (no failure if it already exists)
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- make sure the password is correct even if the user already existed
ALTER USER 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- give all privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
