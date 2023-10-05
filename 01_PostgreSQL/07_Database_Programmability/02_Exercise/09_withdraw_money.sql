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
    insufficient_balance NUMERIC;
BEGIN
    IF (SELECT balance FROM accounts WHERE id = account_id) IS NULL THEN
        RETURN;
    ELSE
        account_balance := (SELECT balance FROM accounts WHERE id = account_id);
        IF account_balance < money_amount THEN
            insufficient_balance := round((money_amount - account_balance), 4);
            RAISE NOTICE 'Insufficient balance to withdraw %', insufficient_balance;
            RETURN;
        ELSE
            UPDATE accounts SET balance = balance - money_amount WHERE id = account_id;
        END IF;
    END IF;
    COMMIT;
END
$$
    LANGUAGE plpgsql;



