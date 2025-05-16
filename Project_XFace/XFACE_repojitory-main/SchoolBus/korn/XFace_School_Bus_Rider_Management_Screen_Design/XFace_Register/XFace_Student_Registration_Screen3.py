import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk
import math

class Screen8(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#e6e6e6", width=600, height=500)
        self.pack_propagate(0)

        # Define Values
        name_txt = ""
        school_txt = ""

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Frame Step Frame
        self.step_frame = customtkinter.CTkFrame(self, width=600, height=150, fg_color="#e6e6e6", corner_radius=0)
        self.step_frame.pack()

        # Add "<" Button
        back_btn = customtkinter.CTkButton(master=self.step_frame, width=30, height=30, command= lambda: self.next_screen(7), text="<", text_color="black", font=("Arial", 30), fg_color="transparent", hover=False)
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
        canvas.create_line(125, 55, 450, 55, width=2, fill="#288fc8")

        # Add Circle 1 Border
        canvas.create_aa_circle(125, 55, 43, math.pi/2, fill="#288fc8")
        # Add Circle 1
        canvas.create_aa_circle(125, 55, 40, math.pi/2, fill="#d9d9d9")
        # Add Text 1
        canvas.create_text(125, 55, text="1", fill="black", font=('Arial 25'))
        # Add Text "Name/School Name"
        canvas.create_text(125, 105, text="Name/School Name", fill="black", font=('Arial 10'))

        # Add Circle 2 Border
        canvas.create_aa_circle(305, 55, 43, math.pi/2, fill="#288fc8")
        # Add Circle 2
        canvas.create_aa_circle(305, 55, 40, math.pi/2, fill="#d9d9d9")
        # Add Text 2
        canvas.create_text(305, 55, text="2", fill="black", font=('Arial 25'))
        # Add Text "Face Registration"
        canvas.create_text(305, 105, text="Face Registration", fill="black", font=('Arial 10'))

        # Add Circle 3 Border
        canvas.create_aa_circle(485, 55, 43, math.pi/2, fill="#288fc8")
        # Add Circle 3
        canvas.create_aa_circle(485, 55, 40, math.pi/2, fill="#d9d9d9")
        # Add Text 3
        canvas.create_text(485, 55, text="3", fill="black", font=('Arial 25'))
        # Add Text "Completed"
        canvas.create_text(485, 105, text="Completed", fill="black", font=('Arial 10'))

        #----------------------------------------------------------------------------
        #                                     Frame 2
        #----------------------------------------------------------------------------

        # Add Frame Step Frame 2
        self.step_frame2 = customtkinter.CTkFrame(self, width=600, height=400, fg_color="#e6e6e6", corner_radius=0)
        self.step_frame2.pack()

        canvas2 = customtkinter.CTkCanvas(
            self.step_frame2,
            width = 600,
            height = 400,
            bg = "#e6e6e6",
            highlightthickness = 0,
            bd = 0
        )
        canvas2.place(relx=0.05, rely=0.24)

        # Add Text "description1"
        description1_label = customtkinter.CTkLabel(master=self.step_frame2, text="Register a user with the following information.", font=customtkinter.CTkFont(size=15), text_color="black")
        description1_label.place(x=150, y=40)

        # Add Text "description2"
        description2_label = customtkinter.CTkLabel(master=self.step_frame2, text="If you are satisfied, press Save.", font=customtkinter.CTkFont(size=15), text_color="black")
        description2_label.place(x=200, y=60)

        # Add Text "Name"
        name_label = customtkinter.CTkLabel(master=self.step_frame2, text="Name", font=customtkinter.CTkFont(size=22), text_color="black")
        name_label.place(x=135, y=120)

        # Add Name Line
        canvas2.create_line(230, 56, 480, 56, width=1)

        # Add Name Text
        self.nametxt_label = customtkinter.CTkLabel(master=self.step_frame2, width=250, height=15, text="", font=customtkinter.CTkFont(size=15), text_color="black", justify="center")
        self.nametxt_label.place(x=260, y=120)

        # Add Text "School Name"
        school_label = customtkinter.CTkLabel(master=self.step_frame2, text="School Name", font=customtkinter.CTkFont(size=22), text_color="black")
        school_label.place(x=100, y=170)

        # Add School Name Line
        canvas2.create_line(230, 106, 480, 106, width=1)

        # Add School Text
        self.schooltxt_label = customtkinter.CTkLabel(master=self.step_frame2, width=250, height=15, text="", font=customtkinter.CTkFont(size=15), text_color="black", justify="center")
        self.schooltxt_label.place(x=260, y=170)

        # Add Button "Save"
        btn_next = customtkinter.CTkButton(master=self.step_frame2, command=lambda: self.next_screen(5), width=80, text="Save", font=customtkinter.CTkFont(size=20), text_color="black", corner_radius=15, fg_color="white", border_color="black", border_width=0.5)
        btn_next.place(x=420, y=280)

    def next_screen(self, index):
        self.main_app.show_next_screen(index)

    def get_name(self):
        self.name_txt = self.main_app.get_name()
        self.nametxt_label.configure(text=self.name_txt)

    def get_school(self):
        self.school_txt = self.main_app.get_school()
        self.schooltxt_label.configure(text=self.school_txt)