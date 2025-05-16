import tkinter as tk
from tkinter import messagebox
import customtkinter
import numpy as np
from XFace_textfile import Department_Registration_textdir
from XFace_Database_Function import fetch_user_attendance1, update_user_attendance
import datetime

class Edit_AttendanceRecord1(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#424242", width=600, height=500)
        self.pack_propagate(0)
        self.yearmonth = "202401"
        self.entries = []
        self._user_id = ""

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Frame for all elements
        self.menu_frame = customtkinter.CTkFrame(self, width=600, height=500, fg_color="#424242", corner_radius=0)
        self.menu_frame.place(x=0, y=0)

        # Back Button
        back_btn = customtkinter.CTkButton(self.menu_frame, text="<", command=lambda: self.back_screen(5), width=30, height=30, text_color="white", font=("Arial", 30), fg_color="transparent")
        back_btn.place(relx=0.02, rely=0.02)

        # Title for the Department Registration section
        title_label = customtkinter.CTkLabel(self.menu_frame, text="Edit attendance record", font=("Arial", 24), text_color="white", fg_color="transparent")
        title_label.place(relx=0.34, rely=0.1, anchor=tk.CENTER)

        # Search Button
        save_btn = customtkinter.CTkButton(self.menu_frame, text="Save", command=self.save_changes, text_color="black", font=("Arial", 20, "bold"), fg_color="white", width=50, height=20, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        save_btn.place(relx=0.85, rely=0.15)

        # Add Year Entry and Button
        current_year = datetime.datetime.now().year
        self.year_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20), justify="center", width=100, height=35)
        self.year_entry.insert(0, str(current_year))
        self.year_entry.place(relx=0.45, rely=0.15)
        self.year_button = customtkinter.CTkButton(self.menu_frame, text="▼", command=self.show_year_menus, text_color="black", font=("Arial",20), fg_color="white", width=35, height=35)
        self.year_button.place(relx=0.61, rely=0.15)

        # Add Month Entry and Button
        self.month_entry = customtkinter.CTkEntry(self.menu_frame, font=("Arial", 20), justify="center", width=50, height=35)
        self.month_entry.insert(0, "01")
        self.month_entry.place(relx=0.69, rely=0.15)
        self.month_button = customtkinter.CTkButton(self.menu_frame, text="▼", command=self.show_month_menus, text_color="black", font=("Arial",20), fg_color="white", width=35, height=35)
        self.month_button.place(relx=0.76, rely=0.15)

        # Initialize Year Frame with Listbox and Scrollbar
        self.year_frame = tk.Frame(self, bg="#424242")
        self.year_listbox = tk.Listbox(self.year_frame, font=("Arial", 15), width=8, height=3)
        for i in range(5):
            self.year_listbox.insert("end",f"{current_year - i}")
        self.year_listbox.bind("<Double-Button-1>", self.select_year)
        self.year_scrollbar = tk.Scrollbar(self.year_frame, orient="vertical", command=self.year_listbox.yview)
        self.year_listbox.config(yscrollcommand=self.year_scrollbar.set)

        # Initialize Month Frame with Listbox and Scrollbar
        self.month_frame = tk.Frame(self, bg="#424242")
        self.month_listbox = tk.Listbox(self.month_frame, font=("Arial", 15), width=4, height=3)
        for i in range(1, 13):
            self.month_listbox.insert("end", f"{i:02d}")
        self.month_listbox.bind("<Double-Button-1>", self.select_month)
        self.month_scrollbar = tk.Scrollbar(self.month_frame, orient="vertical", command=self.month_listbox.yview)
        self.month_listbox.config(yscrollcommand=self.month_scrollbar.set)
        
        # Canvas and Scrollbar for attendance records
        self.canvas = customtkinter.CTkCanvas(self.menu_frame, bg="#424242", highlightthickness=0)
        self.scrollbar = customtkinter.CTkScrollbar(self.menu_frame, orientation="vertical", command=self.canvas.yview)

        # Ensure the scrollable frame can expand as needed
        self.scrollable_frame = tk.Frame(self.canvas, bg="#424242")

        # Create window inside canvas
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor=tk.NW)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Place canvas and scrollbar
        self.canvas.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.7)
        self.scrollbar.place(relx=0.95, rely=0.25, relwidth=0.03, relheight=0.7)

        self.init_headers()
        self.user_id = self.main_app.get_user_id()

    def init_headers(self):
        self.headers = []  
        headers = ["Date", "Clock In", "Clock Out", "WorkTime", "Memo"]
        headers_widths = [40, 50, 50, 40, 100]
        for col, header in enumerate(headers):
            label = customtkinter.CTkLabel(self.scrollable_frame, text=header, font=("Arial", 15), text_color="white", fg_color="transparent", width=headers_widths[col])
            label.grid(row=0, column=col, padx=10, pady=10, sticky="w")
            self.headers.append(label)  

    def update_yearmonth(self):
        year = self.year_entry.get().strip()
        month = self.month_entry.get().strip()
        if year and month:
            self.yearmonth = year + month
            self.load_data()

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        if value != self._user_id:
            self._user_id = value
            self.load_data()

    def get_user_id(self):
        new_user_id = self.main_app.get_user_id()
        self.user_id = new_user_id

    def update_scrollregion(self):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def save_changes(self):
        if messagebox.askokcancel("Update", "Save these changes?"):
            for row_entries in self.entries:
                date = row_entries[0].cget('text') 
                clock_in = row_entries[1].get()    
                clock_out = row_entries[2].get()   
                work_time = row_entries[3].get()   
                memo = row_entries[4].get()         

                update_user_attendance(self.user_id, self.yearmonth, date, clock_in, clock_out, work_time, memo)
            messagebox.showinfo("Update", "Updated successfully!")

    def update_entries(self, attendance_data):
        self.clear_entries()

        for i, data in enumerate(attendance_data, start=1):
            row_entries = []
            for j in range(5):
                entry_width = [40, 50, 50, 40, 100][j]
                if j == 0:
                    label = customtkinter.CTkLabel(self.scrollable_frame, text=str(data[0]), font=("Arial", 12), text_color="white", fg_color="transparent")
                    label.grid(row=i, column=j, padx=10, pady=5, sticky="w")
                    row_entries.append(label)
                else:
                    entry = customtkinter.CTkEntry(self.scrollable_frame, font=("Arial", 12), width=entry_width)
                    entry.insert(0, str(data[j]))
                    entry.grid(row=i, column=j, padx=10, pady=5)
                    row_entries.append(entry)
            self.entries.append(row_entries)

        self.update_scrollregion()

    def clear_entries(self):
        for row_entries in self.entries:
            for widget in row_entries:
                widget.destroy()
        self.entries.clear()

    def load_data(self):
        attendance_data = fetch_user_attendance1(self.user_id, self.yearmonth)
        self.update_entries(attendance_data)

    def back_screen(self, index):
        self.main_app.show_next_screen(index)

    def select_year(self, event):
        selected_year = self.year_listbox.get(tk.ACTIVE)
        self.year_entry.delete(0, tk.END)
        self.year_entry.insert(0, selected_year)
        self.show_year_menus()
        self.update_yearmonth()

    def select_month(self, event):
        selected_month = self.month_listbox.get(tk.ACTIVE)
        self.month_entry.delete(0, tk.END)
        self.month_entry.insert(0, selected_month)
        self.show_month_menus()
        self.update_yearmonth()

    def show_year_menus(self):
        if not self.year_frame.winfo_ismapped():
            self.year_frame.place(relx=0.45, rely=0.22)
            self.year_listbox.pack(side="left")
            self.year_scrollbar.pack(side="right", fill="y")
        else:
            self.year_frame.place_forget()

    def show_month_menus(self):
        if not self.month_frame.winfo_ismapped():
            self.month_frame.place(relx=0.69, rely=0.22)
            self.month_listbox.pack(side="left")
            self.month_scrollbar.pack(side="right", fill="y")
        else:
            self.month_frame.place_forget()