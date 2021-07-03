from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root=Tk()
root.title("Open Files Dialog Box")
root.iconbitmap("C:\\Users\\majid\\OneDrive\\Pictures\\Random\\Sun.ico")

# root.filename=filedialog.askopenfilename(initialdir="D:\\Python",title="Select A File",filetypes=(("png Files", ".png"),("All Files","*.*")))



# def open():
#     global my_image
#     root.filename = filedialog.askopenfilename(initialdir="D:\\Python", title="Open A file",
#                                                filetypes=(("JPG Files", ".jpg"), ("All Files", "*.*")))
#     my_label = Label(root, text=root.filename).pack()
#     my_image = ImageTk.PhotoImage(Image.open(root.filename))
#     my_label2 = Label(image=my_image).pack()

def open():
    global my_image
    root.filename=filedialog.askopenfilename(initialdir="G:\Majid",title="See Images", filetypes=(("PDF Files",".pdf"),("All Files","*.*")))
    my_label1=Label(root, text=root.filename).pack()
    my_image=ImageTk.PhotoImage(Image.open(root.filename))
    my_label2=Label(image=my_image).pack()

btn=Button(root, text="See Image",command=open).pack()

root.mainloop()