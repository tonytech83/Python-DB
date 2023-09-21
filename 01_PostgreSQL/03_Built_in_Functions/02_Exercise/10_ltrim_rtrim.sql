-- 10. LTRIM & RTRIM
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#9

SELECT ltrim(peak_name, 'M') AS "Left Trim",
       rtrim(peak_name, 'm') AS "Right Trim"
FROM peaks;
