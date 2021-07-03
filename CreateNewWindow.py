from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Creating New Window")
root.iconbitmap("C:\\Users\\majid\\OneDrive\\Pictures\\Random\\Sun.ico")

def open():
    global image
    top = Toplevel()
    top.title("New Window")
    top.iconbitmap("C:\\Users\\majid\\OneDrive\\Pictures\\Random\\Sun.ico")
    label = Label(top, text="Majid Ali").pack(anchor=W)

    image = ImageTk.PhotoImage(Image.open("D:\\Python\\Lambo.png"))
    mylabel = Label(top, image=image).pack()
    btn=Button(top,text="Exit", command=top.destroy).pack()


btn=Button(root, text="Next Window", command=open).pack()

root.mainloop()