UPDATE coaches
SET salary = salary * coach_level
WHERE first_name LIKE 'C%'
  AND id IN (SELECT DISTINCT coach_id
             FROM players_coaches
             WHERE coach_id IS NOT NULL);


