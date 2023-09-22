-- 02. Departments Info by Salary
-- url: https://judge.softuni.org/Contests/Practice/Index/4106#1

SELECT department_id,
       count(salary) AS employee_count
FROM employees
GROUP BY department_id
ORDER BY department_id;