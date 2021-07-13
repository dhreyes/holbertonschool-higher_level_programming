-- script to create table called second_table
-- creates table in current server
CREATE TABLE IF NOT EXISTS second_table(id INT,
	name VARCHAR(256),
	score INT);
-- John
INSERT INTO second_table (id, name, score) VALUES (1, "John", 10);
-- Alex
INSERT INTO second_table (id, name, score) VALUES (2, "Alex", 3);
-- Bob
INSERT INTO second_table (id, name, score) VALUES (3, "Bob", 14);
-- George
INSERT INTO second_table (id, name, score) VALUES (4, "George", 8);
