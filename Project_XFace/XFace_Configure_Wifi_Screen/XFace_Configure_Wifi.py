import tkinter as tk
from tkinter import simpledialog
import customtkinter
import subprocess
import tkinter.messagebox

def get_wifi_networks():
    try:
        result = subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True)
        networks = result.stdout.split("\n")
        wifi_networks = [line.split(":")[1].strip() for line in networks if "SSID" in line]
        return wifi_networks
    except Exception as e:
        print("Error occurred while getting WiFi networks:", e)
        return []

class Screen1(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.configure(bg="white", width=600, height=500)
        self.pack_propagate(0)

        #----------------------------------------------------------------------------
        #                                     Frame 1
        #----------------------------------------------------------------------------

        # Add Frame Step Frame
        self.step_frame = customtkinter.CTkFrame(self, width=600, height=40, fg_color="white", corner_radius=0)
        self.step_frame.pack()

        # Add "<" Button
        back_btn = customtkinter.CTkButton(master=self.step_frame, width=30, height=30, text="<", text_color="black", font=("Arial", 30), fg_color="transparent", hover=False)
        back_btn.place(relx=0.02, rely=0.02)

        #----------------------------------------------------------------------------
        #                                     Frame 2
        #----------------------------------------------------------------------------

        # Add Frame Step Frame 2
        self.configure_wifi_text_frame = customtkinter.CTkFrame(self, width=600, height=40, fg_color="white", corner_radius=0)
        self.configure_wifi_text_frame.pack()

        # Add Text "Name"
        configure_wifi_label = customtkinter.CTkLabel(master=self.configure_wifi_text_frame, text="Let's Configure the Wi-Fi", font=customtkinter.CTkFont(size=30, weight="bold"), text_color="black")
        configure_wifi_label.place(relx=0.5, rely=0.5, anchor="center")

        #----------------------------------------------------------------------------
        #                                     Frame 3
        #----------------------------------------------------------------------------

        # Add Frame Step Frame 3
        self.select_wifi_text_frame = customtkinter.CTkFrame(self, width=600, height=80, fg_color="white", corner_radius=0)
        self.select_wifi_text_frame.pack()

        # Add Text "Name"
        select_wifi_label = customtkinter.CTkLabel(master=self.select_wifi_text_frame, text="Please select the Wi-Fi network to connect to.", font=customtkinter.CTkFont(size=20), text_color="black")
        select_wifi_label.place(relx=0.5, rely=0.5, anchor="center")

        #----------------------------------------------------------------------------
        #                                     Frame 4
        #----------------------------------------------------------------------------

        # Frame 4 - Wi-Fi List and Scrollbar
        self.select_wifi_list_frame = customtkinter.CTkFrame(self, width=600, height=200, fg_color="white", corner_radius=0)
        self.select_wifi_list_frame.pack()

        # Wi-Fi Listbox
        listbox_width = 50
        listbox_height = 50
        self.wifi_listbox = tk.Listbox(master=self.select_wifi_list_frame, selectmode=tk.SINGLE, font=("Arial", 20), bg="white", fg="black", highlightbackground="gray", selectbackground="lightgray", width=listbox_width, height=listbox_height)
        self.wifi_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = tk.Scrollbar(master=self.select_wifi_list_frame, command=self.wifi_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Adjusting the size of each item in the Listbox
        listbox_item_width = 30  # Adjust as needed
        listbox_item_height = 4  # Adjust as needed
        self.wifi_listbox.config(width=listbox_item_width, height=listbox_item_height)

        # Adding Wi-Fi networks to the listbox
        self.wifi_networks = get_wifi_networks()
        for network in self.wifi_networks:
            self.wifi_listbox.insert(tk.END, network)

        # Bind the listbox click event to show the popup menu
        self.wifi_listbox.bind("<ButtonRelease-1>", self.enter_password_wifi)

        #----------------------------------------------------------------------------
        #                                     Frame 5
        #----------------------------------------------------------------------------

        # Frame 5 Choose different Wifi
        self.choose_different_wifi_list_frame = customtkinter.CTkFrame(self, width=600, height=140, fg_color="white", corner_radius=0)
        self.choose_different_wifi_list_frame.pack()

        # Add Button "Choose a different Wi-Fi network"
        btn_choose_different_wifi = customtkinter.CTkButton(master=self.choose_different_wifi_list_frame, text="Choose a different Wi-Fi network", font=("Arial", 20), text_color="#3f9de1", fg_color="white", hover_color="white")
        btn_choose_different_wifi.place(relx=0.5, rely=0.5, anchor="center")

        #Bind the listbox click event to show the popup menu
        btn_choose_different_wifi.bind("<ButtonRelease-1>", lambda event: self.open_choose_different_wifi_screen())

    def get_wifi_password(self, wifi_name):
        try:
            result = subprocess.run(["netsh", "wlan", "show", "profile", wifi_name, "key=clear"], capture_output=True, text=True)
            password_info = result.stdout.split("\n")
            password_line = [line for line in password_info if "Key Content" in line][0]
            password = password_line.split(":")[1].strip()
            return password
        except Exception as e:
            print("Error occurred while getting Wi-Fi password:", e)
            return None

    def enter_password_wifi(self, event):

        # Get the index of the clicked item
        index = self.wifi_listbox.nearest(event.y)

        # Get the text of the clicked item
        wifi_name = self.wifi_listbox.get(index)

        # Get Wi-Fi password
        wifi_password = self.get_wifi_password(wifi_name)
        if wifi_password is not None:
            print(f"Wi-Fi password for '{wifi_name}': {wifi_password}")
        else:
            print(f"Wi-Fi password for '{wifi_name}' is not available.")

        # Get the index of the clicked item
        index = self.wifi_listbox.nearest(event.y)

        # Get the text of the clicked item
        wifi_name = self.wifi_listbox.get(index)

        # Create the password enter frame
        self.password_enter_frame = customtkinter.CTkFrame(self, fg_color="#e6e6e6", width=500, height=325, corner_radius=10)
        self.password_enter_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Add "x" Button
        back_btn = customtkinter.CTkButton(master=self.password_enter_frame, width=30, text="x", text_color="gray", font=("Arial", 30), fg_color="transparent", hover=False, command=self.destroy_password_enter_frame)
        back_btn.place(relx=0.02, rely=0.02)

        # Add password enter Label
        password_enter_label = customtkinter.CTkLabel(master=self.password_enter_frame, text="Please enter the password", text_color="black", font=("Arial", 25), fg_color="transparent")
        password_enter_label.place(relx=0.5, rely=0.20, anchor="center")

        # Add name_wifi Label
        name_wifi_label = customtkinter.CTkLabel(master=self.password_enter_frame, text=f"'{wifi_name}'.", text_color="black", font=("Arial", 25), fg_color="transparent")
        name_wifi_label.place(relx=0.5, rely=0.30, anchor="center")

        # Add password Label
        password_label = customtkinter.CTkLabel(master=self.password_enter_frame, text="Password", text_color="black", font=("Arial", 25), fg_color="transparent")
        password_label.place(relx=0.2, rely=0.50, anchor="center")

        # Add Text Box for password
        self.password_entrybox = customtkinter.CTkEntry(master=self.password_enter_frame, width=350, height=40, fg_color="white", border_color="gray", border_width=1, text_color="black", font=customtkinter.CTkFont(size=15), corner_radius=10, show="*")  # Show password as dots initially
        self.password_entrybox.place(relx=0.5, rely=0.63, anchor="center")

        # Add Button "Connect"
        btn_connect_wifi = customtkinter.CTkButton(master=self.password_enter_frame, width=150, height=40, text="Connect", font=customtkinter.CTkFont(size=20, weight="bold"), text_color="White", corner_radius=10, fg_color="#0094ff", border_color="gray", border_width=1, command=self.connected_wifi)
        btn_connect_wifi.place(relx=0.5, rely=0.85, anchor="center")

        # Add Button "Toggle Password Button"
        toggle_password_button = customtkinter.CTkButton(master=self.password_enter_frame, width=1, height=1, command=self.toggle_password_visibility, text="👁️ ", text_color="gray", font=("Arial", 20), fg_color="white", hover=False, border_color="white", bg_color="white")
        toggle_password_button.place(relx=0.83, rely=0.63, anchor="e")

    def open_choose_different_wifi_screen(self):

        # Create choose different wifi screen frame
        self.choose_different_wifi_screen_frame = customtkinter.CTkFrame(self, fg_color="#e6e6e6", width=500, height=325, corner_radius=10)
        self.choose_different_wifi_screen_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Add "x" Button
        back_btn = customtkinter.CTkButton(master=self.choose_different_wifi_screen_frame, width=30, text="x", text_color="gray", font=("Arial", 30), fg_color="transparent", hover=False, command=self.destroy_choose_different_wifi_screen_frame)
        back_btn.place(relx=0.02, rely=0.02)

        # Add network name enter Label 1
        network_name_enter_label1 = customtkinter.CTkLabel(master=self.choose_different_wifi_screen_frame, text="Please enter the network name", text_color="black", font=("Arial", 25), fg_color="transparent")
        network_name_enter_label1.place(relx=0.5, rely=0.10, anchor="center")

        # Add network name enter Label 2
        network_name_enter_label2 = customtkinter.CTkLabel(master=self.choose_different_wifi_screen_frame, text="and security type.", text_color="black", font=("Arial", 25), fg_color="transparent")
        network_name_enter_label2.place(relx=0.5, rely=0.20, anchor="center")

        # Add network name ssid Label
        network_name_ssid_label = customtkinter.CTkLabel(master=self.choose_different_wifi_screen_frame, text="Network name(SSID)", text_color="black", font=("Arial", 20), fg_color="transparent")
        network_name_ssid_label.place(relx=0.3, rely=0.35, anchor="center")

        # Add Text Box for network name ssid
        self.network_name_ssid_entrybox = customtkinter.CTkEntry(master=self.choose_different_wifi_screen_frame, width=350, height=40, fg_color="white", border_color="gray", border_width=1, text_color="black", font=customtkinter.CTkFont(size=15), corner_radius=10)  # Show password as dots initially
        self.network_name_ssid_entrybox.place(relx=0.5, rely=0.47, anchor="center")

        # Add Security type Label
        security_type_label = customtkinter.CTkLabel(master=self.choose_different_wifi_screen_frame, text="Security type", text_color="black", font=("Arial", 20), fg_color="transparent")
        security_type_label.place(relx=0.23, rely=0.60, anchor="center")

        # Define values for Security type ComboBox
        security_type_list = ["WEP", "WPA", "WPA2", "WPA3"]

        # Add Security type ComboBox
        security_type_ComboBox= customtkinter.CTkComboBox(master=self.choose_different_wifi_screen_frame, state="readonly", values=security_type_list, justify="left", width=350, height=40, fg_color="White", font=customtkinter.CTkFont(size=13), text_color="Black", dropdown_fg_color="White", dropdown_font=customtkinter.CTkFont(size=13), dropdown_text_color="Black")
        security_type_ComboBox.place(relx=0.5, rely=0.72, anchor=tk.CENTER)

        # Add Button "Continue"
        btn_continue_wifi = customtkinter.CTkButton(master=self.choose_different_wifi_screen_frame, width=150, height=40, text="Continue >", font=customtkinter.CTkFont(size=20, weight="bold"), text_color="White", corner_radius=20, fg_color="#0094ff", border_color="gray", border_width=1, command=self.continue_to_username_and_password)
        btn_continue_wifi.place(relx=0.5, rely=0.9, anchor="center")

    def continue_to_username_and_password(self):

        # Call the method to enter username and password frame
        self.show_username_and_password_frame()
        
        if hasattr(self, 'choose_different_wifi_screen_frame'):
            self.choose_different_wifi_screen_frame.destroy()

    def show_username_and_password_frame(self):

        # Create enter username and password frame
        self.username_and_password_frame = customtkinter.CTkFrame(self, fg_color="#e6e6e6", width=500, height=325, corner_radius=10)
        self.username_and_password_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Add "x" Button
        back_btn = customtkinter.CTkButton(master=self.username_and_password_frame, width=30, text="x", text_color="gray", font=("Arial", 30), fg_color="transparent", hover=False, command=self.destroy_username_and_password_frame)
        back_btn.place(relx=0.02, rely=0.02)

        # Add username and password Label 1
        username_and_password_label1 = customtkinter.CTkLabel(master=self.username_and_password_frame, text="Please enter your username", text_color="black", font=("Arial", 25), fg_color="transparent")
        username_and_password_label1.place(relx=0.5, rely=0.10, anchor="center")

        # Add username and password Label 2
        username_and_password_label2 = customtkinter.CTkLabel(master=self.username_and_password_frame, text="and password.", text_color="black", font=("Arial", 25), fg_color="transparent")
        username_and_password_label2.place(relx=0.5, rely=0.20, anchor="center")

        # Add "Username" Label
        username_label = customtkinter.CTkLabel(master=self.username_and_password_frame, text="Username", text_color="black", font=("Arial", 20), fg_color="transparent")
        username_label.place(relx=0.21, rely=0.35, anchor="center")

        # Add Text Box for username
        self.username_entrybox = customtkinter.CTkEntry(master=self.username_and_password_frame, width=350, height=40, fg_color="white", border_color="gray", border_width=1, text_color="black", font=customtkinter.CTkFont(size=15), corner_radius=10)
        self.username_entrybox.place(relx=0.5, rely=0.47, anchor="center")

        # Add "Password" Label
        password_label = customtkinter.CTkLabel(master=self.username_and_password_frame, text="Security type", text_color="black", font=("Arial", 20), fg_color="transparent")
        password_label.place(relx=0.23, rely=0.60, anchor="center")

        # Add Text Box for password
        self.password_entrybox = customtkinter.CTkEntry(master=self.username_and_password_frame, width=350, height=40, fg_color="white", border_color="gray", border_width=1, text_color="black", font=customtkinter.CTkFont(size=15), corner_radius=10, show="*")
        self.password_entrybox.place(relx=0.5, rely=0.72, anchor="center")

        # Add Button "Toggle Password Button"
        toggle_password_button = customtkinter.CTkButton(master=self.username_and_password_frame, width=1, height=1, command=self.toggle_password_visibility, text="👁️ ", text_color="gray", font=("Arial", 20), fg_color="white", hover=False, border_color="white", bg_color="white")
        toggle_password_button.place(relx=0.83, rely=0.72, anchor="e")

        # Add Button "Connect"
        btn_connect_wifi = customtkinter.CTkButton(master=self.username_and_password_frame, width=150, height=40, text="Connect", font=customtkinter.CTkFont(size=20, weight="bold"), text_color="White", corner_radius=10, fg_color="#0094ff", border_color="gray", border_width=1, command=self.destroy_username_and_password_frame)
        btn_connect_wifi.place(relx=0.5, rely=0.9, anchor="center")

    def connect_to_wifi(self):
        selected_index = self.wifi_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            selected_wifi = self.wifi_listbox.get(selected_index)
            # Check if the selected Wi-Fi already has " - Connected" appended to it
            if selected_wifi.endswith(" - Connected"):
                return  # If already connected, do nothing
            # Iterate through items in the listbox to find and remove any previous " - Connected" entry
            for i in range(self.wifi_listbox.size()):
                wifi = self.wifi_listbox.get(i)
                if wifi.endswith(" - Connected"):
                    # Remove previous " - Connected" entry
                    self.wifi_listbox.delete(i)
                    # If the index of the removed item is less than the selected index,
                    # adjust the selected index accordingly
                    if i < selected_index:
                        selected_index -= 1
                    break
            # Insert the selected Wi-Fi with " - Connected"
            self.wifi_listbox.insert(selected_index, f"{selected_wifi} - Connected")




    def destroy_password_enter_frame(self):
        if hasattr(self, 'password_enter_frame'):
            self.password_enter_frame.destroy()
    
    def connected_wifi(self):
        if hasattr(self, 'password_enter_frame'):
            entered_password = self.password_entrybox.get()
            selected_index = self.wifi_listbox.curselection()
        
            if selected_index:
                selected_index = selected_index[0]
                selected_wifi = self.wifi_listbox.get(selected_index)

                # Get Wi-Fi password
                wifi_password = self.get_wifi_password(selected_wifi)
            
                if wifi_password is not None and entered_password == wifi_password:
                    print("Password is correct. Connecting to Wi-Fi...")
                    tkinter.messagebox.showinfo("Success", "Connecting to Wi-Fi...")
                    # Close the password enter frame
                    self.password_enter_frame.destroy()
                    self.connect_to_wifi()
                
                    # Update the Wi-Fi listbox to indicate connection
                    self.wifi_listbox.delete(selected_index)
                    self.wifi_listbox.insert(selected_index, f"{selected_wifi} - Connected")
                else:
                    print("Incorrect password. Please try again.")
                    tkinter.messagebox.showinfo("Failed", "Password is wrong") 
                    # You can add a message box or label to indicate incorrect password
                
                return

    def destroy_choose_different_wifi_screen_frame(self):
        if hasattr(self, 'choose_different_wifi_screen_frame'):
            self.choose_different_wifi_screen_frame.destroy()

    def destroy_username_and_password_frame(self):
        if hasattr(self, 'username_and_password_frame'):
            self.username_and_password_frame.destroy()


    def toggle_password_visibility(self):
        # Get the current state of the password entry widget
        current_show_state = self.password_entrybox.cget("show")

        # Toggle between showing and hiding the password
        if current_show_state:
            self.password_entrybox.configure(show="")
        else:
            self.password_entrybox.configure(show="*")


# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    app = Screen1(root, None)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
