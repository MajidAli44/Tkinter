from tkinter import *

root=Tk()
root.title("Radio Button")
root.iconbitmap("C:\\Users\\majid\\OneDrive\\Pictures\\Random\\Sun.ico")

# r=IntVar()
# r.set(2)

modes=[
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion")
]

Pizza=StringVar()
Pizza.set("Pepperoni")

for text, mode in modes:
    Radiobutton(root, text=text, variable=Pizza, value=mode).pack(anchor=W)

def clicked(value):
    label = Label(root, text=value)
    label.pack()


# Radiobutton(root, text="Python",variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Java",variable=r, value=2, command=lambda: clicked(r.get())).pack()

# label=Label(root, text=Pizza.get())
# label.pack(anchor=W)

button=Button(root, text="Click", command=lambda: clicked(Pizza.get()))
button.pack(anchor=W)
root.mainloop()

