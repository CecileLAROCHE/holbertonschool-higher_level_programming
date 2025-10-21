-- This script will create database and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities  (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
    SELECT id FROM states WHERE name = 'California'
    SELECT name FROM cities WHERE state_id = (id_de_california)
    WHERE state_id = (SELECT id FROM states WHERE name = 'California')
    name VARCHAR(256) NOT NULL
);