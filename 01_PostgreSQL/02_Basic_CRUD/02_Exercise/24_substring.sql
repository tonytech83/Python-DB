-- 24. SUBSTRING
-- url: https://judge.softuni.org/Contests/Compete/Index/4103#23

CREATE VIEW view_initials AS
SELECT LEFT(first_name, 2) AS initial,
       last_name
FROM employees
ORDER BY last_name;


-- Same -> using SUBSTRING instead of LEFT
-- CREATE VIEW view_initials AS
-- SELECT SUBSTRING(first_name, 1,2) AS initial,
--        last_name
-- FROM employees
-- ORDER BY last_name;

