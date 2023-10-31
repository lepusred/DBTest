from firstdata import firstdata

from myquerydb import create_connection, create_database, execute_query

connection = create_connection(
    "postgres", "postgres", "postgres", "localhost", "5432"
)
create_database_query = "CREATE DATABASE students_3"
create_database(connection, create_database_query)

create_students_table = """
CREATE TABLE IF NOT EXISTS students(
  name TEXT NOT NULL, 
  mark INTEGER
)
"""
connection = create_connection(
    "students_3", "postgres", "postgres", "localhost", "5432"
)

execute_query(connection, create_students_table)


students_records = ", ".join(["%s"] * len(firstdata))

insert_query = (
    f"INSERT INTO students(name, mark) VALUES {students_records}"
)

cursor = connection.cursor()
cursor.execute(insert_query, firstdata)
