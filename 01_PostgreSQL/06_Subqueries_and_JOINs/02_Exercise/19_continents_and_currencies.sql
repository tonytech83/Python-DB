-- 19. Continents and Currencies
-- https://judge.softuni.org/Contests/Compete/Index/4111#17

CREATE VIEW continent_currency_usage AS
SELECT c.continent_code,
       c.currency_code,
       COUNT(*) AS currency_usage
FROM countries c
GROUP BY c.continent_code,
         c.currency_code
HAVING COUNT(*) > 1
   AND COUNT(*) =
       (SELECT COUNT(*) AS most_used_curr
        FROM countries c2
        WHERE c2.continent_code = c.continent_code
        GROUP BY c2.currency_code
        ORDER BY most_used_curr DESC
        LIMIT 1)
ORDER BY currency_usage DESC, c.continent_code;

