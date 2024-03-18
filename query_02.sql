SELECT students.name AS student, avg(grade) as AverageGrade, s.name AS study
FROM grades
LEFT JOIN students ON grades.student_id = students.id 
LEFT JOIN groups AS g ON students.group_id = g.id 
LEFT JOIN studyes AS s ON grades.study_id = s.id 
WHERE s.id = 4
GROUP BY students.name, s.name
ORDER BY avg(grade) DESC
LIMIT 1