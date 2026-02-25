-- Змініть group_id та subject_id на потрібні значення
SELECT students.full_name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE students.group_id = 1
  AND grades.subject_id = 1
ORDER BY students.full_name;