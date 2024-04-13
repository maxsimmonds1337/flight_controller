import tkinter as tk
import controller.gui_components as gc

class ControllerApp:
    def __init__(self, master):
        self.master = master

        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        self.master.geometry(f"{self.screen_width}x{self.screen_height}")

        self.master.title("Drone Remote Controller")
        self.create_widgets()

    def create_widgets(self):
        # Create GUI widgets (buttons, sliders, etc.)

        # Take of Timer
        self.t_o_time = gc.flight_time(self.master)
        print(f'screen width: {self.screen_width}\nscreen height: {self.screen_height}')
        self.x = int(self.screen_width*0.85)
        self.y = int(self.screen_height*0.75)
        self.t_o_time.place(x=self.x, y=self.y)

        # Take off button
        
        pass

def main():
    root = tk.Tk() # this is the main window

    app = ControllerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
