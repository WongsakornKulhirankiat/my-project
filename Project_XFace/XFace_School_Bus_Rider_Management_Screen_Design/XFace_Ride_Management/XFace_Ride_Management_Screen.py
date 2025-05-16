import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk
import math
import os
from tkinter import PhotoImage

class Screen11(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#e6e6e6", width=600, height=500)
        self.pack_propagate(0)

        def create_grid_overall(rows, columns, frame):
            for i in range(rows):
                for j in range(columns):
                    
                    # Create Cell Grid

                    if i == 0 and j == 0:
                        text = ""
                        background_color="white"

                    elif i == 0 and j == 1:
                        text = "Elementary"
                        background_color="#d9d9d9"

                    elif i == 0 and j == 2:
                        text = "Middle"
                        background_color="#d9d9d9"

                    elif i == 0 and j == 3:
                        text = "High"
                        background_color="#d9d9d9"

                    elif i == 0 and j == 4:
                        text = "Submit"
                        background_color="#d9d9d9"

                    elif i == 1 and j == 0:
                        text = "Scheduled Ride"
                        background_color="#d9d9d9"

                    elif i == 2 and j == 0:
                        text = "Currenr Ride"
                        background_color="#d9d9d9"

                    elif i == 3 and j == 0:
                        text = "People left"
                        background_color="#d9d9d9"

                    elif i == 1 and j == 1:                
                        text = str(scheduled_ride_elementary)
                        background_color="white"

                    elif i == 1 and j == 2:
                        text = str(scheduled_ride_middle)
                        background_color="white"

                    elif i == 1 and j == 3:
                        text = str(scheduled_ride_high)
                        background_color="white"

                    elif i == 1 and j == 4:
                        text = str(scheduled_ride_submmit)
                        background_color="white"

                    elif i == 2 and j == 1:
                        text = str(current_ride_elementary)
                        background_color="white"

                    elif i == 2 and j == 2:
                        text = str(current_ride_middle)
                        background_color="white"

                    elif i == 2 and j == 3:
                        text = str(scheduled_ride_high)
                        background_color="white"

                    elif i == 2 and j == 4:
                        text = str(current_ride_submit)
                        background_color="white"

                    elif i == 3 and j == 1:
                        text = str(people_left_elementary)  
                        background_color="white"

                        if people_left_elementary == 0:
                            background_color="blue"  

                    elif i == 3 and j == 2:
                        text = str(people_left_middle)
                        background_color="white"

                        if people_left_middle == 0:
                            background_color="blue"    

                    elif i == 3 and j == 3:
                        text = str(people_left_high)
                        background_color="white"

                        if people_left_high == 0:
                            background_color="blue" 

                    elif i == 3 and j == 4:
                        text = str(people_left_submit)
                        background_color="white"

                        if people_left_submit > 0:
                            background_color="red"                                 

                    cell = tk.Label(master=frame, text=text, borderwidth=1, relief="solid", width=15, height=3, background=background_color)
                    # Set Position Cell in Grid
                    cell.grid(row=i, column=j)

        def create_grid_ride(student_list, frame):
            # Remove existing cells
            for cell in frame.grid_slaves():
                cell.grid_forget()

            # Create Headers
            cell = tk.Label(master=frame, text="Grand", borderwidth=1, relief="solid", width=17, height=3, background="#d9d9d9")
            cell.grid(row=0, column=0)
            cell = tk.Label(master=frame, text="Class", borderwidth=1, relief="solid", width=17, height=3, background="#d9d9d9")
            cell.grid(row=0, column=1)
            cell = tk.Label(master=frame, text="Name", borderwidth=1, relief="solid", width=17, height=3, background="#d9d9d9")
            cell.grid(row=0, column=2)
            cell = tk.Label(master=frame, text="Status", borderwidth=1, relief="solid", width=17, height=3, background="#d9d9d9")
            cell.grid(row=0, column=3)

            # Rows and Columns Value
            rowindex = 1
            colindex = 0

            # Create Cells
            for student in student_list:
                row_data = [
                    str(student["grand"]),
                    str(student["class"]),
                    str(student["name"]),
                    "x" if student["status"] else "○"
                ]
                for colindex, data in enumerate(row_data):
                    background_color = "red" if colindex == 3 and data == "x" else "white"
                    cell = tk.Label(master=frame, text=data, borderwidth=1, relief="solid", width=17, height=3, background=background_color)
                    cell.grid(row=rowindex, column=colindex)
                rowindex += 1

        # Function to change button color to green when clicked
        def change_grid_ride(button, student_list, frame):
            button.configure(fg_color="green")
            
            # Change color of other buttons back to white
            if button is element_btn:
                middle_btn.configure(fg_color="white")
                high_btn.configure(fg_color="white")
            elif button is middle_btn:
                element_btn.configure(fg_color="white")
                high_btn.configure(fg_color="white")
            elif button is high_btn:
                element_btn.configure(fg_color="white")
                middle_btn.configure(fg_color="white")

            create_grid_ride(student_list, frame)
                
            self.update()  # Update the window to reflect the changes immediately

        # List of Elementary students
        ride_Elementary = [
            {"grand": "1", "class": "1", "name": "John Marston", "status": False},
            {"grand": "2", "class": "1", "name": "Micheal Jordan", "status": False},
            {"grand": "1", "class": "3", "name": "Kevin Costner", "status": True},
        ]

        # List of Elementary students
        ride_Middle = [
            {"grand": "1", "class": "1", "name": "Cave Johnson", "status": True},
            {"grand": "2", "class": "1", "name": "Arthur Morgan", "status": True},
            {"grand": "1", "class": "3", "name": "Saul Goodman", "status": True},
        ]

        ride_High = [
            {"grand": "1", "class": "1", "name": "Jane Doe", "status": False},
            {"grand": "3", "class": "1", "name": "John Doe", "status": True},
            {"grand": "3", "class": "3", "name": "Lebron James", "status": True},
        ]

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Frame Step Frame
        step_frame = customtkinter.CTkFrame(master=self, width=600, height=50, fg_color="#e6e6e6", corner_radius=0)
        step_frame.pack()

        # Add "<" Button
        back_btn = customtkinter.CTkButton(master=step_frame, command= lambda: self.next_screen(5), width=30, height=30, text="<", text_color="black", font=("Arial", 30), fg_color="transparent", hover=False)
        back_btn.place(relx=0.02, rely=0.02)

        # Add Rider Label
        ridership_overall_label = customtkinter.CTkLabel(master=step_frame, text="Ridership - Overall", text_color="black", font=("Arial", 15))
        ridership_overall_label.place(relx=0.115, rely=0.15)

        #----------------------------------------------------------------------------
        #                                     Frame 2
        #----------------------------------------------------------------------------

        step_frame2 = customtkinter.CTkFrame(master=self, width=600, height=175, fg_color="#e6e6e6", corner_radius=0)
        step_frame2.pack()

        scheduled_ride_elementary = 10
        scheduled_ride_middle = 10
        scheduled_ride_high = 6
        scheduled_ride_submmit = scheduled_ride_elementary + scheduled_ride_middle + scheduled_ride_high

        current_ride_elementary = 8
        current_ride_middle = 10
        current_ride_high = 5
        current_ride_submit = current_ride_elementary + current_ride_middle + current_ride_high

        people_left_elementary = scheduled_ride_elementary - current_ride_elementary
        people_left_middle = scheduled_ride_middle - current_ride_middle
        people_left_high = scheduled_ride_high - current_ride_high
        people_left_submit = people_left_elementary + people_left_middle + people_left_high

        create_grid_overall(4,5, step_frame2)

        #----------------------------------------------------------------------------
        #                                     Frame 3
        #----------------------------------------------------------------------------
        step_frame3 = customtkinter.CTkFrame(master=self, width=600, height=110, fg_color="#e6e6e6", corner_radius=0)
        step_frame3.pack()

        # Add School Label
        school_label = customtkinter.CTkLabel(master=step_frame3, text="Change Scool", text_color="black", font=("Arial", 15))
        school_label.place(relx=0.04, rely=0.01)

        # Add Elementary Button
        element_btn = customtkinter.CTkButton(master=step_frame3, text="Elementary", text_color="black", hover_color="lightgray", font=("Arial", 15), border_width=1, width=120, height=50, fg_color="white")
        element_btn.place(relx=0.05, rely=0.25)

        # Add Middle Button
        middle_btn = customtkinter.CTkButton(master=step_frame3, text="Middle", text_color="black", hover_color="lightgray", font=("Arial", 15), border_width=1, width=120, height=50, fg_color="white")
        middle_btn.place(relx=0.4, rely=0.25)

        # Add High Button
        high_btn = customtkinter.CTkButton(master=step_frame3, text="High", text_color="black", hover_color="lightgray", font=("Arial", 15), border_width=1, width=120, height=50, fg_color="white")
        high_btn.place(relx=0.75, rely=0.25)

        # Add Ridership Label
        rider_label = customtkinter.CTkLabel(master=step_frame3, text="Ridership - Elementary", text_color="black", font=("Arial", 15))
        rider_label.place(relx=0.04, rely=0.74)

        # Bind button click events to change color
        element_btn.configure(command=lambda: change_grid_ride(element_btn, ride_Elementary, step_frame4))
        middle_btn.configure(command=lambda: change_grid_ride(middle_btn, ride_Middle, step_frame4))
        high_btn.configure(command=lambda: change_grid_ride(high_btn, ride_High, step_frame4))

        #----------------------------------------------------------------------------
        #                                     Frame 3
        #----------------------------------------------------------------------------
        step_frame4 = customtkinter.CTkScrollableFrame(master=self, width=520, height=145, orientation="vertical", fg_color="#e6e6e6", corner_radius=0, scrollbar_button_color="#57b19e", scrollbar_button_hover_color="#468e7e")
        step_frame4._scrollbar.configure(height=0)
        step_frame4._scrollbar.configure(width=25)

        step_frame4.pack(anchor="center")

        # Set initial grid
        change_grid_ride(element_btn, ride_Elementary, step_frame4)

    def next_screen(self, index):
        self.main_app.show_next_screen(index)