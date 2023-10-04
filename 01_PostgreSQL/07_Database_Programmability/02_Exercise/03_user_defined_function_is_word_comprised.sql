-- 03. User-defined Function Is Word Comprised
-- url: https://judge.softuni.org/Contests/Compete/Index/4113#2

CREATE OR REPLACE FUNCTION fn_is_word_comprised(
    IN set_of_letters VARCHAR(50),
    IN word VARCHAR(50),
    OUT result BOOLEAN
) AS
$$
DECLARE
    len_of_word INT;
    idx         INT := 1;
    letter      CHAR(1);
    counter     INT := 0;
BEGIN
    -- Check length of the word
    len_of_word := (SELECT length(word));

    -- Loop though all letters using variable idx
    WHILE idx <= len_of_word
        LOOP
            letter := (SELECT substring(word FROM idx FOR 1));
            IF (SELECT POSITION(lower(letter) IN lower(set_of_letters)) > 0) THEN
                counter := counter + 1;
            END IF;
            idx = idx + 1;
        END LOOP;

    -- Check if counter of founded letters is equal to length of word
    IF counter = len_of_word THEN
        result := TRUE;
    ELSE
        result := FALSE;
    END IF;
END
$$
    LANGUAGE plpgsql;



