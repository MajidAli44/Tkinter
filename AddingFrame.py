from tkinter import *
from PIL import ImageTk,Image


root=Tk()

root.title("MN Software Company")
root.iconbitmap("C:\\Users\\majid\\OneDrive\\Pictures\\Random\\Sun.ico")

# frame=LabelFrame(root, text="This is my Frame...!",padx=50, pady=50)
frame=LabelFrame(root,padx=50, pady=50)
frame.pack(padx=100, pady=100)

b=Button(frame, text="Don't Click ", command=root.quit)
b2=Button(frame, text="Click Here ")

b.grid(row=0,column=0)
b2.grid(row=1,column=1)
root.mainloop()
