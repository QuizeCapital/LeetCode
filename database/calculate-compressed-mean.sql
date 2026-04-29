# Write your MySQL query statement below
with tmp as(
    select 
    sum(order_occurrences) as deno
    , sum(item_count * order_occurrences) as num
    from Orders
)

select 
round(num / deno, 2) as average_items_per_order 
from tmp 