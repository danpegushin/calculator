import numpy as np
from settings import init
from tkinter import *
from tkinter import messagebox as mb

NAME = 'matrix_button_func'


def matrix_button():
    def mmm():
        txt = e6.get('1.0', 'end').strip()
        txt = txt.replace('\n', ';')
        A = np.matrix(txt)
        mb.showinfo(title='Answer', message=f'det A = {np.linalg.det(A)}')

    init.root.destroy()
    new_window = Tk()
    new_window.title('det matrix')
    new_window.geometry('300x300')

    btn = Button(new_window, text='Start',

                 fg='black', command=mmm)
    btn.place(x=120, y=270, width=60)

    e6 = Text(new_window)
    e6.place(x=100, y=100, width=100, height=100)

    Label(new_window, text='(').place(x=90, y=100, width=5, height=100)
    Label(new_window, text=')').place(x=205, y=100, width=5, height=100)
    Label(new_window, text='A = ').place(x=45, y=140, width=40)

    new_window.mainloop()
