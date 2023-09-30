-- 04. Higher Salary
-- url: https://judge.softuni.org/Contests/Practice/Index/4110#3

SELECT count(*)
FROM employees
WHERE salary > (SELECT avg(salary) FROM employees);