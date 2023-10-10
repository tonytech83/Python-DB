-- 3.9. Volunteers in Sofia
-- url: https://judge.softuni.org/Contests/Practice/Index/4296#8

SELECT v.name,
       v.phone_number,
       substring(v.address FROM position(',' IN v.address) + 2) AS address
FROM volunteers v
         JOIN volunteers_departments vd ON v.department_id = vd.id
WHERE vd.department_name = 'Education program assistant'
  AND v.address LIKE '%Sofia%'
ORDER BY v.name;
