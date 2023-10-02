-- 11. Bulgaria's Peaks Higher than 2835 Meters
-- https://judge.softuni.org/Contests/Compete/Index/4111#9

SELECT mc.country_code,
       m.mountain_range,
       p.peak_name,
       p.elevation
FROM mountains_countries mc
         JOIN mountains m ON m.id = mc.mountain_id
         JOIN peaks p ON p.mountain_id = m.id
WHERE p.elevation > 2835
  AND mc.country_code = 'BG'
ORDER BY p.elevation DESC;