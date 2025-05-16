import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk
import math
import os

class Screen7(tk.Frame):
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
        back_btn = customtkinter.CTkButton(master=self.step_frame, width=30, height=30, command= lambda: self.next_screen(6), text="<", text_color="black", font=("Arial", 30), fg_color="transparent", hover=False)
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

        # Add Blue Line
        canvas.create_line(125, 55, 305, 55, width=2, fill="#288fc8")
        # Add Line
        canvas.create_line(306, 55, 450, 55, width=2)

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

        # Add Circle 3
        canvas.create_aa_circle(485, 55, 40, math.pi/2, fill="#d9d9d9")
        # Add Text 3
        canvas.create_text(485, 55, text="3", fill="black", font=('Arial 25'))
        # Add Text "Completed"
        canvas.create_text(485, 105, text="Completed", fill="black", font=('Arial 10'))

        #----------------------------------------------------------------------------
        #                                     Frame 2
        #----------------------------------------------------------------------------

        # Add Frame Image Frame
        self.image_frame = customtkinter.CTkFrame(self, width=600, height=350, fg_color="#e6e6e6", corner_radius=0)
        self.image_frame.pack()

        # Add Description Text 1
        txt1 = "Register the facial information to be used for authentication.\nSelect one of the methods and complete the registration."
        name_label = customtkinter.CTkLabel(master=self.image_frame, text=txt1, font=customtkinter.CTkFont(size=15), text_color="black", justify="center")
        name_label.place(x=100,y=40)

        # Define Image Source
        current_directory = os.path.dirname(os.path.realpath(__file__))
        images_folder = os.path.join(current_directory, "images")

        cam_path = os.path.join(images_folder, "camera.png")
        img_path = os.path.join(images_folder, "image.png")

        # Add Image
        cam_image = tk.PhotoImage(file=cam_path)
        img_image = tk.PhotoImage(file=img_path)

        # Camera Button
        cam_btn = customtkinter.CTkButton(master=self.image_frame, text="", command= lambda: self.next_screen(12), image=cam_image, hover=False, border_width=0, width=150, height=140, fg_color="white")
        cam_btn.place(x=100, y=90)

        # Camera Text
        cam_label = customtkinter.CTkLabel(master=self.image_frame, text="Register with Camera", font=customtkinter.CTkFont(size=15), text_color="black", justify="center")
        cam_label.place(x=106, y=240)

        # Image Button
        img_btn = customtkinter.CTkButton(master=self.image_frame, text="", image=img_image, hover=False, border_width=0, width=150, height=140, fg_color="white")
        img_btn.place(x=350, y=90)

        # Image Text
        cam_label = customtkinter.CTkLabel(master=self.image_frame, text="Register with Photo", font=customtkinter.CTkFont(size=15), text_color="black", justify="center")
        cam_label.place(x=362, y=240)

        # Add Button "Next"
        btn_next = customtkinter.CTkButton(master=self.image_frame, width=80, text="Next", command= lambda: self.next_screen(8), font=customtkinter.CTkFont(size=20), text_color="black", corner_radius=10, fg_color="white", border_color="black", border_width=1)
        btn_next.place(x=440, y=280)

    def next_screen(self, index):
        self.main_app.show_next_screen(index)