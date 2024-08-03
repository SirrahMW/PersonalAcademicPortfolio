import tkinter as tk
class GUI:
    def __init__(self):
        # Main window #
        self.mainWindow = tk.Tk()
        # Canvas in the main window #
        self.canvas = tk.Canvas(self.mainWindow, width=500, height=500)
        # Rings #
        self.canvas.create_oval(400, 400, 100, 100)
        self.canvas.create_oval(380, 380, 120, 120)
        self.canvas.create_oval(350, 350, 150, 150)
        self.canvas.create_oval(330, 330, 170, 170)
        self.canvas.create_oval(290, 290, 210, 210)
        self.canvas.create_oval(270, 270, 230, 230)
        # Numbering #
        self.canvas.create_text(250, 250, text='core')
        self.canvas.create_text(280, 250, text='1')
        self.canvas.create_text(310, 250, text='2')
        self.canvas.create_text(340, 250, text='3')
        self.canvas.create_text(365, 250, text='4')
        self.canvas.create_text(390, 250, text='5')
        # Pack #
        self.canvas.pack()
        # Main loop #
        tk.mainloop()


# Start #
gui = GUI()