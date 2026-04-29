# Write your MySQL query statement below
SELECT player_id , min(cast(event_date as date)) as first_login
from activity 
group by player_id 
order by cast(event_date as date) asc

-- SELECT
--   player_id,
--   MIN(CAST(first_login AS DATE)) AS first_login_date
-- FROM activity
-- GROUP BY player_id
-- ORDER BY first_login_date ASC;
