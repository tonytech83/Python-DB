-- 3.5. Board Games by Release Year
-- url: https://judge.softuni.org/Contests/Practice/Index/4298#4

SELECT name,
       rating
FROM board_games
ORDER BY release_year, name DESC;


