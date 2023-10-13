-- 2.4. Delete
-- url: https://judge.softuni.org/Contests/Practice/Index/4297#3

DELETE
FROM clients
WHERE id IN (SELECT c1.id
FROM clients c1
         LEFT JOIN courses c2 ON c1.id = c2.client_id
WHERE c2.client_id IS NULL
  AND length(c1.full_name) > 3);

