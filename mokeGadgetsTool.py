import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
from tkinter import filedialog
import matplotlib.pyplot as plt



class mokeCalculator(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('400x400')
        self.title("MOKE Calculator")
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.frames["StartPage"] = StartPage(parent=container, controller=self)
        self.frames["PageOne"] = PageOne(parent=container, controller=self)
        self.frames["PageTwo"] = PageTwo(parent=container, controller=self)

        self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageOne"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageTwo"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[page_name]
        frame.grid()
        frame.winfo_toplevel().geometry("")




class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frame = tk.Frame(self, width=400, height =400)
        frame.pack()
        label = tk.Label(self, text="Choose what do you want \n to calculate:", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label.place(x=50, y=20)

        button1 = tk.Button(self, text="Remanence", bg ='lightblue',
                            command=lambda: controller.show_frame("PageOne"))

        button2 = tk.Button(self, text="Coercivity", bg="lightcoral",
                            command=lambda: controller.show_frame("PageTwo"))

        button1.pack()
        button1.config(font=16)
        button1.place(x=145, y=125, height = 60)
        button2.pack()
        button2.config(font=16)
        button2.place(x=152, y=225, height = 60)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        frame = tk.Frame(self, width=400, height=400)
        frame.pack()
        labelx = tk.Label(self, text="Remanence", font=controller.title_font)
        labelx.pack(side="top", fill="x", pady=10)
        labelx.place(x=200, y=20)

        def calculateRemanence(maxRem, minRem, maxSat, minSat):

            rem = ((maxRem - minRem) / (maxSat - minSat)) * 100
            return rem

        def checkInput():
            entered_maxRem = maxRem_box.get()
            entered_minRem = minRem_box.get()
            entered_maxSat = maxSat_box.get()
            entered_minSat = minSat_box.get()

            try:
                maxRem = float(entered_maxRem)
            except ValueError:
                textbox['text'] = 'Incorrect value entered'
                return
            try:
                minRem = float(entered_minRem)
            except ValueError:
                textbox['text'] = 'Incorrect value entered'
                return
            try:
                maxSat = float(entered_maxSat)
            except ValueError:
                textbox['text'] = 'Incorrect value entered'
                return
            try:
                minSat = float(entered_minSat)
            except ValueError:
                textbox['text'] = 'Incorrect value entered'
                return

            finalRemanence = calculateRemanence(maxRem, minRem, maxSat, minSat)
            textbox['text'] = str(finalRemanence) + ' [%]'

        label = tk.Label(self, text='Maximum Remanence:')
        label.place(x=10, y=20, height=30)
        label.config(bg='lightblue', padx=0)

        maxRem_box = tk.Entry(self, text="")
        maxRem_box.place(x=10, y=60, width=100, height=30)

        label2 = tk.Label(self, text='Minimum Remanence:')
        label2.place(x=10, y=100, height=30)
        label2.config(bg='lightblue', padx=0)

        minRem_box = tk.Entry(self, text="")
        minRem_box.place(x=10, y=140, width=100, height=30)

        label3 = tk.Label(self, text='Maximum Saturation:')
        label3.place(x=10, y=180, height=30)
        label3.config(bg='lightblue', padx=0)

        maxSat_box = tk.Entry(self, text="")
        maxSat_box.place(x=10, y=220, width=100, height=30)

        label4 = tk.Label(self, text='Minimum Saturation:')
        label4.place(x=10, y=260, height=30)
        label4.config(bg='lightblue', padx=0)

        minSat_box = tk.Entry(self, text="")
        minSat_box.place(x=10, y=300, width=100, height=30)

        button = tk.Button(self, text='Calculate Remanence', command=checkInput)
        button.config(font='16')
        button.place(x=10, y=340, width=175, height=40)

        textbox = tk.Message(self, text="Calculated Remanence [%]:", width=200, font='16')
        textbox.config(bg='lightcoral', padx=0)
        textbox.place(x=200, y=250)

        button1 = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button1.place(x=250,y=350)

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        frame = tk.Frame(self, width=600, height=600)
        frame.pack()
        ### Menu
        menubar = tk.Menu(controller)

        menubar.add_command(label="PageTwo", command=lambda: controller.show_frame("PageTwo"))
        controller.config(menu=menubar)
        ### Page content
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()



if __name__ == "__main__":
    app = mokeCalculator()
    app.mainloop()