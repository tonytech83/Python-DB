-- 09. Notes with Dumbledore
-- url: https://judge.softuni.org/Contests/Compete/Index/4107#8

SELECT last_name,
       COUNT(notes) AS "Notes with Dumbledore"
FROM wizard_deposits
WHERE notes LIKE '%Dumbledore%'
GROUP BY last_name;