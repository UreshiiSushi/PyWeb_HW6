select s.name, studyes.name
from grades
left join studyes on grades.study_id = studyes.id
left join students as s on studyes.teacher_id = s.id
where s.id = 4
group by s.name, studyes.name