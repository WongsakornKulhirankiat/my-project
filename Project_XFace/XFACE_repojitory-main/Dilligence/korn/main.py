import tkinter as tk
from tkinter import ttk
import customtkinter
from XFace_Device_Settings_Screen1 import Screen1
from XFace_Device_Settings_Screen2 import Screen2

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("XFace Device Settings")
        self.root.geometry("520x500")

        # Create Canvas Widget
        self.canvas = customtkinter.CTkCanvas(self.root, width=500, height=500)
        self.canvas.grid(row=0, column=0, sticky=tk.NSEW)

        # Add Scrollbar
        self.scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # Configure the Canvas to use the Scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a Frame inside the Canvas to hold the screens
        self.container = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.container, anchor=tk.NW)

        # Create an instance of Screens
        self.screen1 = Screen1(self.container)
        self.screen2 = Screen2(self.container)

        # Pack Screens
        self.screen1.pack()
        self.screen2.pack()

        # Update the scroll region
        self.container.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    app = MainApp()
    app.root.mainloop()
