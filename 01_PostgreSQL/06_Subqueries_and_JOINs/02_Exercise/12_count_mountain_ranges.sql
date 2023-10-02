-- 12. Count Mountain Ranges
-- https://judge.softuni.org/Contests/Compete/Index/4111#10

SELECT country_code,
       count(mountain_range) AS mountain_range_count
FROM mountains_countries ms
         JOIN mountains m ON m.id = ms.mountain_id
WHERE country_code IN ('US', 'RU', 'BG')
GROUP BY country_code
ORDER BY mountain_range_count DESC;