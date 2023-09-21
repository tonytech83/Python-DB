-- 12. Length of a Number
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#11

SELECT population,
       length(population::varchar) AS length
FROM countries;

