import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk
import math
import os
from PIL import Image, ImageTk

class Screen11(tk.Frame):
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

        # Add Frame loading Frame
        self.loading_frame = customtkinter.CTkFrame(self, width=600, height=350, fg_color="#e6e6e6", corner_radius=0)
        self.loading_frame.pack()

        # Add Square
        self.loading_square = customtkinter.CTkFrame(master=self.loading_frame,width=500, height=250, fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
        self.loading_square.place(relx=0.08, rely=0.1)

        # Add "Loading USB" label1
        loading_usb_label = customtkinter.CTkLabel(master=self.loading_frame, text="Loading USB ...", font=customtkinter.CTkFont(size=25), text_color="black", justify="center")
        loading_usb_label.place(relx=0.4, rely=0.3)

        # Define Image Source
        current_directory = os.path.dirname(os.path.realpath(__file__))
        images_folder = os.path.join(current_directory, "images")

        loading_path = os.path.join(images_folder, "loading.png")

        # Load and Resize Image
        loading_image = Image.open(loading_path)
        loading_image = loading_image.resize((50, 50), Image.ANTIALIAS)
        loading_photo = ImageTk.PhotoImage(loading_image)

        # Add Image Label
        loading_label = tk.Label(self.loading_frame, image=loading_photo, bg="#e6e6e6")
        loading_label.image = loading_photo  # Keep a reference to avoid garbage collection
        loading_label.place(relx=0.45, rely=0.45)

        # Add Button "Cancel"
        btn_Cancel = customtkinter.CTkButton(master=self.loading_frame, width=80, command= lambda: self.next_screen(9), text="Cancel", font=customtkinter.CTkFont(size=20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=1)
        btn_Cancel.place(relx=0.7, rely=0.65)

    def next_screen(self, index):
        self.main_app.show_next_screen(index)