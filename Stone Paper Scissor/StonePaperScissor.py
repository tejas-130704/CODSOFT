from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox
root = Tk()
root.title("Rock Paper Scissors")
prev=4
# Load images
stone_img = ImageTk.PhotoImage(Image.open('stone.png').resize((50, 50)))
paper_img = ImageTk.PhotoImage(Image.open('paper.png').resize((50, 50)))
scissor_img = ImageTk.PhotoImage(Image.open('scissor.png').resize((50, 50)))

# Labels and buttons setup
Label(root, text="").grid(row=0, columnspan=5)
Label(root, text="").grid(row=3, columnspan=5)
Label(root, text="").grid(row=5, columnspan=5)
Label(root, text="\t").grid(column=4)
Label(root, text="\t").grid(column=0)

Label(root, text="PLAYER\t").grid(column=1, row=1)
Label(root, text="CPU").grid(column=3, row=1)
Label(root, text="VS").grid(column=2, row=2)
result=Label(root,anchor='center',justify='center')

def CPUTurn():
    global prev 
    lst = [0, 1, 2]
    item = random.choice(lst)
    # if prev==item :
    #     item=(item+1)%3
    
    cpu_choice_label.config(image=get_image(item))
    # prev=item
    return item

    
def MsgBox():
    global root
    top=Toplevel(root)
    Label(top,text="").grid(row=0,columnspan=4)
    Label(top,text="\t").grid(column=4)
    Label(top,text="\t").grid(column=0)
    Label(top,text="\t").grid(column=2)
    Label(top,text="\n\n").grid(row=4)
    Label(top,text="Do you want to?\n").grid(row=2,column=1,columnspan=3)
    Button(top,text="Play Again",command=top.destroy).grid(row=3,column=1)
    Button(top,text="Exit",command=root.quit).grid(row=3,column=3)
    
    # messagebox.showinfo(title='RockPaperScissor',message="")

def SelectedItem(item):
    player_choice_label.config(image=get_image(item))
    ch=CPUTurn()
    WinnerChoice(item,ch)
    MsgBox()

def get_image(item1):

    if item1 == 0:
        return stone_img
    elif item1 == 1:
        return paper_img
    elif item1 == 2:
        return scissor_img
    
def WinnerChoice(item1,item):
    if item1==item:
        result.config(text="Draw!!")
    elif item1==1 and item==0:
        result.config(text="Tejas is Winner!!")
    elif item1==0 and item==1:
        result.config(text="CPU is Winner!!")
    elif item1==0 and item==2:
        result.config(text="Tejas is Winner!!")
    elif item1==2 and item==0:
        result.config(text="CPU is Winner!!")
    elif item1==1 and item==2:
        result.config(text="CPU is Winner!!")
    elif item1==2 and item==1:
        result.config(text="Tejas is Winner!!")
    else:
        result.config(text="Pending...")
    
    result.grid(row=6,column=1,columnspan=3)

    

# Player choice buttons
Button(root, text="Stone", padx=6, pady=3, command=lambda: SelectedItem(0)).grid(column=1, row=4)
Button(root, text="Paper", padx=6, pady=3, command=lambda: SelectedItem(1)).grid(column=2, row=4)
Button(root, text="Scissor", padx=6, pady=3, command=lambda: SelectedItem(2)).grid(column=3, row=4)

# Labels to show choices
player_choice_label = Label(root)
player_choice_label.grid(row=2, column=1)

cpu_choice_label = Label(root)
cpu_choice_label.grid(row=2, column=3)

root.mainloop()
