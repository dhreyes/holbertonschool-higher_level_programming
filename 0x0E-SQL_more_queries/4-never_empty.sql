-- Script to create table id_not_null with id, name
-- Create id_not_null, with int value 1, and VARCHAR(256)
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT NOT NULL DEFAULT 1,
	name VARCHAR(256));
