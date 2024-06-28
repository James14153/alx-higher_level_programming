--  lists all records of the table
-- records sordts tsored
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
