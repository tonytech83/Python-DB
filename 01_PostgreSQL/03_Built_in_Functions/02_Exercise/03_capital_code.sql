-- 03. Capital Code
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#2

ALTER TABLE countries
    ADD COLUMN capital_code CHAR(2);

UPDATE countries
SET capital_code = substring(capital FROM 1 FOR 2);