-- 13. Missing Value
-- url: https://judge.softuni.org/Contests/Compete/Index/4103#12

SELECT id,
       first_name,
       last_name
FROM employees
WHERE middle_name IS NULL
LIMIT 3;
