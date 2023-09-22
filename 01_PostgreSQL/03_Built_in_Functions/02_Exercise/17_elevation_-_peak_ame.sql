-- 17. Elevation --->> Peak Name
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#16

SELECT concat(elevation, ' ', repeat('-', 3), repeat('>', 2), ' ', peak_name) AS "Elevation --->> Peak Name"
FROM peaks
WHERE elevation >= 4884;
