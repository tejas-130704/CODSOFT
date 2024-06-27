import random
import string
from tkinter import *
import pyperclip as pc

res=0
root = Tk()
root.title("Password Generator")
label1=Label(root,font=(21),width=15,wraplength=150)
display=Entry(root,width=15,bd=2,font=("Arial 15"))

def PassGenerator():
    global res
    try:
        len=int(display.get())
        res = ''.join(random.choices(string.ascii_uppercase + string.digits,k=len))
        label1["text"]=res
    except:
        label1["text"]="Error"

def Copy():
    global res
    pc.copy(res)
    Label(root,text="Copied!").grid(row=6,column=2)

Copy=Button(root,text="Copy",command=Copy).grid(row=6,column=1)
click=Button(root,text="Generate",command=PassGenerator)
Label(root,text="").grid(row=0,columnspan=4)
Label(root,text="").grid(row=2,columnspan=4)
Label(root,text="").grid(row=5,columnspan=4)
Label(root,text="").grid(column=0)
Label(root,text="").grid(column=3)
display.grid(row=1,column=1)
label1.grid(row=4,column=1)
# display.insert(0,"Length")
click.grid(row=1,column=2)

root.mainloop()

    