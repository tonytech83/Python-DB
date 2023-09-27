-- 2. Trip Organization
-- url: https://judge.softuni.org/Contests/Practice/Index/4108#1

SELECT v.driver_id,
       v.vehicle_type,
       concat_ws(' ', c.first_name, c.last_name) AS driver_name

FROM campers c
         JOIN vehicles v ON v.driver_id = c.id;