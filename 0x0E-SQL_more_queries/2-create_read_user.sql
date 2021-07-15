-- Script to create database hbtn_0d_2 and user_0d_2
-- create database and user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Privelages for user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
