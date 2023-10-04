-- 17. Monasteries by Continents and Countries
-- https://judge.softuni.org/Contests/Compete/Index/4111#15

UPDATE countries
SET country_name = 'Burma'
WHERE country_name = 'Myanmar';

INSERT INTO monasteries (monastery_name, country_code)
VALUES ('Hanga Abbey', (SELECT country_code FROM countries WHERE country_name = 'Tanzania')),
       ('Myin-Tin-Daik', (SELECT country_code FROM countries WHERE country_name = 'Myanmar'));

SELECT c2.continent_name,
       c1.country_name,
       count(m.id) AS monasteries_count
FROM countries c1
         LEFT JOIN continents c2 USING (continent_code)
         LEFT JOIN monasteries m USING (country_code)
WHERE NOT c1.three_rivers
GROUP BY c1.country_name, continent_name
ORDER BY monasteries_count DESC, country_name;