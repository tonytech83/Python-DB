-- 10. Popular Vacation Destination
-- https://judge.softuni.org/Contests/Compete/Index/4111#8

SELECT a.country,
       count(b.booking_id) AS booking_count
FROM apartments a
         JOIN bookings b USING (apartment_id)
WHERE b.booked_at >= '2021-05-18 07:52:09.904+03'
  AND b.booked_at < '2021-09-17 19:48:02.147+03'
GROUP BY country
ORDER BY booking_count DESC;
