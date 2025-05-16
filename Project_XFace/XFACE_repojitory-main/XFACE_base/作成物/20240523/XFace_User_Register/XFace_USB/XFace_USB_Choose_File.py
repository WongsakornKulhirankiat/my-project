import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk
import math
import os
import customtkinter as ctk

class Screen12(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="white", width=600, height=500)
        self.pack_propagate(0)

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Frame Step Frame
        self.step_frame = customtkinter.CTkFrame(self, width=600, height=500, fg_color="#e6e6e6", corner_radius=0)
        self.step_frame.pack()

        # Add Square
        self.gray_square = customtkinter.CTkFrame(master=self.step_frame,width=500, height=500, fg_color="white", corner_radius=0, border_color="white", border_width=1)
        self.gray_square.place(relx=0.2, rely=0)

        # Add "<" Button
        back_btn = customtkinter.CTkButton(master=self.step_frame, command=lambda: self.next_screen(11), width=30, height=30, text="<", text_color="black", font=("Arial", 30), fg_color="transparent", hover=False)
        back_btn.place(relx=0.02, rely=0.02)

        scrollable_frame = ctk.CTkScrollableFrame(master=self.step_frame, width=460, height=500, bg_color="white", fg_color="white", scrollbar_fg_color="white")
        scrollable_frame.place(relx=0.2, rely=0, relheight=1)

        # Add content to the scrollable frame
        for i in range(50):
            label = ctk.CTkLabel(master=scrollable_frame, text="", fg_color="white")
            label.pack(pady=10)

    def next_screen(self, index):
        self.main_app.show_next_screen(index)

