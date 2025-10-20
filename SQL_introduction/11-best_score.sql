-- This script will lists all records =>10 of second_table ordered by score (

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
