# Write your MySQL query statement below
with tmp as (
    select product_id
    , min(year) as first_year
    from Sales
    group by product_id
)

select s.product_id, t.first_year, s.quantity, s.price
from tmp t 
join Sales s
on t.product_id = s.product_id
and t.first_year = s.year