import tkinter


# importing tkinter
from tkinter import *





# importing message box from tkinter
import tkinter.messagebox as msg 



# making the root of the gui application
root = Tk()



# making function for about us menu
def about_us():
    msg.showinfo("about us" ,"we are the god of this application you don't need to know anything else")
 

# making function for help menu
def help():


    # making a yes no msg box
    yes_no = msg.askquestion("questions you want to ask" , "do you want to know how to copy paste")




    # making if else ladder for yes no msg box
    if yes_no=="yes":
        msg.showinfo("copy paste","for copy you need to press ctrl+c in you keyboard and for paste you need to press ctrl+v in your keyboard")
    else:
        m =msg.askquestion("about us" ,"do you want to know about us")
    if m =="yes":
        msg.showinfo("about us",about_us())
    else:
        print(" ")


# deciding the size of the gui application
root.geometry("600x700")

root.minsize(600,700)

root.title("message box")


# creating the main menu
main = Menu(root)




# adding menu's option in the main menu
main.add_cascade(label="help" , command=help)
main.add_cascade(label="about us" ,command=about_us)



# configuring root to make menu of the root our variable
root.config(menu=main)




# one of the main function to run the gui application of the tkinter
root.mainloop()