select teachers.name, s.name
from teachers
left join studyes as s on teachers.id = s.teacher_id
where teachers.id = 4