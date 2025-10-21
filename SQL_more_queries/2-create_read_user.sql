-- create users read only

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT READ ON hbtn_0d_2 TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
