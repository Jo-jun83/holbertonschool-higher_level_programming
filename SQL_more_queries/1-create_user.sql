-- This SQL statement creates a new user 'user_0d_1' with the specified password if the user does not already exist.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';