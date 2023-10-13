-- 3.7. Creators without Board Games
-- url: https://judge.softuni.org/Contests/Practice/Index/4298#6

SELECT c.id,
       concat_ws(' ', c.first_name, c.last_name) AS creator_name,
       c.email
FROM creators c
         LEFT JOIN creators_board_games cbg ON c.id = cbg.creator_id
WHERE cbg.creator_id IS NULL;
