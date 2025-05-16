import tkinter as tk
from tkinter import messagebox
import customtkinter
import numpy as np
from XFace_textfile import Department_Registration_textdir
import XFace_Database_Function

class Department_Registration_Screen3(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#424242", width=600, height=500)
        self.pack_propagate(0)

        # Password
        self.password = ""
        self.current_password = ""
        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Frame for all elements
        self.menu_frame = customtkinter.CTkFrame(self, width=600, height=500, fg_color="#424242", corner_radius=0)
        self.menu_frame.place(x=0)

        # Back Button
        back_btn = customtkinter.CTkButton(self.menu_frame, text="<", command=lambda: self.back_screen(6), width=30, height=30, text_color="white", font=("Arial", 30), fg_color="transparent")
        back_btn.place(relx=0.02, rely=0.02)

        # Title for the Department Registration section
        title_label = customtkinter.CTkLabel(self.menu_frame, text=Department_Registration_textdir[1], font=("Arial", 24), text_color="white", fg_color="transparent")
        title_label.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

        # Department Name Entry
        department_name_label = customtkinter.CTkLabel(self.menu_frame, text=Department_Registration_textdir[2], font=("Arial", 20), text_color="white", fg_color="transparent")
        department_name_label.place(relx=0.1, rely=0.2)
        self.department_name_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20),  width=400, height=35)
        self.department_name_entry.place(relx=0.1, rely=0.25)

        # Starting Work Time Entry
        starting_time_label = customtkinter.CTkLabel(self.menu_frame, text=Department_Registration_textdir[3], font=("Arial", 20), text_color="white", fg_color="transparent")
        starting_time_label.place(relx=0.1, rely=0.35)
        self.start_time_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20), width=150, height=35)
        self.start_time_entry.place(relx=0.1, rely=0.4)
        self.start_time_menu_button = customtkinter.CTkButton(self.menu_frame, text="▼", command=self.show_start_time_menu, text_color="black", font=("Arial", 20), fg_color="white", width=30, height=35)
        self.start_time_menu_button.place(relx=0.3, rely=0.4)

        # Ending Work Time Entry
        ending_time_label = customtkinter.CTkLabel(self.menu_frame, text=Department_Registration_textdir[4], font=("Arial", 20), text_color="white", fg_color="transparent")
        ending_time_label.place(relx=0.5, rely=0.35)
        self.end_time_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20), width=150, height=35)
        self.end_time_entry.place(relx=0.5, rely=0.4)
        self.end_time_menu_button = customtkinter.CTkButton(self.menu_frame, text="▼", command=self.show_end_time_menu, text_color="black", font=("Arial", 20), fg_color="white", width=30, height=35)
        self.end_time_menu_button.place(relx=0.7, rely=0.4)

        # Rest Time Entry
        rest_time_label = customtkinter.CTkLabel(self.menu_frame, text=Department_Registration_textdir[5], font=("Arial", 20), text_color="white", fg_color="transparent")
        rest_time_label.place(relx=0.1, rely=0.6)
        self.rest_time_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20), width=150, height=35)
        self.rest_time_entry.place(relx=0.1, rely=0.65)
        self.rest_time_menu_button = customtkinter.CTkButton(self.menu_frame, text="▼", command=self.show_rest_time_menu, text_color="black", font=("Arial", 20), fg_color="white", width=30, height=35)
        self.rest_time_menu_button.place(relx=0.3, rely=0.65)

        # Over Time Entry
        over_time_label = customtkinter.CTkLabel(self.menu_frame, text=Department_Registration_textdir[6], font=("Arial", 20), text_color="white", fg_color="transparent")
        over_time_label.place(relx=0.5, rely=0.6)
        self.over_time_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20), width=150, height=35)
        self.over_time_entry.place(relx=0.5, rely=0.65)
        self.over_time_menu_button = customtkinter.CTkButton(self.menu_frame, text="▼", command=self.show_over_time_menu, text_color="black", font=("Arial", 20), fg_color="white", width=30, height=35)
        self.over_time_menu_button.place(relx=0.7, rely=0.65)

        # Save Button
        save_btn = customtkinter.CTkButton(self.menu_frame, text=Department_Registration_textdir[10], command=lambda: self.save_data(5), text_color="black", font=("Arial", 20, "bold"), fg_color="white", width=90, height=50, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        save_btn.place(relx=0.75, rely=0.85)

        # Initialize Start Time Frame with Listbox and Scrollbar
        self.start_time_frame = tk.Frame(self, bg="#424242")
        self.start_time_listbox = tk.Listbox(self.start_time_frame, font=("Arial", 15), width=12, height=2)
        for hour in range(24):
            for minute in (0, 30):
                self.start_time_listbox.insert("end", f"{hour:02d}:{minute:02d}")
        self.start_time_listbox.bind("<Double-Button-1>", self.select_start_time)
        self.start_time_scrollbar = tk.Scrollbar(self.start_time_frame, orient="vertical", command=self.start_time_listbox.yview)
        self.start_time_listbox.config(yscrollcommand=self.start_time_scrollbar.set)

        # Initialize End Time Frame with Listbox and Scrollbar
        self.end_time_frame = tk.Frame(self, bg="#424242")
        self.end_time_listbox = tk.Listbox(self.end_time_frame, font=("Arial", 15), width=12, height=2)
        for hour in range(24):
            for minute in (0, 30):
                self.end_time_listbox.insert("end", f"{hour:02d}:{minute:02d}")
        self.end_time_listbox.bind("<Double-Button-1>", self.select_end_time)
        self.end_time_scrollbar = tk.Scrollbar(self.end_time_frame, orient="vertical", command=self.end_time_listbox.yview)
        self.end_time_listbox.config(yscrollcommand=self.end_time_scrollbar.set)

        # Initialize Rest Time Frame with Listbox and Scrollbar
        self.rest_time_frame = tk.Frame(self, bg="#424242")
        self.rest_time_listbox = tk.Listbox(self.rest_time_frame, font=("Arial", 15), width=12, height=2)
        for i in np.arange(0.5, 5.25, 0.25):
            self.rest_time_listbox.insert("end", f"{i:.02f}")
        self.rest_time_listbox.bind("<Double-Button-1>", self.select_rest_time)
        self.rest_time_scrollbar = tk.Scrollbar(self.rest_time_frame, orient="vertical", command=self.rest_time_listbox.yview)
        self.rest_time_listbox.config(yscrollcommand=self.rest_time_scrollbar.set)

        # Initialize Over Time Frame with Listbox and Scrollbar
        self.over_time_frame = tk.Frame(self, bg="#424242")
        self.over_time_listbox = tk.Listbox(self.over_time_frame, font=("Arial", 15), width=12, height=2)
        for i in np.arange(0, 310, 10):
            self.over_time_listbox.insert("end", f"{i}")
        self.over_time_listbox.bind("<Double-Button-1>", self.select_over_time)
        self.over_time_scrollbar = tk.Scrollbar(self.over_time_frame, orient="vertical", command=self.over_time_listbox.yview)
        self.over_time_listbox.config(yscrollcommand=self.over_time_scrollbar.set)

    def back_screen(self, index):
        self.main_app.show_next_screen(index)

    def select_start_time(self, event):
        selected_time = self.start_time_listbox.get(tk.ACTIVE)
        self.start_time_entry.delete(0, tk.END)
        self.start_time_entry.insert(0, selected_time)
        self.start_time_frame.place_forget()

    def select_end_time(self, event):
        selected_time = self.end_time_listbox.get(tk.ACTIVE)
        self.end_time_entry.delete(0, tk.END)
        self.end_time_entry.insert(0, selected_time)
        self.end_time_frame.place_forget()

    def select_rest_time(self, event):
        selected_time = self.rest_time_listbox.get(tk.ACTIVE)
        self.rest_time_entry.delete(0, tk.END)
        self.rest_time_entry.insert(0, selected_time)
        self.rest_time_frame.place_forget()

    def select_over_time(self, event):
        selected_time = self.over_time_listbox.get(tk.ACTIVE)
        self.over_time_entry.delete(0, tk.END)
        self.over_time_entry.insert(0, selected_time)
        self.over_time_frame.place_forget()

    def show_start_time_menu(self):
        if not self.start_time_frame.winfo_ismapped():
            self.start_time_frame.place(relx=0.1, rely=0.463)
            self.start_time_listbox.pack(side="left")
            self.start_time_scrollbar.pack(side="right", fill="y")
        else:
            self.start_time_frame.place_forget()

    def show_end_time_menu(self):
        if not self.end_time_frame.winfo_ismapped():
            self.end_time_frame.place(relx=0.5, rely=0.463)
            self.end_time_listbox.pack(side="left")
            self.end_time_scrollbar.pack(side="right", fill="y")
        else:
            self.end_time_frame.place_forget()

    def show_rest_time_menu(self):
        if not self.rest_time_frame.winfo_ismapped():
            self.rest_time_frame.place(relx=0.1, rely=0.713)
            self.rest_time_listbox.pack(side="left")
            self.rest_time_scrollbar.pack(side="right", fill="y")
        else:
            self.rest_time_frame.place_forget()

    def show_over_time_menu(self):
        if not self.over_time_frame.winfo_ismapped():
            self.over_time_frame.place(relx=0.5, rely=0.713)            
            self.over_time_listbox.pack(side="left")
            self.over_time_scrollbar.pack(side="right", fill="y")
        else:
            self.over_time_frame.place_forget()

    def back_screen(self, index):
        self.main_app.show_next_screen(index)

    def save_data(self, index):
        department_name = self.department_name_entry.get()
        start_time = self.start_time_entry.get()
        end_time = self.end_time_entry.get()
        rest_time = self.rest_time_entry.get()
        over_time = self.over_time_entry.get()
        XFace_Database_Function.update_department(department_name, start_time, end_time, rest_time, over_time)
        messagebox.showinfo("Operation Success", "Department updated successfully.")

        self.main_app.show_next_screen(index)


    def get_department_name(self):
        self.department_name_txt = self.main_app.get_department_name()
        self.department_name_entry.delete(0, tk.END) 
        self.department_name_entry.insert(0, self.department_name_txt)

    def get_start_time(self):
        self.start_time_txt = self.main_app.get_start_time()
        self.start_time_entry.delete(0, tk.END)
        self.start_time_entry.insert(0, self.start_time_txt)

    def get_end_time(self):
        self.end_time_txt = self.main_app.get_end_time()
        self.end_time_entry.delete(0, tk.END)
        self.end_time_entry.insert(0, self.end_time_txt)

    def get_rest_time(self):
        self.rest_time_txt = self.main_app.get_rest_time()
        self.rest_time_entry.delete(0, tk.END)
        self.rest_time_entry.insert(0, self.rest_time_txt)

    def get_over_time(self):
        self.over_time_txt = self.main_app.get_over_time()
        self.over_time_entry.delete(0, tk.END)
        self.over_time_entry.insert(0, self.over_time_txt)
