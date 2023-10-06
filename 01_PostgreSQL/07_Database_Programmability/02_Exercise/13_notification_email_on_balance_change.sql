-- 13. Notification Email on Balance Change
-- url: https://judge.softuni.org/Contests/Compete/Index/4113#11

CREATE TABLE notification_emails
(
    id           SERIAL PRIMARY KEY,
    recipient_id INT,
    subject      VARCHAR(100),
    body         TEXT
);

CREATE OR REPLACE FUNCTION trigger_fn_send_email_on_balance_change()
    RETURNS TRIGGER AS
$$
BEGIN
    INSERT INTO notification_emails (recipient_id, subject, body)
    VALUES (
        NEW.account_id,
        concat('Balance change for account:', ' ', NEW.account_id),
        concat_ws(' ', 'On', NOW()::date, 'your balance was changed from', NEW.old_sum,'to', NEW.new_sum,'.')
        );
    RETURN NEW;
END;
$$
    LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER tr_send_email_on_balance_change
    AFTER UPDATE
    ON logs
    FOR EACH ROW
EXECUTE PROCEDURE trigger_fn_send_email_on_balance_change();