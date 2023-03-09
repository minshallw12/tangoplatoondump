import csv

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Students.all_students()


class Student:
    def all_students():
        lst = []
        with open('../data/students.csv') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                lst.append(row)
        return lst

class Staff:
    def __init__():
        pass
    def all_staff():
        with open('../data/staff.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)

student_list = Student()
staff1 = Staff()
print(student_list.all_students())
