-- 01. Departments Info by ID
-- url: https://judge.softuni.org/Contests/Practice/Index/4106#0

SELECT department_id,
       count(*) AS employee_count
FROM employees
GROUP BY department_id
ORDER BY department_id;