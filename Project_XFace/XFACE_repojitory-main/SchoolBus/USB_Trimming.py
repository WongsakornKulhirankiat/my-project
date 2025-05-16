#### You need to prepare a image and set image_path


import tkinter.messagebox
import tkinter as tk
import customtkinter
from tkinter import ttk
import math
from PIL import Image, ImageTk


try:
    class TrimmingScreen(tk.Frame):
        def __init__(self):
            self.root = tk.Tk()
            self.root.title("XFace_Student_Registration")
            self.root.geometry("600x500")

            #----------------------------------------------------------------------------
            #                                     Frame 1
            #----------------------------------------------------------------------------

            # Add Frame Step Frame
            self.trim_frame = customtkinter.CTkFrame(self.root, width=600, height=500, fg_color="#e6e6e6", corner_radius=0)
            self.trim_frame.pack()
            #----------------------------------------------------------------------------
            #                                     Cnvas 
            #----------------------------------------------------------------------------

            self.operation_canvas = tk.Canvas(master=self.trim_frame, width=self.trim_frame._current_width/5, height=500, bg="#e6e6e6")
            self.operation_canvas.place(x=0)

            #Add "<" Button
            back_btn = customtkinter.CTkButton(master=self.operation_canvas, width=30, height=30, text="<", text_color="white", font=("Arial", 30), fg_color="transparent", hover=False)
            back_btn.place(relx=0.02, rely=0.02)

            # Add Button "OK"
            btn_ok = customtkinter.CTkButton(master=self.operation_canvas, width=80, text="OK", command=self.next_screen, font=customtkinter.CTkFont(size=20), text_color="black", corner_radius=10, fg_color="white", border_color="")
            btn_ok.place(x=10, y=450)

            dir_angle = [0, 90, 180, 270,"+","-"]
            circle_radius = 20
            triangle_length = 17  

            for directions in dir_angle:
                #Positioning shapes 
                if directions == 0 : circle_center, triangle_center = (90, 250),(90, 250)#→
                elif directions == 90 : circle_center, triangle_center = (60, 300),(60, 300)#↓
                elif directions == 180 : circle_center, triangle_center = (30, 250),(30, 250)#←
                elif directions == 270 : circle_center, triangle_center = (60, 200),(60, 200)#↑
                elif directions == "+" : circle_center, text_center = (30, 100),(30, 100)
                elif directions == "-" : circle_center, text_center = (90, 100),(90, 100)

                #Add circle
                self.operation_canvas.create_oval(circle_center[0] - circle_radius, circle_center[1] - circle_radius,
                                    circle_center[0] + circle_radius, circle_center[1] + circle_radius,
                                    outline="", fill="white")

                #Add text in circle
                if directions == "+" :
                    self.plus_button = self.operation_canvas.create_text(text_center, text="＋", font=("Arial", 20),fill="#e6e6e6")
                    continue
                elif directions == "-" :
                    self.minus_button = self.operation_canvas.create_text(text_center, text="－", font=("Arial", 20),fill="#e6e6e6")
                    continue

                #Add triangle
                rotation_angle = math.radians(directions)
                rotated_points = []
                for angle in range(0, 360, 120):
                    x = triangle_center[0] + triangle_length * math.cos(math.radians(angle)) 
                    y = triangle_center[1] + triangle_length * math.sin(math.radians(angle))  
                    rotated_x = triangle_center[0] + (x - triangle_center[0]) * math.cos(rotation_angle) - (y - triangle_center[1]) * math.sin(rotation_angle)
                    rotated_y = triangle_center[1] + (x - triangle_center[0]) * math.sin(rotation_angle) + (y - triangle_center[1]) * math.cos(rotation_angle)
                    rotated_points.append(rotated_x)
                    rotated_points.append(rotated_y)

                if directions == 0 : self.right_button = self.operation_canvas.create_polygon(rotated_points, outline="", fill="#e6e6e6")
                elif directions == 90 : self.under_button = self.operation_canvas.create_polygon(rotated_points, outline="", fill="#e6e6e6")
                elif directions == 180 : self.left_button = self.operation_canvas.create_polygon(rotated_points, outline="", fill="#e6e6e6")
                elif directions == 270 : self.up_button = self.operation_canvas.create_polygon(rotated_points, outline="", fill="#e6e6e6")
                

            self.operation_canvas.tag_bind(self.right_button, "<Button-1>", lambda event: app.move("right"))
            self.operation_canvas.tag_bind(self.left_button, "<Button-1>", lambda event: app.move("left"))
            self.operation_canvas.tag_bind(self.up_button, "<Button-1>", lambda event: app.move("up"))
            self.operation_canvas.tag_bind(self.under_button, "<Button-1>", lambda event: app.move("down"))
            self.operation_canvas.tag_bind(self.plus_button, "<Button-1>", lambda event: app.resize("increase"))
            self.operation_canvas.tag_bind(self.minus_button, "<Button-1>", lambda event: app.resize("decrease"))


            #----------------------------------------------------------------------------
            #                                     Frame 2
            #----------------------------------------------------------------------------
            self.photo_canvas = tk.Canvas(master=self.trim_frame, width=self.trim_frame._current_width/5*4, height=500, bg="#e6e6e6")
            self.photo_canvas.place(x=self.trim_frame._current_width/5)

            #Add image
            self.image_path = "School Bus\photoSample.png" ##Prepare the image and enter the pass
            self.image = Image.open(self.image_path)
            self.image.thumbnail((self.trim_frame._current_width/5*4, 500))  # Adjust image to canvas size
            self.photo = ImageTk.PhotoImage(self.image)
            self.photo_canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

            center_x = self.image.width // 2
            center_y = self.image.height // 2
            # Add square
            square_size = min(self.image.width, self.image.height) // 2
            self.crop_rect = self.photo_canvas.create_rectangle(center_x - square_size, center_y - square_size,
                                                        center_x + square_size, center_y + square_size,
                                                        outline="gold1",width=3)
            # Add square
            circle_center_y =  self.image.height // 7 * 3
            self.crop_circle = self.photo_canvas.create_oval(center_x - square_size//3*2, circle_center_y - square_size//3*2,
                                                    center_x + square_size//3*2, circle_center_y + square_size//3*2,
                                                    outline="gold1", dash=(20, 50), width=1)
            
            # Add explanatory text(button)
            photo_txt = customtkinter.CTkButton(master=self.photo_canvas, width=250, text="Fit the face to the circle and crop it", font=customtkinter.CTkFont(size=15), text_color="black", corner_radius=10, fg_color="white", border_color="")
            photo_txt.place(x=100, y=450)

        def move(self, direction):
            x0, y0, x1, y1 = self.photo_canvas.coords(self.crop_rect)
            image_width = self.image.width
            image_height = self.image.height
            step = 5  # Movement step size
            if direction == "right" and x1 + step <= image_width:
                self.photo_canvas.move(self.crop_rect, step, 0)
                self.photo_canvas.move(self.crop_circle, step, 0)
            elif direction == "left" and x0 - step >= 0:
                self.photo_canvas.move(self.crop_rect, -step, 0)
                self.photo_canvas.move(self.crop_circle, -step, 0)
            elif direction == "down" and y1 + step <= image_height:
                self.photo_canvas.move(self.crop_rect, 0, step)
                self.photo_canvas.move(self.crop_circle, 0, step)
            elif direction == "up" and y0 - step >= 0:
                self.photo_canvas.move(self.crop_rect, 0, -step)
                self.photo_canvas.move(self.crop_circle, 0, -step)

        def resize(self, operation):
            x0, y0, x1, y1 = self.photo_canvas.coords(self.crop_rect)
            image_width = self.image.width
            image_height = self.image.height
            expansion = 1.05
            reduction = 0.95
            if operation == "increase":
                if x1 + 10 <= image_width and y1 + 10 <= image_height:  # Check if the increased size fits within the image range
                    self.photo_canvas.scale(self.crop_circle, x0, y0, expansion, expansion)
                    self.photo_canvas.scale(self.crop_rect, x0, y0, expansion, expansion)
            elif operation == "decrease":
                if x1 - 10 >= 0 and y1 - 10 >= 0:  # Check if the size after reduction is greater than or equal to 0
                    self.photo_canvas.scale(self.crop_circle, x0, y0, reduction, reduction)
                    self.photo_canvas.scale(self.crop_rect, x0, y0, reduction, reduction)


        def next_screen(self):
            if self.image and self.crop_rect:
                x0, y0, x1, y1 = self.photo_canvas.coords(self.crop_rect)# Get the coordinates of the cropping range
                self.trimmed_image = self.image.crop((x0, y0, x1, y1))# trimming
            # Display cropped image
            if self.trimmed_image:
                self.trimmed_image.thumbnail((400, 400))  # Adjust image to canvas size
                trimmed_photo = ImageTk.PhotoImage(self.trimmed_image)
                self.photo_canvas.create_image(0, 0, anchor=tk.NW, image=trimmed_photo)
                self.photo_canvas.image = trimmed_photo  
            # self.main_app.set_name(self.name_txtbox.get())
            # self.main_app.set_school(self.school_txtbox.get())
            # self.main_app.show_next_screen()
except Exception as e:
    print(e)

if __name__ == "__main__":
    app = TrimmingScreen()
    app.root.mainloop()
