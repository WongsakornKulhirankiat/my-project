import tkinter as tk
import customtkinter
import math
import os
from PIL import Image, ImageTk
import XFace_Database_Function
from tkinter import messagebox

class User_Registration_Screen3(tk.Frame):
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
        back_btn = customtkinter.CTkButton(master=self.step_frame, width=30, height=30, command= lambda: self.back_screen(15), text="<", text_color="black", font=("Arial", 30), fg_color="transparent", hover=False)
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

        # Add Circle 3 Border
        canvas.create_aa_circle(485, 45, 43, math.pi/2, fill="#288fc8")
        # Add Circle 3
        canvas.create_aa_circle(485, 45, 40, math.pi/2, fill="#d9d9d9")
        # Add Text 3
        canvas.create_text(485, 45, text="3", fill="black", font=('Arial 25'))
        # Add Text "Completed"
        canvas.create_text(485, 95, text="Completed", fill="black", font=('Arial 10'))

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
        description1_label.place(x=150, y=20)

        # Add Text "description2"
        description2_label = customtkinter.CTkLabel(master=self.step_frame2, text="If you are satisfied, press Save.", font=customtkinter.CTkFont(size=15), text_color="black")
        description2_label.place(x=200, y=40)

        # Define Image Source
        current_directory = os.path.dirname(os.path.realpath(__file__))
        images_folder = os.path.join(current_directory, "images")

        profile_path = os.path.join(images_folder, "profiles.png")

        # Load and Resize Image
        profile_image = Image.open(profile_path)
        profile_image = profile_image.resize((150, 150), Image.ANTIALIAS)
        profile_photo = ImageTk.PhotoImage(profile_image)

        # Add Image Label
        profile_label = tk.Label(self.step_frame2, image=profile_photo, bg="#e6e6e6")
        profile_label.image = profile_photo  # Keep a reference to avoid garbage collection
        profile_label.place(x=410, y=110)

        # Add Text "Name"
        name_label = customtkinter.CTkLabel(master=self.step_frame2, text="Name", font=customtkinter.CTkFont(size=22), text_color="black")
        name_label.place(x=60, y=85)

        # Add Name Line
        canvas2.create_line(150, 20, 360, 20, width=1)

        # Add Name Label
        self.username_txt_label = customtkinter.CTkLabel(master=self.step_frame2, width=240, height=15, text="", font=customtkinter.CTkFont(size=15), text_color="black", justify="center")
        self.username_txt_label.place(x=170, y=85)

        # Add Text "User ID"
        userid_label = customtkinter.CTkLabel(master=self.step_frame2, text="User ID", font=customtkinter.CTkFont(size=22,weight="bold"), text_color="black")
        userid_label.place(x=55, y=130)

        # Add User ID Line
        canvas2.create_line(150, 66, 360, 66, width=1)

        # Add Userid Label
        self.userid_txt_label = customtkinter.CTkLabel(master=self.step_frame2, text="", width=240, height=15, font=customtkinter.CTkFont(size=15), text_color="black", justify="center")
        self.userid_txt_label.place(x=170, y=130)

        # Add Text "Password"
        password_label = customtkinter.CTkLabel(master=self.step_frame2, text="Password", font=customtkinter.CTkFont(size=22,weight="bold"), text_color="black")
        password_label.place(x=45, y=175)

        # Add Pssword Line
        canvas2.create_line(150, 112, 360, 112, width=1)

        # Add Password Label
        self.password_txt_label = customtkinter.CTkLabel(master=self.step_frame2, width=240, height=15, text="", font=customtkinter.CTkFont(size=15), text_color="black", justify="center")
        self.password_txt_label.place(x=170, y=175)

        # Add Text "Department"
        department_label = customtkinter.CTkLabel(master=self.step_frame2, text="Department", font=customtkinter.CTkFont(size=22,weight="bold"), text_color="black")
        department_label.place(x=40, y=220)

        # Add Department Line
        canvas2.create_line(150, 162, 360, 162, width=1)

        # Add department Label
        self.department_txt_label = customtkinter.CTkLabel(master=self.step_frame2, width=240, height=15, text="", font=customtkinter.CTkFont(size=15), text_color="black", justify="center")
        self.department_txt_label.place(x=170, y=220)

        # Add Text "Administrator"
        adminstrator_label = customtkinter.CTkLabel(master=self.step_frame2, text="Administrator", font=customtkinter.CTkFont(size=22,weight="bold"), text_color="black")
        adminstrator_label.place(x=30, y=270)

        # Add Administrator Line
        canvas2.create_line(150, 210, 360, 210, width=1)

        # Add Administrator Label
        self.administrator_check_label = customtkinter.CTkLabel(master=self.step_frame2, width=30, height=30, text="", font=customtkinter.CTkFont(size=30,weight="bold"), text_color="black", justify="center")
        self.administrator_check_label.place(x=275, y=255)

        # Add Button "Save"
        btn_save = customtkinter.CTkButton(master=self.step_frame2, command=lambda: self.save(5), width=80, text="Save", font=customtkinter.CTkFont(size=20), text_color="black", corner_radius=15, fg_color="white", border_color="white", border_width=1)
        btn_save.place(x=450, y=290)

    def save(self, index):
        username = self.username_txt_label.cget('text')
        password = self.password_txt_label.cget('text')
        department = self.department_txt_label.cget('text')
        admin_text = self.administrator_check_label.cget('text')
        if admin_text == 'O':
            is_admin = 1
        elif admin_text == 'X':
            is_admin = 0
        face_photo = ''
        XFace_Database_Function.insert_userinfo(username, password, department, is_admin, face_photo)
        messagebox.showinfo("Update", "Updated successfully!")
        self.main_app.show_next_screen(index)

    def back_screen(self, index):
        self.main_app.show_next_screen(index)

    def get_username(self):
        self.username_txt = self.main_app.get_user_name()
        self.username_txt_label.configure(text=self.username_txt)

    def get_password(self):
        self.password_txt = self.main_app.get_current_password()
        self.password_txt_label.configure(text=self.password_txt)

    def get_department(self):
        self.department_txt = self.main_app.get_department_name()
        self.department_txt_label.configure(text=self.department_txt)

    def get_userid(self):
        self.userid_txt = XFace_Database_Function.fetch_next_user_id()
        self.userid_txt_label.configure(text=self.userid_txt)

    def get_administrator(self):
        self.administrator_check = self.main_app.get_administrator()
        self.administrator_check_label.configure(text=self.administrator_check)