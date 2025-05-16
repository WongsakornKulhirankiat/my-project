import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk
import math
import os

class Screen8(tk.Frame):
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

        # Add Circle 2 Border
        canvas.create_aa_circle(305, 45, 43, math.pi/2, fill="#288fc8")
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

        # Add Frame Error Frame
        self.error_frame = customtkinter.CTkFrame(self, width=600, height=350, fg_color="#e6e6e6", corner_radius=0)
        self.error_frame.pack()

        # Add Square
        self.error_square = customtkinter.CTkFrame(master=self.error_frame,width=500, height=250, fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
        self.error_square.place(relx=0.1, rely=0.1)

        # Add Error label1
        error_label1 = customtkinter.CTkLabel(master=self.error_frame, text="A face was not detected in the image.", font=customtkinter.CTkFont(size=25), text_color="black", justify="center")
        error_label1.place(relx=0.17, rely=0.3)

        # Add Error label2
        error_label2 = customtkinter.CTkLabel(master=self.error_frame, text="Please select the photo again.", font=customtkinter.CTkFont(size=25), text_color="black", justify="center")
        error_label2.place(relx=0.25, rely=0.4)

        # Add Button "OK"
        btn_ok = customtkinter.CTkButton(master=self.error_frame, width=80, command= lambda: self.next_screen(11), text="OK", font=customtkinter.CTkFont(size=20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=1)
        btn_ok.place(relx=0.7, rely=0.65)

    def next_screen(self, index):
        self.main_app.show_next_screen(index)