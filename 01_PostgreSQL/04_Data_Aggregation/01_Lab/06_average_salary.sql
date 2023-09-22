-- 06. Average Salary
-- url: https://judge.softuni.org/Contests/Practice/Index/4106#5

SELECT department_id,
       avg(salary) AS avg_salary
FROM employees
GROUP BY department_id
ORDER BY department_id;