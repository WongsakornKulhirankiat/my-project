##初期設定後に実行するモジュール

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import font
from tkinter import filedialog
import customtkinter as ctk
from PIL import Image

import time
import os
import glob
import cv2
from datetime import datetime
from datetime import timedelta
from functools import partial

import daomodule

dbaccess = daomodule.UseradminopDAO()



#class Useradminop(tk.Tk):   #tk(tkinter).Tk
class Useradminop(ctk.CTk):  ##ctk.CTk

    ##common##
    def alldestroy(self):
        for widget in self.winfo_children():
            widget.destroy()

    def close_window(self):
        messagebox.showwarning("Close window", "Window cannot be closed!")

    def limit_char4(self,string):
        return len(string) <= 4
    
    def limit_char8(self,string):
        return len(string) <= 8
    
    def limit_char20(self,string):
        return len(string) <= 20
    
    def limit_char50(self,string):
        return len(string) <= 50

    def Keybord(self,event):
        self.widgetinfo = ""
        self.widgetinfo = event.widget
        print(event.widget)
        if self.keybord:
            self.keybord = False
            self.upper = False
            self.frame_Keybord = tk.Frame(self, bg="blue")
            frame_Keybord = self.frame_Keybord
            frame_Keybord.pack(pady=10)

                
            #image_UserScreen2_2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
            
            ##1~0#
            ctk.CTkButton(frame_Keybord, text="1",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("1")).grid(row=0,column=0)
            ctk.CTkButton(frame_Keybord, text="2",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("2")).grid(row=0,column=1)
            ctk.CTkButton(frame_Keybord, text="3",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("3")).grid(row=0,column=2)
            ctk.CTkButton(frame_Keybord, text="4",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("4")).grid(row=0,column=3)
            ctk.CTkButton(frame_Keybord, text="5",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("5")).grid(row=0,column=4)
            ctk.CTkButton(frame_Keybord, text="6",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("6")).grid(row=0,column=5)
            ctk.CTkButton(frame_Keybord, text="7",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("7")).grid(row=0,column=6)
            ctk.CTkButton(frame_Keybord, text="8",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("8")).grid(row=0,column=7)
            ctk.CTkButton(frame_Keybord, text="9",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("9")).grid(row=0,column=8)
            ctk.CTkButton(frame_Keybord, text="0",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("0")).grid(row=0,column=9)

            #q~p
            ctk.CTkButton(frame_Keybord, text="q",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("q")).grid(row=1,column=0)
            ctk.CTkButton(frame_Keybord, text="w",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("w")).grid(row=1,column=1)
            ctk.CTkButton(frame_Keybord, text="e",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("e")).grid(row=1,column=2)
            ctk.CTkButton(frame_Keybord, text="r",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("r")).grid(row=1,column=3)
            ctk.CTkButton(frame_Keybord, text="t",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("t")).grid(row=1,column=4)
            ctk.CTkButton(frame_Keybord, text="y",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("y")).grid(row=1,column=5)
            ctk.CTkButton(frame_Keybord, text="u",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("u")).grid(row=1,column=6)
            ctk.CTkButton(frame_Keybord, text="i",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("i")).grid(row=1,column=7)
            ctk.CTkButton(frame_Keybord, text="o",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("o")).grid(row=1,column=8)
            ctk.CTkButton(frame_Keybord, text="p",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("p")).grid(row=1,column=9)

            #a~-
            ctk.CTkButton(frame_Keybord, text="a",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("a")).grid(row=2,column=0)
            ctk.CTkButton(frame_Keybord, text="s",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("s")).grid(row=2,column=1)
            ctk.CTkButton(frame_Keybord, text="d",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("d")).grid(row=2,column=2)
            ctk.CTkButton(frame_Keybord, text="f",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("f")).grid(row=2,column=3)
            ctk.CTkButton(frame_Keybord, text="g",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("g")).grid(row=2,column=4)
            ctk.CTkButton(frame_Keybord, text="h",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("h")).grid(row=2,column=5)
            ctk.CTkButton(frame_Keybord, text="j",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("j")).grid(row=2,column=6)
            ctk.CTkButton(frame_Keybord, text="k",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("k")).grid(row=2,column=7)
            ctk.CTkButton(frame_Keybord, text="l",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("l")).grid(row=2,column=8)
            ctk.CTkButton(frame_Keybord, text="-",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("-")).grid(row=2,column=9)

            #z~大文字化
            ctk.CTkButton(frame_Keybord, text="z",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("z")).grid(row=3,column=0)
            ctk.CTkButton(frame_Keybord, text="x",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("x")).grid(row=3,column=1)
            ctk.CTkButton(frame_Keybord, text="c",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("c")).grid(row=3,column=2)
            ctk.CTkButton(frame_Keybord, text="v",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("v")).grid(row=3,column=3)
            ctk.CTkButton(frame_Keybord, text="b",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("b")).grid(row=3,column=4)
            ctk.CTkButton(frame_Keybord, text="n",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("n")).grid(row=3,column=5)
            ctk.CTkButton(frame_Keybord, text="m",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("m")).grid(row=3,column=6)
            #ctk.CTkButton(frame_Keybord, text="⇧", height=50,width=150, fg_color="gray", command=self.KeybordUpper).grid(row=3,column=7, columnspan=3)
            self.button_keybord = ctk.CTkButton(frame_Keybord, text="⇧", height=50,width=150, fg_color="gray", command=self.KeybordUpper)
            self.button_keybord.grid(row=3,column=7, columnspan=3)
              
            #close~delete
            ctk.CTkButton(frame_Keybord, text="close",height=50,width=100,fg_color="gray", command=lambda:self.KeybordDestroy(frame_Keybord)).grid(row=4,column=1, columnspan=2)
            ctk.CTkButton(frame_Keybord, text="clear", height=50,width=100, fg_color="gray", command=lambda:self.KeybordGet("clear")).grid(row=4,column=3, columnspan=2)
            ctk.CTkButton(frame_Keybord, text="space", height=50,width=100, fg_color="gray", command=lambda:self.KeybordGet(" ")).grid(row=4,column=5, columnspan=2)
            ctk.CTkButton(frame_Keybord, text="del", height=50,width=100, fg_color="gray", command=lambda:self.KeybordGet("delete")).grid(row=4,column=7, columnspan=2)
                
    def MathKeybord(self, event):
        self.widgetinfo = ""
        self.widgetinfo = event.widget   #Keybordメソッドを実行しているwidget情報を取得
        print(event.widget)
        if self.mathkeybord:
            self.mathkeybord = False
            self.frame_mathKeybord = tk.Frame(self, bg="blue")
            frame_mathKeybord = self.frame_mathKeybord
            frame_mathKeybord.pack(pady=10)
            
            ctk.CTkButton(frame_mathKeybord, text="1",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("1")).grid(row=0,column=0)
            ctk.CTkButton(frame_mathKeybord, text="2",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("2")).grid(row=0,column=1)
            ctk.CTkButton(frame_mathKeybord, text="3",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("3")).grid(row=0,column=2)
            ctk.CTkButton(frame_mathKeybord, text="4",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("4")).grid(row=1,column=0)
            ctk.CTkButton(frame_mathKeybord, text="5",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("5")).grid(row=1,column=1)
            ctk.CTkButton(frame_mathKeybord, text="6",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("6")).grid(row=1,column=2)
            ctk.CTkButton(frame_mathKeybord, text="7",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("7")).grid(row=2,column=0)
            ctk.CTkButton(frame_mathKeybord, text="8",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("8")).grid(row=2,column=1)
            ctk.CTkButton(frame_mathKeybord, text="9",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("9")).grid(row=2,column=2)
            ctk.CTkButton(frame_mathKeybord, text="clear",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("clear")).grid(row=3,column=0)
            ctk.CTkButton(frame_mathKeybord, text="0",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("0")).grid(row=3,column=1)
            ctk.CTkButton(frame_mathKeybord, text="close", height=50,width=50, fg_color="gray", command=lambda:self.KeybordDestroy(frame_mathKeybord)).grid(row=3,column=2)      

    def KeybordDestroy(self,kybord):
        self.keybord = True
        self.mathkeybord = True
        kybord.destroy()

    def KeybordGet(self,value):
        if value == "clear":
            self.widgetinfo.delete(0,tk.END)
        elif value == "delete":
            entryvalue = self.widgetinfo.get()
            length = len(entryvalue)-1
            self.widgetinfo.delete(length,tk.END)
        elif self.upper:
            value = value.upper()
            self.widgetinfo.insert(tk.END,value)
        else:
            self.widgetinfo.insert(tk.END,value)

    def KeybordUpper(self):
        if self.upper:
            self.upper = False
            self.button_keybord.configure(fg_color="gray")            
        else:
            self.upper = True
            self.button_keybord.configure(fg_color="white")


    def CSVoutput(self):
        pass
    
    def poweroff(self):
        res = messagebox.askokcancel("Power Off", "Are you sure you want to turn off the app and the unit?")
        if res:
            self.destroy()
            time.sleep(5)
            #os.system('shutdown -r now')

    ##common##
    
    ##LoginScreen##
    def LoginScreen(self):

        self.alldestroy()

        self.userinfolist = []
        
        self.mathkeybord = True
        self.upper = False
        
        self.label_today = ""
        self.Adminlabel_today = ""
        self.label_today = datetime.now()
        self.Adminlabel_today = datetime.now() 

        frame_LoginScreen_top = tk.Frame(self, bg="green", height=80 ,width=700)
        frame_LoginScreen_top.pack_propagate(False)
        frame_LoginScreen_top.pack()

        frame_LoginScreen_main = tk.Frame(self, bg="red", width=700)
        frame_LoginScreen_main.pack_propagate(False)
        frame_LoginScreen_main.pack(expand=True, fill=tk.BOTH)

        ##UserMstに登録されているユーザーIDとパスワードをリスト形式で取得
        logindict = dbaccess.getUserIDLoginpassword()
        print(logindict)

        WIDTH  = 20        # 幅
        HEIGHT = 20        # 高さ

        image_LoginScreen = tk.PhotoImage(file="assets2/share.png")
        canvas_LoginScreen = tk.Canvas(frame_LoginScreen_main, width=WIDTH, height=HEIGHT)
        canvas_LoginScreen.create_image(WIDTH/2, HEIGHT/2, image=image_LoginScreen)
        canvas_LoginScreen.pack(pady=15)

        passwordlimit = self.register(self.limit_char4)
        
        self.loginuserid = ctk.CTkEntry(frame_LoginScreen_main, width=250, placeholder_text="User ID", placeholder_text_color="white")
        self.loginuserid.configure(validate="key", validatecommand=(passwordlimit, "%P"))
        self.loginuserid.pack(pady=5)
        self.loginuserid.bind("<Button-1>",self.MathKeybord)
        self.loginpassword = ctk.CTkEntry(frame_LoginScreen_main, show="*", width=250, placeholder_text="Password", placeholder_text_color="white")
        self.loginpassword.configure(validate="key", validatecommand=(passwordlimit, "%P"))
        self.loginpassword.pack(pady=5)
        self.loginpassword.bind("<Button-1>",self.MathKeybord)
        self.btn_LoginScreen = ctk.CTkButton(frame_LoginScreen_main, command=self.showchange_LoginScreen, text="")
        self.btn_LoginScreen.pack()


        ctk.CTkButton(frame_LoginScreen_main, text="Login",height=50,width=50, fg_color="black", command=lambda:self.LoginPasswordcheck(logindict)).pack()

        ctk.CTkButton(frame_LoginScreen_main, text="",height=50,width=50, fg_color="black", command=self.SettingScreen).pack(side="left")
        ctk.CTkButton(frame_LoginScreen_main, text="",height=50,width=50, fg_color="black", command=self.poweroff).pack(side="right")

    def LoginPasswordcheck(self, logindict):
        if len(self.loginuserid.get()) == 0 or len(self.loginpassword.get()) == 0:
            messagebox.showerror("Error", "Please userid or passowrd check") 
        else:
            userid = self.loginuserid.get()
            password = self.loginpassword.get()
            print(type(userid), type(password))    
            if userid in logindict:
                logindict_password = logindict[userid]
                if logindict_password == password:
                    print("userid OK")
                    ##この後の画面でログインするユーザーの情報を使うので、ここでUserMSTに登録されている値をリスト形式の変数に代入しておく
                    self.userinfolist = dbaccess.getLoginUserinfo(userid, password)   #[userid, username, companyname, pass, photo, authority]
                    print(self.userinfolist)
                    self.DatainspectScreen()
                else:
                    messagebox.showerror("Password Error", "Please password check")
            else:
                messagebox.showerror("Userid Error", "Please userid check")

    def showchange_LoginScreen(self):
        self.loginpassword.configure(show="")


    ##LoginScreen##
            
    ##SettingScreen##
    def SettingScreen(self):
        print("SettingScreen", "korn create now")
        #korn create now
    ##SettingScreen##
            
    ##DatainspectScreen##
    def DatainspectScreen(self):

        self.alldestroy()

        frame_DatainspectScreen_top = tk.Frame(self, bg="green", height=80 ,width=700)
        frame_DatainspectScreen_top.pack_propagate(False)
        frame_DatainspectScreen_top.pack()

        frame_DatainspectScreen_main = tk.Frame(self, bg="red", height=520 ,width=700)
        frame_DatainspectScreen_main.pack_propagate(False)
        frame_DatainspectScreen_main.pack()

        frame_DatainspectScreen_under = tk.Frame(self, bg="blue")
        frame_DatainspectScreen_under.pack_propagate(False)
        frame_DatainspectScreen_under.pack(expand=True, fill=tk.BOTH)

        ##ここでLoginボタンの表示をさせるかさせないか、UserMstのAuthorityでifで場合分け
        if self.userinfolist[5] == "true":
            image_DatainspectScreen_top1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
            ctk.CTkButton(frame_DatainspectScreen_top, text="Login", height=40 ,width=40, command=self.AdminLoginScreen, image=image_DatainspectScreen_top1, compound="top").pack(side="left")
        image_DatainspectScreen_top2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_DatainspectScreen_top, text="Logout", height=40 ,width=40, command=self.LoginScreen, image=image_DatainspectScreen_top2, compound="top").pack(side="right")

        #ここに各画面の構成を作成する
        frame_DatainspectScreen_main_1 = tk.Frame(frame_DatainspectScreen_main, bg="blue", height=60 ,width=400)
        frame_DatainspectScreen_main_1.pack_propagate(False)
        frame_DatainspectScreen_main_1.pack(pady=10)        
        
        ctk.CTkButton(frame_DatainspectScreen_main_1, text="◀", height=40 ,width=40, command=lambda:self.Changedatebefore(self.label_today)).pack(side="left")
        ctk.CTkButton(frame_DatainspectScreen_main_1, text="▶", height=40 ,width=40, command=lambda:self.Changedateafter(self.label_today)).pack(side="right")      
        self.label_DatainspectScreen_main = tk.Label(frame_DatainspectScreen_main_1, text=self.label_today.strftime('%d/%m/%Y'))
        self.label_DatainspectScreen_main.pack(pady=20)

        frame_DatainspectScreen_main_2 = tk.Frame(frame_DatainspectScreen_main, bg="blue", height=30 ,width=500)
        frame_DatainspectScreen_main_2.pack_propagate(False)
        frame_DatainspectScreen_main_2.pack(pady=10)
        ctk.CTkButton(frame_DatainspectScreen_main_2, text="CSV Output", height=40 ,width=40, command=self.CSVoutput).pack(side="right")
        
        frame_DatainspectScreen_main_3 = ctk.CTkScrollableFrame(frame_DatainspectScreen_main, fg_color="transparent")
        frame_DatainspectScreen_main_3.pack_propagate(False)
        frame_DatainspectScreen_main_3.pack(expand=True, fill=tk.BOTH)

        History_YearAndMonth = self.label_today.strftime('%Y%m')
        History_Day = self.label_today.strftime('%d')
        list_entryleavingtime = dbaccess.getEntryLeavingtime(self.userinfolist[0], History_YearAndMonth, History_Day)
        print(list_entryleavingtime)
        
        for timeinfo in list_entryleavingtime:
            entryingtimetext = ""
            leavingtimetext = ""
            if timeinfo[0] != "":
                entryingtimetext = timeinfo[0]
                entryingtimetext = entryingtimetext[:2] + ':' + entryingtimetext[2:]
                ctk.CTkLabel(frame_DatainspectScreen_main_3, text="{}                     Entering".format(entryingtimetext), height=60 ,width=500, fg_color="green", corner_radius=20).grid(pady=5)
                if timeinfo[1] != "":          
                    leavingtimetext = timeinfo[1]
                    leavingtimetext = leavingtimetext[:2] + ':' + leavingtimetext[2:]
                    ctk.CTkLabel(frame_DatainspectScreen_main_3, text="{}                     Leaving".format(leavingtimetext), height=60 ,width=500, fg_color="green", corner_radius=20).grid(pady=5)

        #ここに各画面の構成を作成する
        frame_DatainspectScreen_under1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_DatainspectScreen_under, text="Data", height=80 ,width=80, fg_color="green", image=frame_DatainspectScreen_under1, compound="top").pack(padx=90, side="left")
        frame_DatainspectScreen_under2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_DatainspectScreen_under, text="User", height=80 ,width=80, command=self.AccountinfoScreen, image=frame_DatainspectScreen_under2, compound="top").pack(padx=90, side="right")

    def Changedatebefore(self, label_today):
        ###ここで前の日のデータを取得し表示させる
        print("Datebefore")
        datebefore = timedelta(days=1)
        label_day = label_today - datebefore
        self.label_today = label_day
        self.label_DatainspectScreen_main["text"] = self.label_today.strftime('%d/%m/%Y')
        self.DatainspectScreen()

    def Changedateafter(self, label_today):
        print("Dateafter")
        ###ここで次の日のデータを取得し表示させる
        dateafter = timedelta(days=1)
        label_day = label_today + dateafter
        self.label_today = label_day
        self.label_DatainspectScreen_main["text"] = self.label_today.strftime('%d/%m/%Y')
        self.DatainspectScreen()

    ##DatainspectScreen##
        
    ##AccountinfoScreen##
    def AccountinfoScreen(self):
        self.alldestroy()

        self.keybord = True
        self.upper = False
        
        frame_AccountinfoScreen_top = tk.Frame(self, bg="green", height=80 ,width=700)
        frame_AccountinfoScreen_top.pack_propagate(False)
        frame_AccountinfoScreen_top.pack()

        frame_AccountinfoScreen_main = tk.Frame(self, bg="red", height=520 ,width=700)
        frame_AccountinfoScreen_main.pack_propagate(False)
        frame_AccountinfoScreen_main.pack()

        frame_AccountinfoScreen_under = tk.Frame(self, bg="blue")
        frame_AccountinfoScreen_under.pack_propagate(False)
        frame_AccountinfoScreen_under.pack(expand=True, fill=tk.BOTH)

        ##ここでLoginボタンの表示をさせるかさせないか、UserMstのAuthorityでifで場合分け
        if self.userinfolist[5] == "true":
            image_AccountinfoScreen_top1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
            ctk.CTkButton(frame_AccountinfoScreen_top, text="Login", height=40 ,width=40, command=self.AdminLoginScreen, image=image_AccountinfoScreen_top1, compound="top").pack(side="left")
        image_AccountinfoScreen_top2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AccountinfoScreen_top, text="Logout", height=40 ,width=40, command=self.LoginScreen, image=image_AccountinfoScreen_top2, compound="top").pack(side="right")

        #ここに各画面の構成を作成する
        frame_AccountinfoScreen_main_1 = ctk.CTkFrame(frame_AccountinfoScreen_main, fg_color="transparent")
        frame_AccountinfoScreen_main_1.pack(pady=5)

        usernamelimit = self.register(self.limit_char20)
        companynamelimit = self.register(self.limit_char50)

        ctk.CTkLabel(frame_AccountinfoScreen_main_1, text="Full Name(Double-click on the form to rename it)", width=500, anchor="w").pack(pady=2)
        entry_AccountinfoScreen_username = ctk.CTkEntry(frame_AccountinfoScreen_main_1, height=60 ,width=500,fg_color="green", validate="key", validatecommand=(usernamelimit, "%P"))
        entry_AccountinfoScreen_username.bind("<Button-1>",self.Keybord)
        entry_AccountinfoScreen_username.bind("<Double-1>", self.changeusername, "+")
        entry_AccountinfoScreen_username.pack()
        entry_AccountinfoScreen_username.insert(0, self.userinfolist[1])
        ctk.CTkLabel(frame_AccountinfoScreen_main_1, text="Comnpany Name(Double-click on the form to rename it)", width=500, anchor="w").pack(pady=2)
        entry_AccountinfoScreen_companyname = ctk.CTkEntry(frame_AccountinfoScreen_main_1, height=60 ,width=500, fg_color="green", validate="key", validatecommand=(companynamelimit, "%P"))     
        entry_AccountinfoScreen_companyname.bind("<Button-1>",self.Keybord)
        entry_AccountinfoScreen_companyname.bind("<Double-1>", self.changecompanyname, "+")
        entry_AccountinfoScreen_companyname.pack()
        entry_AccountinfoScreen_companyname.insert(0,self.userinfolist[2])

        frame_AccountinfoScreen_main_2 = tk.Frame(frame_AccountinfoScreen_main, bg="green", height=30, width=500)
        frame_AccountinfoScreen_main_2.pack_propagate(False)
        frame_AccountinfoScreen_main_2.pack()
        ctk.CTkLabel(frame_AccountinfoScreen_main_2, text="Change Password", width=500, anchor="w").pack(pady=2)

        frame_AccountinfoScreen_main_3 = tk.Frame(frame_AccountinfoScreen_main, bg="green", height=130, width=300)
        frame_AccountinfoScreen_main_3.pack_propagate(False)
        frame_AccountinfoScreen_main_3.pack()
        image_AccountinfoScreen_1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AccountinfoScreen_main_3, text="User  >", height=80 ,width=80, command=self.PasswordchangeScreen,image=image_AccountinfoScreen_1, compound="top").pack(padx=15, side="left")
        
        ##ここでAdminボタンの表示をさせるかさせないか、UserMstのAuthorityでifで場合分け
        if self.userinfolist[5] == "true":
            image_AccountinfoScreen_2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
            ctk.CTkButton(frame_AccountinfoScreen_main_3, text="Admin  >", height=80 ,width=80, command=self.AdminPasswordchangeScreen, image=image_AccountinfoScreen_2, compound="top").pack(padx=15, side="right")
        
        frame_AccountinfoScreen_main_4 = tk.Frame(frame_AccountinfoScreen_main, bg="green", height=30, width=500)
        frame_AccountinfoScreen_main_4.pack_propagate(False)
        frame_AccountinfoScreen_main_4.pack()
        ctk.CTkLabel(frame_AccountinfoScreen_main_4, text="Change Facial info", width=500, anchor="w").pack(pady=2)

        frame_AccountinfoScreen_main_5 = tk.Frame(frame_AccountinfoScreen_main, bg="white", height=130, width=300)
        frame_AccountinfoScreen_main_5.pack_propagate(False)
        frame_AccountinfoScreen_main_5.pack()
        image_AccountinfoScreen_3 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AccountinfoScreen_main_5, text="Camera  >", height=80 ,width=80, command=self.takepicture, image=image_AccountinfoScreen_3, compound="top").pack(padx=15, side="left")
        image_AccountinfoScreen_4 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AccountinfoScreen_main_5, text="Picture  >", height=80 ,width=80, command=self.SelectpictureScreen, image=image_AccountinfoScreen_4, compound="top").pack(padx=15, side="right")

        #ここに各画面の構成を作成する

        image_AccountinfoScreen_under1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AccountinfoScreen_under, text="Data", height=80 ,width=80, command=self.DatainspectScreen, image=image_AccountinfoScreen_under1, compound="top").pack(padx=90, side="left")
        image_AccountinfoScreen_under2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AccountinfoScreen_under, text="User", height=80 ,width=80, fg_color="green", image=image_AccountinfoScreen_under2, compound="top").pack(padx=90, side="right")
    
    def takepicture(self):
        pass

    def changeusername(self, event):
        self.widgetinfo = ""
        self.widgetinfo = event.widget
        username_before = self.userinfolist[1]
        username_after = self.widgetinfo.get()       
        if username_before == username_after:
            messagebox.showwarning("Change Username", "Please change username")
        else:
            res_changeusername = messagebox.askokcancel("Change Username", "Do you want to change your name from {} to {}".format(username_before, username_after))
            if res_changeusername:
                flag = "user"
                userid = self.userinfolist[0]
                dbaccess.updateUserCompanyname(username_before, username_after, userid, flag)

    def changecompanyname(self, event):
        self.widgetinfo = ""
        self.widgetinfo = event.widget
        companyname_before = self.userinfolist[2]
        companyname_after = self.widgetinfo.get()
        if companyname_before == companyname_after:
            messagebox.showwarning("Change Companyname", "Please change companyname")
        else:
            res_changeusername = messagebox.askokcancel("Change Companyname", "Do you want to change your name from {} to {}".format(companyname_before, companyname_after))
            if res_changeusername:
                flag = "company"
                userid = self.userinfolist[0]
                dbaccess.updateUserCompanyname(companyname_before, companyname_after, userid, flag)
                
    ##AccountinfoScreen##
    
    ##SelectpictureScreen##
    def SelectpictureScreen(self):
        self.alldestroy()

        frame_SelectpictureScreen_top = tk.Frame(self, bg="green", height=80 ,width=700)
        frame_SelectpictureScreen_top.pack_propagate(False)
        frame_SelectpictureScreen_top.pack()

        frame_SelectpictureScreen_main = tk.Frame(self, bg="red", height=520 ,width=700)
        frame_SelectpictureScreen_main.pack_propagate(False)
        frame_SelectpictureScreen_main.pack(expand=True, fill=tk.BOTH)

        image_SelectpictureScreen_top1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_SelectpictureScreen_top, text="<", height=40 ,width=40, command=self.AccountinfoScreen, image=image_SelectpictureScreen_top1, compound="top").pack(side="left")
        
        image_SelectpictureScreen = tk.PhotoImage(file="assets2/share.png")
        WIDTH  = 50        # 幅
        HEIGHT = 50        # 高さ
        canvas_SelectpictureScreen_main_1 = tk.Canvas(frame_SelectpictureScreen_main, width=WIDTH, height=HEIGHT)
        canvas_SelectpictureScreen_main_1.create_image(WIDTH/2, HEIGHT/2, image=image_SelectpictureScreen)
        canvas_SelectpictureScreen_main_1.pack()
        
        frame_SelectpictureScreen_main_2 = ctk.CTkScrollableFrame(frame_SelectpictureScreen_main, fg_color="transparent")
        frame_SelectpictureScreen_main_2.pack_propagate(False)
        frame_SelectpictureScreen_main_2.pack(expand=True, fill=tk.BOTH)

        imagelist = []
        ###
        imagelist = glob.glob("assets2/*.png")

        for i in range(0,len(imagelist)):
            image = Image.open(imagelist[i])
            image_SelectpictureScreen_main_2 = ctk.CTkImage(light_image=image, size=(120,120))
            userid = self.userinfolist[0]
            username = self.userinfolist[1]
            password = self.userinfolist[3]
            ctk.CTkButton(frame_SelectpictureScreen_main_2, text="", height=150 ,width=150, command=partial(dbaccess.updatePhoto,userid,username,password,image_SelectpictureScreen_main_2), image=image_SelectpictureScreen_main_2).grid(padx=30, pady=20, row=i//2, column=i%2) 
        
    ##SelectpictureScreen##
        
    ##PasswordchangeScreen##
    def PasswordchangeScreen(self):
        
        self.alldestroy()

        frame_PasswordchangeScreen_top = tk.Frame(self, bg="green", height=80 ,width=700)
        frame_PasswordchangeScreen_top.pack_propagate(False)
        frame_PasswordchangeScreen_top.pack()

        frame_PasswordchangeScreen_main = tk.Frame(self, bg="red", height=520 ,width=700)
        frame_PasswordchangeScreen_main.pack_propagate(False)
        frame_PasswordchangeScreen_main.pack(expand=True, fill=tk.BOTH)

        image_PasswordchangeScreen_top1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_PasswordchangeScreen_top, text="<", height=40 ,width=40, command=self.AccountinfoScreen, image=image_PasswordchangeScreen_top1, compound="top").pack(side="left")

        #ここに各画面の構成を作成する
        frame_PasswordchangeScreen = tk.Frame(frame_PasswordchangeScreen_main, bg="white")
        frame_PasswordchangeScreen.pack(pady=10)

        frame_PasswordchangeScreen_2 = tk.Frame(frame_PasswordchangeScreen_main, bg="white")
        frame_PasswordchangeScreen_2.pack(pady=10)

        tk.Label(frame_PasswordchangeScreen, text="Change Your Password",font=("MSゴシック", "30", "bold"), bg="white").pack()
        tk.Label(frame_PasswordchangeScreen, text="Please enter new password", bg="white", font=("","15","")).pack(pady=10)

        passwordlimit = self.register(self.limit_char4)
        self.changepassword = tk.Entry(frame_PasswordchangeScreen, show="*" , width=10, validate="key", validatecommand=(passwordlimit, "%P"))
        self.changepassword.pack(pady=5)

        image_PasswordchangeScreen_2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))

        ctk.CTkButton(frame_PasswordchangeScreen_2, text="1",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("1")).grid(row=0,column=0)
        ctk.CTkButton(frame_PasswordchangeScreen_2, text="2",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("2")).grid(row=0,column=1)
        ctk.CTkButton(frame_PasswordchangeScreen_2, text="3",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("3")).grid(row=0,column=2)
        ctk.CTkButton(frame_PasswordchangeScreen_2, text="4",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("4")).grid(row=1,column=0)
        ctk.CTkButton(frame_PasswordchangeScreen_2, text="5",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("5")).grid(row=1,column=1)
        ctk.CTkButton(frame_PasswordchangeScreen_2, text="6",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("6")).grid(row=1,column=2)
        ctk.CTkButton(frame_PasswordchangeScreen_2, text="7",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("7")).grid(row=2,column=0)
        ctk.CTkButton(frame_PasswordchangeScreen_2, text="8",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("8")).grid(row=2,column=1)
        ctk.CTkButton(frame_PasswordchangeScreen_2, text="9",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("9")).grid(row=2,column=2)
        ctk.CTkButton(frame_PasswordchangeScreen_2, text="", height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("clear"),compound="right", image=image_PasswordchangeScreen_2).grid(row=3,column=0)
        ctk.CTkButton(frame_PasswordchangeScreen_2, text="0",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("0")).grid(row=3,column=1)
        ctk.CTkButton(frame_PasswordchangeScreen_2, text="Enter",height=70,width=70, fg_color="gray", command=self.Passwordcheck).grid(row=3,column=2)

        #ここに各画面の構成を作成する

    def Passwordget(self,value):
        if value == "clear":
            self.changepassword.delete(0,tk.END)
        else:
            self.changepassword.insert(tk.END,value)

    def Passwordcheck(self):
        if len(self.changepassword.get()) == 4:
            self.changepassword_save = self.changepassword.get()
            self.PasswordchangeScreen_confirm()
        else:
            messagebox.showerror("Password Error", "Please 4Password Insert")
    
    ##PasswordchangeScreen##

    ##PasswordchangeScreen_confirm## 
    def PasswordchangeScreen_confirm(self):
        
        self.alldestroy()

        frame_PasswordchangeScreen_confirm_top = tk.Frame(self, bg="green", height=80 ,width=700)
        frame_PasswordchangeScreen_confirm_top.pack_propagate(False)
        frame_PasswordchangeScreen_confirm_top.pack()

        frame_PasswordchangeScreen_confirm_main = tk.Frame(self, bg="red", height=520 ,width=700)
        frame_PasswordchangeScreen_confirm_main.pack_propagate(False)
        frame_PasswordchangeScreen_confirm_main.pack(expand=True, fill=tk.BOTH)

        image_PasswordchangeScreen_confirm_top1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_PasswordchangeScreen_confirm_top, text="<", height=40 ,width=40, command=self.AccountinfoScreen, image=image_PasswordchangeScreen_confirm_top1, compound="top").pack(side="left")

        #ここに各画面の構成を作成する
        frame_PasswordchangeScreen_confirm = tk.Frame(frame_PasswordchangeScreen_confirm_main, bg="white")
        frame_PasswordchangeScreen_confirm.pack(pady=10)

        frame_PasswordchangeScreen_confirm_2 = tk.Frame(frame_PasswordchangeScreen_confirm_main, bg="white")
        frame_PasswordchangeScreen_confirm_2.pack(pady=10)

        tk.Label(frame_PasswordchangeScreen_confirm, text="Change Your Password",font=("MSゴシック", "30", "bold"), bg="white").pack()
        tk.Label(frame_PasswordchangeScreen_confirm, text="For confirmation, please enter it again.", bg="white", font=("","15","")).pack(pady=10)

        passwordlimit = self.register(self.limit_char4)
        self.changepassword_confirm = tk.Entry(frame_PasswordchangeScreen_confirm, show="*" , width=10, validate="key", validatecommand=(passwordlimit, "%P"))
        self.changepassword_confirm.pack(pady=5)

        image_PasswordchangeScreen_confirm_2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))

        ctk.CTkButton(frame_PasswordchangeScreen_confirm_2, text="1",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("1")).grid(row=0,column=0)
        ctk.CTkButton(frame_PasswordchangeScreen_confirm_2, text="2",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("2")).grid(row=0,column=1)
        ctk.CTkButton(frame_PasswordchangeScreen_confirm_2, text="3",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("3")).grid(row=0,column=2)
        ctk.CTkButton(frame_PasswordchangeScreen_confirm_2, text="4",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("4")).grid(row=1,column=0)
        ctk.CTkButton(frame_PasswordchangeScreen_confirm_2, text="5",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("5")).grid(row=1,column=1)
        ctk.CTkButton(frame_PasswordchangeScreen_confirm_2, text="6",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("6")).grid(row=1,column=2)
        ctk.CTkButton(frame_PasswordchangeScreen_confirm_2, text="7",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("7")).grid(row=2,column=0)
        ctk.CTkButton(frame_PasswordchangeScreen_confirm_2, text="8",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("8")).grid(row=2,column=1)
        ctk.CTkButton(frame_PasswordchangeScreen_confirm_2, text="9",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("9")).grid(row=2,column=2)
        ctk.CTkButton(frame_PasswordchangeScreen_confirm_2, text="", height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("clear"),compound="right", image=image_PasswordchangeScreen_confirm_2).grid(row=3,column=0)
        ctk.CTkButton(frame_PasswordchangeScreen_confirm_2, text="0",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("0")).grid(row=3,column=1)
        ctk.CTkButton(frame_PasswordchangeScreen_confirm_2, text="Enter",height=70,width=70, fg_color="gray", command=self.Passwordcheck_confirm).grid(row=3,column=2)        

        #ここに各画面の構成を作成する

    def Passwordget_confirm(self,value):
        if value == "clear":
            self.changepassword_confirm.delete(0,tk.END)
        else:
            self.changepassword_confirm.insert(tk.END,value)

    def Passwordcheck_confirm(self):
        if len(self.changepassword_confirm.get()) == 4:
            changepassword_confirm = self.changepassword_confirm.get()
            if self.changepassword_save == changepassword_confirm:
                changepassword_save = self.changepassword_save
                userid = self.userinfolist[0]
                username = self.userinfolist[1]
                companyname = self.userinfolist[2]
                dbaccess.updateUserPassword(changepassword_save, userid, username, companyname)
                self.AccountinfoScreen()
            else:
                messagebox.showerror("Password Error", "Password not match")
        else:
            messagebox.showerror("Password Error", "Please 4Password Insert")
    ##PasswordchangeScreen_confirm##

    ##AdminPasswordchangeScreen##
    def AdminPasswordchangeScreen(self):
        
        self.alldestroy()

        frame_AdminPasswordchangeScreen_top = tk.Frame(self, bg="green", height=80 ,width=700)
        frame_AdminPasswordchangeScreen_top.pack_propagate(False)
        frame_AdminPasswordchangeScreen_top.pack()

        frame_AdminPasswordchangeScreen_main = tk.Frame(self, bg="red", width=700)
        frame_AdminPasswordchangeScreen_main.pack_propagate(False)
        frame_AdminPasswordchangeScreen_main.pack(expand=True, fill=tk.BOTH)

        image_PasswordchangeScreen_confirm_top1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AdminPasswordchangeScreen_top, text="<", height=40 ,width=40, command=self.AccountinfoScreen, image=image_PasswordchangeScreen_confirm_top1, compound="top").pack(side="left")

        #ここに各画面の構成を作成する
        self.keybord = True

        frame_AdminPasswordchangeScreen = tk.Frame(frame_AdminPasswordchangeScreen_main, bg="white")
        frame_AdminPasswordchangeScreen.pack(pady=10)

        frame_AdminPasswordchangeScreen_2 = tk.Frame(frame_AdminPasswordchangeScreen_main, bg="blue")
        frame_AdminPasswordchangeScreen_2.pack(pady=10)

        tk.Label(frame_AdminPasswordchangeScreen, text="Change Your Password",font=("MSゴシック", "30", "bold"), bg="white").pack()
        tk.Label(frame_AdminPasswordchangeScreen, text="Please enter the admin password.", bg="white", font=("","15","")).pack(pady=10)

        adminpasswordlimit = self.register(self.limit_char8)
        adminpasswordlimit_confirm = self.register(self.limit_char8)

        tk.Label(frame_AdminPasswordchangeScreen_2, text="Password  ", bg="white", width=30).grid(row=0, column=0, pady=10)
        tk.Label(frame_AdminPasswordchangeScreen_2, text="Confirm\nPassword  ", bg="white", width=30).grid(row=1, column=0, pady=10)
        self.changeadminpassword = ctk.CTkEntry(frame_AdminPasswordchangeScreen_2, width=200, show="*", validate="key", validatecommand=(adminpasswordlimit, "%P"))
        self.changeadminpassword_confirm = ctk.CTkEntry(frame_AdminPasswordchangeScreen_2, width=200, show="*", validate="key", validatecommand=(adminpasswordlimit_confirm, "%P"))
        
        self.changeadminpassword.bind("<Button-1>",self.Keybord)
        self.changeadminpassword_confirm.bind("<Button-1>",self.Keybord)

        self.changeadminpassword.grid(row=0, column=1)
        self.changeadminpassword_confirm.grid(row=1, column=1)

        image_AdminPasswordchangeScreen_2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AdminPasswordchangeScreen_2, text="Continue                ", command=self.AdminPasswordcheck,  image=image_AdminPasswordchangeScreen_2, compound="right").grid(row=2, column=0, columnspan=2, pady=50)

    def AdminPasswordcheck(self):
        changeadminpassword = self.changeadminpassword.get()
        chabngeadminpassword_confirm = self.changeadminpassword_confirm.get()
        space = " "
        if space not in changeadminpassword:
            if len(changeadminpassword) == 8:
                if changeadminpassword == chabngeadminpassword_confirm:
                    changeadminpassword_save = changeadminpassword
                    editor = self.userinfolist[0]
                    dbaccess.updateAdminPassword(changeadminpassword_save, editor)
                    self.AccountinfoScreen()
                else:
                    messagebox.showerror("Password Error", "Password not match")        
            else:
                messagebox.showerror("Password Error", "Password 8password insert")
        else:
            messagebox.showerror("Password Error", "Do not include spaces")
        

        #ここに各画面の構成を作成する

    ##AdminPasswordchangeScreen##

    ##AdminLoginScreen##
    def AdminLoginScreen(self):
        
        self.alldestroy()

        self.keybord = True

        frame_AdminLoginScreen_top = tk.Frame(self, bg="green", height=80 ,width=700)
        frame_AdminLoginScreen_top.pack_propagate(False)
        frame_AdminLoginScreen_top.pack()

        frame_AdminLoginScreen_main = tk.Frame(self, bg="red", width=700)
        frame_AdminLoginScreen_main.pack_propagate(False)
        frame_AdminLoginScreen_main.pack(expand=True, fill=tk.BOTH)

        image_AdminLoginScreen_top1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AdminLoginScreen_top, text="<", height=40 ,width=40, command=self.DatainspectScreen, image=image_AdminLoginScreen_top1, compound="top").pack(side="left")

        #ここに各画面の構成を作成する
        adminpasswordlist = dbaccess.getAdminLoginpassword(self.userinfolist[0])

        WIDTH  = 20        # 幅
        HEIGHT = 20        # 高さ

        image_AdminLoginScreen = tk.PhotoImage(file="assets2/share.png")
        canvas_AdminLoginScreen = tk.Canvas(frame_AdminLoginScreen_main, width=WIDTH, height=HEIGHT)
        canvas_AdminLoginScreen.create_image(WIDTH/2, HEIGHT/2, image=image_AdminLoginScreen)
        canvas_AdminLoginScreen.pack()

        passwordlimit = self.register(self.limit_char8)
        
        self.adminloginpassword = ctk.CTkEntry(frame_AdminLoginScreen_main, show="*", width=250, validate="key", validatecommand=(passwordlimit, "%P"))
        self.adminloginpassword.pack()
        self.adminloginpassword.bind("<Button-1>",self.Keybord)

        ctk.CTkButton(frame_AdminLoginScreen_main, text="Login",height=50,width=50, fg_color="black", command=lambda:self.AdminLoginPasswordcheck(adminpasswordlist)).pack()

        #ここに各画面の構成を作成する

    def AdminLoginPasswordcheck(self, passwordlist):
        password = self.adminloginpassword.get()
        print(type(password), passwordlist)
        if password in passwordlist:
            print("OK")
            self.AdminDatainspectScreen()
        else:
            messagebox.showerror("Password Error", "Please password check")

    ##AdminLoginScreen##
            
    ##AdminDatainspectScreen##
    def AdminDatainspectScreen(self):
        
        self.alldestroy()

        self.keybord = True   

        frame_AdminDatainspectScreen_top = tk.Frame(self, bg="green", height=80 ,width=700)
        frame_AdminDatainspectScreen_top.pack_propagate(False)
        frame_AdminDatainspectScreen_top.pack()

        frame_AdminDatainspectScreen_main = tk.Frame(self, bg="red", height=520 ,width=700)
        frame_AdminDatainspectScreen_main.pack_propagate(False)
        frame_AdminDatainspectScreen_main.pack()

        frame_AdminDatainspectScreen_under = tk.Frame(self, bg="blue")
        frame_AdminDatainspectScreen_under.pack_propagate(False)
        frame_AdminDatainspectScreen_under.pack(expand=True, fill=tk.BOTH)

        image_AdminDatainspectScreen_top1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AdminDatainspectScreen_top, text="Add User", height=40 ,width=40, command=self.AddUserScreen1, image=image_AdminDatainspectScreen_top1, compound="top").pack(side="left")
        image_AdminDatainspectScreen_top2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AdminDatainspectScreen_top, text="Logout", height=40 ,width=40, command=self.LoginScreen, image=image_AdminDatainspectScreen_top2, compound="top").pack(side="right")

        #ここに各画面の構成を作成する
        frame_AdminDatainspectScreen_main_1 = tk.Frame(frame_AdminDatainspectScreen_main, bg="blue", height=60 ,width=400)
        frame_AdminDatainspectScreen_main_1.pack_propagate(False)
        frame_AdminDatainspectScreen_main_1.pack(pady=5) 
        ctk.CTkButton(frame_AdminDatainspectScreen_main_1, text="◀", height=40 ,width=40, command=lambda:self.AdminChangedatebefore(self.Adminlabel_today)).pack(side="left")
        ctk.CTkButton(frame_AdminDatainspectScreen_main_1, text="▶", height=40 ,width=40, command=lambda:self.AdminChangedateafter(self.Adminlabel_today)).pack(side="right")
        self.label_AdminDatainspectScreen_main = tk.Label(frame_AdminDatainspectScreen_main_1, text=self.Adminlabel_today.strftime('%d/%m/%Y'))
        self.label_AdminDatainspectScreen_main.pack(pady=20)

        frame_AdminDatainspectScreen_main_2 = tk.Frame(frame_AdminDatainspectScreen_main, bg="blue")
        frame_AdminDatainspectScreen_main_2.pack(pady=5)
        frame_AdminDatainspectScreen_main_2_1 = tk.Frame(frame_AdminDatainspectScreen_main_2, bg="red")
        frame_AdminDatainspectScreen_main_2_1.pack(pady=5)
        frame_AdminDatainspectScreen_main_2_2 = tk.Frame(frame_AdminDatainspectScreen_main_2, bg="green")
        frame_AdminDatainspectScreen_main_2_2.pack()
        frame_AdminDatainspectScreen_main_2_3 = tk.Frame(frame_AdminDatainspectScreen_main_2, bg="white")
        frame_AdminDatainspectScreen_main_2_3.pack(pady=5)
        
        combo_timelist = ["00:00","01:00","02:00","03:00","04:00","05:00","06:00","07:00","08:00","09:00","10:00","11:00","12:00",
                      "13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"]
        combo_usernamelist = dbaccess.getAllUserName()
        combo_companynamelist = dbaccess.getAllCompanyName()
        
        tk.Label(frame_AdminDatainspectScreen_main_2_1, text="Time", font=("","15","")).pack(side="left")
        
        self.combo_AdminDatainspectScreen_fromtime = ctk.CTkComboBox(frame_AdminDatainspectScreen_main_2_1, values=combo_timelist, height=30, width=90, state="readonly", command=self.SetfromTime)
        self.combo_AdminDatainspectScreen_fromtime.pack(side="left")
        tk.Label(frame_AdminDatainspectScreen_main_2_1, text="~").pack(side="left", padx=10)
        self.combo_AdminDatainspectScreen_totime = ctk.CTkComboBox(frame_AdminDatainspectScreen_main_2_1, values=combo_timelist, height=30, width=90, state="readonly", command=self.SettoTime)
        self.combo_AdminDatainspectScreen_totime.pack(side="left")
        
        tk.Label(frame_AdminDatainspectScreen_main_2_2, text="Full Name").pack(side="left")        
        self.combo_AdminDatainspectScreen_username = ctk.CTkComboBox(frame_AdminDatainspectScreen_main_2_2, values=combo_usernamelist, height=30, state="readonly", command=self.SetfromTime)
        self.combo_AdminDatainspectScreen_username.pack(side="left", padx=10)
        
        tk.Label(frame_AdminDatainspectScreen_main_2_3, text="Company Name").pack(side="left")       
        self.combo_AdminDatainspectScreen_companyname = ctk.CTkComboBox(frame_AdminDatainspectScreen_main_2_3, values=combo_companynamelist, height=30, state="readonly", command=self.SetfromTime)
        self.combo_AdminDatainspectScreen_companyname.pack(side="left", padx=10)       
        image_AdminDatainspectScreen_1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AdminDatainspectScreen_main_2_3, text="Search", height=30, width=90, fg_color="green", command=self.SearchData, image=image_AdminDatainspectScreen_1, compound="left").pack(side="left", padx=10)

        frame_AdminDatainspectScreen_3 = tk.Frame(frame_AdminDatainspectScreen_main, bg="blue", height=30 ,width=500)
        frame_AdminDatainspectScreen_3.pack_propagate(False)
        frame_AdminDatainspectScreen_3.pack(pady=10)
        ctk.CTkButton(frame_AdminDatainspectScreen_3, text="CSV Output", height=40 ,width=40, command=self.CSVoutput).pack(side="right")
        
        frame_AdminDatainspectScreen_4 = ctk.CTkScrollableFrame(frame_AdminDatainspectScreen_main, fg_color="transparent")
        frame_AdminDatainspectScreen_4.pack_propagate(False)
        frame_AdminDatainspectScreen_4.pack(expand=True, fill=tk.BOTH)

        History_YearAndMonth = self.Adminlabel_today.strftime('%Y%m')
        History_Day = self.Adminlabel_today.strftime('%d')
        list_entryleavingtime = dbaccess.getAdminEntryLeavingtime(History_YearAndMonth, History_Day)   #[(EntryTime, LeavingTime, UserMst.UserName, UserMst.CompanyName),(),()..]

        for timeinfo in list_entryleavingtime:
            entryingtimetext = ""
            leavingtimetext = ""
            username = ""
            companyname = ""
            frame_AdminDatainspectScreen_4_1 = ""
            frame_AdminDatainspectScreen_4_2 = ""
            if timeinfo[0] != "":
                frame_AdminDatainspectScreen_4_1 = ctk.CTkFrame(frame_AdminDatainspectScreen_4, height=60 ,width=500, corner_radius=20)
                frame_AdminDatainspectScreen_4_1.pack_propagate(False)
                frame_AdminDatainspectScreen_4_1.grid(pady=3)
                entryingtimetext = timeinfo[0]
                entryingtimetext = entryingtimetext[:2] + ':' + entryingtimetext[2:]
                username = timeinfo[2]
                companyname = timeinfo[3]
                ctk.CTkLabel(frame_AdminDatainspectScreen_4_1,  text="{}".format(entryingtimetext), height=60 ,width=0).pack(side="left", padx=20)
                ctk.CTkLabel(frame_AdminDatainspectScreen_4_1, text="{}\n{}".format(username, companyname), fg_color="green").pack(side="left", padx=20)
                ctk.CTkLabel(frame_AdminDatainspectScreen_4_1,  text="Entering", height=60 ,width=60).pack(side="left", padx=5)
                if timeinfo[1] != "":
                    frame_AdminDatainspectScreen_4_2 = ctk.CTkFrame(frame_AdminDatainspectScreen_4, height=60 ,width=500, corner_radius=20)
                    frame_AdminDatainspectScreen_4_2.pack_propagate(False)
                    frame_AdminDatainspectScreen_4_2.grid(pady=3)
                    leavingtimetext = timeinfo[1]
                    leavingtimetext = leavingtimetext[:2] + ':' + leavingtimetext[2:]
                    username = timeinfo[2]
                    companyname = timeinfo[3]
                    ctk.CTkLabel(frame_AdminDatainspectScreen_4_2,  text="{}".format(leavingtimetext), height=60 ,width=40).pack(side="left", padx=20)
                    ctk.CTkLabel(frame_AdminDatainspectScreen_4_2, text="{}\n{}".format(username, companyname), fg_color="green").pack(side="left", padx=20)
                    ctk.CTkLabel(frame_AdminDatainspectScreen_4_2,  text="Leaving", height=60 ,width=60).pack(side="left", padx=5)

        #ここに各画面の構成を作成する

        image_AdminDatainspectScreen_under1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AdminDatainspectScreen_under, text="Data", height=80 ,width=80, fg_color="green", image=image_AdminDatainspectScreen_under1, compound="top").pack(padx=90, side="left")
        image_AdminDatainspectScreen_under2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AdminDatainspectScreen_under, text="User", height=80 ,width=80, command=self.AdminAccountinfoScreen, image=image_AdminDatainspectScreen_under2, compound="top").pack(padx=90, side="right")


    def SetfromTime(self,event):
        fromtime = self.combo_AdminDatainspectScreen_fromtime.get()
        print(fromtime)

    def SettoTime(self,event):
        totime = self.combo_AdminDatainspectScreen_totime.get()
        print(totime)

    def SearchData(self):
        pass

    def AdminChangedatebefore(self, label_today):
        ###ここで前の日のデータを取得し表示させる
        print("Datebefore")
        datebefore = timedelta(days=1)
        label_day = label_today - datebefore
        self.Adminlabel_today = label_day
        self.label_AdminDatainspectScreen_main["text"] = self.Adminlabel_today.strftime('%d/%m/%Y')
        self.AdminDatainspectScreen()

    def AdminChangedateafter(self, label_today):
        print("Dateafter")
        ###ここで次の日のデータを取得し表示させる
        dateafter = timedelta(days=1)
        label_day = label_today + dateafter
        self.Adminlabel_today = label_day
        self.label_AdminDatainspectScreen_main["text"] = self.Adminlabel_today.strftime('%d/%m/%Y')
        self.AdminDatainspectScreen()
    ##AdminDatainspectScreen##
        
    ##AdminAccountinfoScreen##
    def AdminAccountinfoScreen(self):
        
        self.alldestroy()

        self.keybord = True

        frame_AdminAccountinfoScreen_top = tk.Frame(self, bg="green", height=80 ,width=700)
        frame_AdminAccountinfoScreen_top.pack_propagate(False)
        frame_AdminAccountinfoScreen_top.pack()

        frame_AdminAccountinfoScreen_main = tk.Frame(self, bg="red", height=520 ,width=700)
        frame_AdminAccountinfoScreen_main.pack_propagate(False)
        frame_AdminAccountinfoScreen_main.pack()

        frame_AdminAccountinfoScreen_under = tk.Frame(self, bg="blue")
        frame_AdminAccountinfoScreen_under.pack_propagate(False)
        frame_AdminAccountinfoScreen_under.pack(expand=True, fill=tk.BOTH)

        image_AdminAccountinfoScreen_top1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AdminAccountinfoScreen_top, text="Add User", height=40 ,width=40, command=self.AddUserScreen1, image=image_AdminAccountinfoScreen_top1, compound="top").pack(side="left")
        image_AdminAccountinfoScreen_top2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AdminAccountinfoScreen_top, text="Logout", height=40 ,width=40, command=self.LoginScreen, image=image_AdminAccountinfoScreen_top2, compound="top").pack(side="right")

        #ここに各画面の構成を作成する

        frame_AdminAccountinfoScreen_main_1 = tk.Frame(frame_AdminAccountinfoScreen_main, bg="blue")
        frame_AdminAccountinfoScreen_main_1.pack(pady=5)
        frame_AdminAccountinfoScreen_main_1_1 = tk.Frame(frame_AdminAccountinfoScreen_main_1, bg="blue")
        frame_AdminAccountinfoScreen_main_1_1.pack(pady=5)
        frame_AdminAccountinfoScreen_main_1_2 = tk.Frame(frame_AdminAccountinfoScreen_main_1, bg="blue")
        frame_AdminAccountinfoScreen_main_1_2.pack(pady=5)

        tk.Label(frame_AdminAccountinfoScreen_main_1_1, text="Full Name").pack(side="left")
        usernamelimit = self.register(self.limit_char20)
        self.serch_username = ctk.CTkEntry(frame_AdminAccountinfoScreen_main_1_1, width=150, validate="key", validatecommand=(usernamelimit, "%P"))
        self.serch_username.pack(side="left")
        self.serch_username.bind("<Button-1>",self.Keybord)
        tk.Label(frame_AdminAccountinfoScreen_main_1_2, text="Company Name").pack(side="left")
        companynamelimit = self.register(self.limit_char50)
        self.serch_companyname = ctk.CTkEntry(frame_AdminAccountinfoScreen_main_1_2, width=150, validate="key", validatecommand=(companynamelimit, "%P"))
        self.serch_companyname.pack(side="left")
        self.serch_companyname.bind("<Button-1>",self.Keybord)
        image_AdminAccountinfoScreen_1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AdminAccountinfoScreen_main_1_2, text="Search", height=30, width=90, fg_color="green", image=image_AdminAccountinfoScreen_1, compound="left").pack(side="left")

        frame_AdminAccountinfoScreen_2 = tk.Frame(frame_AdminAccountinfoScreen_main, bg="blue", height=30 ,width=500)
        frame_AdminAccountinfoScreen_2.pack_propagate(False)
        frame_AdminAccountinfoScreen_2.pack(pady=10)
        ctk.CTkButton(frame_AdminAccountinfoScreen_2, text="CSV Output", height=40 ,width=40, command=self.CSVoutput).pack(side="right")
        
        frame_AdminAccountinfoScreen_3 = ctk.CTkScrollableFrame(frame_AdminAccountinfoScreen_main, fg_color="transparent")
        frame_AdminAccountinfoScreen_3.pack_propagate(False)
        frame_AdminAccountinfoScreen_3.pack(expand=True, fill=tk.BOTH)

        self.alluserinfolist = dbaccess.getAllUserinfo()   #[(UserID, UserName, CompanyName, Pass, FacePhoto, Authority),(),..]
       
        image_AdminAccountinfoScreen_3_1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        image_AdminAccountinfoScreen_3_2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        image_AdminAccountinfoScreen_3_3 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))

        for userinfo in self.alluserinfolist:
            userid = ""
            username = ""
            companyname = ""
            frame_AdminAccountinfoScreen_3_1 = ctk.CTkFrame(frame_AdminAccountinfoScreen_3, height=60 ,width=500, corner_radius=20)
            frame_AdminAccountinfoScreen_3_1.pack_propagate(False)
            frame_AdminAccountinfoScreen_3_1.grid(pady=3)
            
            # if Authority is true
            if userinfo[5] == "true":
                userid = userinfo[0]
                username = userinfo[1]
                companyname = userinfo[2]
                ctk.CTkButton(frame_AdminAccountinfoScreen_3_1,  text="", height=40 ,width=40, command=partial(self.deprivationorgrantAuthority, "deprivation", userid, username, companyname), image=image_AdminAccountinfoScreen_3_1).pack(side="left")
                ctk.CTkLabel(frame_AdminAccountinfoScreen_3_1, text="{}\n{}".format(username, companyname), fg_color="green").pack(side="left", padx=20)
                ctk.CTkButton(frame_AdminAccountinfoScreen_3_1,  text="Reset", height=20 ,width=60, command=partial(self.resetPassword,userid, username, companyname), image=image_AdminAccountinfoScreen_3_2, compound="left").pack(side="left", padx=5)
                ctk.CTkButton(frame_AdminAccountinfoScreen_3_1,  text="Delete", height=20 ,width=60, command=partial(self.deleteUserinfo,userid, username, companyname), image=image_AdminAccountinfoScreen_3_3, compound="left").pack(side="left")                   
            else:
                userid = userinfo[0]
                username = userinfo[1]
                companyname = userinfo[2]
                ctk.CTkButton(frame_AdminAccountinfoScreen_3_1,  text="", height=40 ,width=40, command=partial(self.deprivationorgrantAuthority,"grant", userid, username, companyname), image=image_AdminAccountinfoScreen_3_1).pack(side="left")
                ctk.CTkLabel(frame_AdminAccountinfoScreen_3_1, text="{}\n{}".format(username, companyname), fg_color="green").pack(side="left", padx=20)
                ctk.CTkButton(frame_AdminAccountinfoScreen_3_1,  text="Reset", height=20 ,width=60, command=partial(self.resetPassword,userid, username, companyname), image=image_AdminAccountinfoScreen_3_2, compound="left").pack(side="left", padx=5)
                ctk.CTkButton(frame_AdminAccountinfoScreen_3_1,  text="Delete", height=20 ,width=60, command=partial(self.deleteUserinfo,userid, username, companyname), image=image_AdminAccountinfoScreen_3_3, compound="left").pack(side="left")
        #ここに各画面の構成を作成する

        image_AdminAccountinfoScreen_under1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AdminAccountinfoScreen_under, text="Data", height=80 ,width=80, command=self.AdminDatainspectScreen, image=image_AdminAccountinfoScreen_under1, compound="top").pack(padx=90, side="left")
        image_AdminAccountinfoScreen_under2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AdminAccountinfoScreen_under, text="User", height=80 ,width=80, fg_color="green", image=image_AdminAccountinfoScreen_under2, compound="top").pack(padx=90, side="right")

    def deprivationorgrantAuthority(self, Authotity, userid, username, companyname):
        if Authotity == "deprivation":
            res_deprivation = messagebox.askokcancel("Deprivation Authority", "This user has been granted permissinons. \nWould you like to revoke them?")
            if res_deprivation:
                leftoveradminuser = dbaccess.getLeftoverAdminUser()
                if leftoveradminuser[0] == 1:
                    messagebox.showwarning("Authotity Deprivation", "You cannnot revoke pemissions from this user. At least one user with administrator privieges is required.")
                else:
                    grantAdminAuthority_save = "no"
                    authority = "false"
                    dbaccess.updateAdminAuthority(grantAdminAuthority_save, userid, username, companyname, authority)

        elif Authotity == "grant":
            res_grant = messagebox.askokcancel("Grant Authority", "Would you like to grant administrator \nprivileges to this user?")
            if res_grant:
                self.AdminAuthoritygrantScreen(userid, username, companyname)

    def resetPassword(self, userid, username, companyname):
        res_resetpassword = messagebox.askokcancel("Reset Password", "Would you like to reset the password \n and change it to \"0000\"")
        print(userid, username, companyname)
        if res_resetpassword:
            dbaccess.updateResetpassword(userid, username, companyname)
            print("pass reset")

    def deleteUserinfo(self, userid, username, companyname):
        res = messagebox.askokcancel("Delete Userinfo", "Are you sure you want to turn off the app and the unit?")
        if res:
            ###
            dbaccess.deleteUserinfo(userid, username, companyname)
            print("deprivation")

    ##AdminAccountinfoScreen##
            
    ##AdminAuthoritygrantScreen##
            
    def AdminAuthoritygrantScreen(self, userid, username, companyname):
        
        self.alldestroy()

        frame_AdminAuthoritygrantScreen_top = tk.Frame(self, bg="green", height=80 ,width=700)
        frame_AdminAuthoritygrantScreen_top.pack_propagate(False)
        frame_AdminAuthoritygrantScreen_top.pack()

        frame_AdminAuthoritygrantScreen_main = tk.Frame(self, bg="red", width=700)
        frame_AdminAuthoritygrantScreen_main.pack_propagate(False)
        frame_AdminAuthoritygrantScreen_main.pack(expand=True, fill=tk.BOTH)

        image_AdminAuthoritygrantScreen_top = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AdminAuthoritygrantScreen_top, text="<", height=40 ,width=40, command=self.AdminAccountinfoScreen, image=image_AdminAuthoritygrantScreen_top, compound="top").pack(side="left")

        #ここに各画面の構成を作成する
        self.keybord = True

        frame_AdminAuthoritygrantScreen = tk.Frame(frame_AdminAuthoritygrantScreen_main, bg="white")
        frame_AdminAuthoritygrantScreen.pack(pady=10)

        frame_AdminAuthoritygrantScreen_2 = tk.Frame(frame_AdminAuthoritygrantScreen_main, bg="blue")
        frame_AdminAuthoritygrantScreen_2.pack(pady=10)

        tk.Label(frame_AdminAuthoritygrantScreen, text="Change Your Password",font=("MSゴシック", "30", "bold"), bg="white").pack()
        tk.Label(frame_AdminAuthoritygrantScreen, text="Please enter the admin password.", bg="white", font=("","15","")).pack(pady=10)

        AdminAuthoritylimit = self.register(self.limit_char8)
        AdminAuthoritylimit_confirm = self.register(self.limit_char8)

        tk.Label(frame_AdminAuthoritygrantScreen_2, text="Password  ", bg="white", width=30).grid(row=0, column=0, pady=10)
        tk.Label(frame_AdminAuthoritygrantScreen_2, text="Confirm\nPassword  ", bg="white", width=30).grid(row=1, column=0, pady=10)
        self.grantAdminAuthority = ctk.CTkEntry(frame_AdminAuthoritygrantScreen_2, width=200,validate="key", validatecommand=(AdminAuthoritylimit, "%P"))
        self.grantAdminAuthority_confirm = ctk.CTkEntry(frame_AdminAuthoritygrantScreen_2, width=200,validate="key", validatecommand=(AdminAuthoritylimit_confirm, "%P"))
        
        self.grantAdminAuthority.bind("<Button-1>",self.Keybord)
        self.grantAdminAuthority_confirm.bind("<Button-1>",self.Keybord)

        self.grantAdminAuthority.grid(row=0, column=1)
        self.grantAdminAuthority_confirm.grid(row=1, column=1)

        image_AdminAuthoritygrantScreen_2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AdminAuthoritygrantScreen_2, text="Continue                ", command=lambda:self.AdminAuthoritygrant(userid, username, companyname),  image=image_AdminAuthoritygrantScreen_2, compound="right").grid(row=2, column=0, columnspan=2, pady=50)

    def AdminAuthoritygrant(self, userid, username, companyname):
        grantAdminAuthority = self.grantAdminAuthority.get()
        changeAdminAuthority_confirm = self.grantAdminAuthority_confirm.get()
        space = " "
        authority = "true"
        if space not in grantAdminAuthority:
            if len(grantAdminAuthority) == 8:
                if grantAdminAuthority == changeAdminAuthority_confirm:
                    grantAdminAuthority_save = grantAdminAuthority
                    dbaccess.updateAdminAuthority(grantAdminAuthority_save, userid, username, companyname, authority)
                    time.sleep(5)
                    self.AdminAccountinfoScreen()
                else:
                    messagebox.showerror("Password Error", "Password not match")        
            else:
                messagebox.showerror("Password Error", "Password 8password insert")
        else:
            messagebox.showerror("Password Error", "Do not include spaces")
        

        #ここに各画面の構成を作成する

    ##AdminAuthoritygrantScreen##
        
    ##AddUserScreen1  add name companyname##
    def AddUserScreen1(self):
        
        self.alldestroy()      

        frame_AddUserScreen1_top = tk.Frame(self, bg="green", height=80 ,width=700)
        frame_AddUserScreen1_top.pack_propagate(False)
        frame_AddUserScreen1_top.pack()

        frame_AddUserScreen1_main = tk.Frame(self, bg="red", width=700)
        frame_AddUserScreen1_main.pack_propagate(False)
        frame_AddUserScreen1_main.pack(expand=True, fill=tk.BOTH)

        image_AddUserScreen1_top1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AddUserScreen1_top, text="<", height=40 ,width=40, command=self.AccountinfoScreen, image=image_AddUserScreen1_top1, compound="top").pack(side="left")

        #ここに各画面の構成を作成する
        self.keybord = True

        frame_AddUserScreen1_main_1 = tk.Frame(frame_AddUserScreen1_main, bg="white")
        frame_AddUserScreen1_main_1.pack(pady=10)

        frame_AddUserScreen1_main_2 = tk.Frame(frame_AddUserScreen1_main, bg="white")
        frame_AddUserScreen1_main_2.pack(pady=10)

        frame_AddUserScreen1_main_3 = tk.Frame(frame_AddUserScreen1_main, bg="white")
        frame_AddUserScreen1_main_3.pack(pady=10)

        tk.Label(frame_AddUserScreen1_main_1, text="Let's Create the User",font=("MSゴシック", "30", "bold"), bg="white").pack()
        image_AddUserScreen1_1 = ctk.CTkImage(light_image=Image.open("assets2/AddUserScreen1.png"), size=(510,70))
        ctk.CTkLabel(frame_AddUserScreen1_main_1, text="", image=image_AddUserScreen1_1).pack(pady=15)   
        tk.Label(frame_AddUserScreen1_main_1, text="Enter your name and company name.", bg="white", font=("","15","")).pack(pady=10)

        tk.Label(frame_AddUserScreen1_main_2, text="Full Name     ", bg="white", font=("","15","")).grid(row=0, column=0)
        tk.Label(frame_AddUserScreen1_main_2, text="Company Name  ", bg="white", font=("","15","")).grid(row=1, column=0)
        usernamelimit = self.register(self.limit_char20)
        companynamelimit = self.register(self.limit_char50)
        self.createusername = ctk.CTkEntry(frame_AddUserScreen1_main_2, width=200, validate="key", validatecommand=(usernamelimit, "%P"))
        self.createcompanyname = ctk.CTkEntry(frame_AddUserScreen1_main_2, width=200, validate="key", validatecommand=(companynamelimit, "%P"))
        
        self.createusername.bind("<Button-1>",self.Keybord)
        self.createcompanyname.bind("<Button-1>",self.Keybord)

        self.createusername.grid(row=0, column=1)
        self.createcompanyname.grid(row=1, column=1)

        image_AddUserScreen1_2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AddUserScreen1_main_3, text="Continue                ", command=self.setnamevalue,  image=image_AddUserScreen1_2, compound="right").pack()

        #ここに各画面の構成を作成する
    
    def setnamevalue(self):
        if len(self.createusername.get()) != 0 and len(self.createcompanyname.get()) != 0:
            self.createusername_save = self.createusername.get()
            self.createcompanyname_save = self.createcompanyname.get()
            self.AddUserScreen2()
            print("name: ", self.createusername_save, self.createcompanyname_save)
        else:
            messagebox.showerror("Create name Error", "Please name Insert")
    
    ##AddUserScreen1##   
        
    ##AddUserScreen2 add password##
    def AddUserScreen2(self):
        self.alldestroy()      

        frame_AddUserScreen2_top = tk.Frame(self, bg="green", height=80 ,width=700)
        frame_AddUserScreen2_top.pack_propagate(False)
        frame_AddUserScreen2_top.pack()

        frame_AddUserScreen2_main = tk.Frame(self, bg="red", width=700)
        frame_AddUserScreen2_main.pack_propagate(False)
        frame_AddUserScreen2_main.pack(expand=True, fill=tk.BOTH)

        image_AddUserScreen2_top1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AddUserScreen2_top, text="<", height=40 ,width=40, command=self.AddUserScreen1, image=image_AddUserScreen2_top1, compound="top").pack(side="left")

        #ここに各画面の構成を作成する
        self.keybord = True

        frame_AddUserScreen2_main_1 = tk.Frame(frame_AddUserScreen2_main, bg="white")
        frame_AddUserScreen2_main_1.pack(pady=10)

        frame_AddUserScreen2_main_2 = tk.Frame(frame_AddUserScreen2_main, bg="white")
        frame_AddUserScreen2_main_2.pack(pady=10)

        tk.Label(frame_AddUserScreen2_main_1, text="Let's Create the User",font=("MSゴシック", "30", "bold"), bg="white").pack()
        image_AddUserScreen2_1 = ctk.CTkImage(light_image=Image.open("assets2/AddUserScreen2.png"), size=(510,70))
        ctk.CTkLabel(frame_AddUserScreen2_main_1, text="", image=image_AddUserScreen2_1).pack(pady=15)   
        tk.Label(frame_AddUserScreen2_main_1, text="Set up the password for authentication.", bg="white", font=("","15","")).pack(pady=10)

        passwordlimit = self.register(self.limit_char4)
        self.createpassword = tk.Entry(frame_AddUserScreen2_main_1, show="*" ,width=30, validate="key", validatecommand=(passwordlimit, "%P"))
        self.createpassword.pack(pady=5)

        image_AddUserScreen2_2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))

        ctk.CTkButton(frame_AddUserScreen2_main_2, text="1",height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget("1")).grid(row=0,column=0)
        ctk.CTkButton(frame_AddUserScreen2_main_2, text="2",height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget("2")).grid(row=0,column=1)
        ctk.CTkButton(frame_AddUserScreen2_main_2, text="3",height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget("3")).grid(row=0,column=2)
        ctk.CTkButton(frame_AddUserScreen2_main_2, text="4",height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget("4")).grid(row=1,column=0)
        ctk.CTkButton(frame_AddUserScreen2_main_2, text="5",height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget("5")).grid(row=1,column=1)
        ctk.CTkButton(frame_AddUserScreen2_main_2, text="6",height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget("6")).grid(row=1,column=2)
        ctk.CTkButton(frame_AddUserScreen2_main_2, text="7",height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget("7")).grid(row=2,column=0)
        ctk.CTkButton(frame_AddUserScreen2_main_2, text="8",height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget("8")).grid(row=2,column=1)
        ctk.CTkButton(frame_AddUserScreen2_main_2, text="9",height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget("9")).grid(row=2,column=2)
        ctk.CTkButton(frame_AddUserScreen2_main_2, text="", height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget("clear"),compound="right", image=image_AddUserScreen2_2).grid(row=3,column=0)
        ctk.CTkButton(frame_AddUserScreen2_main_2, text="0",height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget("0")).grid(row=3,column=1)
        ctk.CTkButton(frame_AddUserScreen2_main_2, text="Enter",height=70,width=70, fg_color="gray", command=self.createPasswordcheck).grid(row=3,column=2)

    def createPasswordget(self,value):
        if value == "clear":
            self.createpassword.delete(0,tk.END)
        else:
            self.createpassword.insert(tk.END,value)

    def createPasswordcheck(self):
        if len(self.createpassword.get()) == 4:
            self.createpassword_save = self.createpassword.get()
            self.AddUserScreen2_confirm()
        else:
            messagebox.showerror("Password Error", "Please 4Password Insert")

        #ここに各画面の構成を作成する
    
    ##AddUserScreen2##
            
    ##AddUserScreen2_confirm confirm password##
    def AddUserScreen2_confirm(self):
        self.alldestroy()      

        frame_AddUserScreen2_confirm_top = tk.Frame(self, bg="green", height=80 ,width=700)
        frame_AddUserScreen2_confirm_top.pack_propagate(False)
        frame_AddUserScreen2_confirm_top.pack()

        frame_AddUserScreen2_confirm_main = tk.Frame(self, bg="red", width=700)
        frame_AddUserScreen2_confirm_main.pack_propagate(False)
        frame_AddUserScreen2_confirm_main.pack(expand=True, fill=tk.BOTH)

        image_AddUserScreen2_confirm_top1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AddUserScreen2_confirm_top, text="<", height=40 ,width=40, command=self.AddUserScreen2, image=image_AddUserScreen2_confirm_top1, compound="top").pack(side="left")

        #ここに各画面の構成を作成する
        self.keybord = True

        frame_AddUserScreen2_confirm_main_1 = tk.Frame(frame_AddUserScreen2_confirm_main, bg="white")
        frame_AddUserScreen2_confirm_main_1.pack(pady=10)

        frame_AddUserScreen2_confirm_main_2 = tk.Frame(frame_AddUserScreen2_confirm_main, bg="white")
        frame_AddUserScreen2_confirm_main_2.pack(pady=10)

        tk.Label(frame_AddUserScreen2_confirm_main_1, text="Let's Create the User",font=("MSゴシック", "30", "bold"), bg="white").pack()
        image_AddUserScreen2_confirm_1 = ctk.CTkImage(light_image=Image.open("assets2/AddUserScreen3.png"), size=(510,70))
        ctk.CTkLabel(frame_AddUserScreen2_confirm_main_1, text="", image=image_AddUserScreen2_confirm_1).pack(pady=15)   
        tk.Label(frame_AddUserScreen2_confirm_main_1, text="For cofirmation, please enter it again.", bg="white", font=("","15","")).pack(pady=10)

        passwordlimit = self.register(self.limit_char4)
        self.createpassword_confirm = tk.Entry(frame_AddUserScreen2_confirm_main_1, show="*" ,width=30, validate="key", validatecommand=(passwordlimit, "%P"))
        self.createpassword_confirm.pack(pady=5)

        image_AddUserScreen2_confirm_2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))

        ctk.CTkButton(frame_AddUserScreen2_confirm_main_2, text="1",height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget_confirm("1")).grid(row=0,column=0)
        ctk.CTkButton(frame_AddUserScreen2_confirm_main_2, text="2",height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget_confirm("2")).grid(row=0,column=1)
        ctk.CTkButton(frame_AddUserScreen2_confirm_main_2, text="3",height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget_confirm("3")).grid(row=0,column=2)
        ctk.CTkButton(frame_AddUserScreen2_confirm_main_2, text="4",height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget_confirm("4")).grid(row=1,column=0)
        ctk.CTkButton(frame_AddUserScreen2_confirm_main_2, text="5",height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget_confirm("5")).grid(row=1,column=1)
        ctk.CTkButton(frame_AddUserScreen2_confirm_main_2, text="6",height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget_confirm("6")).grid(row=1,column=2)
        ctk.CTkButton(frame_AddUserScreen2_confirm_main_2, text="7",height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget_confirm("7")).grid(row=2,column=0)
        ctk.CTkButton(frame_AddUserScreen2_confirm_main_2, text="8",height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget_confirm("8")).grid(row=2,column=1)
        ctk.CTkButton(frame_AddUserScreen2_confirm_main_2, text="9",height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget_confirm("9")).grid(row=2,column=2)
        ctk.CTkButton(frame_AddUserScreen2_confirm_main_2, text="", height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget_confirm("clear"),compound="right", image=image_AddUserScreen2_confirm_2).grid(row=3,column=0)
        ctk.CTkButton(frame_AddUserScreen2_confirm_main_2, text="0",height=70,width=70, fg_color="gray", command=lambda:self.createPasswordget_confirm("0")).grid(row=3,column=1)
        ctk.CTkButton(frame_AddUserScreen2_confirm_main_2, text="Enter",height=70,width=70, fg_color="gray", command=self.createPasswordcheck_confirm).grid(row=3,column=2)

    def createPasswordget_confirm(self,value):
        if value == "clear":
            self.createpassword_confirm.delete(0,tk.END)
        else:
            self.createpassword_confirm.insert(tk.END,value)

    def createPasswordcheck_confirm(self):
        if len(self.createpassword_confirm.get()) == 4:
            createpassword_confirm = self.createpassword_confirm.get()
            if self.createpassword_save == createpassword_confirm:
                self.AddUserScreen3()
            else:
                messagebox.showerror("Password Error", "Password not match")
        else:
            messagebox.showerror("Password Error", "Please 4Password Insert")

        #ここに各画面の構成を作成する
    ##AddUserScreen2_confirm##

    ##AddUserScreen3##
    def AddUserScreen3(self):
        self.alldestroy()      

        frame_AddUserScreen3_top = tk.Frame(self, bg="green", height=80 ,width=700)
        frame_AddUserScreen3_top.pack_propagate(False)
        frame_AddUserScreen3_top.pack()

        frame_AddUserScreen3_main = tk.Frame(self, bg="red", width=700)
        frame_AddUserScreen3_main.pack_propagate(False)
        frame_AddUserScreen3_main.pack(expand=True, fill=tk.BOTH)

        image_AddUserScreen3_top1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AddUserScreen3_top, text="<", height=40 ,width=40, command=self.AddUserScreen2, image=image_AddUserScreen3_top1, compound="top").pack(side="left")

        #ここに各画面の構成を作成する
        frame_frame_AddUserScreen3_main_1 = tk.Frame(frame_AddUserScreen3_main, bg="white")
        frame_frame_AddUserScreen3_main_1.pack(pady=10)

        frame_frame_AddUserScreen3_main_2 = tk.Frame(frame_AddUserScreen3_main, bg="blue")
        frame_frame_AddUserScreen3_main_2.pack(pady=10)

        tk.Label(frame_frame_AddUserScreen3_main_1, text="Let's Create the User",font=("MSゴシック", "30", "bold"), bg="white").pack()
        image_AddUserScreen2_confirm_1 = ctk.CTkImage(light_image=Image.open("assets2/AddUserScreen4.png"), size=(510,70))
        ctk.CTkLabel(frame_frame_AddUserScreen3_main_1, text="", image=image_AddUserScreen2_confirm_1).pack(pady=15)   
        tk.Label(frame_frame_AddUserScreen3_main_1, text="Register facial information for authentication.", bg="white", font=("","15","")).pack(pady=10)

        image_AccountinfoScreen_3 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_frame_AddUserScreen3_main_2, text="Camera  >", height=120 ,width=200, command=self.createtakepicture, image=image_AccountinfoScreen_3, compound="top").pack(padx=15)
        image_AccountinfoScreen_4 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_frame_AddUserScreen3_main_2, text="Picture  >", height=120 ,width=200, command=self.createselectpicture, image=image_AccountinfoScreen_4, compound="top").pack(padx=15, pady=20)
        #ここに各画面の構成を作成する

    def createtakepicture(self):
        self.AddUserScreen4()

    def createselectpicture(self):
        pass
    ##AddUserScreen3##

    ##AddUserScreen4##
    def AddUserScreen4(self):
        userid = "end +1"   ###
        createusername = self.createusername_save
        createcompanyname = self.createcompanyname_save
        createpassword = self.createpassword_save
        picture = "sample"   ###

        self.alldestroy()      

        frame_AddUserScreen4_top = tk.Frame(self, bg="green", height=80 ,width=700)
        frame_AddUserScreen4_top.pack_propagate(False)
        frame_AddUserScreen4_top.pack()

        frame_AddUserScreen4_main = tk.Frame(self, bg="red", width=700)
        frame_AddUserScreen4_main.pack_propagate(False)
        frame_AddUserScreen4_main.pack(expand=True, fill=tk.BOTH)

        image_AddUserScreen4_top1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_AddUserScreen4_top, text="<", height=40 ,width=40, command=self.AddUserScreen3, image=image_AddUserScreen4_top1, compound="top").pack(side="left")

        #ここに各画面の構成を作成する
        frame_frame_AddUserScreen4_main_1 = tk.Frame(frame_AddUserScreen4_main, bg="white")
        frame_frame_AddUserScreen4_main_1.pack(pady=10)

        frame_frame_AddUserScreen4_main_2 = tk.Frame(frame_AddUserScreen4_main, bg="blue")
        frame_frame_AddUserScreen4_main_2.pack(pady=10)

        frame_frame_AddUserScreen4_main_3 = tk.Frame(frame_AddUserScreen4_main, bg="blue")
        frame_frame_AddUserScreen4_main_3.pack(pady=10)

        tk.Label(frame_frame_AddUserScreen4_main_1, text="Let's Create the User",font=("MSゴシック", "30", "bold"), bg="white").pack()
        image_AddUserScreen2_confirm_1 = ctk.CTkImage(light_image=Image.open("assets2/UserScreen1.png"), size=(510,70))
        ctk.CTkLabel(frame_frame_AddUserScreen4_main_1, text="", image=image_AddUserScreen2_confirm_1).pack(pady=15)   
        tk.Label(frame_frame_AddUserScreen4_main_1, text="Complete user registration with the following information. \n If you are ready, please press OK.", bg="white", font=("","15","")).pack(pady=10)

        myfont = font.Font(underline=True)
        tk.Label(frame_frame_AddUserScreen4_main_2, text="User ID : {}".format(userid), font=myfont, bg="white").grid(row=0, column=0)
        tk.Label(frame_frame_AddUserScreen4_main_2, text="Full Name : {}".format(createusername), font=myfont, bg="white").grid(row=1, column=0)
        tk.Label(frame_frame_AddUserScreen4_main_2, text="Company Name : {}".format(createcompanyname), font=myfont, bg="white").grid(row=2, column=0)
        tk.Label(frame_frame_AddUserScreen4_main_2, text="Password : {}".format(createpassword), font=myfont, bg="white").grid(row=3, column=0)
        #ここに各画面の構成を作成する

        
        ctk.CTkButton(frame_frame_AddUserScreen4_main_3, text="OK", command=lambda:self.createDatasave(userid, createusername, createcompanyname, createpassword, picture)).pack()
    
    def createDatasave(self, userid, createusername, createcompanyname, createpassword, picture):
        try:
            dbaccess.createUserinfo(createusername, createcompanyname, createpassword, picture)
            print("DB反映")
            self.AccountinfoScreen()
        except Exception as e:
            print(e)
            print("languege not DB")

    ##AddUserScreen4##

if __name__ == "__main__":
    app = Useradminop()
    app.title("Start setting")
    app.resizable(False,False)
    #app.deiconify()
    #app.overrideredirect(True)
    #app.minsize(540,720)
    #app.maxsize(540,720)
    app.geometry("540x720")   #横x縦
    app.protocol("WM_DELETE_WINDOW", app.close_window)
    #app.state('iconic')   #normal,iconic, or withdrawn

    #app.configure(bg="white")        #tk(tkinter).Tk
    app.configure(fg_color="white")   #ctk.CTk
    
    app.LoginScreen()

    app.mainloop()