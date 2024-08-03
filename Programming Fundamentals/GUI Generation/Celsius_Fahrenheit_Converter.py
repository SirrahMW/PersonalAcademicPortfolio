# Import tkinterface #
import tkinter as t

# GUI Class #
class GUI:
    # Initialize #
    def __init__(self):
        # Main Window #
        self.main_window = t.Tk()
        self.main_window.title('Convert C to F')
        self.main_window.geometry('250x100')

        # Frames #
        self.celsius_frame = t.Frame(self.main_window)
        self.conversion_frame = t.Frame(self.main_window)
        self.button_frame = t.Frame(self.main_window)

        # Celsius Frame Widgets #
        self.celsius_label = t.Label(self.celsius_frame, text='Celsius: ')
        self.celsius_entry = t.Entry(self.celsius_frame, width=10)
        # Pack #
        self.celsius_label.pack(side='left')
        self.celsius_entry.pack(side='left')

        # Conversion Frame Widgets #
        self.conversion_label = t.Label(self.conversion_frame, text='Fahrenheit: ')
        self.converted = t.StringVar()  # To update the label
        self.converted_label = t.Label(self.conversion_frame, textvariable=self.converted)
        # Pack #
        self.conversion_label.pack(side='left')
        self.converted_label.pack(side='left')

        # Button Frame Widgets #
        self.convert_button = t.Button(self.button_frame, text='Convert', command=self.convert)
        self.quit_button = t.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        # Pack #
        self.convert_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames #
        self.celsius_frame.pack()
        self.conversion_frame.pack()
        self.button_frame.pack()

        # Start the main loop #
        t.mainloop()

    # Defining the convert function used on line 36 #
    def convert(self):
        # Getting the entry and converting it to a float #
        self.celsius = float(self.celsius_entry.get())
        # Perform the calculation #
        self.calc = 9/5 * self.celsius + 32
        # Set the appropriate stringvar to our calculation #
        self.converted.set(str(self.calc))


# Create an instance of the GUI #
converter = GUI()
