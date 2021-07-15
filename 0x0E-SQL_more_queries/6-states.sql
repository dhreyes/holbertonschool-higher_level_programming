-- Script to create database hbtn_0d_usa and table states
-- create states with id, and name
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Select database
USE hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS states(
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL);
