# Write your MySQL query statement below
with tmp as (
  select 
  machine_id
  ,count(*) as rows_count
  ,max(timestamp) - min(timestamp) as diff
from Activity
group by machine_id, process_id 
)

select 
machine_id
, round(avg(diff),3) as processing_time
from tmp
group by machine_id