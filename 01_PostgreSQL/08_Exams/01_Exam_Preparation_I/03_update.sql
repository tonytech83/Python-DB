-- 2.3. Update
-- url: https://judge.softuni.org/Contests/Practice/Index/4296#2

UPDATE animals
SET owner_id = (SELECT id FROM owners WHERE name = 'Kaloqn Stoqnov')
WHERE owner_id IS NULL;
