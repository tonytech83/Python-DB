CREATE OR REPLACE PROCEDURE sp_players_team_name(
    IN player_name VARCHAR(50),
    OUT team_name VARCHAR(45)
)
AS
$$
BEGIN
    SELECT t.name
    INTO team_name
    FROM teams t
             JOIN players p ON t.id = p.team_id
    WHERE concat_ws(' ', p.first_name, p.last_name) = player_name;

    IF NOT FOUND THEN
        team_name := 'The player currently has no team';
    END IF;
END;
$$
    LANGUAGE plpgsql;


CALL sp_players_team_name('Thor Serrels', '');
CALL sp_players_team_name('Walther Olenchenko', '');
CALL sp_players_team_name('Isaak Duncombe', '');

