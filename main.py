import random
from faker import Faker
import psycopg2
from datetime import date, timedelta

fake = Faker("uk_UA")

conn = psycopg2.connect(
    dbname="universitydb",
    user="docker",
    password="docker",
    host="127.0.0.1",
    port=5433
)

cur = conn.cursor()

# --- GROUPS ---
groups = ["КН-21", "КН-22", "КН-23"]
for g in groups:
    cur.execute("INSERT INTO groups (name) VALUES (%s)", (g,))

# --- TEACHERS ---
teacher_ids = []
for _ in range(4):
    cur.execute(
        "INSERT INTO teachers (full_name) VALUES (%s) RETURNING id",
        (fake.name(),)
    )
    teacher_ids.append(cur.fetchone()[0])

# --- SUBJECTS ---
subjects = ["Математика", "Програмування", "Бази даних", "Фізика", "Алгоритми", "ОС"]
subject_ids = []
for s in subjects:
    cur.execute(
        "INSERT INTO subjects (name, teacher_id) VALUES (%s, %s) RETURNING id",
        (s, random.choice(teacher_ids))
    )
    subject_ids.append(cur.fetchone()[0])

# --- STUDENTS ---
student_ids = []
for _ in range(40):
    cur.execute(
        "INSERT INTO students (full_name, group_id) VALUES (%s, %s) RETURNING id",
        (fake.name(), random.randint(1, 3))
    )
    student_ids.append(cur.fetchone()[0])

# --- GRADES ---
for student in student_ids:
    for _ in range(random.randint(10, 20)):
        cur.execute(
            """
            INSERT INTO grades (student_id, subject_id, grade, date_received)
            VALUES (%s, %s, %s, %s)
            """,
            (
                student,
                random.choice(subject_ids),
                random.randint(1, 12),
                date.today() - timedelta(days=random.randint(1, 365))
            )
        )


conn.commit()
cur.close()
conn.close()

print("✅ База данних заповнена")