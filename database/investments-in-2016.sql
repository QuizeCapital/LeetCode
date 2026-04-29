# Write your MySQL query statement below
with tmp_tv as (
    select tiv_2015
    from Insurance 
    group by tiv_2015
    having count(*) > 1
),
tmp_loc as (
    select lat, lon 
    from Insurance 
    group by lat, lon
    having count(*) = 1
)

SELECT ROUND(SUM(i.tiv_2016), 2) AS tiv_2016
FROM Insurance i
JOIN tmp_tv t ON i.tiv_2015 = t.tiv_2015
JOIN tmp_loc l ON i.lat = l.lat AND i.lon = l.lon;