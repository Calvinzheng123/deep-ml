-- your query
WITH ranked_salaries AS (
    SELECT department, name, salary, DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rnk FROM employees)
SELECT department, name, salary, rnk
FROM ranked_salaries
WHERE rnk <= 3