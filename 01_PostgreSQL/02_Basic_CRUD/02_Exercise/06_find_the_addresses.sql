-- 06. Find the Addresses
-- url: https://judge.softuni.org/Contests/Compete/Index/4103#5

SELECT id,
       concat_ws(' ',number, street) AS "Address",
       city_id
FROM addresses
WHERE id >= 20;