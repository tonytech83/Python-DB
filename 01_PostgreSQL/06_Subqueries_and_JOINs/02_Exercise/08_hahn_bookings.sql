-- 08. Hahn`s Bookings
-- https://judge.softuni.org/Contests/Compete/Index/4111#6

SELECT count(*)
FROM bookings b
         JOIN customers c USING (customer_id)
WHERE c.last_name = 'Hahn';