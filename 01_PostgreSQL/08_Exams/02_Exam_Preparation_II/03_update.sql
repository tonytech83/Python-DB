-- 2.3. Update
-- url: https://judge.softuni.org/Contests/Practice/Index/4297#2

UPDATE cars
SET condition = 'C'
WHERE (mileage >= 800000
    OR mileage IS NULL)
  AND year <= 2010
  AND make <> 'Mercedes-Benz';