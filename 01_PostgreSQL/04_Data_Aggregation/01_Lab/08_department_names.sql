-- 08. Department Names
-- url: https://judge.softuni.org/Contests/Practice/Index/4106#7

SELECT id,
       first_name,
       last_name,
       round(salary, 2) AS salary,
       department_id,
       CASE
           WHEN department_id = 1 THEN 'Management'
           WHEN department_id = 2 THEN 'Kitchen Staff'
           WHEN department_id = 3 THEN 'Service Staff'
           ELSE 'Other'
           END          AS department_name
FROM employees
ORDER BY id;