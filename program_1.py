#title:mileage
#author: michael stoll
#date:4/22/2025
import tkinter
import tkinter.messagebox
class GUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('MPG calculator')
#top frame
        self.top_frame = tkinter.Frame(self.window)
        self.top_frame.pack()
#middle frame
        self.middle_frame = tkinter.Frame(self.window)
        self.middle_frame.pack()
#bottom frame
        self.bottom_frame = tkinter.Frame(self.window)
        self.bottom_frame.pack()
#gallons in tank
        self.prompt_gal = tkinter.Label(self.top_frame, text='Enter gallons in a full tank:')
        self.prompt_gal.pack(pady=20, side='left')

        self.entry_gal = tkinter.Entry(self.top_frame, width=10)
        self.entry_gal.pack(pady=20, side='left')
#miles on a full tank
        self.prompt_mi = tkinter.Label(self.top_frame, text='Enter miles traveled on a full tank:')
        self.prompt_mi.pack(pady=20, side='left')

        self.entry_mi = tkinter.Entry(self.top_frame, width=10)
        self.entry_mi.pack(pady=20, side='left')
#calculate and quit buttons
        self.button = tkinter.Button(self.bottom_frame, text='Calculate', command=self.calculate)
        self.button.pack(pady=20, side='left')

        self.gui_quit = tkinter.Button(self.bottom_frame, text='Quit', command=self.window.destroy)
        self.gui_quit.pack(pady=20, side='left')

        tkinter.mainloop()

    def calculate(self):
        gallons = float(self.entry_gal.get())
        miles = float(self.entry_mi.get())
        mpg = miles / gallons
        tkinter.messagebox.showinfo('Results', 'This car has ' + str(mpg) + ' miles per gallon')

my_gui = GUI()