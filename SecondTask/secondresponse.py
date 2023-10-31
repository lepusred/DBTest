from myquerydb import create_connection, execute_read_query

connection = create_connection(
    "students_2", "postgres", "postgres", "localhost", "5432"
)


select_students = """SELECT name, ROUND(AVG(mark), 2) as avg_mark, subject
                    FROM studentsSubject
                    GROUP BY name, subject
                    ORDER BY name, subject"""
students = execute_read_query(connection, select_students)

for student in students:
    print(*student)