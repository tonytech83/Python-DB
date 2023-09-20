-- 02. Replace Titles
-- url: https://judge.softuni.org/Contests/Practice/Index/4104#1

SELECT replace(title, 'The', '***') AS title
FROM books
WHERE starts_with(title, 'The')
ORDER BY id;

