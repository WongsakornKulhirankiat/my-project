import tkinter as tk
import customtkinter
import subprocess

class Menu1(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#424242", width=600, height=500)
        self.pack_propagate(0)

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Menu Frame
        self.menu_frame = customtkinter.CTkFrame(self, width=600, height=500, fg_color="#424242", corner_radius=0)
        self.menu_frame.place(x=0)

        # Add "<" Button
        back_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(1), width=30, height=30, text="<", text_color="white", font=("Arial", 30), fg_color="transparent", hover=False)
        back_btn.place(relx=0.02, rely=0.02)

        # Add Year Label
        self.yeartxt_label = customtkinter.CTkLabel(master=self.menu_frame, text="2024", font=customtkinter.CTkFont(size=22), text_color="white")
        self.yeartxt_label.place(relx=0.1, rely=0.035)

        # Add text "/"
        self.slash1_label = customtkinter.CTkLabel(master=self.menu_frame, text="/", font=customtkinter.CTkFont(size=22), text_color="white")
        self.slash1_label.place(relx=0.2, rely=0.035)

        # Add Month Label
        self.monthtxt_label = customtkinter.CTkLabel(master=self.menu_frame, text="01", font=customtkinter.CTkFont(size=22), text_color="white")
        self.monthtxt_label.place(relx=0.235, rely=0.035)

        # Add text "/"
        self.slash2_label = customtkinter.CTkLabel(master=self.menu_frame, text="/", font=customtkinter.CTkFont(size=22), text_color="white")
        self.slash2_label.place(relx=0.30, rely=0.035)

        # Add Day Label
        self.daytxt_label = customtkinter.CTkLabel(master=self.menu_frame, text="01", font=customtkinter.CTkFont(size=22), text_color="white")
        self.daytxt_label.place(relx=0.335, rely=0.035)

        # Add Logout Button
        logout_btn =customtkinter.CTkButton(master=self.menu_frame, text="Logout", command= lambda: self.next_screen(1), text_color="black", font=("Arial", 15), fg_color="white", width=90, height=40, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        logout_btn.place(relx=0.83, rely=0.03)

        # Add User Registration Button
        student_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(1), text="User Registration", text_color="black", font=("Arial Bold", 15), fg_color="white", width=250, height=50, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        student_btn.place(relx=0.05, rely=0.35)

        # Add Edit User Information Button
        edit_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(9), text="Edit User Information", text_color="black", font=("Arial Bold", 15), fg_color="white", width=250, height=50, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        edit_btn.place(relx=0.05, rely=0.5)

        # Add Excel Output Button
        ride_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(12), text="Excel Output", text_color="black", font=("Arial Bold", 15), fg_color="white", width=250, height=50, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        ride_btn.place(relx=0.05, rely=0.65)

        # Add Department Registration Button
        ride_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(6), text="Department Master", text_color="black", font=("Arial Bold", 15), fg_color="white", width=250, height=50, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        ride_btn.place(relx=0.52, rely=0.35)

        # Add Department Edit Button
        ride_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.next_screen(11), text="Edit Attendance Record", text_color="black", font=("Arial Bold", 15), fg_color="white", width=250, height=50, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        ride_btn.place(relx=0.52, rely=0.5)

        # Add Wifi Setting Button
        ride_btn = customtkinter.CTkButton(master=self.menu_frame, command= lambda: self.open_wifi_settings(), text="Wifi Setting", text_color="black", font=("Arial Bold", 15), fg_color="white", width=250, height=50, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        ride_btn.place(relx=0.52, rely=0.65)

    def open_wifi_settings(self):
        try:
            # This command works for GNOME; modify if using a different desktop environment
            subprocess.Popen(['gnome-control-center'])
        except Exception as e:
            print(f"Failed to open WiFi settings: {e}")

    def next_screen(self, index):
        self.main_app.show_next_screen(index)

    def get_year(self):
        self.year_txt = self.main_app.get_year()
        #self.yeartxt_label.configure(text=self.year_txt)

    def get_month(self):
        self.month_txt = self.main_app.get_month()
        #self.monthtxt_label.configure(text=self.month_txt)

    def get_day(self):
        self.day_txt = self.main_app.get_day()
        #self.daytxt_label.configure(text=self.day_txt)