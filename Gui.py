from tkinter import *

def useless():
    print("I lied, i actually do something! HUEHUEHUE")

def printVars():
    print(entryName.get())
    print(entryUID.get())
    print(entryRights.get())

root = Tk()
root.title("Dit is de titel")
inputVar1 = ""
inputVar2 = ""
inputVar3 = ""

buttonSearch = Button(root, text="Search", command=printVars, height=3)
entryName = Entry(root, textvariable=inputVar1)
labelName = Label(root, text="Name")
entryUID = Entry(root, textvariable=inputVar2)
labelUID = Label(root, text="User ID")
entryRights = Entry(root, textvariable=inputVar3)
labelRights = Label(root, text="Rights")

labelName.grid(row=0, column=0, sticky=E)
entryName.grid(row=0, column=1)
labelUID.grid(row=1, column=0, sticky=E)
entryUID.grid(row=1, column=1)
labelRights.grid(row=2, column=0, sticky=E)
entryRights.grid(row=2, column=1)
buttonSearch.grid(row=0, column=2, rowspan=3)

root.mainloop()