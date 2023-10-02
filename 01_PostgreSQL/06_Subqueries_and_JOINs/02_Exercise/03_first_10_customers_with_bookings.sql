-- 03. First 10 Customers with Bookings
-- https://judge.softuni.org/Contests/Compete/Index/4111#2

SELECT b.booking_id,
       b.starts_at::date,
       b.apartment_id,
       concat_ws(' ', c.first_name, c.last_name) AS customer_name
FROM bookings b
         RIGHT JOIN customers c USING (customer_id)
ORDER BY customer_name
LIMIT 10;



