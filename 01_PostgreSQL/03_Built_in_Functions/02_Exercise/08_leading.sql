-- 08. LEADING
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#7

SELECT continent_name,
       trim(LEADING FROM continent_name) AS trim
FROM continents;
