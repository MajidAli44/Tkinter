from tkinter import *
from PIL import ImageTk,Image

root=Tk()

root.title("Image Viewer APP")

my_img1=ImageTk.PhotoImage(Image.open("D:\\Python\\Lambo.png"))
my_img2=ImageTk.PhotoImage(Image.open("D:\\Python\\Cards.jpg"))
my_img3=ImageTk.PhotoImage(Image.open("D:\\Python\\copy.PNG"))
my_img4=ImageTk.PhotoImage(Image.open("D:\\Python\\Card.jpg"))
my_img5=ImageTk.PhotoImage(Image.open("D:\\Python\\ABC.png"))
# my_img6=ImageTk.PhotoImage(Image.open("D:\\Python\\Girl.jpg"))

img_list=[my_img1,my_img2,my_img3,my_img4,my_img5]


# Status Bar

status=Label(root, text="Image 1 of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)


my_label=Label(image=my_img1)
my_label.grid(row=0,column=0, columnspan=3)


def next(image_number):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()

    my_label=Label(image=img_list[image_number-1])
    button_next=Button(root, text=">>", command=lambda : next(image_number+1))
    button_back=Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 5:
        button_next=Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_next.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    # Update Status Bar
    status = Label(root, text=" Image " + str(image_number) + " of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

def back(img_number):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()

    my_label=Label(image=img_list[img_number-1])
    button_next=Button(root, text=">>", command=lambda : next(img_number+1))
    button_back=Button(root, text="<<", command=lambda : back(img_number-1))

    if img_number == 1:
        button_back=Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_next.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    # Update Status Bar
    status = Label(root, text=" Image " + str(img_number) + " of " + str(len(img_list)), bd=1, relief=SUNKEN,anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)






button_back=Button(root, text="<<", command=back)
button_exit=Button(root, text="Exit", command=root.quit)
button_next=Button(root, text=">>", command=lambda : next(2))


button_back.grid(row=1, column=0)
button_exit.grid(row=1,column=1)
button_next.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)


root.mainloop()