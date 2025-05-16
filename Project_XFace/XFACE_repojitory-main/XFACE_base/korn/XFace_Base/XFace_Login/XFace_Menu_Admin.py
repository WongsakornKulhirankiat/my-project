import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk
from datetime import datetime

class Screen4(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#424242", width=600, height=500)
        self.pack_propagate(0)

        # Get the current date and format it
        current_date = datetime.now().strftime("%Y / %m / %d")

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Menu Frame
        self.menu_frame = customtkinter.CTkFrame(self, width=600, height=500, fg_color="#424242", corner_radius=0)
        self.menu_frame.place(x=0)

        # Add "<" Button
        back_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(), width=30, height=30, text="<", text_color="white", font=("Arial", 30), fg_color="transparent", hover=False)
        back_btn.place(relx=0.02, rely=0.02)

        # Add Date Label
        self.datetxt_label = customtkinter.CTkLabel(master=self.menu_frame, text=current_date, font=customtkinter.CTkFont(size=22), text_color="white")
        self.datetxt_label.place(relx=0.1, rely=0.035)

        # Add Logout Button
        logout_btn =customtkinter.CTkButton(master=self.menu_frame, text="Logout", command= lambda: self.next_screen(1), text_color="black", font=("Arial", 20), fg_color="white", width=90, height=40, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        logout_btn.place(relx=0.83, rely=0.03)

        # Add User Register Button
        user_register_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(6), text="User Registration", text_color="black", font=("Arial Bold", 20), fg_color="white", width=250, height=50, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        user_register_btn.place(relx=0.07, rely=0.3)

        # Add Department Master Button
        department_master_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(15), text="Department Master", text_color="black", font=("Arial Bold", 20), fg_color="white", width=250, height=50, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        department_master_btn.place(relx=0.52, rely=0.3)

        # Add Edit user Information Button
        edit_user_information_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(13), text="Edit user Information", text_color="black", font=("Arial Bold", 20), fg_color="white", width=250, height=50, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        edit_user_information_btn.place(relx=0.07, rely=0.45)

        # Add Edit Attendance Record Button
        edit_attendance_record_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(18), text="Edit Attendance Record", text_color="black", font=("Arial Bold", 20), fg_color="white", width=250, height=50, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        edit_attendance_record_btn.place(relx=0.52, rely=0.45)

        # Add Excel Output Button
        edit_excel_output_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(19), text="Excel Output", text_color="black", font=("Arial Bold", 20), fg_color="white", width=250, height=50, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        edit_excel_output_btn.place(relx=0.07, rely=0.6)

        # Add Wifi Setting Information Button
        edit_wifi_setting_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(), text="Wifi Setting", text_color="black", font=("Arial Bold", 20), fg_color="white", width=250, height=50, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        edit_wifi_setting_btn.place(relx=0.52, rely=0.6)

    def next_screen(self, index):
        self.main_app.show_next_screen(index)
