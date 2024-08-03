# Import tkinterface #
import tkinter as t

# GUI class #
class GUI:
    # Initialize #
    def __init__(self):
        # Creating the main window #
        self.main_window = t.Tk()

        # Building the frames #
        self.gallons_frame = t.Frame(self.main_window)
        self.miles_frame = t.Frame(self.main_window)
        self.results_frame = t.Frame(self.main_window)
        self.buttons_frame = t.Frame(self.main_window)

        # Gallons label and entry #
        self.gallons_label = t.Label(self.gallons_frame, text='Gallons in a full tank:')
        self.gallons_entry = t.Entry(self.gallons_frame, width=10)

        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='left')

        # Miles label and entry #
        self.miles_label = t.Label(self.miles_frame, text='Possible miles on full tank:')
        self.miles_entry = t.Entry(self.miles_frame, width=10)

        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        # Results label and display #
        self.results_label = t.Label(self.results_frame, text='MPG:')
        self.mpg = t.StringVar()    # This will be updated to the mpg_label
        self.mpg_label = t.Label(self.results_frame, textvariable=self.mpg)

        self.results_label.pack(side='left')
        self.mpg_label.pack(side='left')

        # Buttons #
        self.calc_button = t.Button(self.buttons_frame, text='Calculate', command=self.calculate_mpg)
        self.quit_button = t.Button(self.buttons_frame, text='Done', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames #
        self.gallons_frame.pack()
        self.miles_frame.pack()
        self.results_frame.pack()
        self.buttons_frame.pack()

        # Start the main loop #
        t.mainloop()

    # Function to calculate mpg #
    def calculate_mpg(self):
        self.miles = int(self.miles_entry.get())
        self.gallons = int(self.gallons_entry.get())
        self.calc = format(self.miles / self.gallons, '.2f')
        self.mpg.set(str(self.calc))

# Create an instance of the GUI #
mpgCalculator = GUI()
