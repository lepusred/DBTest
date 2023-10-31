from myquerydb import create_connection, execute_read_query

connection = create_connection(
    "students_2", "postgres", "postgres", "localhost", "5432"
)


select_students = """SELECT name, SUM(CASE WHEN mark = 2 THEN 1 ELSE 0 END)
                    FROM students
                    GROUP BY name
                    HAVING SUM(CASE WHEN mark = 5 THEN 1 ELSE 0 END) > 9
                    ORDER BY name"""
students = execute_read_query(connection, select_students)

for student in students:
    print(*student)