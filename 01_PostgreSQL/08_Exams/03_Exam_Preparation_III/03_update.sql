-- 2. 3. Update
-- url: https://judge.softuni.org/Contests/Practice/Index/4298#2

UPDATE players_ranges
SET max_players = max_players + 1
WHERE min_players = 2
  AND max_players = 2;

UPDATE board_games
SET name = concat_ws(' ', name, 'V2')
WHERE release_year >= 2020;
