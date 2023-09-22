-- 11. Character Length and Bits
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#10

SELECT concat_ws(' ', m.mountain_range, p.peak_name)             AS "Mountain Information",
       char_length(concat_ws(' ', m.mountain_range, p.peak_name))     AS "Characters Length",
       bit_length(concat_ws(' ', m.mountain_range, p.peak_name)) AS "Bits of a String"
FROM mountains m
         JOIN peaks p on m.id = p.mountain_id;

