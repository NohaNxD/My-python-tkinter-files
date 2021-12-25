from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

# the area for creating functions 

def new():
    global file

    # creating a message to confirm if the user really wants to create a new file
    message_msg = msg.askquestion("file","do you want create a new file")



    # if the user said yes this command will be executed 
    if message_msg =="yes":
        root.title("untitled - Notepad")
        file = None
        text.delete(1.0,END)


    # if the user said no this command will be executed
    elif message_msg =="no":
        pass    



def Open():
    global file

    # importing files from other directory  
    # the default extension command is used to decide a default extension for the file which is to be opened 
    '''file type command is used to give user a option of which kind of file types he want to import'''


    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("text documents","*.txt")])

    # if the file is blank then the program will not execute anything 
    if file == "":
        file =  NONE



    # the root.title command changes the gui's title to the name of the file
    # the text.delete deletes the text which was written before the open function
    #  was executed and it will replace the text with the new file's text
    # then we will import the file as read mode and replace the previous text with the file's text

    else:
        root.title(os.path.basename(file)+" -  NotePad")
        text.delete(1.0,END)
        with open(file,"r") as f:
            text.insert(1.0,f.read())



def Save():
    global file

    # making a dialog box for saving the file 

    # this command is executed when the file is not got saved even one time 
    if file == None:

        # almost same as open function 
        # the initial file name command decides the default name for the file if the user doesn't choose one


        file = asksaveasfilename(initialfile='untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("text documents","*.txt")])
        

        # if the file is blank then the program will not execute anything 

        if file == "":
            file = None


        # this is the function to save the .txt file in our computer
        else:
            with open(file,"w") as f:
                f.write(text.get(1.0,END))


            # changing the root title to the name that was given by the user 
            root.title(os.path.basename(file) + "-  NotePad")




def Quit():

    # making the quit function you can exit app with it 


    root.destroy()

def cut():

    # this function cuts  the selected text 
    text.event_generate("<<Cut>>")


def copy():

    # this function copy's the selected text 
    text.event_generate("<<Copy>>")


def paste():

    # this function paste the copied text 
    text.event_generate("<<Paste>>")


def Help():
    msg.showinfo("help","this is notepad you can type in this notepad")



def about():
    msg.showinfo("about us","we created this notepad and we know it's not the best")



if __name__ == "__main__":

    # basic python tkinter startup

    root = Tk()

    root.title("untitled - Notepad")

    root.geometry("644x788")



    # creating text area 

    text = Text(root,font="comicsans 12")

    text.pack(fill=BOTH,expand=True)

    f = None



    # adding scrollbar to our notepad 

    scroll = Scrollbar(text)
    scroll.pack(fill=Y,side=RIGHT)
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)


    # creating menu 
    M1 = Menu(root)

    # a file menu 

    file = Menu(M1,tearoff=0)

    file.add_command(label="New",command=new)
    file.add_command(label="Open",command=Open)
    file.add_command(label="Save",command=Save)
    file.add_separator()
    file.add_command(label="Quit",command=Quit)
    

    # creating a edit menu 
    edit = Menu(M1,tearoff=0)
    edit.add_command(label="Cut",command=cut)
    edit.add_command(label="Copy",command=copy)
    edit.add_command(label="Paste",command=paste)




    # creating a help menu 

    help = Menu(M1,tearoff=0)
    help.add_command(label="Help",command=Help)
   
    

    # creating about us menu 


    About_us = Menu(M1,tearoff=0)
    About_us.add_command(label="ABOUT",command=about)
    

    M1.add_cascade(label="File",menu=file)
    M1.add_cascade(label="Edit",menu=edit)
    M1.add_cascade(label="Help",menu=help)
    M1.add_cascade(label="About Us",menu=About_us)

    # created menu 






    # configuring the root to add our variable as it's menu 

    root.config(menu=M1)



    # running the python program through the mainloop command in tkinter 



    root.mainloop()