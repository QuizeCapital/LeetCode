/* Write your T-SQL query statement below */
-- update salary 
-- set sex =
-- case when sex = \'m\' then \'f\'
-- when sex = \'f\' then \'m\'
-- else sex end

UPDATE Salary
SET sex = CASE
            WHEN sex = 'f' THEN 'm'
            ELSE 'f' END