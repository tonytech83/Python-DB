-- 03. Sum Salaries per Department
-- url: https://judge.softuni.org/Contests/Practice/Index/4106#2

SELECT department_id,
       sum(salary) AS total_salaries
FROM employees
GROUP BY department_id
ORDER BY department_id;