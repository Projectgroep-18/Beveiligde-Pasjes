from tkinter import *
import tkinter.messagebox
import UseDatabase
import serial
import python_code_for_reading_uid

root = Tk()

COMPOORT = 4

def door1Func():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    cid = python_code_for_reading_uid.readArduino()
    var = UseDatabase.check(cid, 1)
    if var == True:
        labelDoor.configure(image=doorO)
        labelDoor.image = doorO
    else:
        labelDoor.configure(image=doorC)
        labelDoor.image = doorC

def door2Func():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    cid = python_code_for_reading_uid.readArduino()
    var = UseDatabase.check(cid, 2)
    if var == True:
        labelDoor.configure(image=doorO)
        labelDoor.image = doorO
    else:
        labelDoor.configure(image=doorC)
        labelDoor.image = doorC

def door3Func():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    cid = python_code_for_reading_uid.readArduino()
    var = UseDatabase.check(cid, 3)
    if var == True:
        labelDoor.configure(image=doorO)
        labelDoor.image = doorO
    else:
        labelDoor.configure(image=doorC)
        labelDoor.image = doorC

def door4Func():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    cid = python_code_for_reading_uid.readArduino()
    var = UseDatabase.check(cid, 4)
    if var == True:
        labelDoor.configure(image=doorO)
        labelDoor.image = doorO
    else:
        labelDoor.configure(image=doorC)
        labelDoor.image = doorC

def door5Func():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    cid = python_code_for_reading_uid.readArduino()
    var = UseDatabase.check(cid, 5)
    if var == True:
        labelDoor.configure(image=doorO)
        labelDoor.image = doorO
    else:
        labelDoor.configure(image=doorC)
        labelDoor.image = doorC

def door6Func():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    cid = python_code_for_reading_uid.readArduino()
    var = UseDatabase.check(cid, 6)
    if var == True:
        labelDoor.configure(image=doorO)
        labelDoor.image = doorO
    else:
        labelDoor.configure(image=doorC)
        labelDoor.image = doorC

def door7Func():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    cid = python_code_for_reading_uid.readArduino()
    var = UseDatabase.check(cid, 7)
    if var == True:
        door7.configure(image=doorO)
        door17image = doorO
    else:
        door7.configure(image=doorC)
        door7.image = doorC

def change_img():
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
        UseDatabase.search_naam(var1)


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
    ser = serial.Serial(COMPOORT - 1)
    s = ser.read(10)
    CID = int.from_bytes(s, byteorder='big')
    UseDatabase.add(CID, inputVar4, inputVar5)

def popup_search():
    top_search = Toplevel()
    top_search.title("Search results")
    top_search.focus_set()




def popup_add_vars():
    top = Toplevel()
    top.title('Confirmation')
    top.focus_set()

    msg = Message(top, text="Data added")
    msg.pack()

    button = Button(top, text="Dismiss", command=top.destroy)
    button.pack()


root.title("Dit is de titel")
inputVar1 = ""                                                              # Search name
inputVar2 = ""                                                              # Search UID
inputVar3 = ""                                                              # Search rights
inputVar4 = ""                                                              # Input name
inputVar5 = ""                                                              # Input rights
inputVar6 = ""                                                              # Input UID


doorStart = PhotoImage(file="door_closed.png")

door1 = Button(root, image=doorStart, command=door1Func)
door2 = Button(root, image=doorStart, command=door2Func)
door3 = Button(root, image=doorStart, command=door3Func)
door4 = Button(root, image=doorStart, command=door4Func)
door5 = Button(root, image=doorStart, command=door5Func)
door6 = Button(root, image=doorStart, command=door6Func)
door7 = Button(root, image=doorStart, command=door7Func)

buttonSearchName = Button(root, text="Search", command=search_name_gui)
buttonSearchCID = Button(root, text="Search", command=search_uid_gui)
buttonSearchRights = Button(root, text="Search", command=search_rights_gui)

#buttonSearch = Button(root, text="Search", command=search, height=3)
entryName1 = Entry(root, textvariable=inputVar1)
labelName1 = Label(root, text="Name")
entryCID1 = Entry(root, textvariable=inputVar2)
labelCID1 = Label(root, text="User ID")
entryRights1 = Entry(root, textvariable=inputVar3)
labelRights1 = Label(root, text="Rights")

entryDeleteID = Entry(root, textvariable=inputVar6)
labelDeleteID = Label(root, text="User ID")
buttonDeleteID = Button(root, text="Delete", command=deleteFromDB)

buttonEnter = Button(root, text="Enter", command=add_user, height=3)
entryName2 = Entry(root, textvariable=inputVar4)
labelName2 = Label(root, text="Name")
entryRights2 = Entry(root, textvariable=inputVar5)
labelRights2 = Label(root, text="Rights")
labelWhite = Label(root, text="")


labelDoor = Label(root, image=doorStart)
doorState = IntVar()
doorButton = Checkbutton(root, variable=doorState, command=change_img)

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
labelRights2.grid(row=5, column=0, sticky=E)
entryRights2.grid(row=5, column=1)
buttonEnter.grid(row=4, column=2, rowspan=2)

labelDoor.grid(row=7, column=1)
doorButton.grid(row=7, column=0)

labelDeleteID.grid(row=6, column=0, sticky=E)
entryDeleteID.grid(row=6, column=1)
buttonDeleteID.grid(row=6, column=2)


door1.grid(row=8, column=3)
door2.grid(row=8, column=4)
door3.grid(row=8, column=5)
door4.grid(row=8, column=6)
door5.grid(row=8, column=7)
door6.grid(row=8, column=8)
door7.grid(row=8, column=9)
root.mainloop()