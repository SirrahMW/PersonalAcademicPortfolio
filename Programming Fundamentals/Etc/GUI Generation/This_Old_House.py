import tkinter as tk
class GUI:
    def __init__(self):
        # Main window #
        self.mainWindow = tk.Tk()
        # Canvas in the main window #
        self.canvas = tk.Canvas(self.mainWindow, width=500, height=500)
        # Roof #
        self.canvas.create_line(100, 300, 400, 300)
        self.canvas.create_line(400, 300, 250, 200)
        self.canvas.create_line(250, 200, 100, 300)
        # House #
        self.canvas.create_rectangle(100, 300, 400, 450)
        # Door #
        self.canvas.create_rectangle(240, 400, 260, 450)
        self.canvas.create_oval(253, 432, 256, 435)
        self.canvas.create_rectangle(245, 405, 255, 425)
        self.canvas.create_line(250, 405, 250, 425)
        self.canvas.create_line(245, 415, 255, 415)
        # Windows #
        self.canvas.create_rectangle(310, 360, 350, 420)
        self.canvas.create_rectangle(190, 420, 150, 360)
        self.canvas.create_line(330, 360, 330, 420)
        self.canvas.create_line(310, 390, 350, 390)
        self.canvas.create_line(170, 420, 170, 360)
        self.canvas.create_line(190, 390, 150, 390)
        # Pack #
        self.canvas.pack()
        # Main loop #
        tk.mainloop()


# Start #
gui = GUI()