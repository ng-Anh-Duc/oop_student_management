import model.mvc_exceptions as mvc_exc

class Controller():
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def show_students(self):
        students_to_show = self.model.read_students()
        self.view.display_students(students_list=students_to_show)

    def insert_student(self, id, lastName, middleName, firstName, major, gpa):
        # assert type(lastName) == str, 'ho must be a string'
        # assert type(middleName) == str, 'tenDem must be a string'
        # assert type(firstName) == str, 'ten must be a string'
        # assert type(major) == str, 'monHoc must be a string'
        try:
            self.model.create_student(id, lastName, middleName, firstName, major, gpa)
            self.show_students()
        except:
            self.view.display_student_already_stored_error()

    def update_student(self, id, lastName, middleName, firstName, major, gpa):
        # assert type(lastName) == str, 'ho must be a string'
        # assert type(middleName) == str, 'tenDem must be a string'
        # assert type(firstName) == str, 'ten must be a string'
        # assert type(major) == str, 'monHoc must be a string'
        try:
            self.model.update_student(id, lastName, middleName, firstName, major, gpa)
            self.show_students()
        except:
            self.view.display_student_not_yet_stored_error()

    def delete_student(self, id):
        try:
            self.model.delete_student(id)
            self.show_students()
        except:
            self.view.display_student_not_yet_stored_error()
    
    def sort_students(self, sort_by):
        sorted_students = self.model.sort_students(sort_by)
        self.view.display_students(students_list=sorted_students)