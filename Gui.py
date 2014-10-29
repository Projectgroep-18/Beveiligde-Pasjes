from tkinter import *
import tkinter.messagebox
import UseDatabase
import serial

root = Tk()

COMPOORT = 4


def change_img1():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    if doorState1.get() == 1:
        labelDoor1.configure(image=doorO)
        labelDoor1.image = doorO
    else:
        labelDoor1.configure(image=doorC)
        labelDoor1.image = doorC


def change_img2():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    if doorState2.get() == 1:
        labelDoor2.configure(image=doorO)
        labelDoor2.image = doorO
    else:
        labelDoor2.configure(image=doorC)
        labelDoor2.image = doorC


def change_img3():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    if doorState3.get() == 1:
        labelDoor3.configure(image=doorO)
        labelDoor3.image = doorO
    else:
        labelDoor3.configure(image=doorC)
        labelDoor3.image = doorC


def change_img4():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    if doorState4.get() == 1:
        labelDoor4.configure(image=doorO)
        labelDoor4.image = doorO
    else:
        labelDoor4.configure(image=doorC)
        labelDoor4.image = doorC


def change_img5():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    if doorState5.get() == 1:
        labelDoor5.configure(image=doorO)
        labelDoor5.image = doorO
    else:
        labelDoor5.configure(image=doorC)
        labelDoor5.image = doorC


def change_img6():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    if doorState6.get() == 1:
        labelDoor6.configure(image=doorO)
        labelDoor6.image = doorO
    else:
        labelDoor6.configure(image=doorC)
        labelDoor6.image = doorC


def change_img7():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    if doorState7.get() == 1:
        labelDoor7.configure(image=doorO)
        labelDoor7.image = doorO
    else:
        labelDoor7.configure(image=doorC)
        labelDoor7.image = doorC


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


def search_name_gui():
    var1 = entryName1.get()
    if var1 == "":
        tkinter.messagebox.showerror("No Input", "There must be an input")
    else:
        popup_search(UseDatabase.search_naam(var1))


def search_cid_gui():
    var1 = entryCID1.get()
    if var1 == "":
        tkinter.messagebox.showerror("No Input", "There must be an input")
    elif string_int(var1) == -1:
        tkinter.messagebox.showerror("Wrong Input", "Card ID must be an integer")
    else:
        UseDatabase.search_cid(string_int(var1))


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
inputVar1 = ""                                                              # Search name
inputVar2 = ""                                                              # Search UID
inputVar3 = ""                                                              # Search rights
inputVar4 = ""                                                              # Input name
inputVar5 = ""                                                              # Input rights

buttonSearchName = Button(root, text="Search", command=search_name_gui)
buttonSearchCID = Button(root, text="Search", command=search_cid_gui)
buttonSearchRights = Button(root, text="Search", command=search_rights_gui)

#buttonSearch = Button(root, text="Search", command=search, height=3)
entryName1 = Entry(root, textvariable=inputVar1)
labelName1 = Label(root, text="Name")
entryCID1 = Entry(root, textvariable=inputVar2)
labelCID1 = Label(root, text="Card ID")
entryRights1 = Entry(root, textvariable=inputVar3)
labelRights1 = Label(root, text="Rights")

buttonEnter = Button(root, text="Enter", command=add_user, height=3)
entryName2 = Entry(root, textvariable=inputVar4)
labelName2 = Label(root, text="Name")
entryRights2 = Entry(root, textvariable=inputVar5)
labelRights2 = Label(root, text="Rights")
labelWhite = Label(root, text="")

doorStart1 = PhotoImage(file="door_closed.png")
labelDoor1 = Label(root, image=doorStart1)
doorState1 = IntVar()
doorStart2 = PhotoImage(file="door_closed.png")
labelDoor2 = Label(root, image=doorStart2)
doorState2 = IntVar()
doorStart3 = PhotoImage(file="door_closed.png")
labelDoor3 = Label(root, image=doorStart3)
doorState3 = IntVar()
doorStart4 = PhotoImage(file="door_closed.png")
labelDoor4 = Label(root, image=doorStart4)
doorState4 = IntVar()
doorStart5 = PhotoImage(file="door_closed.png")
labelDoor5 = Label(root, image=doorStart5)
doorState5 = IntVar()
doorStart6 = PhotoImage(file="door_closed.png")
labelDoor6 = Label(root, image=doorStart6)
doorState6 = IntVar()
doorStart7 = PhotoImage(file="door_closed.png")
labelDoor7 = Label(root, image=doorStart7)
doorState7 = IntVar()

buttonSearchName.grid(row=1, column=2)
buttonSearchCID.grid(row=2, column=2)
buttonSearchRights.grid(row=3, column=2)

labelWhite.grid(row=0)
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
labelWhite.grid(row=8)

labelDoor1.grid(row=4, column=4)
labelDoor2.grid(row=4, column=5)
labelDoor3.grid(row=4, column=6)
labelDoor4.grid(row=4, column=7)
labelDoor5.grid(row=5, column=4)
labelDoor6.grid(row=5, column=5)
labelDoor7.grid(row=5, column=6)

root.mainloop()