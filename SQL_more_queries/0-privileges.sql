-- Connect to MySQL server
SELECT VERSION() AS 'mysql_version'; 

-- Check if user_0d_1 is root (all privileges)
SHOW GRANTS FOR 'user_0d_1'@'%'; 

-- Show grants for user_0d_2 focusing on user_2_db
SHOW GRANTS FOR 'user_0d_2'@'localhost' ON `user_2_db`*;
