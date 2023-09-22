-- 22. EXTRACT Booked At
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#20

SELECT extract(YEAR FROM booked_at)                    AS "YEAR",
       extract(MONTH FROM booked_at)                   AS "MONTH",
       extract(DAY FROM booked_at)                     AS "DAY",
       extract(HOUR FROM booked_at AT TIME ZONE 'UTC') AS "HOUR",
       extract(MINUTE FROM booked_at)                  AS "MINUTE",
       ceil(extract(SECOND FROM booked_at))            AS "SECOND"
FROM bookings;
