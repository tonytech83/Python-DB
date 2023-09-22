-- 25. COUNT by Initial
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#22

SELECT substring(first_name, 1, 2) AS initials,
       count(first_name)           AS user_count
FROM users
GROUP BY initials
ORDER BY user_count DESC, initials;

