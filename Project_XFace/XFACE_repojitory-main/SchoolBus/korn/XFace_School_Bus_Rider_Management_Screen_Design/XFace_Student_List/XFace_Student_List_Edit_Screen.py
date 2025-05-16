import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk
import math
import os
from tkinter import PhotoImage
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
        step_frame = customtkinter.CTkFrame(master=self, width=600, height=50, fg_color="#e6e6e6", corner_radius=0)
        step_frame.pack()

        # Add "<" Button
        back_btn = customtkinter.CTkButton(master=step_frame, command= lambda: self.next_screen(9), width=30, height=30, text="<", text_color="black", font=("Arial", 30), fg_color="transparent", hover=False)
        back_btn.place(relx=0.02, rely=0.02)

        # Add Date Label
        date_label = customtkinter.CTkLabel(master=step_frame, text="Edit student information", text_color="black", font=("Arial", 20))
        date_label.place(relx=0.115, rely=0.15)

        #----------------------------------------------------------------------------
        #                                     Frame 2
        #----------------------------------------------------------------------------

        # Add Frame Step Frame 2
        step_frame2 = customtkinter.CTkFrame(master=self, width=600, height=200, fg_color="#e6e6e6", corner_radius=0)
        step_frame2.pack()

        # Define Image Source
        current_directory = os.path.dirname(os.path.realpath(__file__))
        images_folder = os.path.join(current_directory, "images")

        profile_path = os.path.join(images_folder, "profile.png")

        # Load the image
        profile_image_pil = Image.open(profile_path)

        # Resize the image
        new_width = 175  # New width in pixels
        new_height = 175  # New height in pixels
        profile_image_pil_resized = profile_image_pil.resize((new_width, new_height), Image.ANTIALIAS)

        # Convert the resized image to PhotoImage
        profile_image_resized = ImageTk.PhotoImage(profile_image_pil_resized)

        # Add Profile Picture
        cam_btn = customtkinter.CTkButton(master=step_frame2, text="", image=profile_image_resized, hover=False, border_width=0, fg_color="white")
        cam_btn.place(x=60, y=25)

        # Add Text "Name"
        name_label = customtkinter.CTkLabel(master=step_frame2, text="Name", font=customtkinter.CTkFont(size=20), text_color="black")
        name_label.place(x=260, y=25)

        # Add Text Entry for Name
        self.name_entrybox = customtkinter.CTkEntry(master=step_frame2, width=300 , height=32, fg_color="white", border_color="white", text_color="black", font=customtkinter.CTkFont(size=15), corner_radius=10)
        self.name_entrybox.place(x=260, y=60)
        self.name_entrybox.bind("<Button-1>", lambda event: self.show_keyboard(self.name_entrybox))

        # Add Text "School Name"
        schoolname_label = customtkinter.CTkLabel(master=step_frame2, text="School Name", font=customtkinter.CTkFont(size=20), text_color="black")
        schoolname_label.place(x=260, y=100)

        # Add ComboBox for School
        school_entrybox = customtkinter.CTkComboBox(master=step_frame2, text_color="black", values=["","School1","School2","School3"], font=("Arial", 20), width=300, height=32, fg_color="white", dropdown_text_color="black", dropdown_font=("Arial", 20), dropdown_fg_color="white", dropdown_hover_color="white", button_color="white", border_color="white", button_hover_color="white")
        school_entrybox.place(x=260, y=140)

        #----------------------------------------------------------------------------
        #                                     Frame 3
        #----------------------------------------------------------------------------

        # Add Frame Step Frame 3
        step_frame3 = customtkinter.CTkFrame(master=self, width=600, height=250, fg_color="#e6e6e6", corner_radius=0)
        step_frame3.pack()

        # Add Edit Facial information
        edit_facial_label = customtkinter.CTkLabel(master=step_frame3, text="Edit Facial information", text_color="black", font=("Arial", 20))
        edit_facial_label.place(relx=0.098, rely=0)

        # Define Image Source
        current_directory = os.path.dirname(os.path.realpath(__file__))
        images_folder = os.path.join(current_directory, "images")

        cam_path = os.path.join(images_folder, "camera.png")
        img_path = os.path.join(images_folder, "image.png")

        # Add Image
        cam_image = tk.PhotoImage(file=cam_path)
        img_image = tk.PhotoImage(file=img_path)

        # Camera Button
        cam_btn = customtkinter.CTkButton(master=step_frame3, text="", image=cam_image, hover=False, border_width=0, width=150, height=140, fg_color="white")
        cam_btn.place(x=60, y=50)

        # Image Button
        img_btn = customtkinter.CTkButton(master=step_frame3, text="", image=img_image, hover=False, border_width=0, width=150, height=140, fg_color="white")
        img_btn.place(x=260, y=50)

        # Add Button "Next"
        btn_next = customtkinter.CTkButton(master=step_frame3, command= lambda: self.next_screen(9), width=80, text="Save", font=customtkinter.CTkFont(size=20), text_color="black", corner_radius=15, fg_color="white", border_color="white", border_width=1)
        btn_next.place(x=480, y=160)

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
        print("show keyboard")
        entrybox.focus_set()  # Set focus to the clicked entrybox
        self.keyboard_frame.place(relx=0.08, rely=0.65)

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
        self.main_app.show_next_screen(index)
        self.keyboard_frame.place_forget()