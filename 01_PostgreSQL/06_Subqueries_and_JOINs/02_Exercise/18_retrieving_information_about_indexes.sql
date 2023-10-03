-- 18. Retrieving Information about Indexes
-- https://judge.softuni.org/Contests/Compete/Index/4111#16


SELECT tablename,
       indexname,
       indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename, indexname;