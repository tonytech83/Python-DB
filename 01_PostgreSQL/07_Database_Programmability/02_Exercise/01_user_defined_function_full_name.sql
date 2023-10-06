-- 01. User-defined Function Full Name
-- url: https://judge.softuni.org/Contests/Compete/Index/4113#0

CREATE OR REPLACE FUNCTION fn_full_name(
    IN first_name VARCHAR,
    IN last_name VARCHAR,
    OUT full_name VARCHAR
) AS
$$
BEGIN
    full_name := initcap(first_name) || ' ' || initcap(last_name);
END
$$
    LANGUAGE plpgsql;
