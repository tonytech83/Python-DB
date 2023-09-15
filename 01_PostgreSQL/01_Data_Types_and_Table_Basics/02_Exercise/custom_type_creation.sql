-- Create custom type
CREATE TYPE address AS
(
    street      TEXT,
    city        TEXT,
    postal_code CHAR(4)
);

-- Create table with column with custom type
CREATE TABLE customers
(
    id               SERIAL PRIMARY KEY,
    customer_name    TEXT,
    customer_address address
);

-- Insert into table
INSERT INTO customers (customer_name, customer_address)
VALUES ('Anton', ('Some street', 'Sofia', '1407'));

SELECT *
FROM customers;