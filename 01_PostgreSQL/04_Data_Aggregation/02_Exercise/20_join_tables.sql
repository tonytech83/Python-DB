-- 20. JOIN Tables
-- url: https://judge.softuni.org/Contests/Compete/Index/4107#19

SELECT *
FROM departments
         JOIN employees ON departments.id = employees.department_id;