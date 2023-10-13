-- 3.10. Creators by Rating
-- url: https://judge.softuni.org/Contests/Practice/Index/4298#9

SELECT c.last_name,
       ceil(avg(bg.rating)) AS avetage_rating,
       p.name               AS publisher_name
FROM creators c
         JOIN creators_board_games cbg ON c.id = cbg.creator_id
         JOIN board_games bg ON cbg.board_game_id = bg.id
         JOIN publishers p ON bg.publisher_id = p.id
WHERE p.name = 'Stonemaier Games'
GROUP BY c.last_name, p.name
ORDER BY avetage_rating DESC;