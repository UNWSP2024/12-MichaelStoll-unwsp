#title:distance calls
#author: michael stoll
#date:4/25/2025
import tkinter
import tkinter.messagebox
class GUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('Window')

        self.top_frame = tkinter.Frame(self.window)
        self.top_frame.pack()
        self.middle_frame = tkinter.Frame(self.window)
        self.middle_frame.pack()
        self.bottom_frame = tkinter.Frame(self.window)
        self.bottom_frame.pack()

        self.radio = tkinter.IntVar()
        self.radio.set(1)

        self.rb1 = tkinter.Radiobutton(self.top_frame, text='Daytime (6:00 A.M. through 5:59 P.M.)  Rate: $0.02', variable=self.radio, value=1)
        self.rb1.pack()
        self.rb2 = tkinter.Radiobutton(self.top_frame, text='Evening (6:00 P.M. through 11:59 P.M.)  Rate: $0.12', variable=self.radio, value=2)
        self.rb2.pack()
        self.rb3 = tkinter.Radiobutton(self.top_frame, text='Off-Peak (midnight through 5:59 P.M.)  Rate: $0.05', variable=self.radio, value=3)
        self.rb3.pack()

        self.prompt_min = tkinter.Label(self.top_frame, text='Enter minutes on call:')
        self.prompt_min.pack(pady=20, side='left')

        self.entry_min = tkinter.Entry(self.top_frame, width=10)
        self.entry_min.pack(pady=20, side='left')


        self.button = tkinter.Button(self.bottom_frame, text='Show Info', command=self.action1)
        self.button.pack(pady=20)

        self.gui_quit = tkinter.Button(self.bottom_frame, text='Quit', command=self.window.destroy)
        self.gui_quit.pack(pady=20)

        tkinter.mainloop()

    def action1(self):
        minutes = float(self.entry_min.get())
        if self.radio.get() == 1:
            cost = minutes * 0.02
        elif self.radio.get() == 2:
            cost = minutes * 0.12
        else:
            cost = minutes * 0.05
        tkinter.messagebox.showinfo('Cost for call', 'The cost for this call is $' + str(cost))
my_gui = GUI()