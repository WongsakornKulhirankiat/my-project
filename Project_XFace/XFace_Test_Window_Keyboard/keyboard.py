import tkinter as tk

class MyWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("My Window")

        # Set window size to 1280x720
        self.root.geometry("1280x720")

        # Disable window resizing and minimizing
        self.root.resizable(False, False)

        # Bind the closing event to a function
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Add a large centered text
        self.label = tk.Label(self.root, text="Test Screen Keyboard", font=("Helvetica", 36))
        self.label.pack(pady=50)  # Add some vertical padding

        # Add a large centered Entry
        self.entry = tk.Entry(self.root, font=("Helvetica", 24), width=20)
        self.entry.pack(pady=20)  # Add some vertical padding
        self.entry.bind("<Button-1>", self.show_keyboard)  # Bind left mouse click to show keyboard

        # Create the virtual keyboard
        self.create_virtual_keyboard()

    def on_close(self):
        # Your code to handle window closing goes here
        pass

    def create_virtual_keyboard(self):
        # Create a frame to hold the keyboard buttons
        self.keyboard_frame = tk.Frame(self.root, bg="grey")  # Set background color to grey

        # Define keyboard layout
        keys = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'],
            ['Delete', 'End']  # Add "Delete" button and "End" button to close the keyboard
        ]

        # Create keyboard buttons
        for i, row in enumerate(keys):
            for j, key in enumerate(row):
                # Create button for each key
                btn = tk.Button(self.keyboard_frame, text=key, width=5, height=2, font=("Helvetica", 12, "bold"),
                                command=lambda char=key: self.on_key_press(char))  # Set font to bold
                btn.grid(row=i, column=j, padx=5, pady=5)

        # Pack the keyboard frame initially hidden
        self.keyboard_frame.pack_forget()


    def show_keyboard(self, event):
        self.keyboard_frame.place(relx=0.225, rely=0.5) 

    def on_key_press(self, char):
        if char == "End":
            self.keyboard_frame.place_forget()
        elif char == "Delete":
            # Delete the last character from the entry field
            current_text = self.entry.get()
            if current_text:
                self.entry.delete(len(current_text) - 1)
        else:
            self.entry.insert(tk.END, char)


def main():
    root = tk.Tk()
    app = MyWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
