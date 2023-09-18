-- 05. Skip Rows
-- url: https://judge.softuni.org/Contests/Compete/Index/4103#4

SELECT id,
       concat_ws(' ',first_name, middle_name, last_name) AS "Full Name",
       hire_date AS "Hire Date"
FROM employees
ORDER BY "Hire Date"
OFFSET 9;