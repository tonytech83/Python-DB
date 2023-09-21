-- 03. Triangles on Bookshelves
-- url: https://judge.softuni.org/Contests/Practice/Index/4104#2

SELECT id,
       (height * side) / 2 AS area
FROM triangles
ORDER BY id;
