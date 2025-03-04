-- This SQL query creates a table named 'unique_id' if it does not already exist with default value and unique id
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);