from settings import init
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import math

NAME = 'functions_button_func'

def functions_button():
    def fff():
        x_s = float(e4.get())
        x_e = float(e5.get())
        eqn = e3.get()
        y_list = []
        x_list = np.linspace(x_s, x_e, 201)
        for x in range(len(x_list)):
            eqn_list = list(eqn)
            for i in range(0, len(eqn_list)):
                if eqn_list[i] == 'x':
                    eqn_list[i] = str(x_list[x])
            y = ''.join(eqn_list)
            y_list.append(eval(y))
        plt.grid()
        plt.plot(x_list, y_list)
        plt.show()

    init.root.destroy()
    new_window = Tk()
    new_window.title('Functions plot')
    new_window.geometry('300x300')

    e3 = Entry(new_window, width=150)
    e3.place(x=20, y=150, width=260, height=40)

    btn = Button(new_window, text='Start',

                 fg='black', command=fff)
    btn.place(x=130, y=270, width=40, height=20)

    Label(new_window, text='f(x)').place(x=140, y=135, width=20, height=15)

    e4 = Entry(new_window, width=150)
    e4.place(x=80, y=50, width=40, height=20)

    e5 = Entry(new_window, width=150)
    e5.place(x=180, y=50, width=40, height=20)

    Label(new_window, text='start x').place(x=80, y=25, width=40)
    Label(new_window, text='end x').place(x=180, y=25, width=40)
    Label(new_window, text='use syntaxis math module!').place(x=70, y=200, width=160)

    new_window.mainloop()