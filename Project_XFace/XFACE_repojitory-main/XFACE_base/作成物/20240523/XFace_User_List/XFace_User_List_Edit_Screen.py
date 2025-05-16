import tkinter as tk
import customtkinter
import os
from tkinter import messagebox
from PIL import Image, ImageTk
import XFace_Database_Function

class Screen14(tk.Frame):
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
        back_btn = customtkinter.CTkButton(master=step_frame, command= lambda: self.next_screen(13), width=30, height=30, text="<", text_color="black", font=("Arial", 30), fg_color="transparent", hover=False)
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
        new_width = 125 # New width in pixels
        new_height = 125  # New height in pixels
        profile_image_pil_resized = profile_image_pil.resize((new_width, new_height), Image.ANTIALIAS)

        # Convert the resized image to PhotoImage
        profile_image_resized = ImageTk.PhotoImage(profile_image_pil_resized)

        # Add Profile Picture
        profile_picture = customtkinter.CTkButton(master=step_frame2, text="", image=profile_image_resized, hover=False, border_width=0, fg_color="white")
        profile_picture.place(x=60, y=25)

        # Add Text "User Name"
        name_label = customtkinter.CTkLabel(master=step_frame2, text="User Name", font=customtkinter.CTkFont(size=20), text_color="black")
        name_label.place(x=270, y=0)

        # Add Text Entry for User Name
        self.username_entrybox = customtkinter.CTkEntry(master=step_frame2, width=300 , height=32, fg_color="white", border_color="white", text_color="black", font=customtkinter.CTkFont(size=15), corner_radius=10)
        self.username_entrybox.place(x=270, y=25)

        # Add Text "Password"
        name_label = customtkinter.CTkLabel(master=step_frame2, text="Password", font=customtkinter.CTkFont(size=20), text_color="black")
        name_label.place(x=270, y=55)

        # Add Text Entry for Password
        self.password_entrybox = customtkinter.CTkEntry(master=step_frame2, width=300 , height=32, fg_color="white", border_color="white", text_color="black", font=customtkinter.CTkFont(size=15), corner_radius=10)
        self.password_entrybox.place(x=270, y=80)

        # Add Text "Department"
        Department_label = customtkinter.CTkLabel(master=step_frame2, text="Department", font=customtkinter.CTkFont(size=20), text_color="black")
        Department_label.place(x=270, y=110)

        # Add ComboBox for Department
        self.department_entrybox = customtkinter.CTkEntry(master=step_frame2, width=300 , height=32, fg_color="white", border_color="white", text_color="black", font=customtkinter.CTkFont(size=15), corner_radius=10)
        self.department_entrybox.place(x=270, y=145)
        self.department_button = customtkinter.CTkButton(master=step_frame2, text="▼", command=self.show_department_menus, text_color="black", font=("Arial",16), fg_color="white", width=35, height=32)
        self.department_button.place(x=535, y=145)

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
        cam_btn = customtkinter.CTkButton(master=step_frame3, text="", image=cam_image, hover=False, border_width=0, width=150, height=140, fg_color="white", command=lambda: self.next_screen_photoshot(21))
        cam_btn.place(x=60, y=50)
        # Image Button
        img_btn = customtkinter.CTkButton(master=step_frame3, text="", image=img_image, hover=False, border_width=0, width=150, height=140, fg_color="white", command=self.create_usb_loading)
        img_btn.place(x=260, y=50)
        # Add Button "Save"
        btn_save = customtkinter.CTkButton(master=step_frame3, command= lambda:self.save(13), width=80, text="Save", font=customtkinter.CTkFont(size=20), text_color="black", corner_radius=15, fg_color="white", border_color="white", border_width=1)
        btn_save.place(x=480, y=160)

        # Initialize department Frame with Listbox and Scrollbar
        self.department_frame = tk.Frame(self, bg="#424242")
        self.department_listbox = tk.Listbox(self.department_frame, font=("Arial", 15), width=26, height=3)
        department_names = XFace_Database_Function.fetch_departmentname()
        for department in department_names:
            self.department_listbox.insert("end", department[0])
        self.department_listbox.bind("<Double-Button-1>", self.select_department)
        self.department_scrollbar = tk.Scrollbar(self.department_frame, orient="vertical", command=self.department_listbox.yview)
        self.department_listbox.config(yscrollcommand=self.department_scrollbar.set)
            
    def create_error_frame(self):

        self.error_frame = customtkinter.CTkFrame(master=self,width=500, height=250, fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
        self.error_frame.place(relx=0.1, rely=0.25)

        # Add Error label1
        error_label1 = customtkinter.CTkLabel(master=self.error_frame, text="A face was not detected in the image.", font=customtkinter.CTkFont(size=25), text_color="black", justify="center")
        error_label1.place(relx=0.1, rely=0.3)

        # Add Error label2
        error_label2 = customtkinter.CTkLabel(master=self.error_frame, text="Please select the photo again.", font=customtkinter.CTkFont(size=25), text_color="black", justify="center")
        error_label2.place(relx=0.2, rely=0.4)

        # Add Button "OK"
        btn_ok = customtkinter.CTkButton(master=self.error_frame, width=80, command=self.destroy_error_frame, text="OK", font=customtkinter.CTkFont(size=20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=1)
        btn_ok.place(relx=0.75, rely=0.75)

    def create_usb_loading(self):

        self.loading_frame = customtkinter.CTkFrame(master=self,width=500, height=250, fg_color="#e6e6e6", corner_radius=20, border_color="black", border_width=2)
        self.loading_frame.place(relx=0.1, rely=0.25)

        # Add "Loading USB" label1
        loading_usb_label = customtkinter.CTkLabel(master=self.loading_frame, text="Loading USB ...", font=customtkinter.CTkFont(size=25), text_color="black", justify="center")
        loading_usb_label.place(relx=0.35, rely=0.3)

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
        btn_Cancel = customtkinter.CTkButton(master=self.loading_frame, width=80, command=self.destroy_loading_usb_frame, text="Cancel", font=customtkinter.CTkFont(size=20), text_color="black", corner_radius=20, fg_color="white", border_color="white", border_width=1)
        btn_Cancel.place(relx=0.75, rely=0.75)

    def destroy_error_frame(self):
        if self.error_frame:
            self.error_frame.destroy()

    def destroy_loading_usb_frame(self):
        if self.loading_frame:
            self.loading_frame.destroy()

    def next_screen(self,index):
        self.main_app.show_next_screen(index)
    
    def save(self, index):
        userinfo = XFace_Database_Function.fetch_userinfo_by_username(self.username_entrybox_txt)
        userid, username, password, departmentid, adminflag, facephoto = userinfo[0]
        XFace_Database_Function.update_userinfo(userid, self.username_entrybox.get(), self.password_entrybox.get(), self.department_entrybox.get(), adminflag, facephoto)
        self.main_app.editpickle_save(userid,username,adminflag)
        self.username_entrybox.delete(0, tk.END)
        self.password_entrybox.delete(0, tk.END)
        self.department_entrybox.delete(0, tk.END)
        messagebox.showinfo("Update", "Updated successfully!")
        self.main_app.show_next_screen(index)

    def next_screen_photoshot(self,index):
        self.main_app.show_next_screen(index)

    def get_department_name(self):
        self.department_entrybox_txt = self.main_app.get_edit_department_name()
        self.department_entrybox.delete(0, tk.END) 
        self.department_entrybox.insert(0, self.department_entrybox_txt)

    def get_user_name(self):
        self.username_entrybox_txt = self.main_app.get_edit_user_name()
        self.username_entrybox.delete(0, tk.END)
        self.username_entrybox.insert(0, self.username_entrybox_txt)

    def get_current_password(self):
        self.password_entrybox_txt = self.main_app.get_edit_current_password()
        self.password_entrybox.delete(0, tk.END)
        self.password_entrybox.insert(0, self.password_entrybox_txt)

    def select_department(self, event):
        selected_department = self.department_listbox.get(tk.ACTIVE)
        self.department_entrybox.delete(0, tk.END)
        self.department_entrybox.insert(0, selected_department)
        self.show_department_menus()

    def show_department_menus(self):
        if not self.department_frame.winfo_ismapped():
            self.department_frame.place(x=270, y=225)
            self.department_listbox.pack(side="left")
            self.department_scrollbar.pack(side="right", fill="y")
        else:
            self.department_frame.place_forget()