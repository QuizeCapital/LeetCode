# Write your MySQL query statement below
select t.student_id
, t.student_name 
,j.subject_name 
-- ,SUM(CASE WHEN j.subject_name IS NOT NULL THEN 1 ELSE 0 END) AS attended_exams
,count(e.student_id) as attended_exams
from Students as t 
cross join Subjects j 
left join Examinations as e on t.student_id = e.student_id and j.subject_name = e.subject_name
GROUP BY t.student_id, t.student_name, j.subject_name
ORDER BY t.student_id, t.student_name, j.subject_name
