-- 11. Compare Character Values
-- url: https://judge.softuni.org/Contests/Compete/Index/4103#10

SELECT name,
       start_date
FROM projects
WHERE name IN ('Mountain', 'Road', 'Touring')
LIMIT 20;
