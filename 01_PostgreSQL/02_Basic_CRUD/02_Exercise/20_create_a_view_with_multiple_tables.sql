-- 20. Create a View with Multiple Tables
-- url: https://judge.softuni.org/Contests/Compete/Index/4103#19

CREATE VIEW view_addresses AS
SELECT concat_ws(' ', e.first_name, e.last_name) AS "Full Name",
       department_id,
       concat_ws(' ', a.number, a.street)        AS "Address"
FROM employees e
         JOIN addresses a on a.id = e.address_id
ORDER BY "Address";
