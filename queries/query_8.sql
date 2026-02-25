-- Вкажіть потрібний teacher_id замість 1
SELECT ROUND(AVG(g.grade),2) AS avg_grade
FROM grades g
JOIN subjects s ON g.subject_id = s.id
WHERE s.teacher_id = 1;