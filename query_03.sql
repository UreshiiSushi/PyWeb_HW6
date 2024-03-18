SELECT g.name AS groupname, avg(grade) AS AverageGrade, s.name AS study
FROM grades
LEFT JOIN students ON grades.student_id=students.id
LEFT JOIN groups AS g ON students.group_id=g.id
LEFT JOIN studyes AS s ON grades.study_id = s.id
WHERE s.id = 3
GROUP BY s.name, g.name