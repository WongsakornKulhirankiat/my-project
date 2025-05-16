import tkinter
from tkinter import *
from tkinter import simpledialog
import customtkinter as ctk


class CustomDialog(simpledialog.Dialog):
    def __init__(self, master, title=None) -> None:
        super(CustomDialog, self).__init__(parent=master, title=title)            

    def body(self, master) -> None:
        """
        Dialogオブジェクトへ配置するオブジェクトを定義する。

        Parameters
        ----------
        master:
            Dialogオブジェクトの親オブジェクト

        Returns
        -------
        None
        """

        #1-0
        buton1: Button = ctk.CTkButton(master,text="1", fg_color="gray")
        buton2: Button = ctk.CTkButton(master,text="2", fg_color="gray")
        buton3: Button = ctk.CTkButton(master,text="3", fg_color="gray")
        buton4: Button = ctk.CTkButton(master,text="4", fg_color="gray")
        buton5: Button = ctk.CTkButton(master,text="5", fg_color="gray")
        buton6: Button = ctk.CTkButton(master,text="6", fg_color="gray")
        buton7: Button = ctk.CTkButton(master,text="7", fg_color="gray")
        buton8: Button = ctk.CTkButton(master,text="8", fg_color="gray")
        buton9: Button = ctk.CTkButton(master,text="9", fg_color="gray")
        buton0: Button = ctk.CTkButton(master,text="0", fg_color="gray")



        #q~p
        butonq: Button = ctk.CTkButton(master,text="q", fg_color="gray")
        butonw: Button = ctk.CTkButton(master,text="w", fg_color="gray")
        butone: Button = ctk.CTkButton(master,text="e", fg_color="gray")
        butonr: Button = ctk.CTkButton(master,text="r", fg_color="gray")
        butont: Button = ctk.CTkButton(master,text="t", fg_color="gray")
        butony: Button = ctk.CTkButton(master,text="y", fg_color="gray")
        butonu: Button = ctk.CTkButton(master,text="u", fg_color="gray")
        butoni: Button = ctk.CTkButton(master,text="i", fg_color="gray")
        butonp: Button = ctk.CTkButton(master,text="p", fg_color="gray")
        #a~-
 

        #z~大文字化


        buton1.grid(row=0, column=0, padx=1, pady=1)
        buton2.grid(row=0, column=1, padx=1, pady=1)
        buton3.grid(row=0, column=2, padx=1, pady=1)
        buton4.grid(row=1, column=0, padx=1, pady=1)
        buton5.grid(row=1, column=1, padx=1, pady=1)
        buton6.grid(row=1, column=2, padx=1, pady=1)
        buton7.grid(row=2, column=0, padx=1, pady=1)
        buton8.grid(row=2, column=1, padx=1, pady=1)
        buton9.grid(row=2, column=2, padx=1, pady=1)
        buton0.grid(row=3, column=0, padx=1, pady=1)



    def apply(self):
        pass


if __name__ == "__main__":
    root = tkinter.Tk()

    def display_dialog():
        CustomDialog(root)

    button = Button(root)
    button["text"] = "ダイアログ表示"
    button["command"] = display_dialog
    button.grid(column=0, row=0, padx=10, pady=10)

    root.mainloop()