import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk

class Screen1(tk.Frame):
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
        self.display_brightness_frame = customtkinter.CTkFrame(self, width=450, height=100, fg_color="#f5f5f5", corner_radius=20, background_corner_colors=("#afafaf","#afafaf","#afafaf","#afafaf"))
        self.display_brightness_frame.pack(pady=10)

        # Add Text "Display's Brightness"
        brightness_label = customtkinter.CTkLabel(master=self.display_brightness_frame, text="Display's Brightness", font=customtkinter.CTkFont(size=13), text_color="#000000")
        brightness_label.place(x=10, y=10)

        # Add Display Brightness CTkSlider
        display_brightness_slider = customtkinter.CTkSlider(master=self.display_brightness_frame, width=400, button_corner_radius=2, button_length=2, button_hover_color="#0295ff", progress_color="#0295ff", button_color="#0295ff", from_=0, to=100)
        display_brightness_slider.place(relx=0.5, rely=0.6, anchor=tk.CENTER)


        #----------------------------------------------------------------------------
        #                                     Frame 2
        #----------------------------------------------------------------------------
                
        # Add Frame Wifi Settings
        self.wifi_settings_frame = customtkinter.CTkFrame(self, width=450, height=270, fg_color="#f5f5f5", corner_radius=20, background_corner_colors=("#afafaf","#afafaf","#afafaf","#afafaf"))
        self.wifi_settings_frame.pack(pady=5)

        # Add Text "Wi-Fi Setting"
        brightness_label = customtkinter.CTkLabel(master=self.wifi_settings_frame, text="Wi-Fi Setting", font=customtkinter.CTkFont(size=13), text_color="#000000")
        brightness_label.place(x=10, y=10)

        # Add Text "Connected"
        status_label = customtkinter.CTkLabel(master=self.wifi_settings_frame, text="Connected", font=customtkinter.CTkFont(size=13), text_color="#0295ff")
        status_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # Define values for Wi-Fi ComboBox
        wifi_list = ["Wi-Fi 1", "Wi-Fi 2", "Wi-Fi 3", "Wi-Fi 4", "Wi-Fi 5"]

        # Add Wi-Fi ComboBox
        wifi_ComboBox= customtkinter.CTkComboBox(master=self.wifi_settings_frame, state="readonly", values=wifi_list, justify="left", width=400, fg_color="White", font=customtkinter.CTkFont(size=13), text_color="Black", dropdown_fg_color="White", dropdown_font=customtkinter.CTkFont(size=13), dropdown_text_color="Black")
        wifi_ComboBox.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        #----------------------------------------------------------------------------
        #                                     Frame 3
        #----------------------------------------------------------------------------

        self.title_label = tk.Label(self, text="Choose a different Wi-Fi network", font=("Arial", 10), bg="#afafaf", fg="#0295ff")
        self.title_label.pack(side="top", pady=10)