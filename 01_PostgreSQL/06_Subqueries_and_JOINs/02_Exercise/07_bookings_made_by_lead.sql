-- 07. Bookings Made by Lead
-- https://judge.softuni.org/Contests/Compete/Index/4111#5

SELECT b.apartment_id,
       b.booked_for,
       c.first_name,
       c.country
FROM customers c
         RIGHT JOIN bookings b USING (customer_id)
WHERE c.job_type = 'Lead';