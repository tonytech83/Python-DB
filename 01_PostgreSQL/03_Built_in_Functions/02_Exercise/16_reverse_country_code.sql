-- 16. REVERSE country_code
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#15

UPDATE countries
SET country_code = reverse(lower(country_code));
