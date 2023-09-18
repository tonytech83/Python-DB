-- 15. New Table
-- url: https://judge.softuni.org/Contests/Compete/Index/4103#14

CREATE TABLE IF NOT EXISTS company_chart AS
SELECT concat_ws(' ', first_name, last_name) AS "Full Name",
       job_title                             AS "Job Title",
       department_id                         AS "Department ID",
       manager_id                            AS "Manager ID"
FROM employees;
