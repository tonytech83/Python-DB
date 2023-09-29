-- 02. Remove Primary Key
-- url: https://judge.softuni.org/Contests/Compete/Index/4109#1

ALTER TABLE products
    DROP CONSTRAINT products_pkey;
