from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Sliders")
root.iconbitmap("C:\\Users\\majid\\OneDrive\\Pictures\\Random\\Sun.ico")
root.geometry("400x400")

def slides(var):
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+"x400")


vertical=Scale(root, from_=0, to=200).pack()
horizontal=Scale(root, from_=0, to=400, orient=HORIZONTAL, command=slides)
horizontal.pack()





btn=Button(root, text="Click Me!", command=slides).pack()

root.mainloop()