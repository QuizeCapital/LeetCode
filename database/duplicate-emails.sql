/* Write your T-SQL query statement below */
select distinct p.email
from Person p  
left join Person n on p.email = n.email 
where p.id <> n.id
and p.email = n.email 

-- select email from person 
-- group by email 
