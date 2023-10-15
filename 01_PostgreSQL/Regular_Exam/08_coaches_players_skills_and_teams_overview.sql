SELECT concat_ws(' ', c.first_name, c.last_name) AS coach_full_name,
       concat_ws(' ', p.first_name, p.last_name) AS player_full_name,
       t.name                                    AS team_name,
       sd.passing,
       sd.shooting,
       sd.speed
FROM coaches c
         JOIN players_coaches pc ON c.id = pc.coach_id
         JOIN players p ON pc.player_id = p.id
         JOIN skills_data sd ON p.skills_data_id = sd.id
         JOIN teams t ON p.team_id = t.id
ORDER BY coach_full_name, player_full_name DESC;