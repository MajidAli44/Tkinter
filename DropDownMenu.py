from tkinter import *

root = Tk()
root.title("Drop Down Menu")
root.iconbitmap("C:\\Users\\majid\\OneDrive\\Pictures\\Random\\Sun.ico")
root.geometry("400x400")


def show():
    label = Label(root, text=clicked.get())
    label.pack()

option = [
    " Majid ",
    " Nabiya ",
    " Nudrat ",
    " Haroon ",
    " Ibrahim "
]

clicked = StringVar()
clicked.set(option[0])



drop = OptionMenu(root, clicked, *option)
drop.pack()

byn = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
