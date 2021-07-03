from tkinter import *
from PIL import ImageTk, Image

root=Tk()

root.title("Majid Ali")

root.iconbitmap("C:/Users/majid/OneDrive/Pictures/Random/Apple.png")


# my_img=ImageTk.PhotoImage(Image.open("D:\\Python\\Family.png"))
# my_label=Label(image=my_img)
# my_label.pack()

# my_img=ImageTk.PhotoImage(Image.open("D:\\Python\\Nabiya.jpg"))
# my_label=Label(image=my_img)
# my_label.pack()


my_img=ImageTk.PhotoImage(Image.open("D:\\Python\\Lambo.png"))
my_label=Label(image=my_img)
my_label.pack()


button_quit=Button(root, text="Exit", command=root.quit, padx=30, pady=30)
button_quit.pack()



root.mainloop()
