import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk

class Screen3(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#424242", width=600, height=500)
        self.pack_propagate(0)

        # password
        self.new_password = ""
        self.retype_password = ""
        self.current_password = None
        self.get_current_password()
        
        # Count for length password
        self.new_password_count = 0
        self.retype_password_count = 0

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Password Frame
        self.password_frame = customtkinter.CTkFrame(self, width=350, height=500, fg_color="#424242", corner_radius=0)
        self.password_frame.place(x=0)

        # Add "<" Button
        back_btn = customtkinter.CTkButton(master=self.password_frame, command= lambda: self.main_app.show_next_screen(2), width=30, height=30, text="<", text_color="white", font=("Arial", 30), fg_color="transparent", hover=False)
        back_btn.place(relx=0.02, rely=0.02)

        # Add Password Label
        password_label = customtkinter.CTkLabel(self.password_frame, text_color="#a8a8a8", text="New Password", font=("Arial", 20))
        password_label.place(x=30, y=118)

        # Add Password Entries
        #num1_entry = customtkinter.CTkEntry(self.password_frame, text_color="white", font=("Arial", 30), width=50, height=35, fg_color="#424242", show="✱", placeholder_text="✱", placeholder_text_color="white", justify="left", border_width=0)
        #num1_entry.place(x=30, y=160)

        #num2_entry = customtkinter.CTkEntry(self.password_frame, text_color="white", font=("Arial", 30), width=50, height=35, fg_color="#424242", show="✱", placeholder_text="✱", placeholder_text_color="white", justify="left", border_width=0)
        #num2_entry.place(x=80, y=160)

        #num3_entry = customtkinter.CTkEntry(self.password_frame, text_color="white", font=("Arial", 30), width=50, height=35, fg_color="#424242", show="✱", placeholder_text="✱", placeholder_text_color="white", justify="left", border_width=0)
        #num3_entry.place(x=130, y=160)

        #num4_entry = customtkinter.CTkEntry(self.password_frame, text_color="white", font=("Arial", 30), width=50, height=35, fg_color="#424242", show="✱", placeholder_text="✱", placeholder_text_color="white", justify="left", border_width=0)
        #num4_entry.place(x=180, y=160)

        #num5_entry = customtkinter.CTkEntry(self.password_frame, text_color="white", font=("Arial", 30), width=50, height=35, fg_color="#424242", show="✱", placeholder_text="✱", placeholder_text_color="white", justify="left", border_width=0)
        #num5_entry.place(x=230, y=160)

        #num6_entry = customtkinter.CTkEntry(self.password_frame, text_color="white", font=("Arial", 30), width=50, height=35, fg_color="#424242", show="✱", placeholder_text="✱", placeholder_text_color="white", justify="left", border_width=0)
        #num6_entry.place(x=280, y=160)

        #--------------------------------------------
        #               Password Canvas
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
        canvas.place(x=27, y=195)

        # Add Line
        canvas.create_line(5, 5, 45, 5, width=0.5, fill="white")
        canvas.create_line(55, 5, 95, 5, width=0.5, fill="white")
        canvas.create_line(105, 5, 145, 5, width=0.5, fill="white")
        canvas.create_line(155, 5, 195, 5, width=0.5, fill="white")
        canvas.create_line(205, 5, 245, 5, width=0.5, fill="white")
        canvas.create_line(255, 5, 295, 5, width=0.5, fill="white")

        # Add New Password Label
        new_password_label = customtkinter.CTkLabel(self.password_frame, text_color="#a8a8a8", text="Retype Password", font=("Arial", 20))
        new_password_label.place(x=30, y=220)

        # Add New Password Entries
        #new1_entry = customtkinter.CTkEntry(self.password_frame, text_color="white", font=("Arial", 30), width=50, height=35, fg_color="#424242", show="✱", placeholder_text="✱", placeholder_text_color="white", justify="left", border_width=0)
        #new1_entry.place(x=30, y=262)

        #new2_entry = customtkinter.CTkEntry(self.password_frame, text_color="white", font=("Arial", 30), width=50, height=35, fg_color="#424242", show="✱", placeholder_text="✱", placeholder_text_color="white", justify="left", border_width=0)
        #new2_entry.place(x=80, y=262)

        #new3_entry = customtkinter.CTkEntry(self.password_frame, text_color="white", font=("Arial", 30), width=50, height=35, fg_color="#424242", show="✱", placeholder_text="✱", placeholder_text_color="white", justify="left", border_width=0)
        #new3_entry.place(x=130, y=262)

        #new4_entry = customtkinter.CTkEntry(self.password_frame, text_color="white", font=("Arial", 30), width=50, height=35, fg_color="#424242", show="✱", placeholder_text="✱", placeholder_text_color="white", justify="left", border_width=0)
        #new4_entry.place(x=180, y=262)

        #new5_entry = customtkinter.CTkEntry(self.password_frame, text_color="white", font=("Arial", 30), width=50, height=35, fg_color="#424242", show="✱", placeholder_text="✱", placeholder_text_color="white", justify="left", border_width=0)
        #new5_entry.place(x=230, y=262)

        #new6_entry = customtkinter.CTkEntry(self.password_frame, text_color="white", font=("Arial", 30), width=50, height=35, fg_color="#424242", show="✱", placeholder_text="✱", placeholder_text_color="white", justify="left", border_width=0)
        #new6_entry.place(x=280, y=262)

        #--------------------------------------------
        #             New Password Canvas
        #--------------------------------------------

        # Create Canvas
        canvas2 = customtkinter.CTkCanvas(
            self.password_frame,
            width = 600,
            height = 10,
            bg = "#424242",
            highlightthickness = 0,
            bd = 0
        )
        canvas2.place(x=27, y=295)

        # Add Line
        canvas2.create_line(5, 5, 45, 5, width=1, fill="white")
        canvas2.create_line(55, 5, 95, 5, width=1, fill="white")
        canvas2.create_line(105, 5, 145, 5, width=1, fill="white")
        canvas2.create_line(155, 5, 195, 5, width=1, fill="white")
        canvas2.create_line(205, 5, 245, 5, width=1, fill="white")
        canvas2.create_line(255, 5, 295, 5, width=1, fill="white")

        # Add Save Button
        save_btn =customtkinter.CTkButton(master=self.password_frame, command= lambda: self.next_screen(), text="Save", text_color="black", font=("Arial Bold", 20), fg_color="white", width=90, height=45, corner_radius=10, border_width=0, hover_color="gray", cursor="hand2")
        save_btn.place(x=132, y=350)

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

            print("----------------------")
            print("Count New Password : ",self.new_password_count)
            print("Count Retype Password : ",self.retype_password_count)
            print("----------------------")

            if (self.new_password_count < 6):
                # Add number to password
                self.new_password += str(number)

            if (self.new_password_count == 6):

                if (self.retype_password_count < 6):

                    # Add number to password
                    self.retype_password += str(number)
                      
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
            if self.new_password:

                if not self.retype_password:

                    # Delete New Password Right Position
                    self.new_password = self.new_password[:-1]

                    # Delete New Password From Screen
                    last_widget_index = len(self.password_frame.winfo_children()) - 1
                    last_label_widget = self.password_frame.winfo_children()[last_widget_index]
                    last_label_widget.destroy()
                
                    # Reduce New Password Count -1
                    self.new_password_count -= 1

                if self.retype_password:

                    # Delete Retype Password Right Position
                    self.retype_password = self.retype_password[:-1]

                    # Delete Retype Password From Screen
                    last_widget_index = len(self.password_frame.winfo_children()) - 1
                    last_label_widget = self.password_frame.winfo_children()[last_widget_index]
                    last_label_widget.destroy()
                
                    # Reduce Retype Password Count -1
                    self.retype_password_count -= 1

    # Clear password and reset count
    def clear_password(self, frame):
        self.new_password_count = 0
        self.retype_password_count = 0
        self.new_password = ""
        self.retype_password = "" 

        for child in frame.winfo_children():
            if isinstance(child, customtkinter.CTkLabel) and child.cget("text") not in ["New Password", "Retype Password"]:
                child.destroy()

    def display_password(self):

        # Check length password
        if (self.new_password_count < 6):
            
            # Show New Password In Terminal
            print("New Password:", self.new_password)
            print("----------------------")

            if len(self.new_password) >= self.new_password_count + 1:

                # Add Password on Screen
                new_password_label = customtkinter.CTkLabel(self.password_frame, text_color="#a8a8a8", text=self.new_password[self.new_password_count], font=("Arial", 30))
                new_password_label.place(x=43 + self.new_password_count * 50, y=155)

                # Count New Password Add
                self.new_password_count += 1

        if (self.new_password_count == 6):

            if (self.retype_password_count < 6):

                # Show Retype Password In Terminal
                print("Retype Password:", self.retype_password)
                print("----------------------")
        
                if len(self.retype_password) >= self.retype_password_count + 1:

                    # Add Password on Screen
                    retype_password_label = customtkinter.CTkLabel(self.password_frame, text_color="#a8a8a8", text=self.retype_password[self.retype_password_count], font=("Arial", 30))
                    retype_password_label.place(x=43 + self.retype_password_count * 50, y=255)

                    # Count Retype Password Add
                    self.retype_password_count += 1
        
        # Check if password is correct
    
    def check_password(self):

        print("New Password: ", self.new_password)
        print("Retype Password: ", self.retype_password)
        print("Current Password: ", self.current_password)
        print("----------------------")

        if (self.new_password == self.retype_password):

            self.current_password = self.new_password
                
            #Add Pop Up 
            tkinter.messagebox.showinfo("Success", "Password is saved")

            self.clear_password(self.password_frame)
            self.main_app.show_next_screen(1)
            
        if (self.new_password != self.retype_password):
                
            tkinter.messagebox.showinfo("Failed", "Password is wrong")   
            self.clear_password(self.password_frame)
        

    def next_screen(self):
            if self.new_password_count + self.retype_password_count  == 12:
                self.check_password()          

    def get_current_password(self):
        self.current_password = self.main_app.get_current_password()
        print(self.current_password)