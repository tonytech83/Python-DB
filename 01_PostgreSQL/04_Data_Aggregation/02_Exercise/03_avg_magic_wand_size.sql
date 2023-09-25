-- 03. AVG Magic Wand Size
-- url: https://judge.softuni.org/Contests/Compete/Index/4107#2

SELECT round(avg(magic_wand_size), 3) AS "Average Magic Wand Size"
FROM wizard_deposits;