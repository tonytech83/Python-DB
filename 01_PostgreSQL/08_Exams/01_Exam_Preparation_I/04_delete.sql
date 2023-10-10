-- 2.4. Delete
-- url: https://judge.softuni.org/Contests/Practice/Index/4296#3

DELETE
FROM volunteers
WHERE department_id = (SELECT id FROM volunteers_departments WHERE department_name = 'Education program assistant');

DELETE
FROM volunteers_departments
WHERE id = (SELECT id FROM volunteers_departments WHERE department_name = 'Education program assistant');


