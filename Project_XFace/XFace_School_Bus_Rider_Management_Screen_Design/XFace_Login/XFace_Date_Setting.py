import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk

class Screen4(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#424242", width=600, height=500)
        self.pack_propagate(0)

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Date Frame
        self.date_frame = customtkinter.CTkFrame(self, width=600, height=500, fg_color="#424242", corner_radius=0)
        self.date_frame.pack()

        # Add Date Label
        date_label = customtkinter.CTkLabel(self.date_frame, text_color="#a8a8a8", text="Today's Date", font=("Arial", 25))
        date_label.place(relx=0.5, rely=0.35, anchor="center")

        # Add Year ComboBox
        self.year_cmb = customtkinter.CTkComboBox(self.date_frame, text_color="black", values=["2024", "2023","2022", "2021", "2020", "2019"], font=("Arial", 20), width=110, height=20, justify="center", fg_color="white", dropdown_text_color="black", dropdown_font=("Arial", 20), dropdown_fg_color="white", dropdown_hover_color="white", button_color="white", border_color="white", button_hover_color="white", state="readonly")
        self.year_cmb.place(x=140, y=240)

        # Add Month ComboBox
        self.month_cmb = customtkinter.CTkComboBox(self.date_frame, text_color="black", values=["01", "02", "03", "04"], font=("Arial", 20), width=80, height=20, justify="center", fg_color="white", dropdown_text_color="black", dropdown_font=("Arial", 20), dropdown_fg_color="white", dropdown_hover_color="white", button_color="white", border_color="white", button_hover_color="white", state="readonly")
        self.month_cmb.place(x=270, y=240)

        # Add Day ComboBox
        self.day_cmb = customtkinter.CTkComboBox(self.date_frame, text_color="black", values=["01", "02", "03", "04"], font=("Arial", 20), width=80, height=20, justify="center", fg_color="white", dropdown_text_color="black", dropdown_font=("Arial", 20), dropdown_fg_color="white", dropdown_hover_color="white", button_color="white", border_color="white", button_hover_color="white", state="readonly")
        self.day_cmb.place(x=370, y=240)

        # Add OK Button
        ok_btn =customtkinter.CTkButton(master=self.date_frame, text="OK", command= lambda: self.next_screen(5), text_color="black", font=("Arial", 15, "bold"), fg_color="white", width=90, height=50, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        ok_btn.place(relx=0.5, rely=0.68, anchor="center")

    def next_screen(self, index):
        self.main_app.set_year(self.year_cmb.get())
        self.main_app.set_month(self.month_cmb.get())
        self.main_app.set_day(self.day_cmb.get())
        self.main_app.show_next_screen(index)