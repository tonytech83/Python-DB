-- 07. Retrieving Account Holders**
-- url: N/A

CREATE OR REPLACE PROCEDURE sp_retrieving_holders_with_balance_higher_than(
    searched_balance NUMERIC
)
AS
$$
DECLARE
    row_record    account_holders%ROWTYPE;
    total_balance NUMERIC;
BEGIN
    FOR row_record IN SELECT * FROM account_holders ORDER BY first_name, last_name
        LOOP
            -- Set initial total_balance for the current account holder
            total_balance := 0;

            -- Calculate total_balance for current account_holder
            SELECT sum(balance)
            INTO total_balance
            FROM accounts
            WHERE account_holder_id = row_record.id;

            -- Check if total_balance for current account holder is bigger than searched_balance
            IF total_balance > searched_balance THEN
                RAISE NOTICE '% % - %', row_record.first_name, row_record.last_name, total_balance;
            END IF;

        END LOOP;
END;
$$
    LANGUAGE plpgsql;

CALL sp_retrieving_holders_with_balance_higher_than(200000);

-- Expected output:
-- bank_db.public> CALL sp_retrieving_holders_with_balance_higher_than(200000)
-- Monika Miteva - 565649.2000
-- Petar Kirilov - 245656.2300
-- Petko Petkov Junior - 6546543.2300
-- Susan Cane - 5585351.2400
-- Zlatko Zlatyov - 1112627.9000
-- [2023-10-05 13:13:49] completed in 42 ms

