-- 13. Rivers in Africa
-- https://judge.softuni.org/Contests/Compete/Index/4111#11

SELECT c.country_name,
       r.river_name
FROM countries c
         LEFT JOIN countries_rivers cr USING (country_code)
         LEFT JOIN rivers r ON r.id = cr.river_id
WHERE c.continent_code = 'AF'
ORDER BY c.country_name
LIMIT 5;

