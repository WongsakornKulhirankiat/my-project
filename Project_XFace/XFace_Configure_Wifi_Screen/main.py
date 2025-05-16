import tkinter as tk
from tkinter import ttk
import customtkinter
import datetime

from XFace_Configure_Wifi import Screen1

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("XFace Configure Wifi")
        self.root.geometry("600x500")

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

    def show_next_screen(self, index):
        # Hide the current screen
        if self.current_screen == 1:
            self.screen1.grid_remove()

        # Show the next screen
        if index == 1:
            self.screen1.grid(row=0, column=0, sticky="nsew")
            self.screen1.get_current_password()
            self.current_screen = index
            
if __name__ == "__main__":
    app = MainApp()
    app.root.mainloop()