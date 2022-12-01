-- lists all the cities of California

SELECT id, name FROM cities WHERE name = (
SELECT name FROM states WHERE name = "California"
) ORDER BY id ASC;
