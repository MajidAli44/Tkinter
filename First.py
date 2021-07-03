from tkinter import *

root = Tk()

# Creating a Label Widget
# myLabel = Label(root, text="Majid Ali!")

# Showing it onto the Screen
# myLabel.pack()

# root.mainloop()


# 1) Positioning with Tkinter's Grid System

# myLabel1 = Label(root, text="Majid Ali!")
# myLabel2=Label(root,text="UOG-University of Gujrat!")
# myLabel3=Label(root,text="          ")

# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1,column=0)
# myLabel2.grid(row=1,column=1)
# myLabel2.grid(row=1,column=5)
# myLabel3.grid(row=1,column=1)


# myLabel1 = Label(root, text="Majid Akbar").grid(row=0,column=0)
# myLabel2=Label(root,text="University of Gujrat!").grid(row=1,column=1)
# root.mainloop()


# 2) Creating Button

# def click():
#     MyLabel=Label(root, text="Majid Akbar")
#     MyLabel.pack()
#
# MyButton=Button(root,text="Click Me!",padx=20,pady=10, command=click, fg="blue",bg="pink")
# MyButton.pack()
#
# root.mainloop()



# 3) Creating Input Field's

e=Entry(root, width=30, borderwidth=5)
e.pack()
e.insert(0,"Enter your name! ")

def click():

    Text="Hi! " + e.get()
    myLabel=Label(root, text=Text)
    myLabel.pack()

myButton=Button(root,text="Enter Name!", command=click)
myButton.pack()

root.mainloop()


# 34:00