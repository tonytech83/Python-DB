SELECT t.id     AS team_id,
       t.name   AS team_name,
       count(p.id) AS player_count,
       t.fan_base
FROM teams t
        LEFT JOIN players p ON t.id = p.team_id
WHERE t.fan_base > 30000
GROUP BY t.id
ORDER BY player_count DESC, fan_base DESC ;