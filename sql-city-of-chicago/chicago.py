import psycopg
import csv

connection = psycopg.connect(f"dbname=chicago_salaries")

salary_table_creation_query = "CREATE TABLE employees (id serial PRIMARY KEY, first_name varchar(255), last_name varchar(255), job_title varchar(255), full_time bool, department varchar(255), annual_salary money)"
connection.execute(salary_table_creation_query)
connection.commit()
connection.close()