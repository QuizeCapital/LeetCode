/* Write your T-SQL query statement below */
select e.name as Employee 
-- select *
from Employee e   
left join Employee m  on m.id = e.managerId
where e.salary > m.salary;
