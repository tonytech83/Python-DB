-- 4.11. Creator of Board Games
-- url: https://judge.softuni.org/Contests/Practice/Index/4298#10

CREATE OR REPLACE FUNCTION fn_creator_with_board_games(
    IN creator_first_name VARCHAR(30),
    OUT total_board_games INT
)
AS
$$
BEGIN
    SELECT count(*)
    INTO total_board_games
    FROM creators c
             JOIN creators_board_games cbg ON c.id = cbg.creator_id
    WHERE c.first_name = creator_first_name;
END;
$$
    LANGUAGE plpgsql;

-- Test examples
SELECT fn_creator_with_board_games('Bruno');
SELECT fn_creator_with_board_games('Alexander');