-- 06. Replace A
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#5

SELECT replace(mountain_range, 'a', '@') AS "replace_a",
       replace(mountain_range, 'A', '$') AS "replace_A"
FROM mountains;


