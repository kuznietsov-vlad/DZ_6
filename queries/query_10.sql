-- Вкажіть student_id і teacher_id замість 1
SELECT DISTINCT sub.name
FROM subjects sub
JOIN grades g ON sub.id = g.subject_id
WHERE g.student_id = 1 AND sub.teacher_id = 1;