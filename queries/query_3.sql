-- Вкажіть потрібний subject_id замість 1
SELECT st.group_id, gr.name AS group_name, ROUND(AVG(g.grade),2) AS avg_grade
FROM students st
JOIN grades g ON st.id = g.student_id
JOIN groups gr ON st.group_id = gr.id
WHERE g.subject_id = 1
GROUP BY st.group_id, gr.name;