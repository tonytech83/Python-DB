-- 03. Employees Promotion By ID
-- url: https://judge.softuni.org/Contests/Practice/Index/4112#2

CREATE OR REPLACE PROCEDURE sp_increase_salary_by_id(id INT)
AS
$$
BEGIN
    IF (SELECT salary FROM employees WHERE employee_id = id) IS NULL THEN
        RETURN;
    ELSE
        UPDATE employees SET salary = salary * 1.05 WHERE employee_id = id;
    END IF;
    COMMIT;
END
$$
    LANGUAGE plpgsql;

-- ----------- More complex solution -----------------------
-- CREATE OR REPLACE PROCEDURE sp_increase_salary_by_id(id INT)
-- AS
-- $$
-- DECLARE
--     temp_val FLOAT;
-- BEGIN
--     IF id IN (SELECT employee_id FROM employees) THEN
--         SELECT salary FROM employees WHERE employee_id = id INTO temp_val;
--         UPDATE employees SET salary = salary * 1.05 WHERE employee_id = id;
--         IF temp_val * 1.05 <> (SELECT salary FROM employees WHERE employee_id = id) THEN
--             ROLLBACK;
--         ELSE
--             COMMIT;
--         END IF;
--     END IF;
-- END
-- $$
--     LANGUAGE plpgsql;


