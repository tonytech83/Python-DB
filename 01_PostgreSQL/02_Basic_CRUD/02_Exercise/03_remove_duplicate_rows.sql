-- 03. Remove Duplicate Rows
-- url: https://judge.softuni.org/Contests/Compete/Index/4103#2

SELECT distinct name,
                area AS "Aria (km2)"
FROM cities
ORDER BY name DESC;