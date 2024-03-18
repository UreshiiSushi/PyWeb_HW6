SELECT s.name AS student, avg(grade) AS AverageGrade
FROM grades AS grd
JOIN students AS s ON grd.student_id = s.id 
GROUP BY s.name
ORDER BY avg(grade) DESC 
LIMIT 5