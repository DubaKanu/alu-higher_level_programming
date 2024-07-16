-- Connect to MySQL server
SELECT VERSION() AS 'mysql_version'; 

-- Check if user_0d_1 is root (all privileges)
SHOW GRANTS FOR 'user_0d_1'@'%'; 

-- Show grants for user_0d_2 (assuming no root privileges)
SHOW GRANTS FOR 'user_0d_2'@'localhost';
