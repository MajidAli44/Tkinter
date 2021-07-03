from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("CheckBox")
root.iconbitmap("C:\\Users\\majid\\OneDrive\\Pictures\\Random\\Sun.ico")
root.geometry("400x400")

def show():
    label = Label(root, text=var.get()).pack()


var=StringVar()



c=Checkbutton(root, text="Check this box, i dare you!", variable=var,onvalue="On",offvalue="Off")
c.deselect()
c.pack()


btn=Button(root, text="See Selection", command=show).pack()

root.mainloop()