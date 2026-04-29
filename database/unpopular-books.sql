-- # Write your MySQL query statement below
-- with tmp as(
-- select 
-- b.book_id
-- ,b.name
-- ,b.available_from
-- ,o.order_id
-- ,o.quantity
-- ,o.dispatch_date
-- from Books b
-- left join Orders o on o.book_id = b.book_id
-- where o.dispatch_date between  '2018-06-23' and '2019-06-23'
-- -- and b.available_from  < '2019-05-23'
-- )
-- select * from tmp


-- select 
-- *
-- from Books b
-- left join Orders o on o.book_id = b.book_id


-- select 
-- b.book_id
-- , b.name
-- from Books b
-- left join Orders o on o.book_id = b.book_id
-- group by b.book_id, b.name
-- where o.dispatch_date  <  '2018-06-23'
-- having sum(ifnull(quantity, 0)) < 10
-- where b.available_from  > '2019-05-23'
-- and  o.dispatch_date  >  '2018-06-23' 

select b.book_id, b.name
from books b left join orders o
-- on b.book_id = o.book_id and dispatch_date between '2018-06-23' and '2019-06-23'
on b.book_id = o.book_id and dispatch_date > '2018-06-23'
-- where datediff('2019-06-23', available_from) > 30
where available_from < '2019-05-23'
group by b.book_id, b.name
having ifnull(sum(quantity),0) <10;