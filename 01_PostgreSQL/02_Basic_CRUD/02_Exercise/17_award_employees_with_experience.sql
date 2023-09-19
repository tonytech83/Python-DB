-- 17. Award Employees with Experience
-- url: https://judge.softuni.org/Contests/Compete/Index/4103#16

UPDATE employees
SET salary    = salary + 1500,
    job_title = concat_ws(' ', 'Senior', job_title)
WHERE hire_date BETWEEN 'January 1, 1998' AND 'January 5, 2000';
