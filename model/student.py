import model.sqlite_backend as sqlite_backend

class Student():

    def __init__(self):
        self.students = 'students'
        self.connection = sqlite_backend.connect_to_db(sqlite_backend.DB_name)
        sqlite_backend.create_table(self.connection, self.students)
    
    def read_students(self):
        return sqlite_backend.select_all(self.connection, table_name=self.students)
    
    def create_student(self, id, lastName, middleName, firstName, major, gpa):
        sqlite_backend.insert_one(self.connection, id, lastName, middleName, firstName, major, gpa, table_name=self.students)

    def update_student(self, id, lastName, middleName, firstName, major, gpa):
        sqlite_backend.update_one(self.connection, id, lastName, middleName, firstName, major, gpa, table_name=self.students)

    def delete_student(self, id):
        sqlite_backend.delete_one(self.connection, id, table_name=self.students)
    
    def sort_students(self, sort_by):
        students = self.read_students()
        if sort_by == 'Gpa':
            sorted_students = sorted(students, key=lambda student: student['gpa'])
        elif sort_by == 'Họ':
            sorted_students = sorted(students, key=lambda student: student['lastName'])
        elif sort_by == 'Tên':
            sorted_students = sorted(students, key=lambda student: student['firstName'])
        return sorted_students