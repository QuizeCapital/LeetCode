# Write your MySQL query statement below
-- select u.name,
-- sum(distance) as travelled_distance
-- from Rides d
-- join Users u on d.user_id = u.id
-- group by u.name
-- order by travelled_distance desc, name

select u.name,
ifnull(sum(distance), 0) as travelled_distance
from Rides d
right join Users u on d.user_id = u.id
group by u.id, u.name
order by travelled_distance desc, name