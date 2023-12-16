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
    
    def check_false_type(self, string):
        for char in string:
            if not char.isalpha():
                return True
        return False
        
    def insert_student(self, id, lastName, middleName, firstName, major):
        if self.check_false_type(lastName) or self.check_false_type(middleName) or self.check_false_type(firstName):
            self.view.display_type_warning()
        try:
            studentCRUD.insert_one(self.connection, id, lastName, middleName, firstName, major, table_name=self.students)
            self.students_db_show = studentCRUD.select_all(self.connection, table_name=self.students)
            self.view.display_students(students_list=self.students_db_show)
        except mvc_exc.ItemAlreadyStored:
            self.students_db_show = studentCRUD.select_all(self.connection, table_name=self.students)
            self.view.display_student_already_stored_error()

    def update_student(self, id, lastName, middleName, firstName, major):
        if self.check_false_type(lastName) or self.check_false_type(middleName) or self.check_false_type(firstName):
            self.view.display_type_warning()
        try:
            studentCRUD.update_one(self.connection, id, lastName, middleName, firstName, major, table_name=self.students)
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
            for student in students:
                if student.gpa == None:
                    self.view.display_sort_error()
                    sorted_students = students
                    break
            else:
                sorted_students = sorted(students, key=lambda student: student.gpa)
        elif sort_by == 'Họ':
            sorted_students = sorted(students, key=lambda student: student.lastName)
        elif sort_by == 'Tên':
            sorted_students = sorted(students, key=lambda student: student.firstName)
        self.view.display_students(students_list=sorted_students)
    
    def find_student(self, find_by, value):
        students = studentCRUD.select_all(self.connection, table_name=self.students)
        found_student = []
        if find_by == 'Major':
            for s in students:
                if s.major == value:
                    found_student.append(s)
        elif find_by == 'MSSV':
            for s in students:
                if s.id == value:
                    found_student.append(s)
                    break
        self.view.display_students(students_list=found_student)
        