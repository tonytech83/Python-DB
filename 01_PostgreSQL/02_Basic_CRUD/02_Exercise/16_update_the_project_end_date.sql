-- 16. Update the Project End Date
-- url: https://judge.softuni.org/Contests/Compete/Index/4103#15

UPDATE projects
SET end_date = start_date + INTERVAL '5 MONTH'
WHERE end_date IS NULL;
