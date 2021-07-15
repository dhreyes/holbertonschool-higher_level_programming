-- Script to create database hbtn_0d_usa and table cities
-- create cities with id, state_id, and name
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- select database
USE hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS cities(
	id INT PRIMARY KEY AUTO_INCREMENT,
	state_id INT NOT NULL,
	FOREIGN KEY(state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL);
