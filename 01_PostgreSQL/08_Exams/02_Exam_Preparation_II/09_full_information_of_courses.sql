-- 3.9. Full Information of Courses
-- url: https://judge.softuni.org/Contests/Practice/Index/4297#8

SELECT a.name  AS address,
       CASE
           WHEN extract(HOUR FROM c1.start) BETWEEN 6 AND 20 THEN 'Day'
           ELSE 'Night'
           END AS day_time,
       c1.bill,
       c2.full_name,
       c3.make,
       c3.model,
       c4.name AS category_name
FROM addresses a
         JOIN courses c1 ON a.id = c1.from_address_id
         JOIN clients c2 ON c1.client_id = c2.id
         JOIN cars c3 ON c1.car_id = c3.id
         JOIN categories c4 ON c3.category_id = c4.id
ORDER BY c1.id;