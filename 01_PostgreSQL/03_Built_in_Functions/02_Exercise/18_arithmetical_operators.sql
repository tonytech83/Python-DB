-- 18. Arithmetical Operators
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#17

CREATE TABLE bookings_calculation AS
SELECT booked_for,
       (booked_for * 50)::numeric AS multiplication,
       (booked_for % 50)::numeric AS modulo
FROM bookings
WHERE apartment_id = 93;


-- Long way

-- CREATE TABLE bookings_calculation AS
-- SELECT booked_for
-- FROM bookings
-- WHERE apartment_id = 93;
--
-- ALTER TABLE bookings_calculation
--     ADD COLUMN multiplication NUMERIC,
--     ADD COLUMN modulo         NUMERIC;
--
-- UPDATE bookings_calculation
-- SET multiplication = booked_for * 50,
--     modulo         = booked_for % 50;
