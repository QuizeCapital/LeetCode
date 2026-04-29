# Write your MySQL query statement below
-- select  distinct
-- extra as report_reason 
-- ,count(action) over(partition by extra, action, post_id) as report_count
-- -- ,COUNT(action) OVER(PARTITION BY extra) AS report_count
-- from Actions 
-- where action = 'report'
-- and action_date = '2019-07-04'

select 
extra as report_reason 
,count(distinct post_id) as report_count 
from Actions
where action = 'report'
and action_date = '2019-07-04'
group by extra