-- 3.6. Animals Data
-- url: https://judge.softuni.org/Contests/Practice/Index/4296#5

SELECT name,
       at.animal_type,
       to_char(a.birthdate, 'DD.MM.YYYY')
FROM animals a
         JOIN animal_types at ON at.id = a.animal_type_id
ORDER BY a.name;
