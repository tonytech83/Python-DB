-- 23. Early Birds**
-- url: N/A

SELECT user_id,
       age(starts_at, booked_at) AS "Early Birds"
FROM bookings
WHERE starts_at - booked_at >= INTERVAL '10 MONTHS';

