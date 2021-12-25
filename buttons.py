from tkinter import *
root = Tk()

def name():
    print("your name is :\nnaveen sinha")


def city():
    print("your city is :\nraipur")


def state():
    print("your state is :\nChhatisgarh")

def country():
    print("your country is :\nIndia")

root.title("button experiment")

root.geometry("720x400")
root.minsize(720,400)
root.maxsize(1280,720)

frame = Frame(root,bg = "red")
frame.pack(side=LEFT,anchor="nw")

b1 = Button(frame,text="printing the name",command=name)
b1.pack(side=LEFT,padx = 5)

b2 = Button(frame,text="printing the city",command=city)
b2.pack(side=LEFT,padx = 5)

b3 = Button(frame,text="printing the country",command=country)
b3.pack(side=LEFT,padx = 5)

b4 = Button(frame,text="printing the state",command=state)
b4.pack(side=LEFT,padx = 5)


root.mainloop()