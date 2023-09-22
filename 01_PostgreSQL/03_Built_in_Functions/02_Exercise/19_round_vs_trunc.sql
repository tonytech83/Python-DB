-- 19. ROUND vs TRUNC
-- url: https://judge.softuni.org/Contests/Compete/Index/4105#18

SELECT latitude,
       round(latitude, 2),
       trunc(latitude, 2)
FROM apartments;
