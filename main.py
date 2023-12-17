import tkinter as tk
from view.mainPage import MainPage
from view.mainPage import AIPage, ITPage, MKPage
from controller.studentController import StudentController

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
            student_controller = StudentController(frame)
            frame.set_controller(student_controller)
  
        self.show_frame(MainPage)
  
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()





    # def __init__(self):
    #     super().__init__()
    #     self.geometry("1280x450")
    #     self.title('Quan ly sinh vien')
        
    #     # Create page
    #     view = View(self)
    #     view.grid(row=0, column=0, padx=6, pady=6)
    #     controller = StudentController(view)
    #     view.set_controller(controller)
        
        # ai_page = AIPage(view)
        # it_page = ITPage(view)
        # mk_page = MKPage(view)
        
        # # Add
        # controller.add_ai_page("AIPage", ai_page)
        # controller.add_it_page("ITPage", it_page)
        # controller.add_mk_page("MKPage", mk_page)
        
        # # Show pages
        # view.show_page("AIPage")
        # view.show_page("ITPage")
        # view.show_page("MKPage")

if __name__ == '__main__':
    app = App()
    app.mainloop()
    # # we close the current sqlite database connection explicitly
    # if type(c.model) is Student:
    #     sqlite_backend.disconnect_from_db(sqlite_backend.DB_name, c.model.connection)
    #     # the sqlite backend understands that it needs to open a new connection
    #     c.show_items()        