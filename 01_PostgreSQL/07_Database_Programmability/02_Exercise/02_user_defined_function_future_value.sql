-- 02. User-defined Function Future Value
-- url: https://judge.softuni.org/Contests/Compete/Index/4113#1

CREATE OR REPLACE FUNCTION fn_calculate_future_value(
    IN initial_sum DECIMAL,
    IN yearly_interest_rate DECIMAL,
    IN number_of_years INT,
    OUT future_value DECIMAL
) AS
$$
BEGIN
    future_value := TRUNC(initial_sum * power(1 + yearly_interest_rate, number_of_years), 4);
END
$$
    LANGUAGE plpgsql;

--
-- Tests
--
SELECT fn_calculate_future_value(1000, 0.1, 5);
SELECT fn_calculate_future_value(2500, 0.30, 2);
SELECT fn_calculate_future_value(500, 0.25, 10);


