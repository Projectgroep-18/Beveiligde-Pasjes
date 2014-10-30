from tkinter import *
import tkinter.messagebox
import UseDatabase
#import python_code_for_reading_uid

root = Tk()

firestate = 0
ddoor1 = False
ddoor2 = False
ddoor3 = False
ddoor4 = False
ddoor5 = False
ddoor6 = False
ddoor7 = False


def get_history():
    popup_search(UseDatabase.gethistory())


def get_history_name():
    var1 = entryHistoryName.get()
    if var1:
        popup_search(UseDatabase.gethistoryName(var1))
    else:
        tkinter.messagebox.showerror("No Input", "There must be an input")


def get_history_cid():
    var1 = (python_code_for_reading_uid.readArduino())
    popup_search(UseDatabase.gethistoryCID(var1))


def get_history_rights():
    var1 = entryHistoryRights
    if var1:
        popup_search(UseDatabase.gethistoryRights(var1))
    else:
        tkinter.messagebox.showerror("No Input", "There must be an input")


def emergency():
    global firestate
    firestate = UseDatabase.fire()
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    doorO_eigenaar = PhotoImage(file="door_eigenaar_open.png")
    doorC_eigenaar = PhotoImage(file="door_eigenaar_closed.png")
    global ddoor1
    global ddoor2
    global ddoor3
    global ddoor4
    global ddoor5
    global ddoor6
    global ddoor7
    if firestate:
        root.configure(bg="red")
        leftFrame.configure(bg="red")
        rightFrame.configure(bg="red")
        Whitespace9.configure(bg="red")
        Whitespace8.configure(bg="red")
        Whitespace7.configure(bg="red")
        Whitespace6.configure(bg="red")
        Whitespace5.configure(bg="red")
        Whitespace4.configure(bg="red")
        Whitespace3.configure(bg="red")
        Whitespace2.configure(bg="red")
        Whitespace1.configure(bg="red")
        door1.configure(image=doorO_eigenaar)
        door1.image = doorO_eigenaar
        door2.configure(image=doorO)
        door2.image = doorO
        door3.configure(image=doorO)
        door3.image = doorO
        door4.configure(image=doorO)
        door4.image = doorO
        door5.configure(image=doorO)
        door5.image = doorO
        door6.configure(image=doorO)
        door6.image = doorO
        door7.configure(image=doorO)
        door7.image = doorO
        ddoor1 = True
        ddoor2 = True
        ddoor3 = True
        ddoor4 = True
        ddoor5 = True
        ddoor6 = True
        ddoor7 = True
    else:
        root.configure(bg="green")
        leftFrame.configure(bg="green")
        rightFrame.configure(bg="green")
        Whitespace9.configure(bg="green")
        Whitespace8.configure(bg="green")
        Whitespace7.configure(bg="green")
        Whitespace6.configure(bg="green")
        Whitespace5.configure(bg="green")
        Whitespace4.configure(bg="green")
        Whitespace3.configure(bg="green")
        Whitespace2.configure(bg="green")
        Whitespace1.configure(bg="green")
        door1.configure(image=doorC_eigenaar)
        door2.image = doorC_eigenaar
        door2.configure(image=doorC)
        door3.image = doorC
        door3.configure(image=doorC)
        door4.image = doorC
        door4.configure(image=doorC)
        door5.image = doorC
        door5.configure(image=doorC)
        door6.image = doorC
        door6.configure(image=doorC)
        door6.image = doorC
        door7.configure(image=doorC)
        door7.image = doorC
        ddoor1 = False
        ddoor2 = False
        ddoor3 = False
        ddoor4 = False
        ddoor5 = False
        ddoor6 = False
        ddoor7 = False


def door1Func():
    doorO = PhotoImage(file="door_eigenaar_open.png")
    doorC = PhotoImage(file="door_eigenaar_closed.png")
    global ddoor1
    if ddoor1 == False:
        cid = python_code_for_reading_uid.readArduino()
        var = UseDatabase.check(cid, 1)
        if var == True:
            door1.configure(image=doorO)
            door1.image = doorO
            ddoor1 = True
        else:
            door1.configure(image=doorC)
            door1.image = doorC
            ddoor1 = False
    else:
        if not firestate:
            door1.configure(image=doorC)
            door1.image = doorC
            ddoor1 = False


def door2Func():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    global ddoor2
    if ddoor2 == False:
        cid = python_code_for_reading_uid.readArduino()
        var = UseDatabase.check(cid, 2)
        if var == True:
            door2.configure(image=doorO)
            door2.image = doorO
            ddoor2 = True
        else:
            door2.configure(image=doorC)
            door2.image = doorC
            ddoor2 = False
    else:
        if not firestate:
            door2.configure(image=doorC)
            door2.image = doorC
            ddoor2 = False


def door3Func():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    global ddoor3
    if ddoor3 == False:
        cid = python_code_for_reading_uid.readArduino()
        var = UseDatabase.check(cid, 3)
        if var == True:
            door3.configure(image=doorO)
            door3.image = doorO
            ddoor3 = True
        else:
            door3.configure(image=doorC)
            door3.image = doorC
            ddoor3 = False
    else:
        if not firestate:
            door3.configure(image=doorC)
            door3.image = doorC
            ddoor3 = False


def door4Func():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    global ddoor4
    if ddoor4 == False:
        cid = python_code_for_reading_uid.readArduino()
        var = UseDatabase.check(cid, 4)
        if var == True:
            door4.configure(image=doorO)
            door4.image = doorO
            ddoor4 = True
        else:
            door4.configure(image=doorC)
            door4.image = doorC
            ddoor4 = False
    else:
        if not firestate:
            door4.configure(image=doorC)
            door4.image = doorC
            ddoor4 = False


def door5Func():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    global ddoor5
    if ddoor5 == False:
        cid = python_code_for_reading_uid.readArduino()
        var = UseDatabase.check(cid, 5)
        if var == True:
            door5.configure(image=doorO)
            door5.image = doorO
            ddoor5 = True
        else:
            door5.configure(image=doorC)
            door5.image = doorC
            ddoor5 = False
    else:
        if not firestate:
            door5.configure(image=doorC)
            door5.image = doorC
            ddoor5 = False


def door6Func():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    global ddoor6
    if ddoor1 == False:
        cid = python_code_for_reading_uid.readArduino()
        var = UseDatabase.check(cid, 6)
        if var == True:
            door6.configure(image=doorO)
            door6.image = doorO
            ddoor6 = True
        else:
            door6.configure(image=doorC)
            door6.image = doorC
            ddoor6 = False
    else:
        if not firestate:
            door6.configure(image=doorC)
            door6.image = doorC
            ddoor6 = False


def door7Func():
    doorO = PhotoImage(file="door_opened.png")
    doorC = PhotoImage(file="door_closed.png")
    global ddoor7
    if ddoor7 == False:
        cid = python_code_for_reading_uid.readArduino()
        var = UseDatabase.check(cid, 7)
        if var == True:
            door7.configure(image=doorO)
            door7.image = doorO
            ddoor7 = True
        else:
            door7.configure(image=doorC)
            door7.image = doorC
            ddoor7 = False
    else:
        if not firestate:
            door7.configure(image=doorC)
            door7.image = doorC
            ddoor7 = False


def en_card():
    UseDatabase.activeer_cid(python_code_for_reading_uid.readArduino())


def dis_card():
    UseDatabase.deactiveer_cid(python_code_for_reading_uid.readArduino())


def dis_user():
    if string_int(entryDisableID.get()) != -1:
        UseDatabase.deactiveer_uid(string_int(entryDisableID.get()))
    else:
        tkinter.messagebox.showerror("Wrong Input", "User ID must be an integer")


def en_user():
    if string_int(entryEnableID.get()) != -1:
        UseDatabase.activeer_uid(string_int(entryEnableID.get()))
    else:
        tkinter.messagebox.showerror("Wrong Input", "User ID must be an integer")


def string_int(string):
    try:
        int(string)
        return int(string)
    except ValueError:
        return -1


def deleteFromDB():
    if string_int(entryDeleteID.get()) != -1:
        UseDatabase.delete(string_int(entryDeleteID.get()))
    else:
        tkinter.messagebox.showerror("Wrong Input", "User ID must be an integer")


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
    if var1:
        popup_search(UseDatabase.search_naam(var1))
    else:
        tkinter.messagebox.showerror("No Input", "There must be an input")


def search_uid_gui():
    var1 = entryCID1.get()
    if not var1:
        tkinter.messagebox.showerror("No Input", "There must be an input")
    elif string_int(var1) == -1:
        tkinter.messagebox.showerror("Wrong Input", "Card ID must be an integer")
    else:
        popup_search(UseDatabase.search_uid(string_int(var1)))


def search_rights_gui():
    var1 = entryRights1.get()
    if var1:
        popup_search(UseDatabase.search_rechten(var1))
    else:
        tkinter.messagebox.showerror("No Input", "There must be an input")


def add_user():
    var1 = (python_code_for_reading_uid.readArduino())
    UseDatabase.add(var1, entryName2.get(), entryRights2.get())


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
root.resizable(0, 0)

leftFrame = Frame(root)
rightFrame = Frame(root)
leftFrame.pack(side=LEFT, anchor=NW)
rightFrame.pack(side=RIGHT, anchor=NW)

inputVar1 = ""  # Search name
inputVar2 = ""  # Search UID
inputVar3 = ""  # Search rights
inputVar4 = ""  # Input name
inputVar5 = ""  # Input rights
inputVar6 = ""  # Input UID
inputVar7 = ""  # Input UID
inputVar8 = ""
inputVar9 = ""  # History name
inputVar10 = "" # History rights

doorStart = PhotoImage(file="door_closed.png")
doorStartEigenaar= PhotoImage(file="door_eigenaar_closed.png")
fire = PhotoImage(file="fire.png")

door1 = Button(rightFrame, image=doorStartEigenaar, command=door1Func)
door2 = Button(rightFrame, image=doorStart, command=door2Func)
door3 = Button(rightFrame, image=doorStart, command=door3Func)
door4 = Button(rightFrame, image=doorStart, command=door4Func)
door5 = Button(rightFrame, image=doorStart, command=door5Func)
door6 = Button(rightFrame, image=doorStart, command=door6Func)
door7 = Button(rightFrame, image=doorStart, command=door7Func)
history = Button(rightFrame, text="History", command=get_history)

buttonSearchName = Button(leftFrame, text="Search", command=search_name_gui, width=6)
buttonSearchCID = Button(leftFrame, text="Search", command=search_uid_gui, width=6)
buttonSearchRights = Button(leftFrame, text="Search", command=search_rights_gui, width=6)

# buttonSearch = Button(root, text="Search", command=search, height=3)
entryName1 = Entry(leftFrame, textvariable=inputVar1)
labelName1 = Label(leftFrame, text="Name")
entryCID1 = Entry(leftFrame, textvariable=inputVar2)
labelCID1 = Label(leftFrame, text="User ID")
entryRights1 = Entry(leftFrame, textvariable=inputVar3)
labelRights1 = Label(leftFrame, text="Rights")

entryDeleteID = Entry(leftFrame, textvariable=inputVar6)
labelDeleteID = Label(leftFrame, text="User ID")
buttonDeleteID = Button(leftFrame, text="Delete", command=deleteFromDB, width=6)

buttonEnter = Button(leftFrame, text="Enter", command=add_user, height=3, width=6)
entryName2 = Entry(leftFrame, textvariable=inputVar4)
labelName2 = Label(leftFrame, text="Name")
entryRights2 = Entry(leftFrame, textvariable=inputVar5)
labelRights2 = Label(leftFrame, text="Rights")

labelSearch = Label(leftFrame, text="Search by Name, UID or rights")
labelEnter = Label(leftFrame, text="Add someone to database")
labelDelete = Label(leftFrame, text="Delete someone from database")

door1Label = Label(rightFrame, text="Door 1")
door2Label = Label(rightFrame, text="Door 2")
door3Label = Label(rightFrame, text="Door 3")
door4Label = Label(rightFrame, text="Door 4")
door5Label = Label(rightFrame, text="Door 5")
door6Label = Label(rightFrame, text="Door 6")
door7Label = Label(rightFrame, text="Door 7")

Whitespace1 = Label(leftFrame, text="   ")
Whitespace2 = Label(leftFrame, text=" ")
Whitespace3 = Label(leftFrame, text=" ")
Whitespace4 = Label(leftFrame, text=" ")
Whitespace5 = Label(leftFrame, text=" ")
Whitespace6 = Label(leftFrame, text=" ")
Whitespace7 = Label(rightFrame, text=" ")
Whitespace8 = Label(rightFrame, text=" ")
Whitespace9 = Label(leftFrame, text=" ")

labelDisableID = Label(leftFrame, text="User ID")
labelDisable = Label(leftFrame, text="Disable someone in database")
entryDisableID = Entry(leftFrame, textvariable=inputVar7)
disableButton = Button(leftFrame, text="Disable", command=dis_user, width=6)
labelEnableID = Label(leftFrame, text="User ID")
labelEnable = Label(leftFrame, text="Enable someone in database")
entryEnableID = Entry(leftFrame, textvariable=inputVar8)
enableButton = Button(leftFrame, text="Enable", command=en_user, width=6)

labelENDIS = Label(leftFrame, text="Enable or Disable using keycard")
buttonEN = Button(leftFrame, text="Enable", command=en_card, width=7)
buttonDIS = Button(leftFrame, text="Disable", command=dis_card, width=7)

buttonFire = Button(rightFrame, image=fire, command=emergency)
labelFire = Label(rightFrame, text="Fire")

labelHistory = Label(leftFrame, text="History")
labelHistoryName = Label(leftFrame, text="Naam")
labelHistoryCID = Label(leftFrame, text="CID")
labelHistoryRights = Label(leftFrame, text="Rechten")
entryHistoryName = Entry(leftFrame, textvariable=inputVar9)
entryHistoryRights = Entry(leftFrame, textvariable=inputVar10)
buttonHistoryName = Button(leftFrame, text="Search", command=get_history_name)
buttonHistoryCID = Button(leftFrame, text="Search", command=get_history_cid)
buttonHistoryRights = Button(leftFrame, text="Search", command=get_history_rights)

buttonFire.grid(row=8, column=2)
labelFire.grid(row=8, column=1)

labelENDIS.grid(row=19, column=0, columnspan=3)
buttonEN.grid(row=20, column=1)
buttonDIS.grid(row=21, column=1)
Whitespace9.grid(row=22, column=0)

labelDisableID.grid(row=14, column=0, sticky=E)
labelDisable.grid(row=13, column=0, columnspan=3)
entryDisableID.grid(row=14, column=1)
disableButton.grid(row=14, column=2)
Whitespace5.grid(row=15, column=0)
labelEnableID.grid(row=17, column=0, sticky=E)
labelEnable.grid(row=16, column=0, columnspan=3)
entryEnableID.grid(row=17, column=1)
enableButton.grid(row=17, column=2)
Whitespace6.grid(row=18, column=0)

buttonSearchName.grid(row=2, column=2)
buttonSearchCID.grid(row=3, column=2)
buttonSearchRights.grid(row=4, column=2)

Whitespace1.grid(row=0, column=4)
labelSearch.grid(row=1, column=0, columnspan=3)
labelName1.grid(row=2, column=0, sticky=E)
entryName1.grid(row=2, column=1)
labelCID1.grid(row=3, column=0, sticky=E)
entryCID1.grid(row=3, column=1)
labelRights1.grid(row=4, column=0, sticky=E)
entryRights1.grid(row=4, column=1)

#buttonSearch.grid(row=0, column=3, rowspan=3)
Whitespace2.grid(row=5, column=0)
labelEnter.grid(row=6, column=0, columnspan=3)
labelName2.grid(row=7, column=0, sticky=E)
entryName2.grid(row=7, column=1)
labelRights2.grid(row=8, column=0, sticky=E)
entryRights2.grid(row=8, column=1)
buttonEnter.grid(row=7, column=2, rowspan=2)

Whitespace3.grid(row=9, column=0)
labelDelete.grid(row=10, column=0, columnspan=3)
labelDeleteID.grid(row=11, column=0, sticky=E)
entryDeleteID.grid(row=11, column=1)
buttonDeleteID.grid(row=11, column=2)
Whitespace4.grid(row=12, column=0)

door1.grid(row=1, column=2)
door2.grid(row=2, column=2)
door3.grid(row=3, column=2)
door4.grid(row=4, column=2)
door5.grid(row=5, column=2)
door6.grid(row=6, column=2)
door7.grid(row=7, column=2)
history.grid(row=9, column=2)

Whitespace7.grid(row=0, column=0)
Whitespace8.grid(row=0, column=3)

door1Label.grid(row=1, column=1)
door2Label.grid(row=2, column=1)
door3Label.grid(row=3, column=1)
door4Label.grid(row=4, column=1)
door5Label.grid(row=5, column=1)
door6Label.grid(row=6, column=1)
door7Label.grid(row=7, column=1)

labelHistory.grid(row=19, column=0)
labelHistoryName.grid(row=20, column=0)
entryHistoryName.grid(row=20, column=1)
buttonHistoryName.grid(row=20, column=2)
labelHistoryCID.grid(row=21, column=0)
buttonHistoryCID.grid(row=21, column=2)
labelHistoryRights.grid(row=22, column=0)
entryHistoryRights.grid(row=22, column=1)
buttonHistoryRights.grid(row=22, column=2)

# Zorgt dat de bg groen is
root.configure(bg="green")
leftFrame.configure(bg="green")
rightFrame.configure(bg="green")
Whitespace9.configure(bg="green")
Whitespace8.configure(bg="green")
Whitespace7.configure(bg="green")
Whitespace6.configure(bg="green")
Whitespace5.configure(bg="green")
Whitespace4.configure(bg="green")
Whitespace3.configure(bg="green")
Whitespace2.configure(bg="green")
Whitespace1.configure(bg="green")

root.mainloop()