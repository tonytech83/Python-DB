-- 04. Format Costs
-- url: https://judge.softuni.org/Contests/Practice/Index/4104#3

SELECT title,
       round(cost, 3) AS modified_price
FROM books
ORDER BY id;
