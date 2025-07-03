from tkinter import *
import numpy as np
from sklearn.linear_model import LinearRegression
from tkinter import messagebox as mb
from settings import init


NAME = 'stat_button_func'

def stat_button():
    def regression_button():
        x_stat = list(map(float, e1.get().split()))
        y_stat = list(map(float, e2.get().split()))

        x = np.array(x_stat).reshape((-1, 1))
        y = np.array(y_stat)

        model = LinearRegression().fit(x, y)
        R = model.score(x, y)
        b0 = float(model.intercept_)
        b1 = float(model.coef_)
        mb.showinfo(title='Result Regression',
                    message=f'regression coefficient: {R}, Equation: y = {b0} + ({b1})*x')

    init.root.destroy()
    new_window = Tk()
    new_window.title('Regression calc')
    new_window.geometry('300x300')
    e1 = Entry(new_window, width=1300)
    e1.place(x=5, y=100)
    e2 = Entry(new_window, width=1300)
    e2.place(x=5, y=200)
    btn = Button(new_window, text='Start',

                 fg='black', command=regression_button)
    btn.place(x=130, y=250, width=40, height=30)
    Label(text='x').place(x=150, y=70)
    Label(text='f(x)').place(x=150, y=170)

    new_window.mainloop()