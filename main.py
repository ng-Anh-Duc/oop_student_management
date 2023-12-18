import tkinter as tk
from view.mainPage import MainPage
from view.pageAI import AIPage
from view.pageIT import ITPage
from view.pageMK import MKPage
from controller.studentController import StudentController
from controller.courseController import CourseController

class App(tk.Tk):




    def __init__(self, *args, **kwargs): 
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # view = MainPage(container, self)
        # student_controller = StudentController(view)
        # view.set_controller(student_controller)
        # initializing frames to an empty array
        self.frames = {}  
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (MainPage, AIPage, ITPage, MKPage):
  
            frame = F(container, self)
            self.frames[F] = frame 
            frame.grid(row = 0, column = 0, sticky ="nsew")
            if type(frame) == MainPage:
                student_controller = StudentController(frame)
                frame.set_controller(student_controller)
                print("Set student controller:", student_controller)
            elif type(frame) == AIPage:
                course_controller = CourseController(frame)
                frame.set_controller(course_controller)
                print("Set course controller:", course_controller)
            elif type(frame) == ITPage:
                course_controller = CourseController(frame)
                frame.set_controller(course_controller)
                print("Set course controller:", course_controller)
            elif type(frame) == MKPage:
                course_controller = CourseController(frame)
                frame.set_controller(course_controller)
                print("Set course controller:", course_controller)
  
        self.show_frame(MainPage)
  
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == '__main__':
    app = App()
    app.mainloop()
    # # we close the current sqlite database connection explicitly
    # if type(c.model) is Student:
    #     sqlite_backend.disconnect_from_db(sqlite_backend.DB_name, c.model.connection)
    #     # the sqlite backend understands that it needs to open a new connection
    #     c.show_items()        