-- 3.9. Creators with Emails
-- url: https://judge.softuni.org/Contests/Practice/Index/4298#8

SELECT concat_ws(' ', c.first_name, c.last_name) AS full_name,
       c.email,
       max(bg.rating)                            AS rating
FROM creators c
         JOIN creators_board_games cbg ON c.id = cbg.creator_id
         JOIN board_games bg ON cbg.board_game_id = bg.id
WHERE c.email LIKE '%.com'
GROUP BY c.id
ORDER BY full_name;
