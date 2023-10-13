-- 2.4. Delete
-- url: https://judge.softuni.org/Contests/Practice/Index/4298#3

DELETE
FROM board_games
WHERE publisher_id IN (SELECT id
                       FROM publishers
                       WHERE address_id IN (SELECT id
                                            FROM addresses
                                            WHERE town LIKE 'L%'));

DELETE
FROM publishers
WHERE address_id IN (SELECT id
                     FROM addresses
                     WHERE town LIKE 'L%');

DELETE
FROM addresses
WHERE town LIKE 'L%';
