CREATE OR REPLACE FUNCTION fn_stadium_team_name(
    stadium_name VARCHAR(30)
)
    RETURNS TABLE
            (
                team_name VARCHAR(45)
            )
AS
$$
BEGIN
    RETURN QUERY SELECT t.name
                 FROM teams t
                          JOIN stadiums s ON t.stadium_id = s.id
                 WHERE s.name = stadium_name
                 ORDER BY t.name;
END;
$$
    LANGUAGE plpgsql;

SELECT fn_stadium_team_name('BlogXS');
SELECT fn_stadium_team_name('Quaxo');
SELECT fn_stadium_team_name('Jaxworks');