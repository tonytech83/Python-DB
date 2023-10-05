-- 05. Difficulty Level
-- url: https://judge.softuni.org/Contests/Compete/Index/4113#4

CREATE OR REPLACE FUNCTION fn_difficulty_level(
    IN level INT,
    OUT difficulty_level VARCHAR
) AS
$$
BEGIN
    IF level <= 40 THEN
        difficulty_level := 'Normal Difficulty';
    ELSIF level BETWEEN 41 AND 60 THEN
        difficulty_level := 'Nightmare Difficulty';
    ELSE
        difficulty_level := 'Hell Difficulty';
    END IF;
END
$$
    LANGUAGE plpgsql;
