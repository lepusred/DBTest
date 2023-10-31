from seconddata import seconddata

from myquerydb import create_connection, execute_query

connection = create_connection(
    "students_2", "postgres", "postgres", "localhost", "5432"
)


create_studentsSubject_table = """
CREATE TABLE IF NOT EXISTS studentsSubject(
  name TEXT NOT NULL, 
  mark INTEGER,
  SUBJECT TEXT NOT NULL
)
"""

execute_query(connection, create_studentsSubject_table)


students_records = ", ".join(["%s"] * len(seconddata))

insert_query = (
    f"INSERT INTO studentsSubject(name, mark, subject) VALUES {students_records}"
)

cursor = connection.cursor()
cursor.execute(insert_query, seconddata)
