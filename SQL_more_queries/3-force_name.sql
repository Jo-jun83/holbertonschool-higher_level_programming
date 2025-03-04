-- This SQL query creates a table named 'force_name' if it does not already exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);