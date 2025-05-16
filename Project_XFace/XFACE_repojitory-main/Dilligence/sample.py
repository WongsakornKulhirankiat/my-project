import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import font
from tkinter import filedialog
import customtkinter as ctk
from PIL import Image
import glob

class Useradminop(ctk.CTk):  ##ctk.CTk
##SelectpictureScreen##
    def SelectpictureScreen(self):

        frame_SelectpictureScreen_top = tk.Frame(self, bg="green", height=80 ,width=700)
        frame_SelectpictureScreen_top.pack_propagate(False)
        frame_SelectpictureScreen_top.pack()

        frame_SelectpictureScreen_main = tk.Frame(self, bg="red", height=520 ,width=700)
        frame_SelectpictureScreen_main.pack_propagate(False)
        frame_SelectpictureScreen_main.pack(expand=True, fill=tk.BOTH)

        image_SelectpictureScreen_top1 = ctk.CTkImage(light_image=Image.open("assets2/share.png"), size=(15,15))
        ctk.CTkButton(frame_SelectpictureScreen_top, text="<", height=40 ,width=40, image=image_SelectpictureScreen_top1).pack(side="left")
        
        image_SelectpictureScreen = tk.PhotoImage(file="assets2/share.png")
        WIDTH  = 50        # 幅
        HEIGHT = 50        # 高さ
        canvas_SelectpictureScreen_main_1 = tk.Canvas(frame_SelectpictureScreen_main, width=WIDTH, height=HEIGHT)
        canvas_SelectpictureScreen_main_1.create_image(WIDTH/2, HEIGHT/2, image=image_SelectpictureScreen)
        canvas_SelectpictureScreen_main_1.pack()
        
        frame_SelectpictureScreen_main_2 = ctk.CTkScrollableFrame(frame_SelectpictureScreen_main)
        frame_SelectpictureScreen_main_2.pack_propagate(False)
        frame_SelectpictureScreen_main_2.pack(expand=True, fill=tk.BOTH)

        imagelist = []
        imagelist = glob.glob("assets2/*.png")

        for i in range(0,len(imagelist)):
            image = Image.open(imagelist[i])
            image_SelectpictureScreen_main_2 = ctk.CTkImage(light_image=image, size=(120,120))
            

            ctk.CTkButton(frame_SelectpictureScreen_main_2, text="", height=150 ,width=150, image=image_SelectpictureScreen_main_2).grid(pady=10, row=i//2, column=i%2) 
        
    ##SelectpictureScreen##
            
if __name__ == "__main__":
    app = Useradminop()
    app.title("Start setting")
    #app.resizable(0,0)
    #app.overrideredirect(True)
    app.geometry("540x720")   #横x縦

    #app.configure(bg="white")        #tk(tkinter).Tk
    app.configure(fg_color="white")   #ctk.CTk
    
    app.SelectpictureScreen()

    app.mainloop()
