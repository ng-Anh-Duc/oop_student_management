import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from view.mainPage import MainPage as main

class ITPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.course_controller = None
        self.student_id_var = tk.IntVar()
        self.java_var = tk.DoubleVar()
        self.dataStructure_var = tk.DoubleVar()
        self.cloud_var = tk.DoubleVar()

        # self.student_tree = ttk.Treeview(self, columns=("Môn học", "GPA"), show="headings")
        # self.student_tree.heading("Môn học", text="Môn học")
        # self.student_tree.heading("GPA", text="GPA")

        self.studen_id_label = ttk.Label(self, text="MSSV:").grid(row=1, column=0, padx=6, pady=6)
        self.student_id_entry = ttk.Entry(self, textvariable=self.student_id_var).grid(row=1, column=1, padx=6, pady=6)

        self.java_label = ttk.Label(self, text="JAVA:").grid(row=0, column=2, padx=6, pady=6)
        self.java_entry = ttk.Entry(self, textvariable=self.java_var).grid(row=0, column=3, padx=6, pady=6)

        self.dataStructure_label = ttk.Label(self, text="Data Structure:").grid(row=0, column=4, padx=6, pady=6)
        self.dataStructure_entry = ttk.Entry(self, textvariable=self.dataStructure_var).grid(row=0, column=5, padx=6, pady=6)

        self.cloud_label = ttk.Label(self, text="Cloud:").grid(row=0, column=0, padx=6, pady=6)
        self.cloud_entry = ttk.Entry(self, textvariable=self.cloud_var).grid(row=0, column=1, padx=6, pady=6)

        self.finish_button = ttk.Button(self, text="Thêm điểm", command=self.update_score).grid(row=0, column=6, padx=6, pady=6)

        self.show_score_button = ttk.Button(self, text="Xem điểm", command= lambda: self.display_score(show_button=True)).grid(row=1, column=2, padx=6, pady=6)
        self.mainPage_button = ttk.Button(self, text="Trang chủ", command=lambda : controller.show_frame(main)).grid(row=1, column=4, padx=6, pady=6)

        self.score_tree = ttk.Treeview(self, columns=("MSSV", "ID Môn học", "Môn học", "Điểm"), show="headings")
        self.score_tree.heading("MSSV", text="MSSV")
        self.score_tree.heading("ID Môn học", text="ID Môn học")
        self.score_tree.heading("Môn học", text="Môn học")
        self.score_tree.heading("Điểm", text="Điểm")
        self.score_tree.grid(row=5, column=0, columnspan=4, padx=6, pady=6)

    def get_value(self):
        # Get values from entry widgets
        student_id = self.student_id_var.get()
        java = self.java_var.get()
        datatructure = self.dataStructure_var.get()
        cloud = self.cloud_var.get()
        return student_id, java, datatructure, cloud

    def display_score(self, scores_list=None, show_button=False):
        if self.course_controller and show_button:
            print('adnfdskjnfkjs')
            student_id = self.student_id_var.get()
            scores_list = self.course_controller.get_scores_by_student(student_id)
        self.score_tree.delete(*self.score_tree.get_children())
        for score in scores_list:
            values = (score.studentID, score.courseID, score.course, score.score)
            self.score_tree.insert("", "end", values=values)

    def display_student_already_stored_error(self):
        messagebox.showerror("Sinh viên đã tồn tại")

    def display_student_not_yet_stored_error(self):
        messagebox.showerror("Sinh viên chưa tồn tại")

    def update_score(self):
        student_id, java, dataStructure, cloud = self.get_value()
        if self.course_controller:
            scores = (java, dataStructure, cloud)
            self.course_controller.update_scores(student_id, scores)
        self.clear_entries()


    def set_controller(self, controller):
        self.student_controller = controller
    
    def clear_entries(self):
        # Clear entry widgets
        self.student_id_var.set(0)
        self.java_var.set(0.0)
        self.dataStructure_var.set(0.0)
        self.cloud_var.set(0.0)