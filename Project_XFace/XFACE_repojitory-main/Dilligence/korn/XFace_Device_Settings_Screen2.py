import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk

class Screen2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(bg="#afafaf", width=500, height=500)
        self.pack_propagate(0)

        # Add "<" Button
        back_btn = customtkinter.CTkButton(self, width=30, height=30, text="<", text_color="gray", font=("Arial Bold", 30), fg_color="transparent", hover=False)
        back_btn.place(relx=0.05, rely=0.02)

        # Add Text "Device Settings"
        self.label_DeviceSettingsScreen = tk.Label(self, text="Device settings", font=("Arial Bold", 20), bg="#afafaf")
        self.label_DeviceSettingsScreen.pack(side="top", pady=10)


        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Frame Display Brightness Frame
        self.time_zone_frame = customtkinter.CTkFrame(self, width=450, height=100, fg_color="#f5f5f5", corner_radius=20, background_corner_colors=("#afafaf","#afafaf","#afafaf","#afafaf"))
        self.time_zone_frame.pack(pady=10)

        # Add Text "Time Zone"
        timezone_label = customtkinter.CTkLabel(master=self.time_zone_frame, text="Time Zone", font=customtkinter.CTkFont(size=13), text_color="#000000")
        timezone_label.place(x=10, y=10)

        # Define Values for Time Zone ComboBox
        timezone_list = ["TimeZone 1", "TimeZone 2", "TimeZone 3", "TimeZone 4", "TimeZone 5"]

        # Add Time Zone ComboBox
        timezone_ComboBox= customtkinter.CTkComboBox(master=self.time_zone_frame, state="readonly", values=timezone_list, justify="left", width=400, fg_color="White", font=customtkinter.CTkFont(size=13), text_color="Black", dropdown_fg_color="White", dropdown_font=customtkinter.CTkFont(size=13), dropdown_text_color="Black")
        timezone_ComboBox.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        #----------------------------------------------------------------------------
        #                                     Frame 2
        #----------------------------------------------------------------------------
                
        # Add Fram Camera's Test
        self.camera_test_frame = customtkinter.CTkFrame(self, width=450, height=270, fg_color="#f5f5f5", corner_radius=20, background_corner_colors=("#afafaf","#afafaf","#afafaf","#afafaf"))
        self.camera_test_frame.pack(pady=5)

        # Add Text "Time Zone"
        camera_test_label = customtkinter.CTkLabel(master=self.camera_test_frame, text="Camera's Test", font=customtkinter.CTkFont(size=13), text_color="#000000")
        camera_test_label.place(x=10, y=10)

        # Add Camera A Button
        Camera_A = customtkinter.CTkButton(master=self.camera_test_frame, state="readonly", width=400, height=50, text="Camera A", anchor="w", text_color="Black", font=("Arial", 20), fg_color="white", hover_color="Gray", border_width=1, border_color="Gray")
        Camera_A.place(relx=0.05, rely=0.2)

        # Add Camera B Button
        Camera_B = customtkinter.CTkButton(master=self.camera_test_frame, width=400, height=50, text="Camera B", anchor="w", text_color="Black", font=("Arial", 20), fg_color="white", hover_color="Gray", border_width=1, border_color="Gray")
        Camera_B.place(relx=0.05, rely=0.5)