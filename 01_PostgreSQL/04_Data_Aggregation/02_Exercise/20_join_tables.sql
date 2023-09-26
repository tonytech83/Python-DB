-- 20. JOIN Tables
-- url: https://judge.softuni.org/Contests/Compete/Index/4107#19

SELECT d.id,
       d.department_name,
       d.manager_id,
       e.id,
       e.first_name,
       e.last_name,
       e.job_title,
       e.department_id,
       e.manager_id,
       e.hire_date,
       e.salary,
       e.address_id
FROM departments d
         JOIN employees e on d.id = e.department_id;