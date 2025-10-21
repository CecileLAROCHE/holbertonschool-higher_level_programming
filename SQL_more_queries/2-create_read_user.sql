-- create users read only

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT READ ON *.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
