import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk
import math
import os
from PIL import Image, ImageTk

class Screen16(tk.Frame):
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

        # Add "<" Button
        back_btn = customtkinter.CTkButton(master=self.step_frame, command=lambda: self.next_screen(15), width=30, height=30, text="<", text_color="black", font=("Arial", 30), fg_color="transparent", hover=False)
        back_btn.place(relx=0.02, rely=0.02)

        # Add Department Register Label
        department_register_label = customtkinter.CTkLabel(master=self.step_frame, text="Department Register", text_color="black", font=("Arial", 25), fg_color="transparent")
        department_register_label.place(x=80, y=50)

        # Add Department Name Label
        department_name_label = customtkinter.CTkLabel(master=self.step_frame, text="Department Name", text_color="black", font=("Arial", 20), fg_color="transparent")
        department_name_label.place(x=90, y=100)

         # Add Text Box for Department Name
        self.department_name_entrybox = customtkinter.CTkEntry(master=self.step_frame, width=440, height=40, fg_color="white", border_color="white", border_width=1, text_color="black", font=customtkinter.CTkFont(size=20,weight="bold"), corner_radius=20)
        self.department_name_entrybox.place(x=80, y=135)
        self.department_name_entrybox.bind("<Button-1>", lambda event: self.show_keyboard(self.department_name_entrybox))

        # Add WorkStartTime Label
        workstarttime_label = customtkinter.CTkLabel(master=self.step_frame, text="WorkStartTime", text_color="black", font=("Arial", 20), fg_color="transparent")
        workstarttime_label.place(x=115, y=195)

        # Add WorkEndTime Label
        department_name_label = customtkinter.CTkLabel(master=self.step_frame, text="WorkEndTime", text_color="black", font=("Arial", 20), fg_color="transparent")
        department_name_label.place(x=355, y=195)

        # Add ComboBox for WorkStartTime
        self.workstarttime_combobox = customtkinter.CTkComboBox(master=self.step_frame, text_color="black", values=["9:00","9:30","10:00","10:30"], font=("Arial", 20), width=200, height=40, fg_color="white", dropdown_text_color="black", dropdown_font=("Arial", 20), dropdown_fg_color="white", dropdown_hover_color="white", button_color="white", border_color="white", button_hover_color="white", state="readonly", corner_radius=20)
        self.workstarttime_combobox.place(x=80, y=230)

        # Add ComboBox for WorkEndTime
        self.workendtime_entrybox = customtkinter.CTkComboBox(master=self.step_frame, text_color="black", values=["18.00","18.30","19.00","19.30"], font=("Arial", 20), width=200, height=40, fg_color="white", dropdown_text_color="black", dropdown_font=("Arial", 20), dropdown_fg_color="white", dropdown_hover_color="white", button_color="white", border_color="white", button_hover_color="white", state="readonly", corner_radius=20)
        self.workendtime_entrybox.place(x=320, y=230)

        # Add RestTime(hour) Label
        resttime_label = customtkinter.CTkLabel(master=self.step_frame, text="RestTime(hour)", text_color="black", font=("Arial", 20), fg_color="transparent")
        resttime_label.place(x=110, y=290)

        # Add OverTime(minute) Label
        overtime_label = customtkinter.CTkLabel(master=self.step_frame, text="OverTime(minute)", text_color="black", font=("Arial", 20), fg_color="transparent")
        overtime_label.place(x=340, y=290)

        # Add ComboBox for RestTime(hour)
        self.resttime_combobox = customtkinter.CTkComboBox(master=self.step_frame, text_color="black", values=["1","2","3","4"], font=("Arial", 20), width=200, height=40, fg_color="white", dropdown_text_color="black", dropdown_font=("Arial", 20), dropdown_fg_color="white", dropdown_hover_color="white", button_color="white", border_color="white", button_hover_color="white", state="readonly", corner_radius=20)
        self.resttime_combobox.place(x=80, y=325)

        # Add ComboBox for OverTime(minute)
        self.overtime_combobox = customtkinter.CTkComboBox(master=self.step_frame, text_color="black", values=["0","30","60","90"], font=("Arial", 20), width=200, height=40, fg_color="white", dropdown_text_color="black", dropdown_font=("Arial", 20), dropdown_fg_color="white", dropdown_hover_color="white", button_color="white", border_color="white", button_hover_color="white", state="readonly", corner_radius=20)
        self.overtime_combobox.place(x=320, y=325)

        # Add Button "Save"
        btn_save = customtkinter.CTkButton(master=self.step_frame, width=80, command= lambda: self.next_screen(15), text="Save", font=customtkinter.CTkFont(size=20), text_color="black", corner_radius=10, fg_color="white", border_color="white", border_width=1)
        btn_save.place(x=440, y=400)

        # Create the virtual keyboard
        self.create_virtual_keyboard()

    def create_virtual_keyboard(self):
        # Create a frame to hold the keyboard buttons
        self.keyboard_frame = tk.Frame(self.master, bg="grey")  # Set background color to grey

        # Define keyboard layout
        keys = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'],
            ['Delete', 'End']  # Add "Delete" button and "End" button to close the keyboard
        ]

        # Create keyboard buttons
        for i, row in enumerate(keys):
            for j, key in enumerate(row):
                # Create button for each key
                btn = tk.Button(self.keyboard_frame, text=key, width=5, height=1, font=("Helvetica", 9, "bold"),
                                command=lambda char=key: self.on_key_press(char))  # Set font to bold
                btn.grid(row=i, column=j, padx=3, pady=3)

        # Pack the keyboard frame initially hidden
        self.keyboard_frame.pack_forget()


    # Modify show_keyboard method to accept an entrybox parameter
    def show_keyboard(self, entrybox):
        print("show keyboard")
        entrybox.focus_set()  # Set focus to the clicked entrybox
        self.keyboard_frame.place(relx=0.08, rely=0.65)

    # Modify on_key_press method to properly handle the Delete and End keys
    def on_key_press(self, char):

        # Get the widget that currently has focus
        target_entry = self.focus_get()
        
        if char == "End":
            self.keyboard_frame.place_forget()
        elif char == "Delete":
            target_entry.delete(len(target_entry.get()) - 1)
        else:
            target_entry.insert(tk.END, char)

    def next_screen(self, index):
        self.main_app.show_next_screen(index)
        self.keyboard_frame.place_forget()