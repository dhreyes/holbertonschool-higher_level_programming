-- script to list number of records with same score
-- list duplicate scores
SELECT `score`, COUNT(*) AS "number"
FROM second_table
GROUP BY `score`
ORDER BY `number` DESC;
