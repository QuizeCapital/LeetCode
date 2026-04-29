# Write your MySQL query statement below
select substring_index(e.email, '@', -1) as email_domain
,count(*) as count
from emails e
group by 1
having email_domain like "%.com"
order by 1 asc 