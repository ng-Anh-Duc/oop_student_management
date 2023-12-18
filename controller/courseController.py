import model.mvc_exceptions as mvc_exc
import model.scoreCRUD as scoreCRUD
# import view.AIPage as AIPage

class CourseController():
    def __init__(self, view):
        # self.model = model
        self.courses = 'courses'
        self.scores = 'scoresRelationship'
        self.view = view
        self.connection = scoreCRUD.connect_to_db(scoreCRUD.DB_name)
        scoreCRUD.create_course_table(self.connection, self.courses)
        scoreCRUD.insert_course(self.connection, 100, 'PythonOOP', 'AI', table_name=self.courses)
        scoreCRUD.insert_course(self.connection, 101, 'Network', 'AI', table_name=self.courses)
        scoreCRUD.insert_course(self.connection, 102, 'Database', 'AI', table_name=self.courses)
        scoreCRUD.insert_course(self.connection, 200, 'Java', 'IT', table_name=self.courses)
        scoreCRUD.insert_course(self.connection, 201, 'DataStructure', 'IT', table_name=self.courses)
        scoreCRUD.insert_course(self.connection, 202, 'Cloud', 'IT', table_name=self.courses)
        scoreCRUD.insert_course(self.connection, 300, 'Business', 'MK', table_name=self.courses)
        scoreCRUD.insert_course(self.connection, 301, 'Advertisement', 'MK', table_name=self.courses)
        scoreCRUD.insert_course(self.connection, 302, 'Excel', 'MK', table_name=self.courses)
        scoreCRUD.create_score_relationship_table(self.connection, self.scores, self.courses, 'students')
    
    def get_scores_by_student(self, studentID):
        scores_db_show = scoreCRUD.select_scores_by_student(self.connection, studentID, table_name=self.scores)
        return scores_db_show
    
    # def check_false_type(self, string):
    #     for char in string:
    #         if not char.isalpha():
    #             return True
    #     return False
    
    def update_scores(self, studentID, score, major):
        try:
            if major == 'ai':
                scoreCRUD.update_one(self.connection, studentID, 100, score[0], table_name=self.scores)
                scoreCRUD.update_one(self.connection, studentID, 101, score[1], table_name=self.scores)
                scoreCRUD.update_one(self.connection, studentID, 102, score[2], table_name=self.scores)
                scores_db_show = scoreCRUD.select_all(self.connection, table_name=self.scores)
                self.view.display_score(scores_list=scores_db_show)
            elif major == 'it':
                scoreCRUD.update_one(self.connection, studentID, 200, score[0], table_name=self.scores)
                scoreCRUD.update_one(self.connection, studentID, 201, score[1], table_name=self.scores)
                scoreCRUD.update_one(self.connection, studentID, 202, score[2], table_name=self.scores)
                scores_db_show = scoreCRUD.select_all(self.connection, table_name=self.scores)
                self.view.display_score(scores_list=scores_db_show)
            elif major == 'mk':
                scoreCRUD.update_one(self.connection, studentID, 300, score[0], table_name=self.scores)
                scoreCRUD.update_one(self.connection, studentID, 301, score[1], table_name=self.scores)
                scoreCRUD.update_one(self.connection, studentID, 302, score[2], table_name=self.scores)
                scores_db_show = scoreCRUD.select_all(self.connection, table_name=self.scores)
                self.view.display_score(scores_list=scores_db_show)
            # self.scores_db_show = scoreCRUD.select_scores_by_student(self.connection, studentID, table_name=self.scores)
            # self.view.display_score(scores_list=self.scores_db_show)
        except mvc_exc.ItemAlreadyStored:
            self.view.display_student_not_yet_stored_error()

    # def update_student(self, id, lastName, middleName, firstName, major):
    #     if self.check_false_type(lastName) or self.check_false_type(middleName) or self.check_false_type(firstName):
    #         self.view.display_type_warning()
    #     try:
    #         studentCRUD.update_one(self.connection, id, lastName, middleName, firstName, major, table_name=self.students)
    #         self.students_db_show = studentCRUD.select_all(self.connection, table_name=self.students)
    #         self.view.display_students(students_list=self.students_db_show)
    #     except:
    #         self.students_db_show = studentCRUD.select_all(self.connection, table_name=self.students)
    #         self.view.display_student_not_yet_stored_error()

    # def delete_student(self, id):
    #     try:
    #         studentCRUD.delete_one(self.connection, id, table_name=self.students)
    #         self.students_db_show = studentCRUD.select_all(self.connection, table_name=self.students)
    #         self.view.display_students(students_list=self.students_db_show)
    #     except:
    #         self.students_db_show = studentCRUD.select_all(self.connection, table_name=self.students)
    #         self.view.display_student_not_yet_stored_error()
    # def display_courses_page(self):
    #     view = AIPage()
    #     view.display_courses_page()
