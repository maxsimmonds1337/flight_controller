import time
import tkinter as tk
from PIL import Image, ImageTk  # For handling images


class takeoff_button(tk.Button):
    def __init__(self, master, drone_controller):
        image = Image.open("./images/take_off_off.png")
        pressed_image = Image.open("./images/take_off_on.png")

        self.tk_image = ImageTk.PhotoImage(image)
        self.tk_pressed_image = ImageTk.PhotoImage(pressed_image)

        super().__init__(master, text="Take Off", command=drone_controller.take_off, image=self.tk_image)
        self.master = master
        master.config(width = 0.1, height = 0.1)
        self.x = None
        self.y = None
    
    def take_off(self):
        print("Take off command received")
        self.configure(image=self.tk_pressed_image)  # Change image to pressed image


    def land(self):
        self.master.config(image = "./images/take_off_on.png")

    
class land_button(tk.Button):
    def __init__(self, master, drone_controller):
        super().__init__(master, text="Land", command=drone_controller.land)

class flight_time(tk.Label):
    def __init__(self, master):
        super().__init__(master, text="Current Flight Time\n 00:00:00", font=("TKDefaultFont", 25))
        self.update_interval = 50  # Update interval in milliseconds (1 second)
        
        self.timer_running = False
        self.timer_id = None

        self.x = None
        self.y = None
    
    def start_timer(self):
        self.start_time = time.time()  # Initialize start time with current time in seconds since the epoch
        self.timer_running = True
        self.update_time()

    def stop_timer(self):
        self.timer_running = False

    def update_time(self):
        if self.timer_running:
            elapsed_seconds = int(time.time() - self.start_time)  # Calculate elapsed time in seconds
            hours = elapsed_seconds // 3600
            minutes = (elapsed_seconds % 3600) // 60
            seconds = elapsed_seconds % 60
            time_str = f"Current Flight Time\n{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.config(text=time_str)  # Update the label text with the formatted elapsed time
            self.after(10, self.update_time)  # Schedule the update_time method to be called again after the specified interval
