-- This script will create database and table

SELECT id, name 
FROM cities
WHERE state_id = 
    (SELECT id 
    FROM states 
    WHERE name = 'California'
)