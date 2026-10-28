-- your query
SELECT salary
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS nth_salary
FROM employee) AS ranked
WHERE ranked.nth_salary = 3
LIMIT 1

