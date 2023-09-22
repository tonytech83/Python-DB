-- 15. Update iso_code
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#14

UPDATE countries
SET iso_code = upper(left(country_name, 3))
WHERE iso_code IS NULL;