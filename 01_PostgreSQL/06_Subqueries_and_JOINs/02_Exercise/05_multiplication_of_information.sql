-- 05. Multiplication of Information**
-- N/A

SELECT b.booking_id,
       c.first_name AS customer_name
FROM bookings b
         CROSS JOIN customers c
ORDER BY customer_name;

