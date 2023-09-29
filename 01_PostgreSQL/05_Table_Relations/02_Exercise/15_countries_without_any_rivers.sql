-- 15. Countries Without Any Rivers
-- url: https://judge.softuni.org/Contests/Compete/Index/4109#11

SELECT count(*) AS countries_without_rivers
FROM countries c
         LEFT JOIN countries_rivers cr ON cr.country_code = c.country_code
WHERE cr.country_code IS NULL;


-- This works when both sides has same columns
-- SELECT count(*) AS countries_without_rivers
-- FROM countries
-- LEFT JOIN countries_rivers USING (country_code)
-- WHERE country_code IS NULL;