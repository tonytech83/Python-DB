-- 04. Limit Records
-- url: https://judge.softuni.org/Contests/Compete/Index/4103#3

SELECT id                                 AS "ID",
       concat(first_name, ' ', last_name) AS "Full Name",
       job_title                          AS "Job Title"
FROM employees
ORDER BY first_name
LIMIT 50;