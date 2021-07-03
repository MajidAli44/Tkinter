from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root=Tk()
root.title("Message Box")
root.iconbitmap("C:\\Users\\majid\\OneDrive\\Pictures\\Random\\Sun.ico")

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response=messagebox.askquestion("Author!", "Majid Ali")
    Label(root, text=response).pack()
    # if response == 1:
    #     label=Label(root, text="You Clicked Yes!").pack()
    # else:
    #     label = Label(root, text="You Clicked No!").pack()

Button(root,text="Popup", command=popup).pack()

root.mainloop()
