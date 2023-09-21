-- 09. TRAILING
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#8

SELECT continent_name,
       trim(TRAILING FROM continent_name) AS trim
FROM continents;
