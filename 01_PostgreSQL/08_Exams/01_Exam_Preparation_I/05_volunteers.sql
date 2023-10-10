-- 3.5. Volunteers
-- url: https://judge.softuni.org/Contests/Practice/Index/4296#4

SELECT name,
       phone_number,
       address,
       animal_id,
       department_id
FROM volunteers
ORDER BY name, animal_id, department_id;

