-- 04. Booking Information
-- https://judge.softuni.org/Contests/Compete/Index/4111#3

SELECT b.booking_id,
       a.name                                    AS apartment_owner,
       a.apartment_id,
       concat_ws(' ', c.first_name, c.last_name) AS customer_name
FROM bookings b
         FULL JOIN apartments a USING (booking_id)
         FULL JOIN customers c USING (customer_id)
ORDER BY b.booking_id, apartment_owner, customer_name;



