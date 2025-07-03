from settings import init
from tkinter import *

NAME='operation_button_func'

def ravno_button():
    st = init.e.get()
    res=eval(st)
    init.e.delete(0, END)
    init.e.insert(0, res)

def plus_button():
    init.e.insert(END, '+')

def minus_button():
    init.e.insert(END, '-')

def umn_button():
    init.e.insert(END, '*')

def razd_button():
    init.e.insert(END, '/')

def dot_button():
    init.e.insert(END, '.')

def del_button():
    init.e.delete(0, END)