# Write your MySQL query statement below
with tmp as 
(select w.name
,w.product_id
,w.units
,p.product_name
,p.width
,p.length
,p.height
, p.width * p.length * p.height * w.units as Volume
from Warehouse w
left join Products p on p.product_id = w.product_id)

select 
name as warehouse_name
,sum(Volume) as volume
from tmp
group by name
