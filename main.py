 #This is a Python Project Time clock
from tkinter import *
from tkinter.ttk import *  #Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit,

from time import strftime              # import time

value=Tk()                               #gui interface tk
value.title(" Time Clock ")                         #define a title
def time():                                            # function for catching time
    string = strftime('%H %M %S %p')
    label.config(text=string)
    label.after(1000,time)


label =  Label(value, font =("ds-digital",100), background= "black", foreground = "#c800ff")  # cloure for bg and font

label.pack(anchor='center')
time()
mainloop()