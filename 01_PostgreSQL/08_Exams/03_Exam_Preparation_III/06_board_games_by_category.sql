-- 3.6. Board Games by Category
-- url: https://judge.softuni.org/Contests/Practice/Index/4298#5

SELECT bg.id,
       bg.name,
       bg.release_year,
       c.name
FROM board_games bg
         JOIN categories c ON bg.category_id = c.id
WHERE c.name IN ('Strategy Games', 'Wargames')
ORDER BY bg.release_year DESC;
