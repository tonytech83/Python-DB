-- 11. Delete Cascade
-- url: https://judge.softuni.org/Contests/Compete/Index/4109#7

ALTER TABLE countries
    ADD CONSTRAINT fk_countries_continents
        FOREIGN KEY (continent_code)
            REFERENCES continents (continent_code)
            ON DELETE CASCADE,
    ADD CONSTRAINT fk_countries_currencies
        FOREIGN KEY (currency_code)
            REFERENCES currencies (currency_code)
            ON DELETE CASCADE;