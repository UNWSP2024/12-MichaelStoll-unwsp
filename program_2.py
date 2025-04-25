#title:auto repair
#author: michael stoll
#date:4/25/2025
import tkinter
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

        self.cb1 = tkinter.IntVar()
        self.cb1.set(0)
        self.cb2 = tkinter.IntVar()
        self.cb2.set(0)
        self.cb3 = tkinter.IntVar()
        self.cb3.set(0)
        self.cb4 = tkinter.IntVar()
        self.cb4.set(0)
        self.cb5 = tkinter.IntVar()
        self.cb5.set(0)
        self.cb6 = tkinter.IntVar()
        self.cb6.set(0)
        self.cb7 = tkinter.IntVar()
        self.cb7.set(0)

        self.box1 = tkinter.Checkbutton(self.top_frame, text='Oil Change - $30.00', variable=self.cb1)
        self.box1.pack(side='left')
        self.box2 = tkinter.Checkbutton(self.top_frame, text='Lube Job - $20.00', variable=self.cb2)
        self.box2.pack(side='left')
        self.box3 = tkinter.Checkbutton(self.top_frame, text='Radiator Flush - $40.00', variable=self.cb3)
        self.box3.pack(side='left')
        self.box4 = tkinter.Checkbutton(self.top_frame, text='Transmission Fluid - $100.00', variable=self.cb4)
        self.box4.pack(side='left')
        self.box5 = tkinter.Checkbutton(self.top_frame, text='Inspection - $35.00', variable=self.cb5)
        self.box5.pack(side='left')
        self.box6 = tkinter.Checkbutton(self.top_frame, text='Muffler replacement - $200.00', variable=self.cb6)
        self.box6.pack(side='left')
        self.box7 = tkinter.Checkbutton(self.top_frame, text='Tire Rotation - $20.00', variable=self.cb7)
        self.box7.pack(side='left')

        self.total_descr = tkinter.Label(self.middle_frame, text='The repairs will cost $')
        self.total_descr.pack(side='left')

        self.total = tkinter.StringVar()
        self.cost_label = tkinter.Label(self.middle_frame, textvariable=self.total)
        self.cost_label.pack(side='left')

        self.button = tkinter.Button(self.bottom_frame, text='Show Total', command=self.action1)
        self.button.pack(pady=20, side='left')

        self.gui_quit = tkinter.Button(self.bottom_frame, text='Quit', command=self.window.destroy)
        self.gui_quit.pack(pady=20, side='left')

        tkinter.mainloop()
        self.total_cost = 0
    def action1(self):
        self.total_cost = 0
        if self.cb1.get() == 1:
            self.total_cost += 30
        if self.cb2.get() == 1:
            self.total_cost += 20
        if self.cb3.get() == 1:
            self.total_cost += 40
        if self.cb4.get() == 1:
            self.total_cost += 100
        if self.cb5.get() == 1:
            self.total_cost += 35
        if self.cb6.get() == 1:
            self.total_cost += 200
        if self.cb7.get() == 1:
            self.total_cost += 20
        self.total.set(str(self.total_cost))


my_gui = GUI()