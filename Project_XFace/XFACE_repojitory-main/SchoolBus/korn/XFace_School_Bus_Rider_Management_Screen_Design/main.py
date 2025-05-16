import tkinter as tk
from tkinter import ttk
import customtkinter
import datetime
from XFace_Login.XFace_Login import Screen1
from XFace_Login.XFace_Reset_Password_Login import Screen2
from XFace_Login.XFace_Reset_Password_New_Password import Screen3
from XFace_Login.XFace_Date_Setting import Screen4
from XFace_Login.XFace_Menu import Screen5
from XFace_Register.XFace_Student_Registration_Screen1 import Screen6
from XFace_Register.XFace_Student_Registration_Screen2 import Screen7
from XFace_Register.XFace_Student_Registration_Screen3 import Screen8
from XFace_Student_List.XFace_Student_List import Screen9
from XFace_Student_List.XFace_Student_List_Edit_Screen import Screen10
from XFace_Ride_Management.XFace_Ride_Management_Screen import Screen11
from XFace_Register.XFace_Camera_Register.XFace_Camera_Register_Photo_Shoot import Screen12

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("XFace")
        self.root.geometry("600x500")

        # Stored Variables
        self.name = ""
        self.school = ""
        self.current_screen = 0
        self.current_password = "123456"
        self.date = datetime.datetime.now().date()

        # Disable window resizing
        self.root.resizable(False, False)

        # Create Canvas widget
        self.canvas = customtkinter.CTkCanvas(self.root, width=600, height=500)
        self.canvas.grid(row=0, column=0, sticky=tk.NSEW)

        # Create a Frame inside the Canvas to hold the screens
        self.container = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.container, anchor=tk.NW)

        # Create an instance of Screens
        self.screen1 = Screen1(self.root, self)
        self.screen2 = Screen2(self.root, self)
        self.screen3 = Screen3(self.root, self)
        self.screen4 = Screen4(self.root, self)
        self.screen5 = Screen5(self.root, self)
        self.screen6 = Screen6(self.root, self)
        self.screen7 = Screen7(self.root, self)
        self.screen8 = Screen8(self.root, self)
        self.screen9 = Screen9(self.root, self)
        self.screen10 = Screen10(self.root, self)
        self.screen11 = Screen11(self.root, self)
        self.screen12 = Screen12(self.root, self)

        # Pack Screens initially
        self.screen1.grid(row=0, column=0, sticky="nsew")

        # Set current screen index
        self.current_screen = 1

        # Disable window resizing and minimizing
        self.root.resizable(False, False)
        self.root.attributes('-toolwindow', True)

        # Bind the closing event to a function
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        # Do whatever you want here, like confirmation dialog or just ignore the event
        #print("Close button clicked. Ignoring window close.")
        pass

    def set_current_password(self, new_current_password):
        self.current_password = new_current_password

    def set_name(self, new_name):
        self.name = new_name
    
    def set_school(self, new_school):
        self.school = new_school

    def set_year(self, new_year):
        self.year = new_year

    def set_month(self, new_month):
        self.month = new_month

    def set_day(self, new_day):
        self.day = new_day

    def get_current_password(self):
        return self.current_password
    
    def get_name(self):
        return self.name
    
    def get_year(self):
        return self.year
    
    def get_month(self):
        return self.month
    
    def get_day(self):
        return self.day
    
    def get_school(self):
        return self.school

    def show_next_screen(self, index):
        # Hide the current screen
        if self.current_screen == 1:
            self.screen1.grid_remove()
        elif self.current_screen == 2:
            self.screen2.grid_remove()
        elif self.current_screen == 3:
            self.screen3.grid_remove()
        elif self.current_screen == 4:
            self.screen4.grid_remove() 
        elif self.current_screen == 5:
            self.screen5.grid_remove() 
        elif self.current_screen == 6:
            self.screen6.grid_remove()    
        elif self.current_screen == 7:
            self.screen7.grid_remove()
        elif self.current_screen == 8:
            self.screen8.grid_remove()
        elif self.current_screen == 9:
            self.screen9.grid_remove()
        elif self.current_screen == 10:
            self.screen10.grid_remove()
        elif self.current_screen == 11:
            self.screen11.grid_remove()
        elif self.current_screen == 12:
            self.screen12.grid_remove()
                
        # Show the next screen
        if index == 1:
            self.screen1.grid(row=0, column=0, sticky="nsew")
            self.screen1.get_current_password()
            self.current_screen = index
        elif index == 2:
            self.screen2.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 3:
            self.screen3.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 4:
            self.screen4.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 5:
            self.screen5.grid(row=0, column=0, sticky="nsew")
            self.screen5.get_year()
            self.screen5.get_month()
            self.screen5.get_day()
            self.current_screen = index
        elif index == 6:
            self.screen6.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 7:
            self.screen7.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 8:
            self.current_screen = index
            self.screen8.get_name()
            self.screen8.get_school()
            self.screen8.grid(row=0, column=0, sticky="nsew")
        elif index == 9:
            self.current_screen = index
            self.screen9.grid(row=0, column=0, sticky="nsew")
        elif index == 10:
            self.current_screen = index
            self.screen10.grid(row=0, column=0, sticky="nsew")
        elif index == 11:
            self.current_screen = index
            self.screen11.grid(row=0, column=0, sticky="nsew")
        elif index == 12:
            self.current_screen = index
            self.screen12.grid(row=0, column=0, sticky="nsew")

if __name__ == "__main__":
    app = MainApp()
    app.root.mainloop()