from tkinter import *
import tkinter.messagebox
import UseDatabase
import python_code_for_reading_uid

root = Tk()


def door1Func():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    cid = python_code_for_reading_uid.readArduino()
    var = UseDatabase.check(cid, 1)
    if var == True:
        door1.configure(image=doorO)
        door1.image = doorO
    else:
        door1.configure(image=doorC)
        door1.image = doorC


def door2Func():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    cid = python_code_for_reading_uid.readArduino()
    var = UseDatabase.check(cid, 2)
    if var == True:
        door2.configure(image=doorO)
        door2.image = doorO
    else:
        door2.configure(image=doorC)
        door2.image = doorC


def door3Func():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    cid = python_code_for_reading_uid.readArduino()
    var = UseDatabase.check(cid, 3)
    if var == True:
        door3.configure(image=doorO)
        door3.image = doorO
    else:
        door3.configure(image=doorC)
        door3.image = doorC


def door4Func():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    cid = python_code_for_reading_uid.readArduino()
    var = UseDatabase.check(cid, 4)
    if var == True:
        door4.configure(image=doorO)
        door4.image = doorO
    else:
        door4.configure(image=doorC)
        door4.image = doorC


def door5Func():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    cid = python_code_for_reading_uid.readArduino()
    var = UseDatabase.check(cid, 5)
    if var == True:
        door5.configure(image=doorO)
        door5.image = doorO
    else:
        door5.configure(image=doorC)
        door5.image = doorC


def door6Func():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    cid = python_code_for_reading_uid.readArduino()
    var = UseDatabase.check(cid, 6)
    if var == True:
        door6.configure(image=doorO)
        door6.image = doorO
    else:
        door6.configure(image=doorC)
        door6.image = doorC


def door7Func():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    cid = python_code_for_reading_uid.readArduino()
    var = UseDatabase.check(cid, 7)
    if var == True:
        door7.configure(image=doorO)
        door7.image = doorO
    else:
        door7.configure(image=doorC)
        door7.image = doorC


def string_int(string):
    try:
        int(string)
        return int(string)
    except ValueError:
        return -1


def deleteFromDB():
    UseDatabase.delete(inputVar6)


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


def search_name_gui():
    var1 = entryName1.get()
    if var1 == "":
        tkinter.messagebox.showerror("No Input", "There must be an input")
    else:
        popup_search(UseDatabase.search_naam(var1))


def search_uid_gui():
    var1 = entryCID1.get()
    if var1 == "":
        tkinter.messagebox.showerror("No Input", "There must be an input")
    elif string_int(var1) == -1:
        tkinter.messagebox.showerror("Wrong Input", "Card ID must be an integer")
    else:
        UseDatabase.search_uid(string_int(var1))


def search_rights_gui():
    var1 = entryRights1.get()
    if var1 == "":
        tkinter.messagebox.showerror("No Input", "There must be an input")
    else:
        UseDatabase.search_rechten(var1)


def add_user():
    UseDatabase.add(python_code_for_reading_uid.readArduino(), inputVar4, inputVar5)


def popup_search(data):
    top_search = Toplevel()
    top_search.title("Search results")
    top_search.focus_set()

    results = Message(top_search, text=data).pack()


def popup_add_vars():
    top = Toplevel()
    top.title('Confirmation')
    top.focus_set()

    msg = Message(top, text="Data added")
    msg.pack()

    button = Button(top, text="Dismiss", command=top.destroy)
    button.pack()


root.title("Hotelpasjes beheer")

leftFrame = Frame(root)
rightFrame = Frame(root)
leftFrame.pack(side=LEFT, anchor=NE)
rightFrame.pack(side=RIGHT)


inputVar1 = ""  # Search name
inputVar2 = ""  # Search UID
inputVar3 = ""  # Search rights
inputVar4 = ""  # Input name
inputVar5 = ""  # Input rights
inputVar6 = ""  # Input UID

doorStart = PhotoImage(file="door_closed.png")

door1 = Button(rightFrame, image=doorStart, command=door1Func)
door2 = Button(rightFrame, image=doorStart, command=door2Func)
door3 = Button(rightFrame, image=doorStart, command=door3Func)
door4 = Button(rightFrame, image=doorStart, command=door4Func)
door5 = Button(rightFrame, image=doorStart, command=door5Func)
door6 = Button(rightFrame, image=doorStart, command=door6Func)
door7 = Button(rightFrame, image=doorStart, command=door7Func)

buttonSearchName = Button(leftFrame, text="Search", command=search_name_gui)
buttonSearchCID = Button(leftFrame, text="Search", command=search_uid_gui)
buttonSearchRights = Button(leftFrame, text="Search", command=search_rights_gui)

# buttonSearch = Button(root, text="Search", command=search, height=3)
entryName1 = Entry(leftFrame, textvariable=inputVar1)
labelName1 = Label(leftFrame, text="Name")
entryCID1 = Entry(leftFrame, textvariable=inputVar2)
labelCID1 = Label(leftFrame, text="User ID")
entryRights1 = Entry(leftFrame, textvariable=inputVar3)
labelRights1 = Label(leftFrame, text="Rights")

entryDeleteID = Entry(leftFrame, textvariable=inputVar6)
labelDeleteID = Label(leftFrame, text="User ID")
buttonDeleteID = Button(leftFrame, text="Delete", command=deleteFromDB)

buttonEnter = Button(leftFrame, text="Enter", command=add_user, height=3)
entryName2 = Entry(leftFrame, textvariable=inputVar4)
labelName2 = Label(leftFrame, text="Name")
entryRights2 = Entry(leftFrame, textvariable=inputVar5)
labelRights2 = Label(leftFrame, text="Rights")
labelWhite = Label(leftFrame, text="")

door1Label = Label(rightFrame, text="Door 1")
door2Label = Label(rightFrame, text="Door 2")
door3Label = Label(rightFrame, text="Door 3")
door4Label = Label(rightFrame, text="Door 4")
door5Label = Label(rightFrame, text="Door 5")
door6Label = Label(rightFrame, text="Door 6")
door7Label = Label(rightFrame, text="Door 7")

buttonSearchName.grid(row=1, column=2)
buttonSearchCID.grid(row=2, column=2)
buttonSearchRights.grid(row=3, column=2)

labelName1.grid(row=1, column=0, sticky=E)
entryName1.grid(row=1, column=1)
labelCID1.grid(row=2, column=0, sticky=E)
entryCID1.grid(row=2, column=1)
labelRights1.grid(row=3, column=0, sticky=E)
entryRights1.grid(row=3, column=1)

#buttonSearch.grid(row=0, column=3, rowspan=3)

labelName2.grid(row=6, column=0, sticky=E)
entryName2.grid(row=6, column=1)
labelRights2.grid(row=7, column=0, sticky=E)
entryRights2.grid(row=7, column=1)
buttonEnter.grid(row=6, column=2, rowspan=2)
labelWhite.grid(row=9)

labelName2.grid(row=6, column=0, sticky=E)
entryName2.grid(row=6, column=1)
labelRights2.grid(row=7, column=0, sticky=E)
entryRights2.grid(row=7, column=1)
buttonEnter.grid(row=6, column=2, rowspan=2)

labelDeleteID.grid(row=8, column=0, sticky=E)
entryDeleteID.grid(row=8, column=1)
buttonDeleteID.grid(row=8, column=2)

door1.grid(row=1, column=2)
door2.grid(row=2, column=2)
door3.grid(row=3, column=2)
door4.grid(row=4, column=2)
door5.grid(row=1, column=4)
door6.grid(row=2, column=4)
door7.grid(row=3, column=4)


door1Label.grid(row=1, column=1)
door2Label.grid(row=2, column=1)
door3Label.grid(row=3, column=1)
door4Label.grid(row=4, column=1)
door5Label.grid(row=1, column=3)
door6Label.grid(row=2, column=3)
door7Label.grid(row=3, column=3)

root.mainloop()