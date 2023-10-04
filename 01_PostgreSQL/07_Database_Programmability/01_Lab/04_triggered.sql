-- 04. Triggered
-- url: https://judge.softuni.org/Contests/Practice/Index/4112#3

CREATE TABLE deleted_employees
(
    employee_id   SERIAL PRIMARY KEY,
    first_name    VARCHAR(20),
    last_name     VARCHAR(20),
    middle_name   VARCHAR(20),
    job_title     VARCHAR(50),
    department_id INT,
    salary        NUMERIC(19, 4)
);

-- Trigger function
CREATE OR REPLACE FUNCTION fn_backup_fired_employees()
    RETURNS TRIGGER AS
$$
BEGIN
    INSERT INTO deleted_employees
    (
        first_name,
        last_name,
        middle_name,
        job_title,
        department_id,
        salary
    )
    VALUES
    (
        old.first_name,
        old.last_name,
        old.middle_name,
        old.job_title,
        old.department_id,
        old.salary
    );
    RETURN new;
END
$$
    LANGUAGE plpgsql;

-- Trigger
CREATE OR REPLACE TRIGGER backup_fired_employees
    AFTER DELETE
    ON employees
    FOR EACH ROW
EXECUTE PROCEDURE fn_backup_fired_employees();