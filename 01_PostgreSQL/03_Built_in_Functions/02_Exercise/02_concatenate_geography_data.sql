-- 02. Concatenate Geography Data
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#1

CREATE VIEW view_continents_countries_currencies_details AS
SELECT concat_ws(': ', c2.continent_name, c2.continent_code)               AS "Continent Details",
       concat_ws(' - ', c1.country_name, capital, c1.area_in_sq_km, 'km2') AS "Country Information",
       concat(c3.description, ' (', c3.currency_code, ')')                 AS "Currencies"

FROM countries c1
         JOIN continents c2 on c1.continent_code = c2.continent_code
         JOIN currencies c3 on c3.currency_code = c1.currency_code
ORDER BY "Country Information", "Currencies";
