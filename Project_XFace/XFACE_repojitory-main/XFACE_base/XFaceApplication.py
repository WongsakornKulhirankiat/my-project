import tkinter as tk
from tkinter import messagebox
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

import time
from datetime import datetime
from threading import Thread
from multiprocessing import Process, Value

from XFaceExcelOutput import EmployeeInfo
from XFaceExcelOutput import AttendanceRecord
employeeinfo = EmployeeInfo()
attendancerecord = AttendanceRecord()

import XFaceDAO 
dbaccess = XFaceDAO.XFaceDAO()

import BusCamera   #PCで作業を行う場合はBusCamera_MyPCに変更
#import BusCamera_MyPC

class XFaceKornApp():
    def __init__ (self):

        masterlist = dbaccess.getWorkingMaster()   #get master info
        self.startmaster = masterlist[0][0]
        self.endmaster = masterlist[0][1]
        self.restmaster = masterlist[0][2]
        self.overtimemaster = masterlist[0][3]

        self.camerastartflag = True

        self.root = tk.Tk()
        self.root.title("XFace")
        self.root.geometry("600x500")

        # Stored Variables
        self.name = ""
        self.school = ""
        self.current_screen = 0
        self.current_password = "123456"
        self.date = datetime.now().date()

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
        #self.root.attributes('-toolwindow', True)

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

    def camera_start(self):
        if self.camerastartflag:
            self.camerastartflag = False
            BusCamera.camera_start(self)
            #BusCamera_MyPC.camera_start()
    
    def camera_stop(self):
        if not self.camerastartflag:
            BusCamera.camera_stop()
            #BusCamera_MyPC.camera_stop()
            self.camerastartflag = True
    
    def FaceRecognition_match(self,userid,recognitiontime):
        accessid = ""
        accessid_plus1 = ""
        accessid = dbaccess.getAccessRecord_accessid(userid)
        accessid_plus1 = accessid + 1
        if accessid % 2 ==0:   #guusuu
            if accessid == 0:
                dbaccess.insertAccessRecord_Enter(userid,recognitiontime,accessid_plus1)
                dt1 = datetime.strptime(recognitiontime, "%H:%M")
                dt2 = datetime.strptime(self.startmaster, "%H:%M")
                caluculate = dt2 - dt1
                latecheck = round((caluculate.total_seconds() / 3600), 2)
                if latecheck < 0:
                    dbaccess.insertAttendanceRecord_StartingworkTime(userid,recognitiontime)
                else:
                    dbaccess.insertAttendanceRecord_StartingworkTime(userid,self.startmaster)
            else:
                dbaccess.insertAccessRecord_Enter(userid,recognitiontime,accessid_plus1)
        else:
            dbaccess.insertAccessRecord_Exit(userid,recognitiontime,accessid_plus1)
            self.WorkingTimeCaluculate(userid,recognitiontime)

    def WorkingTimeCaluculate(self,userid,exittime):
        resttime = self.restmaster
        startingworktime = dbaccess.getAttendanceRecord_StartingworkTime(userid)
        dt1 = datetime.strptime(startingworktime, "%H:%M")
        dt2 = datetime.strptime(exittime, "%H:%M")
        caluculate = dt2 - dt1
        workingtime = round((caluculate.total_seconds() / 3600) - resttime, 2)
        dbaccess.updateAttendanceRecord_workingtime(userid,exittime,workingtime)

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
            self.camera_stop()
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
            self.camera_start()
        elif index == 12:
            self.current_screen = index
            self.screen12.grid(row=0, column=0, sticky="nsew")

class XFaceMainApp():
    def __init__ (self):

        masterlist = dbaccess.getWorkingMaster()   #get master info
        self.startmaster = masterlist[0][0]
        self.endmaster = masterlist[0][1]
        self.restmaster = masterlist[0][2]
        self.overtimemaster = masterlist[0][3]

        self.camerastartflag = True

        self.root = tk.Tk()
        self.root.title("XFace")
        self.root.geometry("600x500")

        button1 = tk.Button(self.root, text="Exceloutput UserInfo", command=lambda:self.ExcelOutput(entry3.get()))
        button1.pack(pady=10)

        button2 = tk.Button(self.root, text="Exceloutput AttendanceRecor_user", command=lambda:self.ExcelOutput_user(entry1.get(),entry2.get(),entry3.get()))
        button2.pack(pady=10)

        button3 = tk.Button(self.root, text="Exceloutput AttendanceRecor_list", command=lambda:self.ExcelOutput_list(entry3.get()))
        button3.pack(pady=10)

        #camera start
        button4 = tk.Button(self.root, text="camera start", command=self.camera_start)
        button4.pack(pady=10)

        #camera start
        button5 = tk.Button(self.root, text="camera stop", command=self.camera_stop)
        button5.pack(pady=10)
     
        #userid
        label1 = tk.Label(self.root, text="userid")
        label1.pack()
        entry1 = tk.Entry(self.root)
        entry1.pack(pady=10)

        #username
        label2 = tk.Label(self.root, text="username")
        label2.pack()
        entry2 = tk.Entry(self.root)
        entry2.pack(pady=10)

        #yearmonth
        label3 = tk.Label(self.root, text="yearmonth")
        label3.pack()
        entry3 = tk.Entry(self.root)
        entry3.pack(pady=10)

    def ExcelOutput(self,yearmonth):
        if yearmonth == "":
            messagebox.showerror("ExcelOutput", "yeamonth empty")
        else:
            res = messagebox.askokcancel("ExcelOutput", "UserInfo ExcelOutput?")
            if res:
                employeeinfo.ExcelOutput(yearmonth)
            
    def ExcelOutput_user(self,userid,username,yearmonth):
        if userid == "" or username == "" or yearmonth == "":
            messagebox.showerror("ExcelOutput", "empty")
        else:
            res = messagebox.askokcancel("ExcelOutput", "AttendanceRecor_user ExcelOutput?")
            if res:
                attendancerecord.ExcelOutput_user(userid,username,yearmonth)

    def ExcelOutput_list(self,yearmonth):
        if yearmonth == "":
            messagebox.showerror("ExcelOutput", "yeamonth empty")
        else:
            res = messagebox.askokcancel("ExcelOutput", "AttendanceRecor_list ExcelOutput?")
            if res:
                attendancerecord.ExcelOutput_list(yearmonth)

    def camera_start(self):
        if self.camerastartflag:
            self.camerastartflag = False
            BusCamera.camera_start(self)
            #BusCamera_MyPC.camera_start()
    
    def camera_stop(self):
        if not self.camerastartflag:
            BusCamera.camera_stop()
            #BusCamera_MyPC.camera_stop()
            self.camerastartflag = True
    
    def FaceRecognition_match(self,userid,recognitiontime):
        accessid = ""
        accessid_plus1 = ""
        accessid = dbaccess.getAccessRecord_accessid(userid)
        accessid_plus1 = accessid + 1
        if accessid % 2 ==0:   #guusuu
            if accessid == 0:
                dbaccess.insertAccessRecord_Enter(userid,recognitiontime,accessid_plus1)
                dt1 = datetime.strptime(recognitiontime, "%H:%M")
                dt2 = datetime.strptime(self.startmaster, "%H:%M")
                caluculate = dt2 - dt1
                latecheck = round((caluculate.total_seconds() / 3600), 2)
                if latecheck < 0:
                    dbaccess.insertAttendanceRecord_StartingworkTime(userid,recognitiontime)
                else:
                    dbaccess.insertAttendanceRecord_StartingworkTime(userid,self.startmaster)
            else:
                dbaccess.insertAccessRecord_Enter(userid,recognitiontime,accessid_plus1)
        else:
            dbaccess.insertAccessRecord_Exit(userid,recognitiontime,accessid_plus1)
            self.WorkingTimeCaluculate(userid,recognitiontime)

    def WorkingTimeCaluculate(self,userid,exittime):
        resttime = self.restmaster
        startingworktime = dbaccess.getAttendanceRecord_StartingworkTime(userid)
        dt1 = datetime.strptime(startingworktime, "%H:%M")
        dt2 = datetime.strptime(exittime, "%H:%M")
        caluculate = dt2 - dt1
        workingtime = round((caluculate.total_seconds() / 3600) - resttime, 2)
        dbaccess.updateAttendanceRecord_workingtime(userid,exittime,workingtime)

if __name__ == '__main__':
    #mainapp = XFaceMainApp()
    mainapp = XFaceKornApp()
    mainapp.root.mainloop()