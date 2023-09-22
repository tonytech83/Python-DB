-- 14. Positive and Negative RIGHT
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#13

SELECT peak_name,
       right(peak_name, 4) AS "Positive Right",
       right(peak_name, -4) AS "Negative Right"
FROM peaks;