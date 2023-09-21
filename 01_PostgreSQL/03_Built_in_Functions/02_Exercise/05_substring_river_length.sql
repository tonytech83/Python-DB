-- 05. Substring River Length
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#4

SELECT (regexp_match("River Information", '([0-9]{1,4})'))[1] AS river_length
FROM view_river_info;

-- SELECT substring("River Information", '([0-9]{1,4})') AS river_length
-- FROM view_river_info;


