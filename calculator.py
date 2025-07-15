#import tkinter as tk
from tkinter import *

# Create a GUI interface
window = Tk()
window.geometry("450x300")
window.title("Jairaj")

#Add an input to the window

#ENTRY BOX
e = Entry(window, width=48, borderwidth=6)
e.place(x=0,y=0)

#BUTTONS
def click(num):
    result =e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

b = Button(window, text="1", width=12, command=lambda:click(1))
b.place(x=10,y=60)

b = Button(window, text="2", width=12, command=lambda:click(2))
b.place(x=150,y=60)

b = Button(window, text="3", width=12, command=lambda:click(3))
b.place(x=290,y=60)

b = Button(window, text="4", width=12, command=lambda:click(4))
b.place(x=10,y=100)

b = Button(window, text="5", width=12, command=lambda:click(5))
b.place(x=150,y=100)

b = Button(window, text="6", width=12, command=lambda:click(6))
b.place(x=290,y=100)

b = Button(window, text="7", width=12, command=lambda:click(7))
b.place(x=10,y=140)

b = Button(window, text="8", width=12, command=lambda:click(8))
b.place(x=150,y=140)

b = Button(window, text="9", width=12, command=lambda:click(9))
b.place(x=290,y=140)

b = Button(window, text="0", width=12, command=lambda:click(0))
b.place(x=150,y=180)

def add():
    n1 = e.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    e.delete(0, END)


b = Button(window, text="+", width=12, command= add)
b.place(x=10,y=180)

def subtract():
    n1 = e.get()
    global math
    math = "subtraction"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text="-", width=12, command= subtract)
b.place(x=290,y=180)

def multiply():
    n1 = e.get()
    global math
    math = "multiply"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text="*", width=12, command= multiply)
b.place(x=290,y=220)

def divide():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text="/", width=12, command= divide)
b.place(x=10,y=220)

def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, i + int(n2))
    elif math == "subtraction":
        e.insert(0, i - int(n2))
    elif math == "multiply":
        e.insert(0, i * int(n2))
    elif math == "division":
        e.insert(0, i / int(n2))
    
b = Button(window, text="=", width=12, command= equal)
b.place(x=150,y=260)

def clear():
    e.delete(0, END)

b = Button(window, text="Clear", width=12, command=lambda:clear())
b.place(x=150,y=220)

#Create a main loop 
window.mainloop()
