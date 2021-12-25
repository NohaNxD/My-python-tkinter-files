from tkinter import *
root = Tk()


# the area to make functions for the code and execute

def click(event):



    # taking the text of the button and using to do the calculation
    text = event.widget.cget("text")
    if text == "=":
        if cals.get().isdigit():
            equal = int(cals.get())
        else:
            try:
                equal = eval(main.get())


            except Exception as e:
                equal="ERROR"

        cals.set(equal)    
        main.update()

        with open("calculator_values.txt","a") as f:
            f.write("\n"+str(cals.get()))
            
        


    elif text == "C":
        cals.set("")
        main.update

    else:
        cals.set(cals.get()+text)
        main.update()












# the code for title and icon and the size of the window
root.title("calculator")
root.geometry("433x400")
root.wm_iconbitmap("a new start/icon.ico")



# our main frame and entry code 

cals = StringVar()
cals.set("")




# making the screen which will show the number and their calculation
main = Entry(textvariable=cals,font="comicsans 20 bold")
main.pack(fill=X,padx=10,pady=4)


# The first frame which contains the number 987

f1=Frame(root,bg="grey")





# making all the buttons of this frame 

b=Button(f1,text="9",font="comicsans 10 bold")
b.pack(ipadx=10,ipady=5,padx=10,pady=4,side=LEFT)
b.bind("<Button-1>",click)


b=Button(f1,text="8",font="comicsans 10 bold")
b.pack(ipadx=10,ipady=5,padx=10,pady=4,side=LEFT)
b.bind("<Button-1>",click)




b=Button(f1,text="7",font="comicsans 10 bold")
b.pack(ipadx=10,ipady=5,padx=10,pady=4,side=LEFT)
b.bind("<Button-1>",click)

f1.pack(pady=10)


# End of the first frame 







# The second frame which contains the number 654


f1=Frame(root,bg="grey")




# making all the buttons of this frame 

b=Button(f1,text="6",font="comicsans 10 bold")
b.pack(ipadx=10,ipady=5,padx=10,pady=4,side=LEFT)
b.bind("<Button-1>",click)



b=Button(f1,text="5",font="comicsans 10 bold")
b.pack(ipadx=10,ipady=5,padx=10,pady=4,side=LEFT)
b.bind("<Button-1>",click)




b=Button(f1,text="4",font="comicsans 10 bold")
b.pack(ipadx=10,ipady=5,padx=10,pady=4,side=LEFT)
b.bind("<Button-1>",click)

f1.pack(pady=10)

# The end of the second frame 







# the third frame which contains the number 321


f1=Frame(root,bg="grey")





# making all the buttons of this frame 



b=Button(f1,text="3",font="comicsans 10 bold")
b.pack(ipadx=10,ipady=5,padx=10,pady=4,side=LEFT)
b.bind("<Button-1>",click)



b=Button(f1,text="2",font="comicsans 10 bold")
b.pack(ipadx=10,ipady=5,padx=10,pady=4,side=LEFT)
b.bind("<Button-1>",click)




b=Button(f1,text="1",font="comicsans 10 bold")
b.pack(ipadx=10,ipady=5,padx=10,pady=4,side=LEFT)
b.bind("<Button-1>",click)

f1.pack(pady=10)


# the end of the third frame 







# the 4th frame which contains * / 0


f1=Frame(root,bg="grey")






# making all the buttons of this frame 



b=Button(f1,text="*",font="comicsans 10 bold")
b.pack(ipadx=10,ipady=5,padx=11,pady=4,side=LEFT)
b.bind("<Button-1>",click)



b=Button(f1,text="0",font="comicsans 10 bold")
b.pack(ipadx=10,ipady=5,padx=11,pady=4,side=LEFT)
b.bind("<Button-1>",click)




b=Button(f1,text="/",font="comicsans 10 bold")
b.pack(ipadx=10,ipady=5,padx=11,pady=4,side=LEFT)
b.bind("<Button-1>",click)

f1.pack(pady=10)


# the end of the 4th frame 





# the beginning of the = frame 
f1=Frame(root,bg="grey")




# making all the buttons of this frame 
b=Button(f1,text="-",font="comicsans 12 bold")
b.pack(ipadx=10,ipady=5,padx=11,pady=4,side=LEFT)
b.bind("<Button-1>",click)


b=Button(f1,text="C",font="comicsans 12 bold")
b.pack(ipadx=10,ipady=5,padx=11,pady=4,side=LEFT)
b.bind("<Button-1>",click)

b=Button(f1,text="=",font="comicsans 12 bold")
b.pack(ipadx=10,ipady=5,padx=11,pady=4,side=LEFT)
b.bind("<Button-1>",click)

b=Button(f1,text="+",font="comicsans 12 bold")
b.pack(ipadx=10,ipady=5,padx=11,pady=4,side=LEFT)
b.bind("<Button-1>",click)


b=Button(f1,text="%",font="comicsans 12 bold")
b.pack(ipadx=10,ipady=5,padx=11,pady=4,side=LEFT)
b.bind("<Button-1>",click)





f1.pack(pady=10)

# the end of the = frame 





# executing the code with mainloop command 
root.mainloop()