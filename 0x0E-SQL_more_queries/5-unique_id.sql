-- Script to create table unique_id with id and name
-- create unique_id with unique id and VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256));
