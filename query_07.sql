select studyes.name, g.name, s.name, grade
from grades
left join students as s on grades.student_id = s.id
left join groups as g on s.group_id = g.id
left join studyes on grades.study_id = studyes.id
where g.id = 3 and studyes.id = 4