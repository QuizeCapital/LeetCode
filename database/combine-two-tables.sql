# Write your MySQL query statement below
-- select
-- firstName
-- ,lastName 
-- ,ifnull(city, NULL) AS city
-- ,ifnull(state, NULL) AS state
-- from 
-- Person p 
-- left join Address a as p.personId = a.personId

-- select 
-- firstName
-- ,lastName 
-- ,ifnull(city, NULL) AS city
-- ,ifnull(state, NULL) AS state
-- from PERSON p
-- left join Address a 
-- on a.personId = p.personId
 
SELECT firstName,lastName,city, state 
FROM Person p
LEFT JOIN Address a
ON p.personId = a.personId;