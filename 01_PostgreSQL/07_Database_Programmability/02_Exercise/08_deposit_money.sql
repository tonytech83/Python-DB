-- 08. Deposit Money
-- url: https://judge.softuni.org/Contests/Compete/Index/4113#6

CREATE OR REPLACE PROCEDURE sp_deposit_money(
    account_id INT,
    money_amount NUMERIC
)
AS
$$
BEGIN
    IF (SELECT balance FROM accounts WHERE id = account_id) IS NULL THEN
        RETURN;
    ELSE
        UPDATE accounts SET balance = balance + money_amount WHERE id = account_id;
    END IF;
    COMMIT;
END
$$
    LANGUAGE plpgsql;



