import os
import psutil
from PIL import Image, ImageTk
import tkinter as tk

def get_usb_drive():
    drives = [disk.device for disk in psutil.disk_partitions() if 'media' in disk.mountpoint]
    print(drives)  # Added print statement to display the drives
    if drives:
        return drives[0]  # Return the first found removable drive
    return None

def load_images_from_directory(directory):
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
    image_paths = [os.path.join(directory, file) for file in os.listdir(directory) if file.lower().endswith(image_extensions)]
    return image_paths

def display_images(image_paths):
    window = tk.Tk()
    window.title("Image Viewer")
    image_label = tk.Label(window)
    image_label.pack()

    def show_image(index):
        if 0 <= index < len(image_paths):
            image = Image.open(image_paths[index])
            image.thumbnail((800, 600))  # Resize
            img = ImageTk.PhotoImage(image)
            image_label.config(image=img)
            image_label.image = img
            window.title(f"Image Viewer - {os.path.basename(image_paths[index])}")

    current_image_index = [0]

    def next_image():
        current_image_index[0] = (current_image_index[0] + 1) % len(image_paths)
        show_image(current_image_index[0])

    def prev_image():
        current_image_index[0] = (current_image_index[0] - 1) % len(image_paths)
        show_image(current_image_index[0])

    next_button = tk.Button(window, text="Next", command=next_image)
    next_button.pack(side="right")

    prev_button = tk.Button(window, text="Previous", command=prev_image)
    prev_button.pack(side="left")

    if image_paths:
        show_image(0)
    else:
        image_label.config(text="Not Found Picture")

    window.mainloop()

def main():
    usb_drive = get_usb_drive()
    if usb_drive:
        print(f"Found USB drive: {usb_drive}")
        image_paths = load_images_from_directory(usb_drive)
        display_images(image_paths)
    else:
        print("Not Found USB drive")

if __name__ == "__main__":
    main()