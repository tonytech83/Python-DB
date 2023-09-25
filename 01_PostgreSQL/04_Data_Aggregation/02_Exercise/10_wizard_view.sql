-- 10. Wizard View
-- url: https://judge.softuni.org/Contests/Compete/Index/4107#9

CREATE VIEW view_wizard_deposits_with_expiration_date_before_1983_08_17
AS
SELECT concat_ws(' ', first_name, last_name) AS "Wizard Name",
       deposit_start_date:: date             AS "Start Date",
       deposit_expiration_date::date         AS "Expiration Date",
       deposit_amount                        AS "Amount"
FROM wizard_deposits
WHERE deposit_expiration_date <= '1983-08-17'
GROUP BY "Wizard Name", "Start Date", "Expiration Date", "Amount"
ORDER BY "Expiration Date";