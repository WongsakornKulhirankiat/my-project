import tkinter as tk

class MyKeyboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Keyboard")

        # Define keyboard layout
        self.keys = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']
        ]

        # Create keyboard buttons
        for i, row in enumerate(self.keys):
            for j, key in enumerate(row):
                # Create button for each key
                btn = tk.Button(self.root, text=key, width=5, height=2,
                                command=lambda char=key: self.on_key_press(char))
                btn.grid(row=i, column=j, padx=5, pady=5)

    def on_key_press(self, char):
        print(char)  # Replace this with your desired action, e.g., sending key to application

def main():
    root = tk.Tk()
    app = MyKeyboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()
