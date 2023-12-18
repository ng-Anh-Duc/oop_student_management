class Score:
    def __init__(self, studentID, courseID, score):
        self.studentID = studentID
        self.courseID = courseID
        self.score = score
        if self.courseID == 100:
            self.course = 'Python OOP'
        elif self.courseID == 101:
            self.course = 'Network'
        elif self.courseID == 102:
            self.course = 'Database'
        elif self.courseID == 200:
            self.course = 'JAVA'
        elif self.courseID == 201:
            self.course = 'Data Structure'
        elif self.courseID == 202:
            self.course = 'Cloud'
        elif self.courseID == 300:
            self.course = 'Business'
        elif self.courseID == 301:
            self.course = 'Advertisement'
        elif self.courseID == 302:
            self.course = 'Excel'