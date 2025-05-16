import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk
import math
import threading
import subprocess

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
        back_btn = customtkinter.CTkButton(master=self.step_frame, command= lambda: self.next_screen(5), width=30, height=30, text="<", text_color="black", font=("Arial", 30), fg_color="transparent", hover=False)
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
        canvas.create_line(125, 55, 450, 55, width=2)

        # Add Circle 1 Border
        canvas.create_aa_circle(125, 55, 43, math.pi/2, fill="#288fc8")
        # Add Circle 1
        canvas.create_aa_circle(125, 55, 40, math.pi/2, fill="#d9d9d9")
        # Add Text 1
        canvas.create_text(125, 55, text="1", fill="black", font=('Arial 25'))
        # Add Text "Name/School Name"
        canvas.create_text(125, 105, text="Name/School Name", fill="black", font=('Arial 10'))

        # Add Circle 2
        canvas.create_aa_circle(305, 55, 40, math.pi/2, fill="#d9d9d9")
        # Add Text 2
        canvas.create_text(305, 55, text="2", fill="black", font=('Arial 25'))
        # Add Text "Face Registration"
        canvas.create_text(305, 105, text="Face Registration", fill="black", font=('Arial 10'))

        # Add Circle 3
        canvas.create_aa_circle(485, 55, 40, math.pi/2, fill="#d9d9d9")
        # Add Text 3
        canvas.create_text(485, 55, text="3", fill="black", font=('Arial 25'))
        # Add Text "Completed"
        canvas.create_text(485, 105, text="Completed", fill="black", font=('Arial 10'))

        #----------------------------------------------------------------------------
        #                                     Frame 2
        #----------------------------------------------------------------------------

        # Add Frame Name Frame
        self.name_frame = customtkinter.CTkFrame(self, width=600, height=350, fg_color="#e6e6e6", corner_radius=0)
        self.name_frame.pack()

        # Add Text "Name"
        name_label = customtkinter.CTkLabel(master=self.name_frame, text="Name", font=customtkinter.CTkFont(size=20), text_color="black")
        name_label.place(x=90, y=50)

        # Add Text Box for Name
        self.name_entrybox = customtkinter.CTkEntry(master=self.name_frame, width=440 , height=40, fg_color="white", border_color="black", border_width=1, text_color="black", font=customtkinter.CTkFont(size=15), corner_radius=10)
        self.name_entrybox.place(x=80, y=85)
        self.name_entrybox.bind("<Button-1>", lambda event: self.show_keyboard(self.name_entrybox))

        # Add Text "School Name"
        schoolname_label = customtkinter.CTkLabel(master=self.name_frame, text="School Name", font=customtkinter.CTkFont(size=20), text_color="black")
        schoolname_label.place(x=90, y=150)

        # Add Text Box for School
        self.school_entrybox= customtkinter.CTkEntry(master=self.name_frame, width=440 , height=40, fg_color="white", border_color="black", border_width=1, text_color="black", font=customtkinter.CTkFont(size=15), corner_radius=10)
        self.school_entrybox.place(x=80, y=185)
        self.school_entrybox.bind("<Button-1>", lambda event: self.show_keyboard(self.school_entrybox))

        # Add Button "Next"
        btn_next = customtkinter.CTkButton(master=self.name_frame, width=80, command= lambda: self.next_screen(7), text="Next", font=customtkinter.CTkFont(size=20), text_color="black", corner_radius=10, fg_color="white", border_color="black", border_width=1)
        btn_next.place(x=440, y=280)

        # Create the virtual keyboard
        self.create_virtual_keyboard()

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


    def next_screen(self, index):
        self.main_app.set_name(self.name_entrybox.get())
        self.main_app.set_school(self.school_entrybox.get())
        self.main_app.show_next_screen(index)
        self.keyboard_frame.place_forget()