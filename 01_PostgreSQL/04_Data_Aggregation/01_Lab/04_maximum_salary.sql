-- 04. Maximum Salary
-- url: https://judge.softuni.org/Contests/Practice/Index/4106#3

SELECT department_id,
       max(salary) AS max_salary
FROM employees
GROUP BY department_id
ORDER BY department_id;