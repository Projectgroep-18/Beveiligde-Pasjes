from tkinter import *


def useless():
    print("I lied, i actually do something! HUEHUEHUE")


def printVars():
    print(entryName.get())
    print(entryUID.get())
    print(entryRights.get())


root = Tk()
root.title("Dit is de titel")
inputVar1 = ""                                                              # Search name
inputVar2 = ""                                                              # Search UID
inputVar3 = ""                                                              # Search rights
inputVar4 = ""                                                              # Input name
inputVar5 = ""                                                              # Input UID
inputVar6 = ""                                                              # Input rights

buttonSearch = Button(root, text="Search", command=printVars, height=3)
entryName1 = Entry(root, textvariable=inputVar1)
labelName1 = Label(root, text="Name")
entryUID1 = Entry(root, textvariable=inputVar2)
labelUID1 = Label(root, text="User ID")
entryRights1 = Entry(root, textvariable=inputVar3)
labelRights1 = Label(root, text="Rights")

buttonEnter = Button(root, text="Enter", command=printVars, height=3)
entryName2 = Entry(root, textvariable=inputVar4)
labelName2 = Label(root, text="Name")
entryUID2 = Entry(root, textvariable=inputVar5)
labelUID2 = Label(root, text="User ID")
entryRights2 = Entry(root, textvariable=inputVar6)
labelRights2 = Label(root, text="Rights")
labelWhite = Label(root, text="")

labelName1.grid(row=0, column=0, sticky=E)
entryName1.grid(row=0, column=1)
labelUID1.grid(row=1, column=0, sticky=E)
entryUID1.grid(row=1, column=1)
labelRights1.grid(row=2, column=0, sticky=E)
entryRights1.grid(row=2, column=1)
buttonSearch.grid(row=0, column=2, rowspan=3)

labelWhite.grid(row=3)
labelName2.grid(row=4, column=0, sticky=E)
entryName2.grid(row=4, column=1)
labelUID2.grid(row=5, column=0, sticky=E)
entryUID2.grid(row=5, column=1)
labelRights2.grid(row=6, column=0, sticky=E)
entryRights2.grid(row=6, column=1)
buttonEnter.grid(row=4, column=2, rowspan=3)



root.mainloop()