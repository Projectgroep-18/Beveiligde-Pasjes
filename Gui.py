from tkinter import *

def useless():
    print("I lied, i actually do something! HUEHUEHUE")

root = Tk()
root.title("Dit is de titel")
#root.geometry("500x500")

image = PhotoImage(file="dickbutt.png")

button1 = Button(root, text="Knop 1", command=useless)
button2 = Button(root, text="Knop 2", command=useless)
button3 = Button(root, image=image, command=useless, bd=5)

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=1, columnspan=2)

root.mainloop()