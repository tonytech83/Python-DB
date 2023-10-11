-- 4.12. Animals with Owner or Not
-- url: https://judge.softuni.org/Contests/Practice/Index/4296#11

CREATE OR REPLACE PROCEDURE sp_animals_with_owners_or_not(
    IN animal_name VARCHAR(30),
    OUT owner VARCHAR(30)
)
AS
$$
BEGIN
    IF (SELECT owner_id FROM animals WHERE name = animal_name) IS NULL THEN
        owner := 'For adoption';
    ELSE
        owner := (SELECT o.name
                  FROM owners o
                           JOIN animals a ON o.id = a.owner_id
                  WHERE a.name = animal_name);
    END IF;
END;
$$
    LANGUAGE plpgsql;

-- Test examples:
CALL sp_animals_with_owners_or_not('Pumpkinseed Sunfish');
CALL sp_animals_with_owners_or_not('Hippo');
CALL sp_animals_with_owners_or_not('Brown bear');