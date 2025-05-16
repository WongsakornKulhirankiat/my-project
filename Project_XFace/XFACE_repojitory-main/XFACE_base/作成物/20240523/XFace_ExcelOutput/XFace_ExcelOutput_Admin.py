import tkinter as tk
from tkinter import messagebox
import customtkinter
import numpy as np
#from XFace_textfile import Department_Registration_textdir
from XFace_ExcelOutput.XFace_ExcelOutput_Function import AttendanceRecord
from XFace_ExcelOutput.XFace_ExcelOutput_Function import EmployeeInfo
employeeinfo = EmployeeInfo()
attendancerecord = AttendanceRecord()

class Screen19(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#424242", width=600, height=500)
        self.pack_propagate(0)

        # Password
        self.password = ""
        self.current_password = ""
        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Frame for all elements
        self.menu_frame = customtkinter.CTkFrame(self, width=600, height=500, fg_color="#424242", corner_radius=0)
        self.menu_frame.place(x=0)

        # Back Button
        back_btn = customtkinter.CTkButton(self.menu_frame, text="<", command=lambda: self.back_screen(4), width=30, height=30, text_color="white", font=("Arial", 30), fg_color="transparent")
        back_btn.place(relx=0.02, rely=0.02)

        # Title for the Excel Output section
        title_label = customtkinter.CTkLabel(self.menu_frame, text="Excel Output", font=("Arial", 24), text_color="white", fg_color="transparent")
        title_label.place(relx=0.3, rely=0.12, anchor=tk.CENTER)

        # User Name Entry
        user_name_label = customtkinter.CTkLabel(self.menu_frame, text="User Name", font=("Arial", 20), text_color="white", fg_color="transparent")
        user_name_label.place(relx=0.1, rely=0.2)
        self.user_name_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20),  width=250, height=35)
        self.user_name_entry.place(relx=0.1, rely=0.25)

        # Yearmonth Entry
        yearmonth_label = customtkinter.CTkLabel(self.menu_frame, text="YearMonth", font=("Arial", 20), text_color="white", fg_color="transparent")
        yearmonth_label.place(relx=0.6, rely=0.2)
        self.yearmonth_entry = customtkinter.CTkEntry(self.menu_frame, placeholder_text="YYYYMM", font=("Arial", 20), width=150, height=35)
        self.yearmonth_entry.place(relx=0.6, rely=0.25)

        # User ID Entry
        user_id_label = customtkinter.CTkLabel(self.menu_frame, text="User ID", font=("Arial", 20), text_color="white", fg_color="transparent")
        user_id_label.place(relx=0.1, rely=0.4)
        self.user_id_entry = customtkinter.CTkEntry(self.menu_frame, placeholder_text="000000", font=("Arial", 20), width=250, height=35)
        self.user_id_entry.place(relx=0.1, rely=0.45)

        # UserInfo list Button
        userinfo_btn = customtkinter.CTkButton(self.menu_frame, text="UserInfo List", command=lambda:self.ExcelOutput(self.yearmonth_entry.get()), text_color="black", font=("Arial", 15, "bold"), fg_color="white", width=50, height=25, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        userinfo_btn.place(relx=0.1, rely=0.65)

        # AttendanceRecord User Button
        AttendanceRecord_user_btn = customtkinter.CTkButton(self.menu_frame, text="AttendanceRecord User", command=lambda:self.ExcelOutput_user(self.user_id_entry.get(), self.user_name_entry.get(), self.yearmonth_entry.get()), text_color="black", font=("Arial", 15, "bold"), fg_color="white", width=50, height=25, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        AttendanceRecord_user_btn.place(relx=0.1, rely=0.75)

        # AttendanceRecord List Button
        AttendanceRecord_list_btn = customtkinter.CTkButton(self.menu_frame, text="AttendanceRecord List", command=lambda:self.ExcelOutput_list(self.yearmonth_entry.get()), text_color="black", font=("Arial", 15, "bold"), fg_color="white", width=50, height=25, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        AttendanceRecord_list_btn.place(relx=0.5, rely=0.75)

    def next_screen(self, index):
        self.main_app.set_user_name(self.user_name_entry.get())
        self.main_app.set_yearmonth(self.yearmonth_entry.get())
        self.main_app.set_user_id(self.user_id_entry.get())
        self.main_app.show_next_screen(index)

    def back_screen(self, index):
        self.main_app.show_next_screen(index)

    def ExcelOutput(self,yearmonth):
        if yearmonth == "":
            messagebox.showerror("Error", "Has not been entered!")
        else:
            res = messagebox.askokcancel("Excel Output", "Output user information?")
            if res:
                employeeinfo.ExcelOutput(yearmonth)
            
    def ExcelOutput_user(self,userid,username,yearmonth):
        if userid == "" or username == "" or yearmonth == "":
            messagebox.showerror("Error", " Has not been entered!")
        else:
            res = messagebox.askokcancel("Excel Output", f"Do you want to output {username} attendance information for {yearmonth}")
            if res:
                attendancerecord.ExcelOutput_user(userid,username,yearmonth)
                
    def ExcelOutput_list(self,yearmonth):
        if yearmonth == "":
            messagebox.showerror("Error", "Has not been entered!")
        else:
            res = messagebox.askokcancel("Excel Output", f"Do you want to output alluser attendance information for {yearmonth}")
            if res:
                attendancerecord.ExcelOutput_list(yearmonth)