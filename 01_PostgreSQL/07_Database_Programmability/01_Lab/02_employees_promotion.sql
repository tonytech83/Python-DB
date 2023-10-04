-- 02. Employees Promotion
-- url: https://judge.softuni.org/Contests/Practice/Index/4112#1

CREATE OR REPLACE PROCEDURE sp_increase_salaries(department_name VARCHAR)
AS
$$
BEGIN
    UPDATE employees
    SET salary = salary + salary * 0.05
    WHERE department_id = (SELECT department_id FROM departments WHERE name = department_name);
END;
$$
    LANGUAGE plpgsql;

CALL sp_increase_salaries('Finance')

