import tkinter as tk
import controller.gui_components as gc
import controller.controller as dc

class ControllerApp:
    def __init__(self, master, drone_controller):
        self.master = master
        self.controller = drone_controller

        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        self.master.geometry(f"{self.screen_width}x{self.screen_height}")

        self.master.title("Drone Remote Controller")
        self.create_widgets()
        self.bind_keys()

    def create_widgets(self):
        # Create GUI widgets (buttons, sliders, etc.)

        # Take off Timer
        self.t_o_time = gc.flight_time(self.master)
        print(f'screen width: {self.screen_width}\nscreen height: {self.screen_height}')
        self.t_o_time.x = int(self.screen_width*0.85)
        self.t_o_time.y = int(self.screen_height*0.75)
        self.t_o_time.place(x=self.t_o_time.x, y=self.t_o_time.y)

        # Take off button
        self.t_o_button = gc.takeoff_button(self.master, self.controller)
        self.t_o_button.x = self.screen_width*0.875
        self.t_o_button.y = self.screen_height*0.65
        self.t_o_button.place(x=self.t_o_button.x, y=self.t_o_button.y)


    def bind_keys(self):
        self.master.bind('<KeyPress-t>', self.t_o_button_pressed)

    def t_o_button_pressed(self, event):
        print("Starting timer")
        self.t_o_time.start_timer()
        self.controller.take_off()
        self.t_o_button.take_off()

def main():
    root = tk.Tk() # this is the main window

    controller = dc.DroneController()

    app = ControllerApp(root, controller)
    root.mainloop()

if __name__ == "__main__":
    main()
