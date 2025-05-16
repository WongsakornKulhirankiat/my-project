import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk
import math
import threading
import subprocess

import XFace_Database_Function

class Screen6(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#e6e6e6", width=600, height=500)
        self.pack_propagate(0)

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Frame Step Frame
        self.step_frame = customtkinter.CTkFrame(self, width=600, height=150, fg_color="#e6e6e6", corner_radius=0)
        self.step_frame.pack()

        # Add "<" Button
        back_btn = customtkinter.CTkButton(master=self.step_frame, command= lambda: self.back_screen(), width=30, height=30, text="<", text_color="black", font=("Arial", 30), fg_color="transparent", hover=False)
        back_btn.place(relx=0.02, rely=0.02)

        #--------------------------------------------
        #                   Canvas
        #--------------------------------------------

        # Create Canvas
        canvas = customtkinter.CTkCanvas(
            self.step_frame,
            width = 600,
            height = 150,
            bg = "#e6e6e6",
            highlightthickness = 0,
            bd = 0
        )
        canvas.place(relx=0, rely=0.24)

        # Add Line
        canvas.create_line(125, 45, 450, 45, width=2)

        # Add Circle 1 Border
        canvas.create_aa_circle(125, 45, 43, math.pi/2, fill="#288fc8")
        # Add Circle 1
        canvas.create_aa_circle(125, 45, 40, math.pi/2, fill="#d9d9d9")
        # Add Text 1
        canvas.create_text(125, 45, text="1", fill="black", font=('Arial 25'))
        # Add Text "Username/Password/"
        canvas.create_text(125, 95, text="Username/Password/", fill="black", font=('Arial 10'))
        # Add Text "Department"
        canvas.create_text(125, 107, text="Department", fill="black", font=('Arial 10'))

        # Add Circle 2
        canvas.create_aa_circle(305, 45, 40, math.pi/2, fill="#d9d9d9")
        # Add Text 2
        canvas.create_text(305, 45, text="2", fill="black", font=('Arial 25'))
        # Add Text "Face Registration"
        canvas.create_text(305, 95, text="Face Registration", fill="black", font=('Arial 10'))

        # Add Circle 3
        canvas.create_aa_circle(485, 45, 40, math.pi/2, fill="#d9d9d9")
        # Add Text 3
        canvas.create_text(485, 45, text="3", fill="black", font=('Arial 25'))
        # Add Text "Completed"
        canvas.create_text(485, 95, text="Completed", fill="black", font=('Arial 10'))

        #----------------------------------------------------------------------------
        #                                     Frame 2
        #----------------------------------------------------------------------------

        # Add Frame Name Frame
        self.name_frame = customtkinter.CTkFrame(self, width=600, height=350, fg_color="#e6e6e6", corner_radius=0)
        self.name_frame.pack()

        # Add Text "Username"
        username_label = customtkinter.CTkLabel(master=self.name_frame, text="User Name", font=customtkinter.CTkFont(size=20), text_color="black")
        username_label.place(x=90, y=20)

        # Add Text Box for Name
        self.username_entrybox = customtkinter.CTkEntry(master=self.name_frame, width=440 , height=40, fg_color="white", border_color="white", border_width=1, text_color="black", font=customtkinter.CTkFont(size=20,weight="bold"), corner_radius=10)
        self.username_entrybox.place(x=80, y=55)
        self.username_entrybox.bind("<Button-1>", lambda event: self.show_keyboard(self.username_entrybox))

        # Add Text "Password"
        password_label = customtkinter.CTkLabel(master=self.name_frame, text="Password", font=customtkinter.CTkFont(size=20), text_color="black")
        password_label.place(x=90, y=100)

        # Add Text Box for Password
        self.password_entrybox= customtkinter.CTkEntry(master=self.name_frame, width=200 , height=40, fg_color="white", border_color="white", border_width=1, text_color="black", font=customtkinter.CTkFont(size=20,weight="bold"), corner_radius=10)
        self.password_entrybox.place(x=80, y=135)
        self.password_entrybox.bind("<Button-1>", lambda event: self.show_keyboard(self.password_entrybox))

        # Add Text "Administrator"
        administrator_label = customtkinter.CTkLabel(master=self.name_frame, text="Administrator", font=customtkinter.CTkFont(size=20), text_color="black")
        administrator_label.place(x=300, y=100)

        def checkbox_event():
            print("checkbox toggled, current value:", check_var.get())

        check_var = tkinter.StringVar(value="on")

        self.administrator_checkbox = customtkinter.CTkCheckBox(
            master=self.name_frame,
            text="",
            width=40,
            height=40, 
            checkbox_width=40, 
            checkbox_height=40,  
            command=checkbox_event,
            variable=check_var, 
            onvalue="O", 
            offvalue="X",
            border_color="white",
            bg_color="white",
            fg_color="white",
            corner_radius=10,
            checkmark_color="black",
            hover_color="white",
        )

        self.administrator_checkbox.place(x=335, y=135)

        # Add Text "Department"
        department_label = customtkinter.CTkLabel(master=self.name_frame, text="Department", font=customtkinter.CTkFont(size=20), text_color="black")
        department_label.place(x=90, y=180)

        # Add ComboBox for Department
        self.department_entrybox = customtkinter.CTkEntry(master=self.name_frame, width=440 , height=30, fg_color="white", border_color="white", border_width=1, text_color="black", font=customtkinter.CTkFont(size=20,weight="bold"), corner_radius=10)
        self.department_entrybox.place(x=80, y=215)
        self.department_button = customtkinter.CTkButton(master=self.name_frame, text="▼", command=self.show_department_menus, text_color="black", font=("Arial",15), fg_color="white", width=35, height=30)
        self.department_button.place(x=485, y=215)

        # Add Button "Next"
        btn_next = customtkinter.CTkButton(master=self.name_frame, width=80, command= lambda: self.next_screen(7), text="Next", font=customtkinter.CTkFont(size=20), text_color="black", corner_radius=10, fg_color="white", border_color="white", border_width=1)
        btn_next.place(x=440, y=280)

        # Create the virtual keyboard
        #self.create_virtual_keyboard()

        # Initialize department Frame with Listbox and Scrollbar
        self.department_frame = tk.Frame(self, bg="#424242")
        self.department_listbox = tk.Listbox(self.department_frame, font=("Arial", 15), width=38, height=3)
        department_names = XFace_Database_Function.fetch_departmentname()
        for department in department_names:
            self.department_listbox.insert("end", department)
        self.department_listbox.bind("<Double-Button-1>", self.select_department)
        self.department_scrollbar = tk.Scrollbar(self.department_frame, orient="vertical", command=self.department_listbox.yview)
        self.department_listbox.config(yscrollcommand=self.department_scrollbar.set)
    
    
    
    def create_virtual_keyboard(self):
        # Create a frame to hold the keyboard buttons
        self.keyboard_frame = tk.Frame(self.master, bg="grey")  # Set background color to grey

        # Define keyboard layout
        keys = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'],
            ['Delete', 'End']  # Add "Delete" button and "End" button to close the keyboard
        ]

        # Create keyboard buttons
        for i, row in enumerate(keys):
            for j, key in enumerate(row):
                # Create button for each key
                btn = tk.Button(self.keyboard_frame, text=key, width=5, height=1, font=("Helvetica", 9, "bold"),
                                command=lambda char=key: self.on_key_press(char))  # Set font to bold
                btn.grid(row=i, column=j, padx=3, pady=3)

        # Pack the keyboard frame initially hidden
        self.keyboard_frame.pack_forget()


    # Modify show_keyboard method to accept an entrybox parameter
    def show_keyboard(self, entrybox):
        entrybox.focus_set()  # Set focus to the clicked entrybox
        self.keyboard_frame.place(relx=0.08, rely=0.08)

    # Modify on_key_press method to properly handle the Delete and End keys
    def on_key_press(self, char):

        # Get the widget that currently has focus
        target_entry = self.focus_get()
        
        if char == "End":
            self.keyboard_frame.place_forget()
        elif char == "Delete":
            target_entry.delete(len(target_entry.get()) - 1)
        else:
            target_entry.insert(tk.END, char)

    def clear_entry_boxes_and_checkbox(self):
        self.username_entrybox.delete(0, tk.END)
        self.password_entrybox.delete(0, tk.END)
        self.department_entrybox.delete(0, tk.END)
        self.administrator_checkbox.deselect()

    def next_screen(self, index):
        self.main_app.set_username(self.username_entrybox.get())
        self.main_app.set_password(self.password_entrybox.get())
        self.main_app.set_department(self.department_entrybox.get())
        self.main_app.set_administrator(self.administrator_checkbox.get())
        self.main_app.show_next_screen(index)
        self.clear_entry_boxes_and_checkbox()

    def back_screen(self):
        loginuseradminflag = self.main_app.get_loginuseradminflag()
        
        if loginuseradminflag:
            self.main_app.show_next_screen(4)
        else:
            self.main_app.show_next_screen(5)

    def select_department(self, event):
        selected_department = self.department_listbox.get(tk.ACTIVE)
        self.department_entrybox.delete(0, tk.END)
        self.department_entrybox.insert(0, selected_department)
        self.show_department_menus()

    def show_department_menus(self):
        if not self.department_frame.winfo_ismapped():
            self.department_listbox.delete(0, 'end')
            department_names = XFace_Database_Function.fetch_departmentname()
            for department in department_names:
                self.department_listbox.insert("end", department)
            self.department_frame.place(x=80, y=392)
            self.department_listbox.pack(side="left")
            self.department_scrollbar.pack(side="right", fill="y")
        else:
            self.department_frame.place_forget()