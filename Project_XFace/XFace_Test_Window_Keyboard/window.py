import tkinter as tk

class MyWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("My Window")

        # Set window size to 1280x720
        self.root.geometry("1280x720")

        # Disable window resizing and minimizing
        self.root.resizable(False, False)
        self.root.attributes('-toolwindow', True)

        # Bind the closing event to a function
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Add a large centered text
        self.label = tk.Label(self.root, text="Test Window button settings", font=("Helvetica", 36))
        self.label.place(relx=0.5, rely=0.5, anchor="center")

    def on_close(self):
        # Your code to handle window closing goes here
        pass

def main():
    root = tk.Tk()
    app = MyWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
