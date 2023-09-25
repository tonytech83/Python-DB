-- 06. GROUP BY Deposit Interest
-- url: https://judge.softuni.org/Contests/Compete/Index/4107#5

SELECT deposit_group,
       sum(deposit_interest) AS "Deposit Interest"
FROM wizard_deposits
GROUP BY deposit_group
ORDER BY "Deposit Interest" DESC;