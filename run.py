import psycopg2

def run_query(cur, file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        sql = f.read().strip()
    cur.execute(sql)
    try:
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except psycopg2.ProgrammingError:
        print(f"Запит {file_name} виконано, результатів немає.")

if __name__ == "__main__":
    conn = psycopg2.connect(
        dbname="universitydb",
        user="docker",
        password="docker",
        host="127.0.0.1",
        port=5433
    )
    cur = conn.cursor()

    # Виконати один запит
    run_query(cur, "queries/query_7.sql")

    # for i in range(1, 11):
    #     run_query(cur, f"queries/query_{i}.sql")

    cur.close()
    conn.close()