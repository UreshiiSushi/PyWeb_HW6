select s.name, studyes.name, t.name
from grades
left join studyes on grades.study_id = studyes.id
left join teachers as t on studyes.teacher_id = t.id
left join students as s on studyes.teacher_id = s.id
where s.id = 4 and t.id = 4
group by s.name, studyes.name, t.name