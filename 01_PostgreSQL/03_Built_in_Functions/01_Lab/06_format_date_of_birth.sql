-- 06. Format Date of Birth
-- url: https://judge.softuni.org/Contests/Practice/Index/4104#5

SELECT last_name                         AS "Last Name",
       to_char(born, 'DD (Dy) Mon YYYY') AS "Date of Birth"
FROM authors;

