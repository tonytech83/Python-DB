-- 05. Minimum Salary
-- url: https://judge.softuni.org/Contests/Practice/Index/4106#4

SELECT department_id,
       min(salary) AS min_salary
FROM employees
GROUP BY department_id
ORDER BY department_id;