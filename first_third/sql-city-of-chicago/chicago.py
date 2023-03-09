import psycopg
import csv

def data_cleaner(row):
    cleaned = {}
    cleaned['first_name'] = row['Name'].split(', ')[1]
    cleaned['last_name'] = row['Name'].split(', ')[0]
    cleaned['job_title'] = row['Job Titles']
    if row['Full or Part-Time'] == 'F':
        cleaned['full_time'] = True
        cleaned['annual_salary'] = row['Annual Salary']
    else:
        cleaned['full_time'] = False
        if row['Typical Hours'] != '':
            cleaned['annual_salary'] = int(row['Typical Hours']) * float(row['Hourly Rate']) 
        else:  
            cleaned['annual_salary'] = 0
    cleaned['department'] = row['Department']
    return cleaned


connection = psycopg.connect(f"dbname=chicago_salaries")

salary_table_creation_query = "CREATE TABLE employees (id serial PRIMARY KEY, first_name varchar(255), last_name varchar(255), job_title varchar(255), full_time bool, department varchar(255), annual_salary numeric)"
connection.execute(salary_table_creation_query)

with open("./Current_Employee_Names__Salaries__and_Position_Titles.csv") as csv_file:
    reader = csv.DictReader(csv_file)
    for employee in reader:
        cleaned_employee = data_cleaner(employee)
        connection.execute("INSERT INTO employees (first_name, last_name, job_title, full_time, annual_salary, department) VALUES (%s,%s,%s,%s,%s,%s)", (cleaned_employee['first_name'], cleaned_employee['last_name'], cleaned_employee['job_title'], cleaned_employee['full_time'], cleaned_employee['annual_salary'], cleaned_employee['department']))

connection.commit()
connection.close()

