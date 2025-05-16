import tkinter as tk
from tkinter import messagebox
import customtkinter
import numpy as np
#from XFace_textfile import Department_Registration_textdir
from XFace_ExcelOutput.XFace_ExcelOutput_Function import AttendanceRecord
from XFace_ExcelOutput.XFace_ExcelOutput_Function import EmployeeInfo
import XFace_Database_Function
employeeinfo = EmployeeInfo()
attendancerecord = AttendanceRecord()

class Screen20(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#424242", width=600, height=500)
        self.pack_propagate(0)
        self.user_id = ""

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Frame for all elements
        self.menu_frame = customtkinter.CTkFrame(self, width=600, height=500, fg_color="#424242", corner_radius=0)
        self.menu_frame.place(x=0)

        # Back Button
        back_btn = customtkinter.CTkButton(self.menu_frame, text="<", command=lambda: self.back_screen(5), width=30, height=30, text_color="white", font=("Arial", 30), fg_color="transparent")
        back_btn.place(relx=0.02, rely=0.02)

        # Title for the Excel Output section
        title_label = customtkinter.CTkLabel(self.menu_frame, text="Excel Output", font=("Arial", 24), text_color="white", fg_color="transparent")
        title_label.place(relx=0.3, rely=0.12, anchor=tk.CENTER)

        # Yearmonth Entry
        yearmonth_label = customtkinter.CTkLabel(self.menu_frame, text="YearMonth", font=("Arial", 20), text_color="white", fg_color="transparent")
        yearmonth_label.place(relx=0.1, rely=0.2)
        self.yearmonth_entry = customtkinter.CTkEntry(self.menu_frame, placeholder_text="YYYYMM", font=("Arial", 20), width=150, height=35)
        self.yearmonth_entry.place(relx=0.1, rely=0.25)

        # AttendanceRecord User Button
        AttendanceRecord_user_btn = customtkinter.CTkButton(self.menu_frame, text="AttendanceRecord User", command=lambda:self.ExcelOutput_user(self.user_id, self.user_name, self.yearmonth_entry.get()), text_color="black", font=("Arial", 15, "bold"), fg_color="white", width=50, height=25, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        AttendanceRecord_user_btn.place(relx=0.1, rely=0.45)
        ###fujiwara syuusei user_name[0] -> user_name

    def get_user_id(self):
        new_user_id = self.main_app.get_loginuserid()
        self.user_id = new_user_id
        #self.user_name = XFace_Database_Function.fetch_username(self.user_id)   ###fujiwara syuusei
        self.user_name = self.main_app.get_loginusername()
        

    def back_screen(self, index):
        self.main_app.show_next_screen(index)
            
    def ExcelOutput_user(self,userid,username,yearmonth):
        if yearmonth == "":
            messagebox.showerror("Error", "Yearmonth has not been entered!")
        else:
            res = messagebox.askokcancel("Excel Output", f"Do you want to output {username} attendance information for {yearmonth}")
            if res:
                attendancerecord.ExcelOutput_user(userid,username,yearmonth)
