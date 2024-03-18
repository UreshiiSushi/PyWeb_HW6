select groups.name, s.name
from groups
left join students as s on groups.id = s.group_id
where groups.id = 2