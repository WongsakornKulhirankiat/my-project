import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk
import math
import os
from PIL import Image, ImageTk

class Face_Recognition_Screen1(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#e6e6e6", width=600, height=500)
        self.pack_propagate(0)

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Frame Step Frame
        self.step_frame = customtkinter.CTkFrame(self, width=600, height=500, fg_color="#e6e6e6", corner_radius=0)
        self.step_frame.pack()

        # Define Image Source
        current_directory = os.path.dirname(os.path.realpath(__file__))
        images_folder = os.path.join(current_directory, "images")

        photo_shoot_confirm_path = os.path.join(images_folder, "photo_shoot_confirm.png")

        # Add Image
        self.photo_shoot_confirm_image = tk.PhotoImage(file=photo_shoot_confirm_path)

        # Add Image Photo Shoot Picture
        self.photo_shoot_confirm_picture = customtkinter.CTkButton(master=self.step_frame, width=500, height=500, text="", image=self.photo_shoot_confirm_image, border_width=0, fg_color="#e6e6e6", border_color="#e6e6e6", bg_color="#e6e6e6", hover_color="#e6e6e6")
        self.photo_shoot_confirm_picture.place(x=110, y=0)

        # Add Button "pass"
        btn_pass = customtkinter.CTkButton(master=self.step_frame, width=80, command= lambda: self.next_screen(1), text="Pass", font=customtkinter.CTkFont(size=20), text_color="black", corner_radius=10, fg_color="white", border_color="white", border_width=1)
        btn_pass.place(relx=0.02, rely=0.9)

    def next_screen(self, index):
        self.main_app.show_next_screen(index)
