import model.mvc_exceptions as mvc_exc
import model.sqlite_backend as sqlite_backend

class Controller():
    def __init__(self, view):
        # self.model = model
        self.view = view
        self.students = 'students'
        self.connection = sqlite_backend.connect_to_db(sqlite_backend.DB_name)
        sqlite_backend.create_table(self.connection, self.students)
    
    def show_students(self):
        students_to_show = sqlite_backend.select_all(self.connection, table_name=self.students)
        self.view.display_students(students_list=students_to_show)

    def insert_student(self, id, lastName, middleName, firstName, major, gpa):
        # assert type(lastName) == str, 'ho must be a string'
        # assert type(middleName) == str, 'tenDem must be a string'
        # assert type(firstName) == str, 'ten must be a string'
        # assert type(major) == str, 'monHoc must be a string'
        try:
            sqlite_backend.insert_one(self.connection, id, lastName, middleName, firstName, major, gpa, table_name=self.students)
            self.show_students()
        except:
            self.view.display_student_already_stored_error()

    def update_student(self, id, lastName, middleName, firstName, major, gpa):
        # assert type(lastName) == str, 'ho must be a string'
        # assert type(middleName) == str, 'tenDem must be a string'
        # assert type(firstName) == str, 'ten must be a string'
        # assert type(major) == str, 'monHoc must be a string'
        try:
            sqlite_backend.update_one(self.connection, id, lastName, middleName, firstName, major, gpa, table_name=self.students)
            self.show_students()
        except:
            self.view.display_student_not_yet_stored_error()

    def delete_student(self, id):
        try:
            sqlite_backend.delete_one(self.connection, id, table_name=self.students)
            self.show_students()
        except:
            self.view.display_student_not_yet_stored_error()
    
    def sort_students(self, sort_by):
        students = sqlite_backend.select_all(self.connection, table_name=self.students)
        if sort_by == 'Gpa':
            sorted_students = sorted(students, key=lambda student: student['gpa'])
        elif sort_by == 'Họ':
            sorted_students = sorted(students, key=lambda student: student['lastName'])
        elif sort_by == 'Tên':
            sorted_students = sorted(students, key=lambda student: student['firstName'])
        self.view.display_students(students_list=sorted_students)
    
    def find_student(self, find_by, value):
        students = sqlite_backend.select_all(self.connection, table_name=self.students)
        found_student = []
        if find_by == 'Major':
            for s in students:
                if s['major'] == value:
                    found_student.append(s)
        elif find_by == 'MSSV':
            for s in students:
                if s['id'] == value:
                    found_student.append(s)
                    break
        if len(found_student) == 0:
            self.view.display_student_not_yet_stored_error()
        else:
            self.view.display_students(students_list=found_student)