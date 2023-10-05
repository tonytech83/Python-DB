-- 06. Cash in User Games Odd Rows
-- url: https://judge.softuni.org/Contests/Compete/Index/4113#5

CREATE OR REPLACE FUNCTION fn_cash_in_users_games(game_name VARCHAR(50))
    RETURNS TABLE
            (
                total_cash NUMERIC
            )
AS
$$
BEGIN
    RETURN QUERY
        SELECT round(SUM(cash)::numeric, 2)
        FROM (SELECT cash,
                     ROW_NUMBER() OVER (ORDER BY ug.cash DESC) AS idx
              FROM users_games ug
                       JOIN games g ON ug.game_id = g.id
              WHERE g.name = game_name) subquery
        WHERE mod(idx, 2) = 1;
END
$$
    LANGUAGE plpgsql;


-- Test examples:

SELECT fn_cash_in_users_games('Love in a mist');            -- Output: 8585.00
SELECT fn_cash_in_users_games('Delphinium Pacific Giant');  -- Output: 6921.00

