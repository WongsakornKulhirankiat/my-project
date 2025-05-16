import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk
import math
import os
from tkinter import PhotoImage
from PIL import Image, ImageTk

class Screen9(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="#424242", width=600, height=500)
        self.pack_propagate(0)

        # Portraits List
        portraits_list = []
        # Toggle Confirm
        self.confirm = 0

        # Define Image Source
        current_directory = os.path.dirname(os.path.realpath(__file__))
        images_folder = os.path.join(current_directory, "images")

        # Load images and create PhotoImage objects
        for filename in os.listdir(images_folder):
            if "portrait" in filename:
                image_path = os.path.join(images_folder, filename)
                image = Image.open(image_path)
                portrait_image = ImageTk.PhotoImage(image)
                portraits_list.append(portrait_image)

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Name Frame
        name_frame = customtkinter.CTkFrame(master=self, width=290, height=500, fg_color="#e6e6e6", corner_radius=0)
        name_frame.place(x=0)

        # Add "<" Button
        back_btn = customtkinter.CTkButton(master=name_frame, command= lambda: self.next_screen(5), width=30, height=30, text="<", text_color="black", font=("Arial", 30), fg_color="transparent", hover=False)
        back_btn.place(relx=0.02, rely=0.02)

        # Add Name Label
        name_label = customtkinter.CTkLabel(master=name_frame, text="Name", text_color="black", font=("Arial", 20), fg_color="transparent")
        name_label.place(relx=0.2, rely=0.01)

        # Add Text Entry for Name
        self.name_entrybox = customtkinter.CTkEntry(master=name_frame, width=200 , height=30, fg_color="white", border_color="white", text_color="black", font=customtkinter.CTkFont(size=15), corner_radius=10)
        self.name_entrybox.place(relx=0.2, rely=0.06)
        self.name_entrybox.bind("<Button-1>", lambda event: self.show_keyboard(self.name_entrybox))

        # Add School Name Label
        school_label = customtkinter.CTkLabel(master=name_frame, text="School Name", text_color="black", font=("Arial", 20), fg_color="transparent")
        school_label.place(relx=0.2, rely=0.12)

        # Add ComboBox for School Name
        school_combobox = customtkinter.CTkComboBox(name_frame, text_color="black", state="readonly", values=["School1", "School2","School3"], font=("Arial", 15), width=200, height=30, justify="left", fg_color="white", dropdown_text_color="black", dropdown_font=("Arial", 15), dropdown_fg_color="white", dropdown_hover_color="white", button_color="white", border_color="white", button_hover_color="white")
        school_combobox.place(relx=0.2, rely=0.17)

        # Define Image Source
        current_directory = os.path.dirname(os.path.realpath(__file__))
        images_folder = os.path.join(current_directory, "images")

        search_path = os.path.join(images_folder, "search.png")

        # Add Image
        search_image = tk.PhotoImage(file=search_path)

        # Search Button
        search_btn = customtkinter.CTkButton(master=name_frame, image=search_image, text="Search", text_color="black", hover_color="lightgray", font=("Arial", 20), border_width=0, width=110, height=30, fg_color="white")
        search_btn.place(relx=0.51, rely=0.27)

        #----------------------------------------------------------------------------
        #                                     Frame 2
        #----------------------------------------------------------------------------

        # Add Info Frame
        info_frame = customtkinter.CTkScrollableFrame(master=self, width=298, height=500, fg_color="#d9d9d9", corner_radius=0)
        info_frame.place(x=290)

        # Add student frame 1
        student_frame_1 = customtkinter.CTkFrame(master=info_frame, width=250, height=70, fg_color="white", corner_radius=10, border_width=0, border_color="#5cb6f8")
        student_frame_1.bind('<Button-1>', lambda event: toggle_border(student_frame_1))
        student_frame_1.tag = 1
        student_frame_1.pack(padx=10, pady=5)
        # Create Canvas student frame 1
        canvas1 = customtkinter.CTkCanvas(
            student_frame_1,
            width = 7,
            height = 65,
            bg = "#fce467",
            highlightthickness = 0,
            bd = 0
        )
        canvas1.bind('<Button-1>', lambda event: toggle_border(student_frame_1))
        canvas1.place(x=15, y=2)
        # Student Name
        name1_label = customtkinter.CTkLabel(master=student_frame_1, text="Jame Bond", text_color="black", font=("Arial", 20), fg_color="transparent")
        name1_label.bind('<Button-1>', lambda event: toggle_border(student_frame_1))
        name1_label.place(x=50, y=10)
        # School Name
        school1_label = customtkinter.CTkLabel(master=student_frame_1, text="Bear Academy", text_color="black", font=("Arial", 13), fg_color="transparent")
        school1_label.bind('<Button-1>', lambda event: toggle_border(student_frame_1))
        school1_label.place(x=50, y=35)

        # Add student frame 2
        student_frame_2 = customtkinter.CTkFrame(master=info_frame, width=250, height=70, fg_color="white", corner_radius=10, border_width=0, border_color="#5cb6f8")
        student_frame_2.bind('<Button-1>', lambda event: toggle_border(student_frame_2))
        student_frame_2.tag = 2
        student_frame_2.pack(padx=10, pady=5)
        # Create Canvas student frame 1
        canvas2 = customtkinter.CTkCanvas(
            student_frame_2,
            width = 7,
            height = 65,
            bg = "#65dd71",
            highlightthickness = 0,
            bd = 0
        )
        canvas2.bind('<Button-1>', lambda event: toggle_border(student_frame_2))
        canvas2.place(x=15, y=2)
        # Student Name
        name2_label = customtkinter.CTkLabel(master=student_frame_2, text="Timmy Wong", text_color="black", font=("Arial", 20), fg_color="transparent")
        name2_label.bind('<Button-1>', lambda event: toggle_border(student_frame_2))
        name2_label.place(x=50, y=10)
        # School Name
        school2_label = customtkinter.CTkLabel(master=student_frame_2, text="Tiger School", text_color="black", font=("Arial", 13), fg_color="transparent")
        school2_label.bind('<Button-1>', lambda event: toggle_border(student_frame_2))
        school2_label.place(x=50, y=35)

        # Add student frame 3
        student_frame_3 = customtkinter.CTkFrame(master=info_frame, width=250, height=70, fg_color="white", corner_radius=10, border_width=0, border_color="#5cb6f8")
        student_frame_3.bind('<Button-1>', lambda event: toggle_border(student_frame_3))
        student_frame_3.tag = 3
        student_frame_3.pack(padx=10, pady=5)
        # Create Canvas student frame 1
        canvas3 = customtkinter.CTkCanvas(
            student_frame_3,
            width = 7,
            height = 65,
            bg = "#56b3f7",
            highlightthickness = 0,
            bd = 0
        )
        canvas3.bind('<Button-1>', lambda event: toggle_border(student_frame_3))
        canvas3.place(x=15, y=2)
        # Student Name
        name3_label = customtkinter.CTkLabel(master=student_frame_3, text="Will Smith", text_color="black", font=("Arial", 20), fg_color="transparent")
        name3_label.bind('<Button-1>', lambda event: toggle_border(student_frame_3))
        name3_label.place(x=50, y=10)
        # School Name
        school3_label = customtkinter.CTkLabel(master=student_frame_3, text="Bear Academy", text_color="black", font=("Arial", 13), fg_color="transparent")
        school3_label.bind('<Button-1>', lambda event: toggle_border(student_frame_3))
        school3_label.place(x=50, y=35)

        # Add student frame 4
        student_frame_4 = customtkinter.CTkFrame(master=info_frame, width=250, height=70, fg_color="white", corner_radius=10, border_width=0, border_color="#5cb6f8")
        student_frame_4.bind('<Button-1>', lambda event: toggle_border(student_frame_4))
        student_frame_4.tag = 4
        student_frame_4.pack(padx=10, pady=5)
        # Create Canvas student frame 1
        canvas4 = customtkinter.CTkCanvas(
            student_frame_4,
            width = 7,
            height = 65,
            bg = "#fce467",
            highlightthickness = 0,
            bd = 0
        )
        canvas4.bind('<Button-1>', lambda event: toggle_border(student_frame_4))
        canvas4.place(x=15, y=2)
        # Student Name
        name4_label = customtkinter.CTkLabel(master=student_frame_4, text="Jimmy White", text_color="black", font=("Arial", 20), fg_color="transparent")
        name4_label.bind('<Button-1>', lambda event: toggle_border(student_frame_4))
        name4_label.place(x=50, y=10)
        # School Name
        school4_label = customtkinter.CTkLabel(master=student_frame_4, text="Shark School", text_color="black", font=("Arial", 13), fg_color="transparent")
        school4_label.bind('<Button-1>', lambda event: toggle_border(student_frame_4))
        school4_label.place(x=50, y=35)

        # Add student frame 5
        student_frame_5 = customtkinter.CTkFrame(master=info_frame, width=250, height=70, fg_color="white", corner_radius=10, border_width=0, border_color="#5cb6f8")
        student_frame_5.bind('<Button-1>', lambda event: toggle_border(student_frame_5))
        student_frame_5.tag = 5
        student_frame_5.pack(padx=10, pady=5)
        # Create Canvas student frame 1
        canvas5 = customtkinter.CTkCanvas(
            student_frame_5,
            width = 7,
            height = 65,
            bg = "#fce467",
            highlightthickness = 0,
            bd = 0
        )
        canvas5.bind('<Button-1>', lambda event: toggle_border(student_frame_5))
        canvas5.place(x=15, y=2)
        # Student Name
        name5_label = customtkinter.CTkLabel(master=student_frame_5, text="Mary Beth", text_color="black", font=("Arial", 20), fg_color="transparent")
        name5_label.bind('<Button-1>', lambda event: toggle_border(student_frame_5))
        name5_label.place(x=50, y=10)
        # School Name
        school5_label = customtkinter.CTkLabel(master=student_frame_5, text="Shark School", text_color="black", font=("Arial", 13), fg_color="transparent")
        school5_label.bind('<Button-1>', lambda event: toggle_border(student_frame_5))
        school5_label.place(x=50, y=35)

        # Add student frame 6
        student_frame_6 = customtkinter.CTkFrame(master=info_frame, width=250, height=70, fg_color="white", corner_radius=10, border_width=0, border_color="#5cb6f8")
        student_frame_6.bind('<Button-1>', lambda event: toggle_border(student_frame_6))
        student_frame_6.tag = 6
        student_frame_6.pack(padx=10, pady=5)
        # Create Canvas student frame 1
        canvas6 = customtkinter.CTkCanvas(
            student_frame_6,
            width = 7,
            height = 65,
            bg = "#56b3f7",
            highlightthickness = 0,
            bd = 0
        )
        canvas6.bind('<Button-1>', lambda event: toggle_border(student_frame_6))
        canvas6.place(x=15, y=2)
        # Student Name
        name6_label = customtkinter.CTkLabel(master=student_frame_6, text="Michelle Leon", text_color="black", font=("Arial", 20), fg_color="transparent")
        name6_label.bind('<Button-1>', lambda event: toggle_border(student_frame_6))
        name6_label.place(x=50, y=10)
        # School Name
        school6_label = customtkinter.CTkLabel(master=student_frame_6, text="Frog Academy", text_color="black", font=("Arial", 13), fg_color="transparent")
        school6_label.bind('<Button-1>', lambda event: toggle_border(student_frame_6))
        school6_label.place(x=50, y=35)

        # Add student frame 7
        student_frame_7 = customtkinter.CTkFrame(master=info_frame, width=250, height=70, fg_color="white", corner_radius=10, border_width=0, border_color="#5cb6f8")
        student_frame_7.bind('<Button-1>', lambda event: toggle_border(student_frame_7))
        student_frame_7.tag = 7
        student_frame_7.pack(padx=10, pady=5)
        # Create Canvas student frame 1
        canvas7 = customtkinter.CTkCanvas(
            student_frame_7,
            width = 7,
            height = 65,
            bg = "#65dd71",
            highlightthickness = 0,
            bd = 0
        )
        canvas7.bind('<Button-1>', lambda event: toggle_border(student_frame_7))
        canvas7.place(x=15, y=2)
        # Student Name
        name7_label = customtkinter.CTkLabel(master=student_frame_7, text="Jean Arc", text_color="black", font=("Arial", 20), fg_color="transparent")
        name7_label.bind('<Button-1>', lambda event: toggle_border(student_frame_7))
        name7_label.place(x=50, y=10)
        # School Name
        school7_label = customtkinter.CTkLabel(master=student_frame_7, text="Frog Academy", text_color="black", font=("Arial", 13), fg_color="transparent")
        school7_label.bind('<Button-1>', lambda event: toggle_border(student_frame_7))
        school7_label.place(x=50, y=35)

        # Toggle border
        def toggle_border(frame):
            # Toggle Border for current frame
            if frame._border_width == 0:
                for child in frame.master.winfo_children():
                    # Reset Border
                    if isinstance(child, customtkinter.CTkFrame):
                        child.configure(border_width=0)

                frame.configure(border_width=2)
                # Get Portrait Color
                color = frame.winfo_children()[0].cget("bg")
                # Get Name
                name = frame.winfo_children()[1].cget("text")
                # Get School Name
                schoolname = frame.winfo_children()[2].cget("text")
                # Get Portrait index
                index = frame.tag
                toggle_detail_frame(1, a=color, b=name, c=schoolname, d=index)
            else:
                frame.configure(border_width=0)
                toggle_detail_frame(0)

        # Create a detail frame
        def toggle_detail_frame(toggle, *args, **kwargs):
            # Check if detail_frame has already been created
            if toggle == 1:
                if hasattr(toggle_detail_frame, 'detail_frame') and toggle_detail_frame.detail_frame.winfo_exists():
                    toggle_detail_frame.detail_frame.destroy()

                # Create and pack the detail_frame
                detail_frame = customtkinter.CTkFrame(master=name_frame, width=260, height=310, fg_color="white", corner_radius=10, border_width=0)
                detail_frame.place(relx=0.05, rely=0.36)

                # Get Info
                border_color = kwargs.get('a', "white")
                name = kwargs.get('b', "")
                schoolname = kwargs.get('c', "")
                index = kwargs.get('d', "")
                
                # Create Canvas
                canvas_detail = customtkinter.CTkCanvas(
                    detail_frame,
                    width = 175,
                    height = 175,
                    bg = "white",
                    highlightthickness = 0,
                    bd = 0
                )

                # Add Portrait Border
                canvas_detail.create_aa_circle(88, 89, 86, math.pi/2, fill=border_color)
                # Add Portrait Image
                canvas_detail.create_image(87, 87, image=portraits_list[index - 1], anchor=tk.CENTER)
                canvas_detail.place(relx=0.16, rely=0.01)

                # Add Name label
                name_detail_label = customtkinter.CTkLabel(master=detail_frame, justify="center", width=260, text=name, text_color="black", font=("Arial", 25), fg_color="transparent")
                name_detail_label.place(relx=0, rely=0.6)

                # Add School label
                school_detail_label = customtkinter.CTkLabel(master=detail_frame, justify="center", width=260, text=schoolname, text_color="black", font=("Arial", 15), fg_color="transparent")
                school_detail_label.place(relx=0, rely=0.7)

                # Add Edit Button
                edit_btn = customtkinter.CTkButton(master=detail_frame, command= lambda: self.next_screen(10), text="Edit", text_color="black", hover_color="lightgray", font=("Arial", 20), border_width=0, width=90, height=30, fg_color="#d9d9d9")
                edit_btn.place(relx=0.1, rely=0.85)

                # Add Delete Button
                delete_btn = customtkinter.CTkButton(master=detail_frame, command= lambda: confirm_delete(), text="Delete", text_color="black", hover_color="lightgray", font=("Arial", 20), border_width=0, width=90, height=30, fg_color="#d9d9d9")
                delete_btn.place(relx=0.55, rely=0.85)

                # Save the reference to detail_frame
                toggle_detail_frame.detail_frame = detail_frame
            else:
                # Destroy detail frame
                if hasattr( toggle_detail_frame, 'detail_frame') and  toggle_detail_frame.detail_frame.winfo_exists():
                    toggle_detail_frame.detail_frame.destroy()
        
        def confirm_delete():
            if self.confirm == 0:
                self.confirm == 1
                self.confirm_frame = customtkinter.CTkFrame(self, fg_color="#e6e6e6", width=300, height=180, corner_radius=0)
                self.confirm_frame.place(x=80, y=150)

                # Add Confirm Label
                confirm_label = customtkinter.CTkLabel(master=self.confirm_frame, justify="center", width=300, text="Delete this data.", text_color="black", font=("Arial", 25), fg_color="transparent")
                confirm_label.place(relx=0, rely=0.2)

                # Add OK Button
                ok_btn = customtkinter.CTkButton(self.confirm_frame, command= lambda: self.close_frame(), text="OK", text_color="black", hover_color="lightgray", font=("Arial", 20), border_width=0, width=90, height=30, fg_color="#d9d9d9")
                ok_btn.place(x=30, y=130)

                # Add Cancel Button
                cancel_btn = customtkinter.CTkButton(self.confirm_frame, command= lambda: self.close_frame(), text="Cancel", text_color="black", hover_color="lightgray", font=("Arial", 20), border_width=0, width=90, height=30, fg_color="#d9d9d9")
                cancel_btn.place(x=180, y=130)

        # Create the virtual keyboard
        self.create_virtual_keyboard()

    def create_virtual_keyboard(self):
        # Create a frame to hold the keyboard buttons
        self.keyboard_frame = tk.Frame(self.master, bg="grey")  # Set background color to grey

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
                btn = tk.Button(self.keyboard_frame, text=key, width=5, height=1, font=("Helvetica", 9, "bold"),
                                command=lambda char=key: self.on_key_press(char))  # Set font to bold
                btn.grid(row=i, column=j, padx=3, pady=3)

        # Pack the keyboard frame initially hidden
        self.keyboard_frame.pack_forget()


    # Modify show_keyboard method to accept an entrybox parameter
    def show_keyboard(self, entrybox):
        print("show keyboard")
        entrybox.focus_set()  # Set focus to the clicked entrybox
        self.keyboard_frame.place(relx=0.08, rely=0.65)

    # Modify on_key_press method to properly handle the Delete and End keys
    def on_key_press(self, char):

        # Get the widget that currently has focus
        target_entry = self.focus_get()
        
        if char == "End":
            self.keyboard_frame.place_forget()
        elif char == "Delete":
            target_entry.delete(len(target_entry.get()) - 1)
        else:
            target_entry.insert(tk.END, char)

    def close_frame(self):
        self.confirm == 0
        self.confirm_frame.destroy()

    def next_screen(self, index):
        self.main_app.show_next_screen(index)
        self.keyboard_frame.place_forget()