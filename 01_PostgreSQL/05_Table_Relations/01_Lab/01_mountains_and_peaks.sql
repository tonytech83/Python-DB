-- 1. Mountains and Peaks
-- url: https://judge.softuni.org/Contests/Practice/Index/4108#0

CREATE TABLE mountains
(
    id   SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE peaks
(
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(50),
    mountain_id INT,
    CONSTRAINT fk_peaks_mountains
        FOREIGN KEY (mountain_id)
            REFERENCES mountains (id)
);