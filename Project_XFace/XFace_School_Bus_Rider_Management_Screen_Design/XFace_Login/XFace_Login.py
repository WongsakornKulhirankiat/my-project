import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk

class Screen1(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#424242", width=600, height=500)
        self.pack_propagate(0)

        # Password
        self.password = ""
        self.current_password = "123456"

        # Count for length password
        self.count = 0

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Password Frame
        self.password_frame = customtkinter.CTkFrame(self, width=350, height=500, fg_color="#424242", corner_radius=0)
        self.password_frame.place(x=0)

        # Add Password Label
        password_label = customtkinter.CTkLabel(self.password_frame, text_color="#a8a8a8", text="Password", font=("Arial", 20))
        password_label.place(x=30, y=165)

        # Add Number Entries
        num1_entry = customtkinter.CTkEntry(self.password_frame, text_color="white", font=("Arial", 30), width=50, height=35, fg_color="#424242", show="✱", placeholder_text="✱", placeholder_text_color="white", justify="left", border_width=0)
        num1_entry.place(x=30, y=200)

        num2_entry = customtkinter.CTkEntry(self.password_frame, text_color="white", font=("Arial", 30), width=50, height=35, fg_color="#424242", show="✱", placeholder_text="✱", placeholder_text_color="white", justify="left", border_width=0)
        num2_entry.place(x=80, y=200)

        num3_entry = customtkinter.CTkEntry(self.password_frame, text_color="white", font=("Arial", 30), width=50, height=35, fg_color="#424242", show="✱", placeholder_text="✱", placeholder_text_color="white", justify="left", border_width=0)
        num3_entry.place(x=130, y=200)

        num4_entry = customtkinter.CTkEntry(self.password_frame, text_color="white", font=("Arial", 30), width=50, height=35, fg_color="#424242", show="✱", placeholder_text="✱", placeholder_text_color="white", justify="left", border_width=0)
        num4_entry.place(x=180, y=200)

        num5_entry = customtkinter.CTkEntry(self.password_frame, text_color="white", font=("Arial", 30), width=50, height=35, fg_color="#424242", show="✱", placeholder_text="✱", placeholder_text_color="white", justify="left", border_width=0)
        num5_entry.place(x=230, y=200)

        num6_entry = customtkinter.CTkEntry(self.password_frame, text_color="white", font=("Arial", 30), width=50, height=35, fg_color="#424242", show="✱", placeholder_text="✱", placeholder_text_color="white", justify="left", border_width=0)
        num6_entry.place(x=280, y=200)

        # Add Reset Password Button
        reset_btn = customtkinter.CTkButton(master=self.password_frame, command= lambda: self.next_screen(2), text="Reset Password", text_color="black", font=("Arial", 20), fg_color="white", width=210, height=40, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        reset_btn.place(x=70, y=350)

        # Add Hidden Button
        next_btn = customtkinter.CTkButton(master=self.password_frame, command= lambda: self.next_screen(4), fg_color="transparent", text="", hover=False, cursor="hand2", width=300, height=40)
        next_btn.place(x=30, y=200)

        #--------------------------------------------
        #                   Canvas
        #--------------------------------------------

        # Create Canvas
        canvas = customtkinter.CTkCanvas(
            self.password_frame,
            width = 600,
            height = 10,
            bg = "#424242",
            highlightthickness = 0,
            bd = 0
        )
        canvas.place(x=27, y=240)

        # Add Line
        canvas.create_line(5, 5, 45, 5, width=1, fill="white")
        canvas.create_line(55, 5, 95, 5, width=1, fill="white")
        canvas.create_line(105, 5, 145, 5, width=1, fill="white")
        canvas.create_line(155, 5, 195, 5, width=1, fill="white")
        canvas.create_line(205, 5, 245, 5, width=1, fill="white")
        canvas.create_line(255, 5, 295, 5, width=1, fill="white")

        #----------------------------------------------------------------------------
        #                                     Frame 2
        #----------------------------------------------------------------------------
        # Add Numpad Frame
        self.numpad_frame = customtkinter.CTkFrame(self, width=240, height=305, fg_color="#424242", corner_radius=0)
        self.numpad_frame.place(x=360, y=100)

        #--------------------------------------------
        #                   Numpad
        #--------------------------------------------

        num1_btn = customtkinter.CTkButton(master=self.numpad_frame, text="1", text_color="black", font=("Tahoma", 35), width=75, height=75, fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        num1_btn.grid(row=1, column=1)

        num2_btn = customtkinter.CTkButton(master=self.numpad_frame, text="2", text_color="black", font=("Tahoma", 35), width=75, height=75, fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        num2_btn.grid(row=1, column=2, padx=1)

        num3_btn = customtkinter.CTkButton(master=self.numpad_frame, text="3", text_color="black", font=("Tahoma", 35), width=75, height=75, fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        num3_btn.grid(row=1, column=3)

        num4_btn = customtkinter.CTkButton(master=self.numpad_frame, text="4", text_color="black", font=("Tahoma", 35), width=75, height=75, fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        num4_btn.grid(row=2, column=1, pady=1)

        num5_btn = customtkinter.CTkButton(master=self.numpad_frame, text="5", text_color="black", font=("Tahoma", 35), width=75, height=75, fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        num5_btn.grid(row=2, column=2, padx=1, pady=1)

        num6_btn = customtkinter.CTkButton(master=self.numpad_frame, text="6", text_color="black", font=("Tahoma", 35), width=75, height=75, fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        num6_btn.grid(row=2, column=3, pady=1)

        num7_btn = customtkinter.CTkButton(master=self.numpad_frame, text="7", text_color="black", font=("Tahoma", 35), width=75, height=75, fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        num7_btn.grid(row=3, column=1)

        num8_btn = customtkinter.CTkButton(master=self.numpad_frame, text="8", text_color="black", font=("Tahoma", 35), width=75, height=75, fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        num8_btn.grid(row=3, column=2, padx=1)

        num9_btn = customtkinter.CTkButton(master=self.numpad_frame, text="9", text_color="black", font=("Tahoma", 35), width=75, height=75, fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        num9_btn.grid(row=3, column=3)

        del_btn = customtkinter.CTkButton(master=self.numpad_frame, text="⌫", text_color="black", font=("Tahoma", 35), width=75, height=75, fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        del_btn.grid(row=4, column=1, pady=1)

        num0_btn = customtkinter.CTkButton(master=self.numpad_frame, text="0", text_color="black", font=("Tahoma", 35), width=75, height=75, fg_color="#d6d6d6", corner_radius=10, hover_color="gray", cursor="hand2")
        num0_btn.grid(row=4, column=2, padx=1, pady=1)

        def add_to_password(number):

            # Add number to password
            self.password += str(number)

            # Run Function display_password
            self.display_password()
        
        # Set function number pad
        num1_btn.configure(command=lambda: add_to_password(1))
        num2_btn.configure(command=lambda: add_to_password(2))
        num3_btn.configure(command=lambda: add_to_password(3))
        num4_btn.configure(command=lambda: add_to_password(4))
        num5_btn.configure(command=lambda: add_to_password(5))
        num6_btn.configure(command=lambda: add_to_password(6))
        num7_btn.configure(command=lambda: add_to_password(7))
        num8_btn.configure(command=lambda: add_to_password(8))
        num9_btn.configure(command=lambda: add_to_password(9))
        num0_btn.configure(command=lambda: add_to_password(0))
        del_btn.configure(command=lambda: delete_from_password())

        def delete_from_password():
            if self.password:
                # Delete Password Right Position
                self.password = self.password[:-1]

                # Delete Password From Screen
                last_widget_index = len(self.password_frame.winfo_children()) - 1
                last_label_widget = self.password_frame.winfo_children()[last_widget_index]
                last_label_widget.destroy()
                
                # Reduce Count -1
                self.count -= 1



    # Clear password and reset count
    def clear_password(self, frame):
        self.count = 0
        self.password = "" 

        for child in frame.winfo_children():
            if isinstance(child, customtkinter.CTkLabel) and child.cget("text") != "Password":
                child.destroy()

    def display_password(self):
        
        # Show Password In Terminal
        print("Password:", self.password)

        # Check length password
        if (self.count < 6):

            if len(self.password) >= self.count + 1:

                # Add Password on Screen
                password_label = customtkinter.CTkLabel(self.password_frame, text_color="#a8a8a8", text=self.password[self.count], font=("Arial", 30))
                password_label.place(x=43 + self.count * 50, y=205)
        
        # Count Add
        self.count += 1

        # Check if password is correct
        if self.count == 6:
            self.check_password()
    
    def check_password(self):
        print("Password:", self.password)
        print("Correct Password:", self.current_password)
        if self.password == self.current_password:
            self.clear_password(self.password_frame)
            self.next_screen(4)
        else:   
            self.clear_password(self.password_frame)

    def get_current_password(self):
        self.current_password = self.main_app.get_current_password()
        print(self.current_password)

    def next_screen(self, index):
        self.main_app.show_next_screen(index)
        self.main_app.set_current_password(self.current_password)