from tkinter import *
# from tkinter.font import tkFont


expression=""
root=Tk()
root.title("Calculator")
display=Entry(root,width=15,bd=6,font=("Arial 25"))
# display=Entry(root)
root.geometry('285x287')
display.grid(row=0,columnspan=5)

def ButtonDisplay(exp):
    global display
    global expression
    expression+=exp
    display.insert(END, exp)  # Use 'end' to append the new character

def Calculate():
    global display
    global expression
    try:
        result=eval(expression)
        expression=str(result)
    except:
        result="Error"
    display.delete(0,END)
    display.insert(END, result)

def ClearDisplay():
    global display
    global expression
    expression=""
    display.delete(0,END)
    
#First Row
button1 =Button(root, text="1", width=6, height=2, font=(20), padx=0, pady=0, borderwidth=1, command=lambda: ButtonDisplay("1"))
button2=Button(root,text="2",width=6,height=2,font=(20),padx=0,pady=0,borderwidth=1, command=lambda: ButtonDisplay("2"))
button3=Button(root,text="3",width=6,height=2,font=(20),padx=0,pady=0,borderwidth=1, command=lambda: ButtonDisplay("3"))
button4=Button(root,text="+",width=6,height=2,font=(20),padx=0,pady=0,borderwidth=1, command=lambda: ButtonDisplay("+"))

button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=1,column=3)

#Second Row
button5=Button(root,text="4",width=6,height=2,font=(20),padx=0,pady=0,borderwidth=1, command=lambda: ButtonDisplay("4"))
button6=Button(root,text="5",width=6,height=2,font=(20),padx=0,pady=0,borderwidth=1, command=lambda: ButtonDisplay("5"))
button7=Button(root,text="6",width=6,height=2,font=(20),padx=0,pady=0,borderwidth=1, command=lambda: ButtonDisplay("6"))
button8=Button(root,text="-",width=6,height=2,font=(20),padx=0,pady=0,borderwidth=1, command=lambda: ButtonDisplay("-"))

button5.grid(row=2,column=0)
button6.grid(row=2,column=1)
button7.grid(row=2,column=2)
button8.grid(row=2,column=3)

#Third Row
button9=Button(root,text="7",width=6,height=2,font=(20),padx=0,pady=0,borderwidth=1, command=lambda: ButtonDisplay("7"))
button10=Button(root,text="8",width=6,height=2,font=(20),padx=0,pady=0,borderwidth=1, command=lambda: ButtonDisplay("8"))
button11=Button(root,text="9",width=6,height=2,font=(20),padx=0,pady=0,borderwidth=1, command=lambda: ButtonDisplay("9"))
button12=Button(root,text="X",width=6,height=2,font=(20),padx=0,pady=0,borderwidth=1, command=lambda: ButtonDisplay("*"))

button9.grid(row=3,column=0)
button10.grid(row=3,column=1)
button11.grid(row=3,column=2)
button12.grid(row=3,column=3)


#Forth Row
button13=Button(root,text="C",width=6,height=2,font=(20),padx=0,pady=0,borderwidth=1,command=ClearDisplay)
button14=Button(root,text="0",width=6,height=2,font=(20),padx=0,pady=0,borderwidth=1, command=lambda: ButtonDisplay("0"))
button15=Button(root,text="/",width=6,height=2,font=(20),padx=0,pady=0,borderwidth=1, command=lambda: ButtonDisplay("/"))
button16=Button(root,text="Ans",width=6,height=2,font=(20),padx=0,pady=0,borderwidth=1,bg="#FFFF2E", command=Calculate)

button13.grid(row=4,column=0)
button14.grid(row=4,column=1)
button15.grid(row=4,column=2)
button16.grid(row=4,column=3)



root.mainloop()