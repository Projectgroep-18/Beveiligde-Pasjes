from tkinter import *
import tkinter.messagebox

root = Tk()


def changeImg():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    if doorState.get() == 1:
        labelDoor.configure(image=doorO)
        labelDoor.image = doorO
    else:
        labelDoor.configure(image=doorC)
        labelDoor.image = doorC


def string_int(string):
    try:
        int(string)
        return int(string)
    except ValueError:
        return -1


def search():
    var1 = entryName1.get()
    var2 = entryCID1.get()
    if var2 != "":
        var2 = string_int(var2)
    var3 = entryRights1.get()
    if var2 != -1:
        if var1 != "":
            print(var1, var2, var3)
    else:
        tkinter.messagebox.showerror("Wrong Input", "Card ID must be an integer")

def searchName():
    var1 = entryName1.get()
    if var1 == "":
        tkinter.messagebox.showerror("No Input", "There must be an input")
    else:
        print(var1)

def searchCID():
    var1 = entryCID1.get()
    if var1 == "":
        tkinter.messagebox.showerror("No Input", "There must be an input")
    elif string_int(var1) == -1:
        tkinter.messagebox.showerror("Wrong Input", "Card ID must be an integer")
    else:
        print(var1)

def searchRights():
    var1 = entryRights1.get()
    if var1 == "":
        tkinter.messagebox.showerror("No Input", "There must be an input")
    else:
        print(var1)

def add_vars():
    var1 = entryName2.get()
    var2 = entryCID2.get()
    if var2 != "":
        var2 = string_int(var2)
    var3 = entryRights2.get()
    if var1 != "" and var2 != "" and var3 != "":
        if var2 != -1:
            print(var1, var2, var3)
        else:
            tkinter.messagebox.showerror("Wrong Input", "Card ID must be an integer")
    else:
        tkinter.messagebox.showerror("Wrong Input", "Some fields are empty")



root.title("Dit is de titel")
inputVar1 = ""                                                              # Search name
inputVar2 = ""                                                              # Search UID
inputVar3 = ""                                                              # Search rights
inputVar4 = ""                                                              # Input name
inputVar5 = ""                                                              # Input UID
inputVar6 = ""                                                              # Input rights

buttonSearchName = Button(root, text="Search", command=searchName)
buttonSearchCID = Button(root, text="Search", command=searchCID)
buttonSearchRights = Button(root, text="Search", command=searchRights)

#buttonSearch = Button(root, text="Search", command=search, height=3)
entryName1 = Entry(root, textvariable=inputVar1)
labelName1 = Label(root, text="Name")
entryCID1 = Entry(root, textvariable=inputVar2)
labelCID1 = Label(root, text="Card ID")
entryRights1 = Entry(root, textvariable=inputVar3)
labelRights1 = Label(root, text="Rights")

buttonEnter = Button(root, text="Enter", command=add_vars, height=3)
entryName2 = Entry(root, textvariable=inputVar4)
labelName2 = Label(root, text="Name")
entryCID2 = Entry(root, textvariable=inputVar5)
labelCID2 = Label(root, text="Card ID")
entryRights2 = Entry(root, textvariable=inputVar6)
labelRights2 = Label(root, text="Rights")
labelWhite = Label(root, text="")

doorStart = PhotoImage(file="door_closed.png")
labelDoor = Label(root, image=doorStart)
doorState = IntVar()
doorButton = Checkbutton(root, variable=doorState, command=changeImg)

buttonSearchName.grid(row=0, column=2)
buttonSearchCID.grid(row=1, column=2)
buttonSearchRights.grid(row=2, column=2)

labelName1.grid(row=0, column=0, sticky=E)
entryName1.grid(row=0, column=1)
labelCID1.grid(row=1, column=0, sticky=E)
entryCID1.grid(row=1, column=1)
labelRights1.grid(row=2, column=0, sticky=E)
entryRights1.grid(row=2, column=1)
#buttonSearch.grid(row=0, column=3, rowspan=3)

labelWhite.grid(row=3)
labelName2.grid(row=4, column=0, sticky=E)
entryName2.grid(row=4, column=1)
labelCID2.grid(row=5, column=0, sticky=E)
entryCID2.grid(row=5, column=1)
labelRights2.grid(row=6, column=0, sticky=E)
entryRights2.grid(row=6, column=1)
buttonEnter.grid(row=4, column=2, rowspan=3)

labelDoor.grid(row=7, column=1)
doorButton.grid(row=7, column=0)


root.mainloop()