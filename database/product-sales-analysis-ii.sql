# Write your MySQL query statement below
select 
s.product_id
,SUM(s.quantity) as total_quantity


from Sales s
left join Product p ON s.product_id = p.product_id
group by s.product_id