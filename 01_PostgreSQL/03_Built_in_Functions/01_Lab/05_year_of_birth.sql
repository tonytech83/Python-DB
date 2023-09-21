-- 05. Year of Birth
-- url: https://judge.softuni.org/Contests/Practice/Index/4104#4

SELECT first_name,
       last_name,
       extract(YEAR from born) AS year
FROM authors;
