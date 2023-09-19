-- 19. Create a View
-- url: https://judge.softuni.org/Contests/Compete/Index/4103#18

CREATE VIEW view_company_chart AS
SELECT "Full Name",
       "Job Title"
FROM company_chart
WHERE "Manager ID" = 184;

