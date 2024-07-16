-- Check if database hbtn_0d_2 already exists
SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'hbtn_0d_2';

-- Create database hbtn_0d_2 if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Check if user user_0d_2 already exists
SELECT USER FROM mysql.user WHERE USER = 'user_0d_2';

-- Create user user_0d_2 if it doesn't exist
CREATE USER IF NOT EXISTS user_0d_2 IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on hbtn_0d_2 to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
