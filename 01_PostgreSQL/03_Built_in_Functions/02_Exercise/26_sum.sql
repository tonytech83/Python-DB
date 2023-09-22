-- 26. SUM
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#23

SELECT sum(booked_for) AS total_value
FROM bookings
WHERE apartment_id = 90;

