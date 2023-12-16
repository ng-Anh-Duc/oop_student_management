import tkinter as tk
from view.mainPage import MainPage
from controller.studentController import StudentController

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x450")
        self.title('Quan ly sinh vien')
        view = MainPage(self)
        view.grid(row=0, column=0, padx=6, pady=6)
        controller = StudentController(view)
        view.set_controller(controller)

if __name__ == '__main__':
    app = App()
    app.mainloop()
    # # we close the current sqlite database connection explicitly
    # if type(c.model) is Student:
    #     sqlite_backend.disconnect_from_db(sqlite_backend.DB_name, c.model.connection)
    #     # the sqlite backend understands that it needs to open a new connection
    #     c.show_items()        