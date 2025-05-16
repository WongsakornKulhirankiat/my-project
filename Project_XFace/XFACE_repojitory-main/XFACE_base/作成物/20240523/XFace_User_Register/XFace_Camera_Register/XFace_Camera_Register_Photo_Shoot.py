import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk
import math
import os
from PIL import Image, ImageTk

class Screen10(tk.Frame):
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

        # Add "<" Button
        back_btn = customtkinter.CTkButton(master=self.step_frame, command=lambda: self.next_screen(7), width=30, height=30, text="<", text_color="black", font=("Arial", 30), fg_color="transparent", hover=False)
        back_btn.place(relx=0.02, rely=0.02)

        # Add Button Big Camera "Shoot Camera"
        circle_camera_shoot = customtkinter.CTkButton(master=self.step_frame, width=80, height=80, text="", corner_radius=60, fg_color="white", border_color="black", border_width=2, hover_color="white")
        circle_camera_shoot.place(x=25, y=200)

        # Add Button small Camera "Shoot Camera"
        camera_shoot_btn = customtkinter.CTkButton(master=self.step_frame, command=lambda:self.camera_shoot_click(), width=40, height=40, text="", corner_radius=60, fg_color="white", border_color="black", border_width=2, bg_color="white")
        camera_shoot_btn.place(x=45, y=220)

        # Define Image Source
        current_directory = os.path.dirname(os.path.realpath(__file__))
        images_folder = os.path.join(current_directory, "images")

        photo_shoot_path = os.path.join(images_folder, "photo_shoot.png")

        # Add Image
        self.photo_shoot_image = tk.PhotoImage(file=photo_shoot_path)

        # Add Image Photo Shoot Picture
        self.photo_shoot_picture = customtkinter.CTkButton(master=self.step_frame, width=500, height=500, text="", image=self.photo_shoot_image, border_width=0, fg_color="#e6e6e6", border_color="#e6e6e6", bg_color="#e6e6e6", hover_color="#e6e6e6")
        self.photo_shoot_picture.place(x=110, y=0)

        # Initialize retake_button and accept_button
        self.retake_button = None
        self.accept_button = None

        # Call reset_state() when the screen is initialized
        self.reset_state()

    def camera_shoot_click(self):
        if self.photogetableflag:
            photo_shoot_confirm_path = self.main_app.photo_get()
        
            # Load the confirm image
            photo_shoot_confirm_image = tk.PhotoImage(file=photo_shoot_confirm_path)

            # Set the new image to the photo_shoot_picture button
            self.photo_shoot_picture.configure(image=photo_shoot_confirm_image)
            self.photo_shoot_picture.image = photo_shoot_confirm_image  # Keep a reference to avoid garbage collection

            # Create two additional buttons
            self.retake_button = customtkinter.CTkButton(master=self.step_frame, text="Retake", command=lambda: self.retake_click(), font=customtkinter.CTkFont(size=20), text_color="black", width=120, height=60, fg_color="#D9D9D9", bg_color="#ffffff", corner_radius=10)
            self.retake_button.place(x=130, y=425)

            self.accept_button = customtkinter.CTkButton(master=self.step_frame, command=lambda: self.next_screen(7), text="OK", font=customtkinter.CTkFont(size=20), text_color="black", width=120, height=60, fg_color="#D9D9D9", bg_color="#ffffff", corner_radius=10)
            self.accept_button.place(x=470, y=425)

            self.photogetableflag = False

    def retake_click(self):
        self.photogetableflag = True

        # Reload the original photo_shoot.png image
        current_directory = os.path.dirname(os.path.realpath(__file__))
        images_folder = os.path.join(current_directory, "images")
        photo_shoot_path = os.path.join(images_folder, "photo_shoot.png")

        # Add Image
        self.photo_shoot_image = tk.PhotoImage(file=photo_shoot_path)

        # Update the photo_shoot_picture button with the original image
        self.photo_shoot_picture.configure(image=self.photo_shoot_image)
        self.photo_shoot_picture.image = self.photo_shoot_image  # Keep a reference to avoid garbage collection

        # Remove the retake_button and accept_button from the screen
        if self.retake_button:
            self.retake_button.destroy()
        if self.accept_button:
            self.accept_button.destroy()

    def next_screen(self, index):
        self.main_app.show_next_screen(index)

    def reset_state(self):
        # Reload the original photo_shoot.png image
        current_directory = os.path.dirname(os.path.realpath(__file__))
        images_folder = os.path.join(current_directory, "images")
        photo_shoot_path = os.path.join(images_folder, "photo_shoot.png")

        # Add Image
        self.photo_shoot_image = tk.PhotoImage(file=photo_shoot_path)

        # Update the photo_shoot_picture button with the original image
        self.photo_shoot_picture.configure(image=self.photo_shoot_image)
        self.photo_shoot_picture.image = self.photo_shoot_image  # Keep a reference to avoid garbage collection

        # Remove the retake_button and accept_button from the screen
        if self.retake_button:
            self.retake_button.destroy()
        if self.accept_button:
            self.accept_button.destroy()

    def set_photogetableflag(self):
        self.photogetableflag = True
