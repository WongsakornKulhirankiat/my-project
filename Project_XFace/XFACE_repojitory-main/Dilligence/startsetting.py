#
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import font
from tkinter import filedialog
import customtkinter as ctk
from PIL import Image

import time

import daomodule

dbaccess = daomodule.StartsettingDAO()

# Todo class
#class StartSetting(tk.Tk):       #tk(tkinter).Tk
class StartSetting(ctk.CTk):      #ctk.CTk

    ##common#

    def alldestroy(self):
        for widget in self.winfo_children():
            widget.destroy()

    def limit_char4(self,string):
        return len(string) <= 4
    
    def limit_char8(self,string):
        return len(string) <= 8
    
    def Keybord(self,event):
        self.widgetinfo = ""
        self.widgetinfo = event.widget   #Keybordメソッドを実行しているwidget情報を取得
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
            ctk.CTkButton(frame_Keybord, text="_",height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("_")).grid(row=3,column=7)
            #ctk.CTkButton(frame_Keybord, text="clear", height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("clear"),compound="right", image=image_UserScreen2_2).grid(row=3,column=8)
            ctk.CTkButton(frame_Keybord, text="clear", height=50,width=50, fg_color="gray", command=lambda:self.KeybordGet("clear")).grid(row=3,column=8)
            #ctk.CTkButton(frame_Keybord, text="OK",height=50,width=50, fg_color="gray", command=self.KeybordDelete).grid(row=3,column=9)
            ctk.CTkButton(frame_Keybord, text="⇧", height=50,width=50, fg_color="gray", command=self.KeybordUpper).grid(row=3,column=9)
    
    def KeybordDelete(self):
        self.keybord = True
        self.frame_Keybord.destroy()

    def KeybordGet(self,value):
        if value == "clear":
            self.widgetinfo.delete(0,tk.END)
        elif self.upper:
            value = value.upper()
            self.widgetinfo.insert(tk.END,value)
        else:
            self.widgetinfo.insert(tk.END,value)

    def KeybordUpper(self):
        if self.upper:
            self.upper = False
        else:
            self.upper = True

    ##common#

    ##TimezoneScreen##
    def TimezoneScreen(self):

        self.time_zone_dict = {"-12:00":("International Date Line West", "Etc/GMT+12"),
                        "-11:00":("Midway Island, Samoa", "Etc/GMT+11"),
                        "-10:00":("Hawaii", "Etc/GMT+10"),
                        "-9:00":("Alaska", "Etc/GMT+9"),
                        "-8:00":("Pacific Time (US and Canada); Tijuana", "Etc/GMT+8"),
                        "-7:00":("Mountain Time (US and Canada), Chihuahua, La Paz, Mazatlan, Arizona", "Etc/GMT+7"),
                        "-6:00":("Central Time (US and Canada), Saskatchewan, Guadalajara, Mexico City, Monterrey", "Etc/GMT+6"),
                        "-5:00":("Eastern Time (US and Canada), Indiana (East), Bogota, Lima, Quito", "Etc/GMT+5"),
                        "-4:00":("Atlantic Time (Canada),  Georgetown, La Paz, San Juan, Santiago", "Etc/GMT+4"),
                        "-3:00":("Brasilia, Georgetown", "Etc/GMT+3"),
                        "-2:00":("Mid-Atlantic", "Etc/GMT+2"),
                        "-1:00":("Azores, Cape Verde Islands", "Etc/GMT+1"),
                        "0:00":("Dublin, Edinburgh, Lisbon, London, Monrovia, Reykjavik", "GMT"),
                        "+1:00":("Belgrade, Bratislava, Budapest, Ljubljana, Prague, Sarajevo, Skopje, Warsaw, Zagreb, Brussels, Copenhagen, Madrid, Paris, Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna", "Etc/GMT-1"),
                        "+2:00":("Minsk, Cairo, Helsinki, Kiev, Riga, Sofia, Tallinn, Vilnius", "Etc/GMT-2"),
                        "+3:00":("Moscow, St. Petersburg, Volgograd", "Etc/GMT-3"),
                        "+4:00":("Abu Dhabi, Muscat, Baku, Tbilisi, Yerevan", "Etc/GMT-4"),
                        "+5:00":("Ekaterinburg, Tashkent", "Etc/GMT-5"),
                        "+6:00":("Astana, Dhaka, Sri Jayawardenepura, Almaty, Novosibirsk", "Etc/GMT-6"),
                        "+6:30":("Yangon (Rangoon)", "Asia/Yangon"),
                        "+7:00":("Bangkok, Hanoi, Jakarta, Krasnoyarsk", "Etc/GMT-7"),
                        "+8:00":("Beijing, Chongqing, Hong Kong, Kuala Lumpur, Singapore, Taipei", "Etc/GMT-8"),
                        "+9:00":("Seoul, Osaka, Sapporo, Tokyo, Yakutsk", "Etc/GMT-9"),
                        "+10:00":("Canberra, Melbourne, Sydney, Brisbane, Hobart, Guam", "Etc/GMT-10"),
                        "+11:00":("Magadan, Solomon Islands, New Caledonia", "Etc/GMT-11"),
                        "+12:00":("Fiji, Kamchatka, Marshall Is.", "Etc/GMT-12"),
                        "+13:00":("Nuku'alofa", "Etc/GMT-13"),
                        "+14:00":("Kiritimati", "Etc/GMT-14")
                        }
        
        combo_list = []
        self.combo_list_key = {}
        for self.key in self.time_zone_dict.keys():
            dict_value =self.time_zone_dict[self.key][0]
            dict_value_set = "GMT: {}   Place:{}".format(self.key, dict_value)
            combo_list.append(dict_value_set)
            self.combo_list_key[dict_value_set] = self.key


        frame_TimezoneScreen = tk.Frame(self, bg="green")
        frame_TimezoneScreen.pack(pady=10)

        frame_TimezoneScreen_2 = tk.Frame(self)
        frame_TimezoneScreen_2.pack(pady=60)
        
        tk.Label(frame_TimezoneScreen, text="Let's Start Intial Setup",font=("MSゴシック", "30", "bold"),bg="blue").pack()
        tk.Label(frame_TimezoneScreen, text="Complete the Initial setup \nand experience the world of security \nwith facial recogniton!",bg="red", justify="left",font=("","15","")).pack(pady=10)

        tk.Label(frame_TimezoneScreen_2, text="Select Timezone.", bg="blue").pack()

        self.combo_TimezoneScreen_variable = ""
        self.combo_TimezoneScreen = ctk.CTkComboBox(frame_TimezoneScreen_2, values=combo_list, state="readonly", command=self.SetTimezone)
        self.combo_TimezoneScreen.pack()
        self.combo_TimezoneScreen.set("select timezone")

        image_TimezoneScreen =  ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        self.btn_frame_TimezoneScreen = ctk.CTkButton(frame_TimezoneScreen_2, text="Continue                ", image=image_TimezoneScreen, compound="right", command=self.CheckTimezone)
        self.btn_frame_TimezoneScreen.pack(pady=5)

    def SetTimezone(self,event):
        variable = self.combo_TimezoneScreen.get()
        print(variable)
        key = self.combo_list_key[variable]
        self.combo_TimezoneScreen_variable = self.time_zone_dict[key][1]
        print(self.combo_TimezoneScreen_variable)


    def CheckTimezone(self):
        if self.combo_TimezoneScreen_variable == "":
            messagebox.showerror("Select Timezone", "Slect Timezone")
        else:
            self.LanguegeScreen()

    ##TimezoneScreen##

    ##LanguegeScreen##
    def LanguegeScreen(self):
        self.alldestroy()

        frame_LanguegeScreen = tk.Frame(self, bg="green")
        frame_LanguegeScreen.pack(pady=10)

        frame_LanguegeScreen_2 = tk.Frame(self)
        frame_LanguegeScreen_2.pack(pady=60)
        
        tk.Label(frame_LanguegeScreen, text="Let's Start Intial Setup",font=("MSゴシック", "30", "bold"),bg="blue").pack()
        tk.Label(frame_LanguegeScreen, text="Complete the Initial setup \nand experience the world of security \nwith facial recogniton!",bg="red", justify="left",font=("","15","")).pack(pady=10)

        tk.Label(frame_LanguegeScreen_2, text="Select display language").pack()

        combo_list = ['ENGLISH', '日本語']
        self.combo_LanguegeScreen_variable = ""
        self.combo_LanguegeScreen = ctk.CTkComboBox(frame_LanguegeScreen_2, values=combo_list, state="readonly", command=self.Setlanguage)
        self.combo_LanguegeScreen.pack()
        self.combo_LanguegeScreen.set("select language")

        image_LanguegeScreen =  ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        self.btn_frame_LanguegeScreen = ctk.CTkButton(frame_LanguegeScreen_2, text="Continue                ", image=image_LanguegeScreen, compound="right", command=self.Checklanguage)
        self.btn_frame_LanguegeScreen.bind("<Button-1>", self.Checklanguage)
        self.btn_frame_LanguegeScreen.pack(pady=5)

    def Setlanguage(self,event):
        self.combo_LanguegeScreen_variable = self.combo_LanguegeScreen.get()

    def Checklanguage(self):
        if self.combo_LanguegeScreen_variable == "":
            messagebox.showerror("Select Language", "Slect Language")
        else:
            self.WifiScreen()

    ##LanguegeScreen##
                
    ##WifiScreen##
    def WifiScreen(self):
        
        self.alldestroy()

        print(self.combo_LanguegeScreen_variable)

        frame_WifiScreen = tk.Frame(self, bg="white")
        frame_WifiScreen.pack(pady=10)

        frame_WifiScreen_2 = tk.Frame(self, bg="white")
        frame_WifiScreen_2.pack(pady=20)

        frame_WifiScreen_3 = tk.Frame(self, bg="white")
        frame_WifiScreen_3.pack(pady=20)
        
        tk.Label(frame_WifiScreen, text="Let's Configure the Wi-Fi", font=("MSゴシック", "30", "bold"), bg="white").pack()
        tk.Label(frame_WifiScreen, text="Please select the Wi-Fi network \nto connect to.", justify="left", bg="white",font=("","15","")).pack(pady=10)

        #Wifiの設定をここに追加
        #pythonで行うか他の言語で行うか要相談
        #treeを使わずに、customtkinterのラベルやボタンを並べて作成？        
        ###wifi_list = Wifi取得するモジュール.クラス.メソッド リスト形式
        wifi_list = ['123456789', 'abcdefg', 'hijklmn', 'aiueo','kkkkk','aaaaa','bvbbbbb','12345','123456789', 'abcdefg', 'hijklmn', 'aiueo','kkkkk','aaaaa','bvbbbbb','12345']

        column = ('wifiname','icon')
        
        # Treeviewの生成
        global tree_wifi
        tree_wifi = ttk.Treeview(frame_WifiScreen_2, columns=column)
        scrollbar = ctk.CTkScrollbar(frame_WifiScreen_2, command=tree_wifi.yview)
        tree_wifi.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree_wifi.bind("<<TreeviewSelect>>", self.WifiDialog)
        # 列の設定
        tree_wifi.column('#0',width=0, stretch='no')
        tree_wifi.column('wifiname', anchor='w', width=100)
        tree_wifi.column('icon',anchor='e', width=50)
        # 列の見出し設定
        tree_wifi.heading('#0',text='')
        tree_wifi.heading('wifiname',anchor='center')
        tree_wifi.heading('icon')
        # レコードの追加
        #iconに入るのは、フリーwifiかパスワード付きかで変わる
        for wifi in wifi_list:
            tree_wifi.insert(parent='', index='end', values=(wifi, "icon"))
        
        tree_wifi.pack(pady=10)

        ctk.CTkButton(frame_WifiScreen_3, text="Continue                ", command=self.UserScreen1).pack(pady=10)

    def WifiDialog(self,event):
        record_id = tree_wifi.focus()
        record_values = tree_wifi.item(record_id, 'values')
        wifipassword = simpledialog.askstring("Connection wifi", "Please enter the password \n    \"{}\" ".format(record_values[0]))
        if wifipassword != None:
            print("password check")
            #この wifipassword を使って、別モジュール内でwifiに接続処理を行う
            ###パスワードチェックを行う別モジュール.クラス.メソッド(wifipassword)
        
    ##WifiScreen##
    
    ##UserScreen1##
    def UserScreen1(self):
        self.alldestroy()

        self.keybord = True

        frame_UserScreen1 = tk.Frame(self, bg="white")
        frame_UserScreen1.pack(pady=10)

        frame_UserScreen1_2 = tk.Frame(self, bg="green")
        frame_UserScreen1_2.pack(pady=0)

        frame_UserScreen1_3 = tk.Frame(self, bg="blue")
        frame_UserScreen1_3.pack(pady=10)

        tk.Label(frame_UserScreen1, text="Let's Create the User",font=("MSゴシック", "30", "bold"), bg="white").pack()        
        image_UserScreen1_1 = ctk.CTkImage(light_image=Image.open("assets2/UserScreen1.png"), size=(510,70))
        ctk.CTkLabel(frame_UserScreen1, text="", image=image_UserScreen1_1).pack(pady=15)   
        tk.Label(frame_UserScreen1, text="Enter your name and company name.", bg="white", font=("","15","")).pack(pady=10)

        tk.Label(frame_UserScreen1_2, text="Full Name  ", bg="white").grid(row=1, column=1)
        tk.Label(frame_UserScreen1_2, text="Company Name  ", bg="white").grid(row=2, column=1)
        self.username = ctk.CTkEntry(frame_UserScreen1_2, width=250)
        self.companyname = ctk.CTkEntry(frame_UserScreen1_2, width=250)
        self.username.bind("<Button-1>",self.Keybord)
        self.companyname.bind("<Button-1>",self.Keybord)
        self.username.grid(row=1, column=25)
        self.companyname.grid(row=2, column=25)

        #print("self.username: ",self.username, "self.companyname: ",self.companyname)

        image_UserScreen1_3 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_UserScreen1_3, text="Continue                ", command=self.InsertCheck,  image=image_UserScreen1_3, compound="right").pack(pady=40)
    
    def InsertCheck(self):
        username = self.username.get()
        companyname = self.companyname.get()
        if username != "" and companyname != "":
            self.username_save = username
            self.companyname_save = companyname
            self.UserScreen2()
        else:
            messagebox.showerror("Name Error", "Please name Insert")

    ##UserScreen1##

    ##UserScreen2##
    def UserScreen2(self):
        
        self.alldestroy()

        frame_UserScreen2 = tk.Frame(self, bg="white")
        frame_UserScreen2.pack(pady=10)

        frame_UserScreen2_2 = tk.Frame(self, bg="white")
        frame_UserScreen2_2.pack(pady=10)

        tk.Label(frame_UserScreen2, text="Let's Create the User",font=("MSゴシック", "30", "bold"), bg="white").pack()
        image_UserScreen2_1 = ctk.CTkImage(light_image=Image.open("assets2/UserScreen2.png"), size=(510,70))
        ctk.CTkLabel(frame_UserScreen2, text="", image=image_UserScreen2_1).pack(pady=15)
        tk.Label(frame_UserScreen2, text="Set up the password for authentication.", bg="white", font=("","15","")).pack(pady=10)

        passwordlimit = self.register(self.limit_char4)
        self.password = tk.Entry(frame_UserScreen2, show="*" ,width=30, validate="key", validatecommand=(passwordlimit, "%P"))
        self.password.pack(pady=5)

        image_UserScreen2_2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))

        ctk.CTkButton(frame_UserScreen2_2, text="1",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("1")).grid(row=0,column=0)
        ctk.CTkButton(frame_UserScreen2_2, text="2",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("2")).grid(row=0,column=1)
        ctk.CTkButton(frame_UserScreen2_2, text="3",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("3")).grid(row=0,column=2)
        ctk.CTkButton(frame_UserScreen2_2, text="4",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("4")).grid(row=1,column=0)
        ctk.CTkButton(frame_UserScreen2_2, text="5",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("5")).grid(row=1,column=1)
        ctk.CTkButton(frame_UserScreen2_2, text="6",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("6")).grid(row=1,column=2)
        ctk.CTkButton(frame_UserScreen2_2, text="7",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("7")).grid(row=2,column=0)
        ctk.CTkButton(frame_UserScreen2_2, text="8",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("8")).grid(row=2,column=1)
        ctk.CTkButton(frame_UserScreen2_2, text="9",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("9")).grid(row=2,column=2)
        ctk.CTkButton(frame_UserScreen2_2, text="", height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("clear"),compound="right", image=image_UserScreen2_2).grid(row=3,column=0)
        ctk.CTkButton(frame_UserScreen2_2, text="0",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget("0")).grid(row=3,column=1)
        ctk.CTkButton(frame_UserScreen2_2, text="Enter",height=70,width=70, fg_color="gray", command=self.Passwordcheck).grid(row=3,column=2)

    def Passwordget(self,value):
        if value == "clear":
            self.password.delete(0,tk.END)
        else:
            self.password.insert(tk.END,value)

    def Passwordcheck(self):
        if len(self.password.get()) == 4:
            self.password_save = self.password.get()
            self.UserScreen2_confirm()
        else:
            messagebox.showerror("Password Error", "Please 4Password Insert")
            
    ##UserScreen2##
    
    ##UserScreen2_confirm##
    def UserScreen2_confirm(self):
        print(self.password.get())

        print(self.password_save)

        self.alldestroy()

        print(self.password_save)

        frame_UserScreen2_confirm = tk.Frame(self, bg="white")
        frame_UserScreen2_confirm.pack(pady=10)

        frame_UserScreen2_confirm_2 = tk.Frame(self, bg="white")
        frame_UserScreen2_confirm_2.pack(pady=10)

        tk.Label(frame_UserScreen2_confirm, text="Let's Create the User",font=("MSゴシック", "30", "bold"), bg="white").pack()
        image_UserScreen2_confirm_1 = ctk.CTkImage(light_image=Image.open("assets2/UserScreen2.png"), size=(510,70))
        ctk.CTkLabel(frame_UserScreen2_confirm, text="", image=image_UserScreen2_confirm_1).pack(pady=15)
        tk.Label(frame_UserScreen2_confirm, text="For cofirmation, pleae enter it again.", bg="white", font=("","15","")).pack(pady=10)

        passwordlimit_confirm = self.register(self.limit_char4)
        self.password_confirm = tk.Entry(frame_UserScreen2_confirm, show="*" ,width=30, validate="key", validatecommand=(passwordlimit_confirm, "%P"))
        self.password_confirm.pack(pady=5)

        image_UserScreen2_2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
           
        ctk.CTkButton(frame_UserScreen2_confirm_2, text="1",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("1")).grid(row=0,column=0)
        ctk.CTkButton(frame_UserScreen2_confirm_2, text="2",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("2")).grid(row=0,column=1)
        ctk.CTkButton(frame_UserScreen2_confirm_2, text="3",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("3")).grid(row=0,column=2)
        ctk.CTkButton(frame_UserScreen2_confirm_2, text="4",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("4")).grid(row=1,column=0)
        ctk.CTkButton(frame_UserScreen2_confirm_2, text="5",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("5")).grid(row=1,column=1)
        ctk.CTkButton(frame_UserScreen2_confirm_2, text="6",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("6")).grid(row=1,column=2)
        ctk.CTkButton(frame_UserScreen2_confirm_2, text="7",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("7")).grid(row=2,column=0)
        ctk.CTkButton(frame_UserScreen2_confirm_2, text="8",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("8")).grid(row=2,column=1)
        ctk.CTkButton(frame_UserScreen2_confirm_2, text="9",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("9")).grid(row=2,column=2)
        ctk.CTkButton(frame_UserScreen2_confirm_2, text="", height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("clear"),compound="right", image=image_UserScreen2_2).grid(row=3,column=0)
        ctk.CTkButton(frame_UserScreen2_confirm_2, text="0",height=70,width=70, fg_color="gray", command=lambda:self.Passwordget_confirm("0")).grid(row=3,column=1)
        ctk.CTkButton(frame_UserScreen2_confirm_2, text="Enter",height=70,width=70, fg_color="gray", command=self.Passwordcheck_confirm).grid(row=3,column=2)

    def Passwordget_confirm(self,value):
        if value == "clear":
            self.password_confirm.delete(0,tk.END)
        else:
            self.password_confirm.insert(tk.END,value)

    def Passwordcheck_confirm(self):
        if len(self.password_confirm.get()) == 4:
            passeord_confirm = self.password_confirm.get()
            if self.password_save == passeord_confirm:
                self.UserScreen3()
            else:
                messagebox.showerror("Password Error", "Password not match")
        else:
            messagebox.showerror("Password Error", "Please 4Password Insert")

    ##UserScreen2_confirm##
            
    ##UserScreen3##
    def UserScreen3(self):
        
        self.alldestroy()

        print(self.password_save)

        frame_UserScreen3 = tk.Frame(self, bg="white")
        frame_UserScreen3.pack(pady=10)
        frame_UserScreen3_2 = tk.Frame(self, bg="white")
        frame_UserScreen3_2.pack(pady=10)

        tk.Label(frame_UserScreen3, text="Let's Create the User",font=("MSゴシック", "30", "bold"), bg="white").pack()
        image_UserScreen3_3 = ctk.CTkImage(light_image=Image.open("assets2/UserScreen3.png"), size=(510,70))
        ctk.CTkLabel(frame_UserScreen3, text="", image=image_UserScreen3_3).pack(pady=15)
        tk.Label(frame_UserScreen3, text="Register facial information for authentication.", bg="white", font=("","15","")).pack(pady=10)

        image_UserScreen3_1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        #ctk.CTkButton(frame_UserScreen3_2, text="Using the camera      >", command=self.UsingCamera,  image=image_UserScreen3_1, compound="top").pack()
        ctk.CTkButton(frame_UserScreen3_2, text="Using the camera      >", command=self.UserScreen4,  image=image_UserScreen3_1, compound="top").pack()
        image_UserScreen3_2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_UserScreen3_2, text="Using the picture      >", command=self.UsingPicture,  image=image_UserScreen3_2, compound="top").pack(pady=5)

    def UsingCamera(self):
        ###カメラで写真を撮影するメソッド
        pass

    def UsingPicture(self):

        selectpicture = tk.filedialog.askopenfilename(title="ファイル選択", initialdir="C:/", filetypes=[("Image File","*.png")])
        ###initialdirをUSBのパスのみにしたい

        self.image_selectpicture = tk.PhotoImage(file=selectpicture)
    
    ##UserScreen3##

    ##UserScreen4##
    def UserScreen4(self):
        self.alldestroy()

        self.keybord = True

        frame_UserScreen4 = tk.Frame(self, bg="white")
        frame_UserScreen4.pack(pady=10)

        frame_UserScreen4_2 = tk.Frame(self, bg="white")
        frame_UserScreen4_2.pack(pady=10)

        tk.Label(frame_UserScreen4, text="Let's Create the User",font=("MSゴシック", "30", "bold"), bg="white").pack()
        image_UserScreen4_1 = ctk.CTkImage(light_image=Image.open("assets2/UserScreen4.png"), size=(510,70))
        ctk.CTkLabel(frame_UserScreen4, text="", image=image_UserScreen4_1).pack(pady=15)
        tk.Label(frame_UserScreen4, text="Set up the administrator password.", bg="white", font=("","15","")).pack(pady=10)

        adminpasswordlimit = self.register(self.limit_char8)
        adminpasswordlimit_confirm = self.register(self.limit_char8)

        tk.Label(frame_UserScreen4_2, text="Password  ", bg="white").grid(row=1, column=4)
        tk.Label(frame_UserScreen4_2, text="Confirm Password  ", bg="white").grid(row=2, column=4)
        self.adminpassword = ctk.CTkEntry(frame_UserScreen4_2, width=150,validate="key", validatecommand=(adminpasswordlimit, "%P"))
        self.adminpassword_confirm = ctk.CTkEntry(frame_UserScreen4_2, width=150,validate="key", validatecommand=(adminpasswordlimit_confirm, "%P"))
        
        self.adminpassword.bind("<Button-1>",self.Keybord)
        self.adminpassword_confirm.bind("<Button-1>",self.Keybord)

        self.adminpassword.grid(row=1, column=5)
        self.adminpassword_confirm.grid(row=2, column=5)

        image_UserScreen4_2 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_UserScreen4_2, text="Continue                ", command=self.AdminPasswordcheck,  image=image_UserScreen4_2, compound="right").grid(row=6)

    def AdminPasswordcheck(self):
        adminpassword = self.adminpassword.get()
        adminpassword_confirm = self.adminpassword_confirm.get()
        space =" "
        if space not in adminpassword:
            if len(adminpassword) == 8:
                if adminpassword == adminpassword_confirm:
                    self.adminpassword_save = adminpassword
                    self.UserScreen5()
                else:
                    messagebox.showerror("Password Error", "Password not match")        
            else:
                messagebox.showerror("Password Error", "Password 8password insert")
        else:
            messagebox.showerror("Password Error", "Do not include spaces")
        
    ##UserScreen4##
    
    ##UserScreen5##
    def UserScreen5(self):
        ##ここで選択した言語の値をDBに反映させる必要がある
        
        timezone = self.combo_TimezoneScreen_variable
        language = self.combo_LanguegeScreen_variable
        userid = "0001"
        username = self.username_save
        companyname = self.companyname_save
        password = self.password_save
        adminpassword = self.adminpassword_save
        editorid = "0001"
        createdate = time.strftime('%Y%m%d%H%M')
        admin = "true"
        
        ###image_selectpicture と image_takepicure のどちらかのみを変数に入れる
        if self.image_selectpicture != "": #and image_takepicure == "":
            picture = self.image_selectpicture
        #elif image_selectpicture == "": and image_takepicure != "":
        #    picture =image_takepicture

        print(timezone, language, username, companyname, password, adminpassword)
        print("time: ", createdate)

        self.alldestroy()

        frame_UserScreen5 = tk.Frame(self, bg="white")
        frame_UserScreen5.pack(pady=10)

        frame_UserScreen5_2 = tk.Frame(self, bg="white")
        frame_UserScreen5_2.pack(pady=10)

        tk.Label(frame_UserScreen5, text="Let's Create the User",font=("MSゴシック", "30", "bold"), bg="white").pack()
        image_UserScreen5_1 = ctk.CTkImage(light_image=Image.open("assets2/UserScreen5.png"), size=(510,70))
        ctk.CTkLabel(frame_UserScreen5, text="", image=image_UserScreen5_1).pack(pady=15)
        tk.Label(frame_UserScreen5, text="Complete user registration with the following information.\nif you are ready, please press OK.", bg="white", font=("","15","")).pack(pady=10)

        myfont = font.Font(underline=True)
        tk.Label(frame_UserScreen5_2, text="User ID : {}".format(userid), font=myfont, bg="white").grid(row=0, column=0)
        tk.Label(frame_UserScreen5_2, text="Full Name : {}".format(username), font=myfont, bg="white").grid(row=1, column=0)
        tk.Label(frame_UserScreen5_2, text="Company Name : {}".format(companyname), font=myfont, bg="white").grid(row=2, column=0)
        tk.Label(frame_UserScreen5_2, text="Password : {}".format(password), font=myfont, bg="white").grid(row=3, column=0)
        tk.Label(frame_UserScreen5_2, text="Password(Admin) : {}".format(adminpassword), font=myfont, bg="white").grid(row=4, column=0)

        ctk.CTkButton(frame_UserScreen5_2, text="OK", command=lambda:self.Datasave(timezone,language, userid, username, companyname, password, picture, admin, adminpassword, editorid, createdate)).grid(row=6)

        WIDTH  = 640        # 幅
        HEIGHT = 400        # 高さ

        # キャンバス作成・配置
        canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT)
        canvas.pack()
        
        # キャンバスに表示
        canvas.create_image(WIDTH/2, HEIGHT/2, image=picture)
        
    def Datasave(self,timezone,language, userid, username, companyname, password, picture, admin, adminpassword, editorid, createdate):
        try:
            dbaccess.setTimezone(timezone)
            dbaccess.setLanguage(language)
            dbaccess.insertUserMst(userid, username, companyname, password, picture, admin)
            dbaccess.insertAdministrator(editorid, adminpassword, createdate)
            print("DB反映")
            print(timezone,language, userid, username, companyname, password, picture, adminpassword, editorid, createdate)
            self.SetcompleteScreen()
        except Exception as e:
            print(e)
            print("languege not DB")
        

    ##UserScreen5##
    
    ##SetcompleteScreen##
    def SetcompleteScreen(self):
        self.alldestroy()

        frame_SetcompleteScreen = tk.Frame(self, bg="white")
        frame_SetcompleteScreen.pack(pady=10)

        tk.Label(frame_SetcompleteScreen, text="Congratulations on \ncompleting the setup!",font=("MSゴシック", "30", "bold"), bg="white").pack(pady=15)
        tk.Label(frame_SetcompleteScreen, text="Welcome to a new era of facial recognition security.\n With just a glance, unlock your device and\n embrace a secure future.\n Your face is the key. Let the experience begin!", bg="white", font=("","15","")).pack(pady=10)
        ctk.CTkButton(frame_SetcompleteScreen, text="Let's begin").pack()

    ##SetcompleteScreen##
                    
if __name__ == "__main__":
    app = StartSetting()
    app.title("Start setting")
    #app.resizable(0,0)
    #app.overrideredirect(True)
    app.geometry("540x720")   #横x縦

    #app.configure(bg="white")        #tk(tkinter).Tk
    app.configure(fg_color="white")   #ctk.CTk
    
    app.TimezoneScreen()

    app.mainloop()