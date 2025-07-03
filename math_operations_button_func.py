from tkinter import *
from settings import init
import math
from tkinter import messagebox as mb

NAME = 'math_operations_button_func'


def digit_func(a):
    if a.count('.') == 1:
        x = a.replace('.', '')
        if x.isdigit():
            return True
        else:
            return False


def sinus_button():
    txt = init.e.get()
    if txt.isdigit() or digit_func(txt):
        init.e.delete(0, END)
        init.e.insert(0, math.sin(float(txt)))
    else:
        mb.showerror(title='ERROR', message='ERROR')


def cosinus_button():
    txt = init.e.get()
    if txt.isdigit() or digit_func(txt):
        init.e.delete(0, END)
        init.e.insert(0, math.cos(float(txt)))
    else:
        mb.showerror(title='ERROR', message='ERROR')


def tangens_button():
    txt = init.e.get()
    if txt.isdigit() or digit_func(txt):
        init.e.delete(0, END)
        init.e.insert(0, math.tan(float(txt)))
    else:
        mb.showerror(title='ERROR', message='ERROR')


def lg_button():
    txt = init.e.get()
    if txt.isdigit() or digit_func(txt):
        init.e.delete(0, END)
        init.e.insert(0, math.log10(float(txt)))
    else:
        mb.showerror(title='ERROR', message='ERROR')


def ln_button():
    txt = init.e.get()
    if txt.isdigit() or digit_func(txt):
        init.e.delete(0, END)
        init.e.insert(0, math.log(float(txt)))
    else:
        mb.showerror(title='ERROR', message='ERROR')


def factorial_button():
    txt = init.e.get()
    init.e.delete(0, END)
    if txt.isdigit():
        init.e.insert(0, math.factorial(int(txt)))
