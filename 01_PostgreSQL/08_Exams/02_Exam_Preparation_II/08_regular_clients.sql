-- 3.8. Regular Clients
-- url: https://judge.softuni.org/Contests/Practice/Index/4297#7

SELECT c1.full_name,
       count(c1.id) AS count_of_cars,
       sum(c2.bill) AS total_sum
FROM clients c1
         JOIN courses c2 ON c1.id = c2.client_id
WHERE substring(c1.full_name FROM 2 FOR 1) = 'a'
GROUP BY c1.full_name
HAVING count(c1.id) > 1
ORDER BY c1.full_name;
