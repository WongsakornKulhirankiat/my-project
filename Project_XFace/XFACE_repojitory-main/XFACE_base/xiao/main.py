import tkinter as tk
import customtkinter
import datetime
from XFace_Login_Screen1 import Login1 #Screen1
from XFace_Date_Setting_Screen4 import Date_Setting #Screen4
from XFace_Menu_Screen5 import Menu1 #Screen5
from XFace_Menu_Screen3 import Menu2 #Screen3
from XFace_Department_Master_Screen6 import Department_Registration_Screen1 #Screen6
from XFace_Department_Master_Screen7 import Department_Registration_Screen2 #Screen7
from XFace_Department_Master_Screen8 import Department_Registration_Screen3 #Screen8
from XFace_Edit_AttendanceRecord_Screen11 import Edit_AttendanceRecord1 #Screen11
from XFace_Edit_AttendanceRecord_Screen2 import Edit_AttendanceRecord2 #Screen2
from XFace_ExcelOutput_Screen12 import Exceloutput1 #Screen12
from XFace_ExcelOutput_Screen13 import Exceloutput2 #Screen13
from XFace_User_List_Screen9 import Userinfo1 #Screen9
from XFace_User_List_Edit_Screen10 import Edituserinfo1 #Screen10
from XFace_User_Registration_Screen14 import User_Registration_Screen1 #Screen14
from XFace_User_Registration_Screen15 import User_Registration_Screen2 #Screen15
from XFace_User_Registration_Screen16 import User_Registration_Screen2_error #Screen16
from XFace_User_Registration_Screen17 import User_Registration_Screen3 #Screen17
from XFace_Face_Recognition_Screen18 import Face_Recognition_Screen1 #Screen18
from XFace_Face_Recognition_Success_Screen19 import Face_Recognition_Screen2 #Screen19
 
class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("XFace")
        self.root.geometry("600x500")
        # Disable window resizing and minimizing
        self.root.resizable(False, False)
        self.root.attributes('-fullscreen', True)

        # Stored Variables
        self.user_id = ""
        self.school = ""
        self.current_screen = 0
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
        self.screen1 = Login1(self.root, self)
        self.screen2 = Edit_AttendanceRecord2(self.root, self)
        self.screen3 = Menu2(self.root, self)
        self.screen4 = Date_Setting(self.root, self)
        self.screen5 = Menu1(self.root, self)
        self.screen6 = Department_Registration_Screen1(self.root, self)
        self.screen7 = Department_Registration_Screen2(self.root, self)
        self.screen8 = Department_Registration_Screen3(self.root, self)
        self.screen9 = Userinfo1(self.root, self)
        self.screen10 = Edituserinfo1(self.root, self)
        self.screen11 = Edit_AttendanceRecord1(self.root, self)
        self.screen12 = Exceloutput1(self.root, self)
        self.screen13 = Exceloutput2(self.root, self)
        self.screen14 = User_Registration_Screen1(self.root, self)
        self.screen15 = User_Registration_Screen2(self.root, self)
        self.screen16 = User_Registration_Screen2_error(self.root, self)
        self.screen17 = User_Registration_Screen3(self.root, self)
        self.screen18 = Face_Recognition_Screen1(self.root, self)
        self.screen19 = Face_Recognition_Screen2(self.root, self)

        # Pack Screens initially
        self.screen18.grid(row=0, column=0, sticky="nsew")

        # Set current screen index
        self.current_screen = 18

        # Bind the closing event to a function
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        # Do whatever you want here, like confirmation dialog or just ignore the event
        #print("Close button clicked. Ignoring window close.")
        pass

    def set_current_password(self, new_current_password):
        self.current_password = new_current_password

    def set_year(self, new_year):
        self.year = new_year

    def set_month(self, new_month):
        self.month = new_month

    def set_day(self, new_day):
        self.day = new_day

    def set_department_name(self, new_department_name):
        self.department_name = new_department_name

    def set_department_name_search(self, new_department_name_search):
        self.department_name_search = new_department_name_search

    def set_start_time(self, new_start_time):
        self.start_time = new_start_time

    def set_end_time(self, new_end_time):
        self.end_time = new_end_time
    
    def set_rest_time(self, new_rest_time):
        self.rest_time = new_rest_time
    
    def set_over_time(self, new_over_time):
        self.over_time = new_over_time

    def set_user_name(self, new_user_name):
        self.user_name = new_user_name
    
    def set_yearmonth(self, new_yearmonth):
        self.yearmonth = new_yearmonth
    
    def set_user_id(self, new_user_id):
        self.user_id = new_user_id
    
    def set_administrator(self, new_administrator):
        self.administrator = new_administrator

    def get_administrator(self):
        return self.administrator

    def get_current_password(self):
        return self.current_password
    
    def get_year(self):
        return self.year
    
    def get_month(self):
        return self.month
    
    def get_day(self):
        return self.day
    
    def get_department_name(self):
        return self.department_name

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time
    
    def get_rest_time(self):
        return self.rest_time
    
    def get_over_time(self):
        return self.over_time
    
    def get_user_name(self):
        return self.user_name
    
    def get_yearmonth(self):
        return self.yearmonth
    
    def get_user_id(self):
        return self.user_id
    
    def get_department_name_search(self):
        return self.department_name_search

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
        elif self.current_screen == 13:
            self.screen13.grid_remove()
        elif self.current_screen == 14:
            self.screen14.grid_remove()
        elif self.current_screen == 15:
            self.screen15.grid_remove()
        elif self.current_screen == 16:
            self.screen16.grid_remove()
        elif self.current_screen == 17:
            self.screen17.grid_remove()           
        elif self.current_screen == 18:
            self.screen18.grid_remove()
        elif self.current_screen == 19:
            self.screen19.grid_remove()           

        # Show the next screen
        if index == 1:
            self.screen1.grid(row=0, column=0, sticky="nsew")
            #self.screen1.get_current_password()
            self.current_screen = index
        elif index == 2:
            self.screen2.grid(row=0, column=0, sticky="nsew")
            self.screen2.get_user_id()
            self.current_screen = index
        elif index == 3:
            self.screen3.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 4:
            self.screen4.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 5:
            self.screen5.grid(row=0, column=0, sticky="nsew")
            #self.screen5.get_year()
            #self.screen5.get_month()
            #self.screen5.get_day()
            self.current_screen = index
        elif index == 6:
            self.current_screen = index
            self.screen6.grid(row=0, column=0, sticky="nsew")
        elif index == 7:
            self.screen7.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 8:
            self.screen8.grid(row=0, column=0, sticky="nsew")
            self.screen8.get_department_name()
            self.screen8.get_start_time()
            self.screen8.get_end_time()
            self.screen8.get_rest_time()
            self.screen8.get_over_time()
            self.current_screen = index
        elif index == 9:
            self.current_screen = index
            self.screen9.grid(row=0, column=0, sticky="nsew")
        elif index == 10:
            self.current_screen = index
            self.screen10.get_department_name()
            self.screen10.get_user_name()
            self.screen10.get_current_password()
            self.screen10.grid(row=0, column=0, sticky="nsew")
        elif index == 11:
            self.screen11.grid(row=0, column=0, sticky="nsew")
            self.screen11.get_user_id()
            self.current_screen = index
        elif index == 12:
            self.current_screen = index
            self.screen12.grid(row=0, column=0, sticky="nsew")
        elif index == 13:
            self.current_screen = index
            self.screen13.get_user_id()
            self.screen13.grid(row=0, column=0, sticky="nsew")
        elif index == 14:
            self.current_screen = index
            self.screen14.grid(row=0, column=0, sticky="nsew")
        elif index == 15:
            self.current_screen = index
            self.screen15.grid(row=0, column=0, sticky="nsew")
        elif index == 16:
            self.current_screen = index
            self.screen16.grid(row=0, column=0, sticky="nsew")
        elif index == 17:
            self.current_screen = index
            self.screen17.get_administrator()
            self.screen17.get_department()
            self.screen17.get_password()
            self.screen17.get_username()
            self.screen17.get_userid()
            self.screen17.grid(row=0, column=0, sticky="nsew")
        elif index == 18:
            self.current_screen = index
            self.screen18.grid(row=0, column=0, sticky="nsew")
        elif index == 19:
            self.current_screen = index
            self.screen19.get_username()
            self.screen19.grid(row=0, column=0, sticky="nsew")

if __name__ == "__main__":
    app = MainApp()
    app.root.mainloop()