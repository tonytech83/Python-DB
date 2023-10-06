-- 09. Withdraw Money
-- url: https://judge.softuni.org/Contests/Compete/Index/4113#7

CREATE OR REPLACE PROCEDURE sp_withdraw_money(
    account_id INT,
    money_amount NUMERIC
)
AS
$$
DECLARE
    account_balance NUMERIC;
BEGIN
    -- check if provided account_id exists
    IF (SELECT balance FROM accounts WHERE id = account_id) IS NULL THEN
        RETURN;
    ELSE
        account_balance := (SELECT balance FROM accounts WHERE id = account_id);
        IF account_balance < money_amount THEN
            RAISE NOTICE 'Insufficient balance to withdraw %', money_amount;
            RETURN;
        ELSE
            UPDATE accounts SET balance = balance - money_amount WHERE id = account_id;
        END IF;
    END IF;
    COMMIT;
END
$$
    LANGUAGE plpgsql;
