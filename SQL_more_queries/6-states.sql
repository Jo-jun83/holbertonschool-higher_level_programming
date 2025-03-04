-- This SQL statement creates the database 'hbtn_0d_usa' if it does not already exist and the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(256) NOT NULL
);