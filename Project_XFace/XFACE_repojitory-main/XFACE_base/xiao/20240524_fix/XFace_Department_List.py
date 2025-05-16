import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk
import math
import os
from tkinter import PhotoImage
from PIL import Image, ImageTk

import XFace_Database_Function

class Screen15(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#424242", width=600, height=500)
        self.pack_propagate(0)

        # Toggle Confirm
        self.confirm = 0

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Name Frame
        self.name_frame = customtkinter.CTkFrame(master=self, width=290, height=500, fg_color="#e6e6e6", corner_radius=0)
        self.name_frame.place(x=0)

        # Add "<" Button
        back_btn = customtkinter.CTkButton(master=self.name_frame, command= lambda: self.back_screen2(), width=30, height=30, text="<", text_color="black", font=("Arial", 30), fg_color="transparent", hover=False)
        back_btn.place(relx=0.02, rely=0.02)

        # create Button
        create_btn = customtkinter.CTkButton(master=self.name_frame,  command= lambda: self.back_screen(16), text="Create", text_color="black", hover_color="lightgray", font=("Arial", 20), border_width=0, width=200, height=30, fg_color="white", corner_radius=15)
        create_btn.place(relx=0.2, rely=0.05)

        # Add School Name Label
        department_label = customtkinter.CTkLabel(master=self.name_frame, text="Department", text_color="black", font=("Arial", 20), fg_color="transparent")
        department_label.place(relx=0.2, rely=0.12)

        #Add Entrybox for Department
        self.department_entrybox = customtkinter.CTkEntry(master=self.name_frame, width=200 , height=30, fg_color="white", border_color="white", text_color="black", font=customtkinter.CTkFont(size=15), corner_radius=10)
        self.department_entrybox.place(relx=0.2, rely=0.17)
        self.department_button = customtkinter.CTkButton(master=self.name_frame, text="▼", command=self.show_department_menus, text_color="black", font=("Arial",15), fg_color="white", width=35, height=30)
        self.department_button.place(relx=0.78, rely=0.17)        

        # Define Image Source
        current_directory = os.path.dirname(os.path.realpath(__file__))
        images_folder = os.path.join(current_directory, "images")

        search_path = os.path.join(images_folder, "search.png")

        # Add Image
        search_image = tk.PhotoImage(file=search_path)

        # Search Button
        self.search_btn = customtkinter.CTkButton(master=self.name_frame, command=self.search, image=search_image, text="Search", text_color="black", hover_color="lightgray", font=("Arial", 20), border_width=0, width=110, height=30, fg_color="white")
        self.search_btn.place(relx=0.51, rely=0.27)

        # Initialize department Frame with Listbox and Scrollbar
        self.department_frame = tk.Frame(self, bg="#424242")
        self.department_listbox = tk.Listbox(self.department_frame, font=("Arial", 15), width=16, height=3)
        self.department_listbox.insert("end", "All")
        department_names = XFace_Database_Function.fetch_departmentname()
        for department in department_names:
            self.department_listbox.insert("end", department)
        self.department_listbox.bind("<Double-Button-1>", self.select_department)
        self.department_scrollbar = tk.Scrollbar(self.department_frame, orient="vertical", command=self.department_listbox.yview)
        self.department_listbox.config(yscrollcommand=self.department_scrollbar.set)

        #----------------------------------------------------------------------------
        #                                     Frame 2
        #----------------------------------------------------------------------------

        self.info_frame = customtkinter.CTkScrollableFrame(master=self, width=298, height=500, fg_color="#d9d9d9", corner_radius=0)
        self.info_frame.place(x=290)

        self.user_details = XFace_Database_Function.fetch_departmentname() 
        self.build_user_frames(self.user_details)

    def build_user_frames(self, users):
        self.clear_user_frames()
        if len(users) == 1:
            self.add_user_frame(self.info_frame, users, 1)
        else:
            for index, user in enumerate(users):
                self.add_user_frame(self.info_frame, user, index)

    def clear_user_frames(self):
        for widget in self.info_frame.winfo_children():
            widget.destroy()

    def search(self):
        departmentname = self.department_entrybox.get()
        if departmentname == '' or departmentname == 'All':  ###xiao_fix 20240523 + departmentname == '' 
            users = XFace_Database_Function.fetch_departmentname()
        else:
            users = XFace_Database_Function.fetch_departmentname_by_departmentname(departmentname)
        self.build_user_frames(users)

    def add_user_frame(self, parent_frame, user_name, tag):
        student_frame = customtkinter.CTkFrame(master=parent_frame, width=250, height=70, fg_color="white", corner_radius=10, border_width=0, border_color="#5cb6f8")
        student_frame.bind('<Button-1>', lambda event: self.toggle_border(student_frame))
        student_frame.tag = tag
        student_frame.pack(padx=10, pady=5)

        canvas = customtkinter.CTkCanvas(
            student_frame,
            width=7,
            height=65,
            bg="#fce467",  # Example background color
            highlightthickness=0,
            bd=0
        )
        canvas.bind('<Button-1>', lambda event: self.toggle_border(student_frame))
        canvas.place(x=15, y=2)

        name_label = customtkinter.CTkLabel(master=student_frame, text=user_name, text_color="black", font=("Arial", 20), fg_color="transparent")
        name_label.bind('<Button-1>', lambda event: self.toggle_border(student_frame))
        name_label.place(x=50, y=10)

    def toggle_border(self, frame):
        if frame._border_width == 0:
            for child in frame.master.winfo_children():
                if isinstance(child, customtkinter.CTkFrame):
                    child.configure(border_width=0)
            frame.configure(border_width=2)
            color = frame.winfo_children()[0].cget("bg")
            name = frame.winfo_children()[1].cget("text")
            index = frame.tag
            self.toggle_detail_frame(1, a=color, b=name, c=index)
        else:
            frame.configure(border_width=0)
            self.toggle_detail_frame(0)

    def toggle_detail_frame(self, toggle, *args, **kwargs):
        if toggle == 1:
            if hasattr(self, 'detail_frame') and self.detail_frame.winfo_exists():
                self.detail_frame.destroy()

            detail_frame = customtkinter.CTkFrame(master=self.name_frame, width=260, height=310, fg_color="white", corner_radius=10, border_width=0)
            detail_frame.place(relx=0.05, rely=0.36)
            name = kwargs.get('b', "")
            
            username_detail_label = customtkinter.CTkLabel(master=detail_frame, justify="center", width=260, text=name, text_color="black", font=("Arial", 25), fg_color="transparent")
            username_detail_label.place(relx=0, rely=0.6)

            edit_btn = customtkinter.CTkButton(master=detail_frame, command=lambda: self.next_screen(name, 17), text="Edit", text_color="black", hover_color="lightgray", font=("Arial", 20), border_width=0, width=90, height=30, fg_color="#d9d9d9")
            edit_btn.place(relx=0.1, rely=0.85)

            delete_btn = customtkinter.CTkButton(master=detail_frame, command=lambda: self.confirm_delete(name), text="Delete", text_color="black", hover_color="lightgray", font=("Arial", 20), border_width=0, width=90, height=30, fg_color="#d9d9d9")
            delete_btn.place(relx=0.55, rely=0.85)

            self.detail_frame = detail_frame
        else:
            if hasattr(self, 'detail_frame') and self.detail_frame.winfo_exists():
                self.detail_frame.destroy()

    def confirm_delete(self, name):
        if self.confirm == 0:
            self.confirm = 1
            self.confirm_frame = customtkinter.CTkFrame(master=self, width=300, height=180, fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
            self.confirm_frame.place(x=150, y=150)
            confirm_label = customtkinter.CTkLabel(master=self.confirm_frame, justify="center", width=300, text="Delete this data.", text_color="black", font=("Arial", 25), fg_color="transparent")
            confirm_label.place(relx=0, rely=0.2)
            ok_btn = customtkinter.CTkButton(self.confirm_frame, command=lambda: self.ok_frame(name), text="OK", text_color="black", hover_color="lightgray", font=("Arial", 20), border_width=0, width=90, height=30, fg_color="white")
            ok_btn.place(x=30, y=130)
            cancel_btn = customtkinter.CTkButton(self.confirm_frame, command=self.close_frame, text="Cancel", text_color="black", hover_color="lightgray", font=("Arial", 20), border_width=0, width=90, height=30, fg_color="white")
            cancel_btn.place(x=180, y=130)

    def close_frame(self):
        self.confirm = 0
        self.confirm_frame.destroy()

    def ok_frame(self, name):
        self.confirm = 0
        if isinstance(name, list):
            name = name[0]
        XFace_Database_Function.delete_department(name)
        self.toggle_detail_frame(0)
        users= XFace_Database_Function.fetch_departmentname() 
        self.build_user_frames(users)
        self.confirm_frame.destroy()

    def next_screen(self, name, index):
        if isinstance(name, list):
            name = name[0]
        department_info = XFace_Database_Function.fetch_department(name)
        self.main_app.set_department_name(department_info[0])
        self.main_app.set_start_time(department_info[1])
        self.main_app.set_end_time(department_info[2])
        self.main_app.set_rest_time(department_info[3])
        self.main_app.set_over_time(department_info[4])
        self.department_entrybox.delete(0, tk.END)
        self.main_app.show_next_screen(index)

    def back_screen(self, index):
        self.main_app.show_next_screen(index)
        self.department_entrybox.delete(0, tk.END)

    def back_screen2(self):
        self.department_entrybox.delete(0, tk.END)
        loginuseradminflag = self.main_app.get_loginuseradminflag()
        
        if loginuseradminflag:
            self.main_app.show_next_screen(4)
        else:
            self.main_app.show_next_screen(5)

    def select_department(self, event):
        self.selected_department = self.department_listbox.get(tk.ACTIVE)
        self.department_entrybox.delete(0, tk.END)
        self.department_entrybox.insert(0, self.selected_department)
        self.show_department_menus()

    def show_department_menus(self):
        if not self.department_frame.winfo_ismapped():
            self.department_listbox.delete(0, 'end')
            department_names = XFace_Database_Function.fetch_departmentname()
            self.department_listbox.insert("end", "All")
            for department in department_names:
                self.department_listbox.insert("end", department)  ###xiao_fix 20240523 department list reset
            self.department_frame.place(relx=0.1, rely=0.23)
            self.department_listbox.pack(side="left")
            self.department_scrollbar.pack(side="right", fill="y")
        else:
            self.department_frame.place_forget()