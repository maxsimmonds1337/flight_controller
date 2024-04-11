class TakeoffButton(tk.Button):
    def __init__(self, master, drone_controller):
        super().__init__(master, text="Take Off", command=drone_controller.take_off)

class LandButton(tk.Button):
    def __init__(self, master, drone_controller):
        super().__init__(master, text="Land", command=drone_controller.land)

# Define other GUI components as needed
