-- Script to list all cities in database hbtn_0d_usa
-- Display by cities.id - cities.name - states.name
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id;
