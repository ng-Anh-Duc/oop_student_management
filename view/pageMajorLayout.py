import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MajorPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.student_controller = None
        self.student_id_var = tk.IntVar()
        self.pythonOOP_var = tk.DoubleVar()
        self.network_var = tk.DoubleVar()
        self.database_var = tk.DoubleVar()

        # self.student_tree = ttk.Treeview(self, columns=("Môn học", "GPA"), show="headings")
        # self.student_tree.heading("Môn học", text="Môn học")
        # self.student_tree.heading("GPA", text="GPA")

        self.studen_id_label = ttk.Label(self, text="MSSV:").grid(row=1, column=0, padx=6, pady=6)
        self.student_id_entry = ttk.Entry(self, textvariable=self.student_id_var).grid(row=1, column=1, padx=6, pady=6)

        self.pythonOOP_label = ttk.Label(self, text="Python OOP:").grid(row=0, column=2, padx=6, pady=6)
        self.pythonOOP_entry = ttk.Entry(self, textvariable=self.pythonOOP_var).grid(row=0, column=3, padx=6, pady=6)

        self.network_label = ttk.Label(self, text="Network:").grid(row=0, column=4, padx=6, pady=6)
        self.network_entry = ttk.Entry(self, textvariable=self.network_var).grid(row=0, column=5, padx=6, pady=6)

        self.database_label = ttk.Label(self, text="Database:").grid(row=0, column=0, padx=6, pady=6)
        self.database_entry = ttk.Entry(self, textvariable=self.pythonOOP_var).grid(row=0, column=1, padx=6, pady=6)

        self.finish_button = ttk.Button(self, text="Thêm điểm", command=self.add_score()).grid(row=0, column=6, padx=6, pady=6)

        self.show_score_button = ttk.Button(self, text="Xem điểm", command=self.display_score()).grid(row=1, column=2, padx=6, pady=6)

        # self.student_tree.grid(row=3, column=0, columnspan=6, padx=6, pady=6)
    def display_score(self):
        pass

    def add_score(self):
        pass

    def set_controller(self, controller):
        self.student_controller = controller