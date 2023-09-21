-- 07. Translate
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#6

SELECT capital,
       translate(capital, 'áãåçéíñóú', 'aaaceinou') AS translated_name
FROM countries;


