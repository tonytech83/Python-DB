-- 03. Employees Projects
-- url: https://judge.softuni.org/Contests/Practice/Index/4110#2

SELECT e.employee_id,
       concat_ws(' ', e.first_name, e.last_name) AS full_name,
       p.project_id,
       p.name                                    AS project_name
FROM employees e
         JOIN employees_projects ep USING (employee_id)
         JOIN projects p USING (project_id)
WHERE p.project_id = 1;
