-- Script to create table force_name with id and name
-- Create force_name with id and name, name cannot be null
CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) NOT NULL);
