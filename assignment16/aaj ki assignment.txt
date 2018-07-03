
#q1
from tkinter import *
import sys
root = Tk()
root.title("Hello World")
w = Label(None)
w.config(text="First tkinter....")
w.pack()
b = Button(None,text="Exit",command=sys.exit)
b.pack()
#mainloop()

#q2

def func():
    print("Button clicked...")
widget = Button(None,text="Hello GUI World",command=func)
widget.pack(side=BOTTOM,expand = YES,fill=Y)
#widget.mainloop()

#q3
import sys
root = Tk()
fr = Frame()
fr.pack()
lbl = Label(fr,text="This is sample text")
lbl.pack(side=TOP)
def display():
    global lbl
    lbl.config(text="Text Changed...")
btn1 = Button(fr,text="Change Text",command=display)
btn1.pack(side=LEFT,expand=YES,fill=Y)
btn2 = Button(fr,text="Quit",command=sys.exit)
btn2.pack(side=RIGHT,expand=YES,fill=Y)
btn2.mainloop()

#q4

fr = Frame()
fr.pack()
ent = Entry(fr)
ent.pack(side=TOP)
ent.insert(0,"type here...")

#ent.config(state='disabled')
ent.focus()

def display():
    print("This is the input:",ent.get())
widget = Button(fr,text="Hello GUI World",command=display)
widget.pack(side=LEFT,expand=YES,fill=Y)
widget.mainloop()