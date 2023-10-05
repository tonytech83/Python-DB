-- 10. Money Transfer
-- url: https://judge.softuni.org/Contests/Compete/Index/4113#8

CREATE OR REPLACE PROCEDURE sp_transfer_money(
    sender_id INT,
    receiver_id INT,
    amount NUMERIC
)
AS
$$
BEGIN
    CALL sp_withdraw_money(sender_id, amount);
    CALL sp_deposit_money(receiver_id, amount);
END;
$$
    LANGUAGE plpgsql;
