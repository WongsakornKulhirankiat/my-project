import tkinter as tk
from tkinter import ttk
import customtkinter
import datetime

from XFace_Face_Recognition.XFace_Face_Recognition import Screen1
from XFace_Face_Recognition.XFace_Face_Recognition_Success import Screen2
from XFace_Login.XFace_Login import Screen3
from XFace_Login.XFace_Menu_Admin import Screen4
from XFace_Login.XFace_Menu_User import Screen5
from XFace_User_Register.XFace_User_Registration_Screen1 import Screen6
from XFace_User_Register.XFace_User_Registration_Screen2 import Screen7
from XFace_User_Register.XFace_User_Registration_Screen2_Error import Screen8
from XFace_User_Register.XFace_User_Registration_Screen3 import Screen9
from XFace_User_Register.XFace_Camera_Register.XFace_Camera_Register_Photo_Shoot import Screen10
from XFace_User_Register.XFace_USB.XFace_USB_Loading import Screen11
from XFace_User_Register.XFace_USB.XFace_USB_Choose_File import Screen12
from XFace_User_List.XFace_User_List import Screen13
from XFace_User_List.XFace_User_List_Edit_Screen import Screen14
from XFace_Department_List.XFace_Department_List import Screen15
from XFace_Department_List.XFace_Department_Registration import Screen16
from XFace_Department_List.XFace_Department_Edit import Screen17
from XFace_Edit_Attendance_Record.XFace_Edit_AttendanceRecord_Screen1 import Screen18
from XFace_ExcelOutput.XFace_ExcelOutput_Admin import Screen19
from XFace_ExcelOutput.XFace_ExcelOutput_User import Screen20

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("XFace Base")
        self.root.geometry("600x500")

        # Stored Variables
        self.name = ""
        self.school = ""
        self.current_screen = 0
        self.user_id = "123456"
        self.password = "123456"
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
        self.screen13 = Screen13(self.root, self)
        self.screen14 = Screen14(self.root, self)
        self.screen15 = Screen15(self.root, self)
        self.screen16 = Screen16(self.root, self)
        self.screen17 = Screen17(self.root, self)
        self.screen18 = Screen18(self.root, self)
        self.screen19 = Screen19(self.root, self)
        self.screen20 = Screen20(self.root, self)

        # Pack Screens initially
        self.screen1.grid(row=0, column=0, sticky="nsew")

        # Set current screen index
        self.current_screen = 1

        ## Disable window minimizing
        self.root.attributes('-topmost', True)  # Always on top
        self.root.attributes('-fullscreen', True)  # Set fullscreen mode

        # Hide the window and then show it to remove window decorations
        self.root.withdraw()
        self.root.after(0, self.show_root_window)

        # Bind the closing event to a function
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def show_root_window(self):
        self.root.deiconify()
        self.root.update_idletasks()

    def on_close(self):
        # Do whatever you want here, like confirmation dialog or just ignore the event
        pass

    def set_current_password(self, new_current_password):
        self.current_password = new_current_password

    def set_username(self, new_username):
        self.username = new_username
    
    def set_password(self, new_password):
        self.password = new_password

    def set_department(self, new_department):
        self.department = new_department

    def set_administrator(self, new_administartor):
        self.administrator = new_administartor

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password
    
    def get_department(self):
        return self.department
    
    def get_administrator(self):
        return self.administrator

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
        elif self.current_screen == 20:
            self.screen20.grid_remove()
                
        # Show the next screen
        if index == 1:
            self.screen1.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 2:
            self.screen2.grid(row=0, column=0, sticky="nsew")
            self.screen2.get_username()
            self.current_screen = index
        elif index == 3:
            self.screen3.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 4:
            self.screen4.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 5:
            self.screen5.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 6:
            self.screen6.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 7:
            self.screen7.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 8:
            self.screen8.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 9:
            self.screen9.grid(row=0, column=0, sticky="nsew")
            self.screen9.get_username()
            self.screen9.get_password()
            self.screen9.get_department()
            self.screen9.get_administrator()
            self.current_screen = index
        elif index == 10:
            self.screen10.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 11:
            self.screen11.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 12:
            self.screen12.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 13:
            self.screen13.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 14:
            self.screen14.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 15:
            self.screen15.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 16:
            self.screen16.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 17:
            self.screen17.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 18:
            self.screen18.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 19:
            self.screen19.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index
        elif index == 20:
            self.screen20.grid(row=0, column=0, sticky="nsew")
            self.current_screen = index

if __name__ == "__main__":
    app = MainApp()
    app.root.mainloop()