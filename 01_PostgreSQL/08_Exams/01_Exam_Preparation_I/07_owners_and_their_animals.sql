-- 3.7. Owners and Their Animals
-- url: https://judge.softuni.org/Contests/Practice/Index/4296#6

SELECT o.name,
       count(*) AS count_of_animals
FROM owners o
         JOIN animals a ON o.id = a.owner_id
GROUP BY o.name
ORDER BY count_of_animals DESC, o.name
LIMIT 5;