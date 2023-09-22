-- 25. COUNT by Initial
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#22

SELECT left(first_name, 2) AS initials,
       count(id)           AS user_count
FROM users
GROUP BY initials
ORDER BY user_count DESC, initials;

-- Other way of solution
-- SELECT left(first_name, 2) AS initials,
--        count('initials')   AS user_count
-- FROM users
-- GROUP BY initials
-- ORDER BY user_count DESC, initials;

