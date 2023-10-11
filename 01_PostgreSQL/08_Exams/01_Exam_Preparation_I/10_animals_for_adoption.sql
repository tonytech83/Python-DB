-- 3.10. Animals for Adoption
-- url: https://judge.softuni.org/Contests/Practice/Index/4296#9

SELECT a.name AS animal,
       EXTRACT(YEAR FROM a.birthdate) AS birth_year,
       at.animal_type
from animals a
         JOIN animal_types at ON a.animal_type_id = at.id
WHERE a.owner_id IS NULL
  AND at.animal_type <> 'Birds'
  AND extract(YEAR FROM age('01/01/2022', a.birthdate)) < 5
ORDER BY a.name;
