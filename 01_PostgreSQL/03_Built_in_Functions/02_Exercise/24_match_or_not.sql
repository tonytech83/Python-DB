-- 24. Match or Not
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#21

SELECT companion_full_name,
       email
FROM users
WHERE companion_full_name ILIKE '%aNd%'
  AND email NOT LIKE '%@gmail';

