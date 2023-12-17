import tkinter as tk
from tkinter import ttk

class AIPage:
    def display_courses_page(self):
        new_window = tk.Toplevel()
        new_window.title("AI Controller Page")
        label = ttk.Label(new_window, text="This is the AI Controller Page")
        label.pack(padx=10, pady=10)