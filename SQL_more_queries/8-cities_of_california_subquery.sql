-- This script will create database and table

USE hbtn_0d_usa;
SELECT name 
FROM cities
WHERE state_id = 
    (SELECT id 
    FROM states 
    WHERE name = 'California'
)
ORDER BY cities ASC;
