-- Script to list all cities in california
-- list records with only one California
SELECT id, name FROM cities
WHERE state_id =
	(SELECT id
	FROM states
	WHERE name = "California")
ORDER BY cities.id;
