select t.name, avg(grade)
from grades
left join studyes on grades.study_id = studyes.id
left join teachers as t on studyes.teacher_id = t.id
where t.id = 4
group by t.name