-- This script will create database and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities  (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
    states(id) NOT NULL,
    name VARCHAR(256) NOT NULL
    FOREIGN KEY (state_id) REFERENCES states(id) NOT NULL,
);
