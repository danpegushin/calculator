# calculator
from tkinter import *
from tkinter import messagebox as mb
from simple_button_func import *
from info_button_func import info_button
from close_button_func import close_button
from settings import init
from stat_button_func import stat_button
from eq_button_func import eq_button
from functions_button_func import functions_button
from operation_button_func import *
from math_operations_button_func import *
from matrix_button_func import matrix_button

# drawing window
init.root = Tk()
init.root.title('Engineer calculator')
init.root.geometry('500x500')

# buttons

btn = Button(init.root, text="1",

             fg="black", bg='#BBFFFF', command=simple_button1)
btn.place(x=100, y=250, width=70, height=70)

btn = Button(init.root, text="sin",

             fg="black", command=sinus_button)
btn.place(x=5, y=250, width=90, height=70)

btn = Button(init.root, text="2",

             fg="black", bg='#BBFFFF', command=simple_button2)
btn.place(x=170, y=250, width=70, height=70)
btn = Button(init.root, text="3",

             fg="black", bg='#BBFFFF', command=simple_button3)
btn.place(x=240, y=250, width=70, height=70)

btn = Button(init.root, text="0",

             fg="black", bg='#BBFFFF', command=simple_button0)
btn.place(x=310, y=250, width=70, height=70)

btn = Button(init.root, text="4",

             fg="black", bg='#BBFFFF', command=simple_button4)
btn.place(x=100, y=320, width=70, height=70)

btn = Button(init.root, text="cos",

             fg="black", command=cosinus_button)
btn.place(x=5, y=320, width=90, height=70)

btn = Button(init.root, text="5",

             fg="black", bg='#BBFFFF', command=simple_button5)
btn.place(x=170, y=320, width=70, height=70)

btn = Button(init.root, text="6",

             fg="black", bg='#BBFFFF', command=simple_button6)
btn.place(x=240, y=320, width=70, height=70)

btn = Button(init.root, text=".",

             fg="black", bg='#BBFFFF', command=dot_button)
btn.place(x=310, y=320, width=70, height=70)

btn = Button(init.root, text="7",

             fg="black", bg='#BBFFFF', command=simple_button7)
btn.place(x=100, y=390, width=70, height=70)

btn = Button(init.root, text="tan",

             fg="black", command=tangens_button)
btn.place(x=5, y=390, width=90, height=70)

btn = Button(init.root, text="8",

             fg="black", bg='#BBFFFF', command=simple_button8)
btn.place(x=170, y=390, width=70, height=70)

btn = Button(init.root, text="9",

             fg="black", bg='#BBFFFF', command=simple_button9)
btn.place(x=240, y=390, width=70, height=70)

btn = Button(init.root, text="del",

             fg="black", bg='#BBFFFF', command=del_button)
btn.place(x=310, y=390, width=70, height=70)

btn = Button(init.root, text="=",

             fg="black", command=ravno_button)
btn.place(x=385, y=390, width=110, height=70)

btn = Button(init.root, text="+",

             fg="black", command=plus_button)
btn.place(x=385, y=250, width=55, height=70)

btn = Button(init.root, text="-",

             fg="black", command=minus_button)
btn.place(x=385, y=320, width=55, height=70)

btn = Button(init.root, text="x",

             fg="black", command=umn_button)
btn.place(x=440, y=250, width=55, height=70)

btn = Button(init.root, text="/",

             fg="black", command=razd_button)
btn.place(x=440, y=320, width=55, height=70)

btn = Button(init.root, text="lg",

             fg="black", command=lg_button)
btn.place(x=5, y=200, width=90, height=45)

btn = Button(init.root, text="ln",

             fg="black", command=ln_button)
btn.place(x=95, y=200, width=90, height=45)

btn = Button(init.root, text="!",

             fg="black", command=factorial_button)
btn.place(x=185, y=200, width=90, height=45)

btn = Button(init.root, text="info",

             fg="black", command=info_button)
btn.place(x=275, y=200, width=90, height=45)

btn = Button(init.root, text="close",

             fg="black", bg='red', command=close_button)
btn.place(x=365, y=200, width=130, height=45)

btn = Button(text='equation',

             fg='black', command=eq_button)
btn.place(x=5, y=85, width=125, height=50)

btn = Button(text='stat',

             fg='black', command=stat_button)
btn.place(x=130, y=85, width=125, height=50)

btn = Button(text='functions',

             fg='black', command=functions_button)
btn.place(x=255, y=85, width=125, height=50)

btn = Button(text='matrix',

             fg='black', command=matrix_button)
btn.place(x=380, y=85, width=115, height=50)

# entry window
init.e = Entry(init.root, width=1500)
init.e.place(x=0, y=150)

# Text
Label(text='Python calculator').place(x=5, y=25, width=500, height=20)

init.root.mainloop()
