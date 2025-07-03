from scipy.optimize import fsolve
from tkinter import *
from settings import init
from tkinter import messagebox as mb

NAME = 'eq_button_func'

def eq_button():
    def eq_schet_button():
        s0 = float(a0.get())
        s1 = float(a1.get())
        s2 = float(a2.get())
        s3 = float(a3.get())
        s4 = float(a4.get())
        s5 = float(a5.get())
        x0 = float(x_p.get())

        def function(x):
            nonlocal s0, s1, s2, s3, s4, s5
            return s5 * x ** 5 + s4 * x ** 4 + s3 * x ** 3 + s2 * x ** 2 + s1 * x + s0

        res = fsolve(function, x0)
        mb.showinfo(title='Answer', message=f'x = {float(res)}')

    init.root.destroy()
    new_new_window = Tk()
    new_new_window.title('Equation')
    new_new_window.geometry('400x400')
    a5 = Entry(new_new_window, width=20)
    a5.place(x=100, y=150, width=35)
    a4 = Entry(new_new_window, width=20)
    a4.place(x=100, y=180, width=34)
    a3 = Entry(new_new_window, width=20)
    a3.place(x=100, y=210, width=34)
    a2 = Entry(new_new_window, width=20)
    a2.place(x=100, y=240, width=34)
    a1 = Entry(new_new_window, width=20)
    a1.place(x=100, y=270, width=34)
    a0 = Entry(new_new_window, width=20)
    a0.place(x=100, y=300, width=35)
    Label(new_new_window, text='Equation').place(x=150, y=5, width=100)
    Label(new_new_window, text='A').place(x=150, y=150)
    Label(new_new_window, text='B').place(x=150, y=180)
    Label(new_new_window, text='C').place(x=150, y=210)
    Label(new_new_window, text='D').place(x=150, y=240)
    Label(new_new_window, text='E').place(x=150, y=270)
    Label(new_new_window, text='F').place(x=150, y=300)

    Label(new_new_window, text='A*x^5 + B*x^4 + C*x^3 + D*x^2 + E*x + F = 0').place(x=75, y=100, width=250)
    btn = Button(new_new_window, text='Start',

                 fg='black', command=eq_schet_button)
    btn.place(x=270, y=225, width=100)
    Label(new_new_window, text='Predict answer:').place(x=100, y=330)
    x_p = Entry(new_new_window)
    x_p.place(x=190, y=330, width=50)

    new_new_window.mainloop()