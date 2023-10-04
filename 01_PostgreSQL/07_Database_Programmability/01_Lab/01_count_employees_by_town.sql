-- 01. Count Employees by Town
-- url: https://judge.softuni.org/Contests/Practice/Index/4112#0

CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name VARCHAR)
    RETURNS INT
AS
$$
BEGIN
    RETURN (SELECT count(*)
            FROM employees e
                     JOIN addresses a USING (address_id)
                     JOIN towns t USING (town_id)
            WHERE t.name = town_name);
END
$$
LANGUAGE plpgsql;

SELECT fn_count_employees_by_town('Sofia') AS count;


