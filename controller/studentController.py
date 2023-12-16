import model.mvc_exceptions as mvc_exc
import model.studentCRUD as studentCRUD

class StudentController():
    def __init__(self, view):
        # self.model = model
        self.view = view
        self.students = 'students'
        self.connection = studentCRUD.connect_to_db(studentCRUD.DB_name)
        studentCRUD.create_table(self.connection, self.students)
        self.students_db_show = None
    
    def get_all_students(self):
        self.students_db_show = studentCRUD.select_all(self.connection, table_name=self.students)
        return self.students_db_show

    def insert_student(self, id, lastName, middleName, firstName, major, gpa):
        # assert type(lastName) == str, 'ho must be a string'
        # assert type(middleName) == str, 'tenDem must be a string'
        # assert type(firstName) == str, 'ten must be a string'
        # assert type(major) == str, 'monHoc must be a string'
        try:
            studentCRUD.insert_one(self.connection, id, lastName, middleName, firstName, major, gpa, table_name=self.students)
            self.students_db_show = studentCRUD.select_all(self.connection, table_name=self.students)
            self.view.display_students(students_list=self.students_db_show)
        except:
            self.students_db_show = studentCRUD.select_all(self.connection, table_name=self.students)
            self.view.display_student_already_stored_error()

    def update_student(self, id, lastName, middleName, firstName, major, gpa):
        # assert type(lastName) == str, 'ho must be a string'
        # assert type(middleName) == str, 'tenDem must be a string'
        # assert type(firstName) == str, 'ten must be a string'
        # assert type(major) == str, 'monHoc must be a string'
        try:
            studentCRUD.update_one(self.connection, id, lastName, middleName, firstName, major, gpa, table_name=self.students)
            self.students_db_show = studentCRUD.select_all(self.connection, table_name=self.students)
            self.view.display_students(students_list=self.students_db_show)
        except:
            self.students_db_show = studentCRUD.select_all(self.connection, table_name=self.students)
            self.view.display_student_not_yet_stored_error()

    def delete_student(self, id):
        try:
            studentCRUD.delete_one(self.connection, id, table_name=self.students)
            self.students_db_show = studentCRUD.select_all(self.connection, table_name=self.students)
            self.view.display_students(students_list=self.students_db_show)
        except:
            self.students_db_show = studentCRUD.select_all(self.connection, table_name=self.students)
            self.view.display_student_not_yet_stored_error()
    
    def sort_students(self, sort_by):
        students = studentCRUD.select_all(self.connection, table_name=self.students)
        if sort_by == 'Gpa':
            sorted_students = sorted(students, key=lambda student: student['gpa'])
        elif sort_by == 'Họ':
            sorted_students = sorted(students, key=lambda student: student['lastName'])
        elif sort_by == 'Tên':
            sorted_students = sorted(students, key=lambda student: student['firstName'])
        self.view.display_students(students_list=sorted_students)
    
    def find_student(self, find_by, value):
        students = studentCRUD.select_all(self.connection, table_name=self.students)
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
        self.view.display_students(students_list=found_student)
        