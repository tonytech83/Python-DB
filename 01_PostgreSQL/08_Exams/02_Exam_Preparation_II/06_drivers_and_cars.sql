-- 3.6. Drivers and Cars
-- url: https://judge.softuni.org/Contests/Practice/Index/4297#5

SELECT d.first_name,
       d.last_name,
       c.make,
       c.model,
       c.mileage
FROM drivers d
         JOIN cars_drivers cd ON d.id = cd.driver_id
         JOIN cars c ON cd.car_id = c.id
WHERE c.mileage IS NOT NULL
ORDER BY c.mileage DESC, d.first_name;

