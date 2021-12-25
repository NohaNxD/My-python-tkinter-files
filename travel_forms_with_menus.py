from tkinter import *


root = Tk()

root.geometry("400x300")



root.title("travel form")


def save():
    with open("text/text1.txt","w") as f:
        pass

def save_as():
    pass

def copy():
    pass

def paste():
    pass
def travel():
    pass

mainmenu = Menu(root)

submenu = Menu(mainmenu , tearoff=0)
submenu.add_command(label="save" , command=save)
submenu.add_command(label="save as" , command=save_as)
submenu.add_separator()
submenu.add_command(label="copy" , command=copy)
submenu.add_command(label="paste" , command=paste)

mainmenu.add_cascade(label="file/edit", menu=submenu)

submenu2 = Menu(mainmenu,tearoff=0)
submenu2.add_command(label="kuchh bhi",command=travel)


mainmenu.add_cascade(label="lol",menu=submenu2)


root.config(menu=mainmenu)


Label(text="TRAVEL FORM" ,font="comicsans 34 bold").pack(pady=23,padx=50)
Label(text="Name", font="comicsans 16").pack(pady=80)






root.mainloop()