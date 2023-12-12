import tkinter as tk
from view.view import View
from controller.controller import Controller
from model.student import Student
import model.sqlite_backend as sqlite_backend

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x450")
        self.title('Quan ly sinh vien')

        model = Student()
        view = View(self)
        view.grid(row=0, column=0, padx=6, pady=6)
        controller = Controller(model, view)
        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
    # # we close the current sqlite database connection explicitly
    # if type(c.model) is Student:
    #     sqlite_backend.disconnect_from_db(sqlite_backend.DB_name, c.model.connection)
    #     # the sqlite backend understands that it needs to open a new connection
    #     c.show_items()        