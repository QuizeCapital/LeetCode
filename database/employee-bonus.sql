# Write your MySQL query statement below
-- select 
-- name
-- ,bonus
-- from Employee e
-- left join Bonus b on e.empId = b.empId
-- where bonus is null or bonus < 1000

select e.name, b.bonus from Employee e
left join Bonus b on e.empId = b.empId  where b.bonus < 1000 or b.bonus is null;