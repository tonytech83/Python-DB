-- 13. Positive and Negative LEFT
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#12

SELECT peak_name,
       LEFT(peak_name, 4) AS "Positive Left",
       LEFT(peak_name, -4) AS "Negative Left"
FROM peaks;