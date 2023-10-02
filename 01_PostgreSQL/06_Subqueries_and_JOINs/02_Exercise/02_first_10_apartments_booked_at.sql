-- 02. First 10 Apartments Booked At
-- https://judge.softuni.org/Contests/Compete/Index/4111#1

SELECT a.name,
       a.country,
       b.booked_at::date
FROM apartments a
         LEFT JOIN bookings b USING (booking_id)
LIMIT 10;



