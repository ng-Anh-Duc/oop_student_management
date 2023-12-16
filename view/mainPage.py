import tkinter as tk
from tkinter import ttk, messagebox

class MainPage(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        self.student_id_var = tk.IntVar()
        self.first_name_var = tk.StringVar()
        self.middle_name_var = tk.StringVar()
        self.last_name_var = tk.StringVar()
        self.major_var = tk.StringVar()
        self.sort_by_var = tk.StringVar()
        self.find_by_var = tk.StringVar()
        # Create labels and entry widgets
        self.id_label = ttk.Label(self, text="MSSV:").grid(row=2, column=0, padx=6, pady=6)
        self.id_entry = ttk.Entry(self, textvariable=self.student_id_var).grid(row=2, column=1, padx=6, pady=6)

        self.last_name_label = ttk.Label(self, text="Họ:").grid(row=1, column=0, padx=6, pady=6)
        self.last_name_entry = ttk.Entry(self, textvariable=self.last_name_var).grid(row=1, column=1, padx=6, pady=6)

        self.middle_name_label = ttk.Label(self, text="Tên đệm:").grid(row=1, column=2, padx=6, pady=6)
        self.middle_name_entry = ttk.Entry(self, textvariable=self.middle_name_var).grid(row=1, column=3, padx=6, pady=6)

        self.first_name_label = ttk.Label(self, text="Tên:").grid(row=1, column=4, padx=6, pady=6)
        self.first_name_entry = ttk.Entry(self, textvariable=self.first_name_var).grid(row=1, column=5, padx=6, pady=6)

        self.major_label = ttk.Label(self, text="Môn học:").grid(row=2, column=2, padx=6, pady=6)
        self.major_entry = ttk.Entry(self, textvariable=self.major_var).grid(row=2, column=3, padx=6, pady=6)

        self.sort_by_choices = ttk.Combobox(self, textvariable=self.sort_by_var, values=["Gpa", "Họ", "Tên"]).grid(row=4, column=4, padx=6, pady=6)
        self.find_by_choices = ttk.Combobox(self, textvariable=self.find_by_var, values=["Major", "MSSV"]).grid(row=4, column=5, padx=6, pady=6)

        self.show_button = ttk.Button(self, text="DSSV", command=lambda: self.display_students(show_button=True)).grid(row=3, column=0, padx=6, pady=6)
        self.add_button = ttk.Button(self, text="Thêm Sinh viên", command=self.add_student).grid(row=3, column=1, padx=6, pady=6)
        self.update_button = ttk.Button(self, text="Cập nhật Sinh viên", command=self.update_student).grid(row=3, column=2, padx=6, pady=6)
        self.delete_button = ttk.Button(self, text="Xoá Sinh viên", command=self.delete_student).grid(row=3, column=3, padx=6, pady=6)
        self.sort_button = ttk.Button(self, text="Sắp xếp", command=self.sort_students).grid(row=3, column=4, padx=6, pady=6)
        self.find_button = ttk.Button(self, text="Tìm Sinh viên", command=self.find_student).grid(row=3, column=5, padx=6, pady=6)
        # self.point_button = ttk.Button(self, text="Thêm điểm", command=self.)

        # Create student table
        self.student_tree = ttk.Treeview(self, columns=("MSSV", "Họ", "Tên đệm", "Tên", "Môn học", "GPA"), show="headings")
        self.student_tree.heading("MSSV", text="MSSV")
        self.student_tree.heading("Họ", text="Họ")
        self.student_tree.heading("Tên đệm", text="Tên đệm")
        self.student_tree.heading("Tên", text="Tên")
        self.student_tree.heading("Môn học", text="Môn học")
        self.student_tree.heading("GPA", text="GPA")
        self.student_tree.grid(row=5, column=0, columnspan=6, padx=6, pady=6)

    def display_students(self, students_list=None, show_button=False):
        if self.controller and show_button == True:
            students_list = self.controller.get_all_students()
        self.student_tree.delete(*self.student_tree.get_children())
        for student in students_list:
            values = (student.id, student.lastName, student.middleName, student.firstName, student.major, student.gpa)
            self.student_tree.insert("", "end", values=values)
    
    def display_type_warning(self):
        messagebox.showerror("Ho, ten dem, ten co kieu du lieu la chu")

    def display_student_already_stored_error(self):
        messagebox.showerror("Sinh viên đã tồn tại")

    def display_student_not_yet_stored_error(self):
        messagebox.showerror("Sinh viên chưa tồn tại")
    
    def display_sort_error(self):
        messagebox.showerror("none type object can't be sorted")

    def get_value(self):
        # Get values from entry widgets
        student_id = self.student_id_var.get()
        first_name = self.first_name_var.get()
        middle_name = self.middle_name_var.get()
        last_name = self.last_name_var.get()
        major = self.major_var.get()
        return student_id, first_name, middle_name, last_name, major
    
    def add_student(self):
        student_id, first_name, middle_name, last_name, major = self.get_value()
        if self.controller:
            self.controller.insert_student(student_id, last_name, middle_name, first_name, major)
        self.clear_entries()
    
    def update_student(self):
        student_id, first_name, middle_name, last_name, major = self.get_value()

        if self.controller:
            self.controller.update_student(student_id, last_name, middle_name, first_name, major)
        self.clear_entries()
    
    def delete_student(self):
        student_id, _, _, _, _, _ = self.get_value()
        if self.controller:
            self.controller.delete_student(student_id)
        self.clear_entries()
    
    def find_student(self):
        find_by = self.find_by_var.get()
        if self.controller:
            if find_by == 'Major':
                _, _, _, _, major, _ = self.get_value()
                self.controller.find_student(find_by, major)
            else:
                student_id, _, _, _, _, _ = self.get_value()
                self.controller.find_student(find_by, student_id)
        self.clear_entries()

    def sort_students(self):
        sort_by = self.sort_by_var.get()
        if self.controller:
            self.controller.sort_students(sort_by)

    def set_controller(self, controller):
        self.controller = controller

    def clear_entries(self):
        # Clear entry widgets
        self.student_id_var.set(0)
        self.first_name_var.set("")
        self.middle_name_var.set("")
        self.last_name_var.set("")
        self.major_var.set("")
        self.gpa_var.set(0.0)