import time
import tkinter as tk

class takeoff_button(tk.Button):
    def __init__(self, master, drone_controller):
        super().__init__(master, text="Take Off", command=drone_controller.take_off)

class land_button(tk.Button):
    def __init__(self, master, drone_controller):
        super().__init__(master, text="Land", command=drone_controller.land)

class flight_time(tk.Label):
    def __init__(self, master):
        super().__init__(master, text="Current Flight Time: 00:00:00", font=("TKDefaultFont", 25))
        self.start_time = time.time()  # Initialize start time with current time in seconds since the epoch
        self.update_interval = 50  # Update interval in milliseconds (1 second)
    
    def update_time(self):
        elapsed_seconds = int(time.time() - self.start_time)  # Calculate elapsed time in seconds
        hours = elapsed_seconds // 3600
        minutes = (elapsed_seconds % 3600) // 60
        seconds = elapsed_seconds % 60
        time_str = f"Current Flight Time\n{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.config(text=time_str)  # Update the label text with the formatted elapsed time
        self.after(10, self.update_time)  # Schedule the update_time method to be called again after the specified interval
