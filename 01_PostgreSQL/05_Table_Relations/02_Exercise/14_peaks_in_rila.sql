-- 14. Peaks in Rila
-- url: https://judge.softuni.org/Contests/Compete/Index/4109#10

SELECT m.mountain_range,
       p.peak_name,
       p.elevation
FROM mountains m
         JOIN peaks p ON p.mountain_id = m.id
WHERE mountain_range = 'Rila'
ORDER BY p.elevation DESC;