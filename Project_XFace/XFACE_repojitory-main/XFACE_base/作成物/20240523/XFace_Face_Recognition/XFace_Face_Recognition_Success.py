import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk
import math
import os
import XFace_Database_Function

class Screen2(tk.Frame):
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

        # Add Square
        self.error_square = customtkinter.CTkFrame(master=self.step_frame,width=500, height=400, fg_color="white", corner_radius=20, border_color="white", border_width=1)
        self.error_square.place(relx=0.08, rely=0.1)

        # Add "Hello," label
        hello_label = customtkinter.CTkLabel(master=self.step_frame, text="Hello,", font=customtkinter.CTkFont(size=25), text_color="black", bg_color="white")
        hello_label.place(x=205,y=190)

        # Add Username label
        self.username_txt_label = customtkinter.CTkLabel(master=self.step_frame, text="", font=customtkinter.CTkFont(size=25), text_color="black", bg_color="white", justify="center")
        self.username_txt_label.place(x=275,y=190)

        # Add "Name()" label
        name_label = customtkinter.CTkLabel(master=self.step_frame, text="(Name)", font=customtkinter.CTkFont(size=25), text_color="black", bg_color="white")
        name_label.place(x=250,y=240)

        # Add Button "Attendance"
        btn_attendance = customtkinter.CTkButton(master=self.step_frame, width=60, command= lambda: self.attendance_starttime(), text="Attendance", font=customtkinter.CTkFont(size=20), text_color="black", corner_radius=20, fg_color="#d9d9d9", border_color="#d9d9d9", border_width=1, bg_color="white")
        btn_attendance.place(x=80,y=320)

        # Add Button "Clocking out"
        btn_clocking_out = customtkinter.CTkButton(master=self.step_frame, width=60, command= lambda: self.attendance_endtime(), text="Clocking out", font=customtkinter.CTkFont(size=20), text_color="black", corner_radius=20, fg_color="#d9d9d9", border_color="#d9d9d9", border_width=1, bg_color="white")
        btn_clocking_out.place(x=240,y=320)

        # Add Button "Menu"
        btn_menu = customtkinter.CTkButton(master=self.step_frame, width=60, command= lambda: self.next_screen(), text="Menu", font=customtkinter.CTkFont(size=20), text_color="black", corner_radius=20, fg_color="#d9d9d9", border_color="#d9d9d9", border_width=1, bg_color="white")
        btn_menu.place(x=420,y=320)

        # Add Description label
        description_label = customtkinter.CTkLabel(master=self.step_frame, text="If there is no operation, the system automatically logs out after 10 seconds.", font=customtkinter.CTkFont(size=14), text_color="black", bg_color="white")
        description_label.place(x=70,y=400)

    def timecountup(self):
        if self.timecount < 10:
            self.timecount += 1
            self.afterid = self.after(1000,self.timecountup)
        else:
            self.back_screen()

    def get_username(self):
        self.user_id = self.main_app.get_loginuserid()
        self.username_txt = self.main_app.get_loginusername()
        self.username_txt_label.configure(text=self.username_txt)

    def get_timecount(self):
        self.timecount = 0

    def attendance_starttime(self):
        XFace_Database_Function.save_work_start_time(self.user_id)
        self.main_app.show_next_screen(1)

    def attendance_endtime(self):
        XFace_Database_Function.save_work_end_time(self.user_id)
        self.main_app.show_next_screen(1)

    def next_screen(self):
        self.after_cancel(self.afterid)
        self.main_app.facerecognition_stop()        
        
        loginuseradminflag = self.main_app.get_loginuseradminflag()
        
        if loginuseradminflag:
            self.main_app.show_next_screen(4)
        else:
            self.main_app.show_next_screen(5)

    def back_screen(self):
        self.main_app.show_next_screen(1)