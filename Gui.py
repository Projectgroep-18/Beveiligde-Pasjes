from tkinter import *
import tkinter.messagebox
import UseDatabase
#import python_code_for_reading_uid

login = Tk()
go = False
login.title("Wachtwoord")
login.resizable(0, 0)
login.geometry("300x150")
password = ""


def loginGo():
    passVar = entryLogin.get()
    global go
    if passVar == "1234":
        go = True
        login.destroy()
    else:
        tkinter.messagebox.showerror("Verkeerd wachtwoord", "Het wachtwoord dat u invoerde is incorrect")


loginFrame = Frame(login)
labelLogin = Label(loginFrame, text="Vul uw wachtwoord in", height=2, font=("Purisa", 18))
entryLogin = Entry(loginFrame, textvar=password, show="*", font=("Purisa", 16))
buttonLogin = Button(loginFrame, text="Login", command=loginGo, font=("Purisa", 18))
loginFrame.pack(anchor=CENTER)
buttonLogin.grid(row=3, column=1)
labelLogin.grid(row=1, column=1)
entryLogin.grid(row=2, column=1)
login.mainloop()

if go:
    root = Tk()

    firestate = 0
    ddoor1 = False
    ddoor2 = False
    ddoor3 = False
    ddoor4 = False
    ddoor5 = False
    ddoor6 = False
    ddoor7 = False
    stdbg = root.cget("bg")

    def get_history():
        top = Toplevel()
        top.title("Resultaten")
        top.focus_set()
        top.resizable(0, 0)
        lbname = Listbox(top, height=50)
        lbcid = Listbox(top, height=50)
        lbtime = Listbox(top, height=50)
        lbtid = Listbox(top, height=50)
        data = UseDatabase.gethistory()
        if data:
            lbname.insert(END, "Naam:")
            lbcid.insert(END, "Card ID:")
            lbtime.insert(END, "Datum:")
            lbtid.insert(END, "Deur:")
            for x in range(0, len(data)):
                lbname.insert(END, data[x][0])
                lbcid.insert(END, data[x][1])
                lbtime.insert(END, data[x][2])
                lbtid.insert(END, data[x][3])
        else:
            lbname.insert(END, "Geen Data")
        lbname.grid(column=1, row=1)
        lbcid.grid(column=3, row=1)
        lbtime.grid(column=4, row=1)
        lbtid.grid(column=2, row=1)


    def get_history_name():
        var0 = entryHistoryName.get()
        var1 = UseDatabase.searchhistory_name(var0)
        top = Toplevel()
        top.title("Geschiedenis")
        top.focus_set()

        if var1 != 0:
            for x in range(0, len(var1)):
                name = "Naam: %s" % var1[x][0]
                tid = "TID: %s" % var1[x][3]
                cid = "Pasjes ID: %s" % var1[x][1]
                time = "Tijd: %s" %var1[x][2]

                Message(top, text=name, width=500, anchor=NE).pack()
                Message(top, text=cid, width=500, anchor=NE).pack()
                Message(top, text=time, width=500, anchor=NE).pack()
                Message(top, text=tid, width=500, anchor=NE).pack()
                Message(top, text=" ", width=500).pack()

            top.geometry('{}x{}'.format(300, 300))
        else:
            Message(top, text="Geschiedenis", width=500, anchor=NE).pack()


    def get_history_cid():
        var0 = (python_code_for_reading_uid.readArduino())
        var1 = (UseDatabase.searchhistory_cid(var0))
        top = Toplevel()
        top.title("Geschiedenis")
        top.focus_set()

        if var1 != 0:
            for x in range(0, len(var1)):
                name = "Naam: %s" % var1[x][0]
                tid = "TID: %s" % var1[x][3]
                cid = "Pasjes ID: %s" % var1[x][1]
                time = "Tijd: %s" %var1[x][2]

                Message(top, text=name, width=500, anchor=NE).pack()
                Message(top, text=cid, width=500, anchor=NE).pack()
                Message(top, text=time, width=500, anchor=NE).pack()
                Message(top, text=tid, width=500, anchor=NE).pack()
                Message(top, text=" ", width=500).pack()

            top.geometry('{}x{}'.format(300, 300))
        else:
            Message(top, text="Geschiedenis", width=500, anchor=NE).pack()


    def get_history_rights():
        var1 = entryHistoryRights.get()
        if var1 == 'Eigenaar' or var1 == 'Gast' or var1 == 'Beveiliging' or var1 == 'Schoonmaker':
            var2 = UseDatabase.searchhistory_rights(var1)
            if var2:
                top = Toplevel()
                top.title("Geschiedenis")
                top.focus_set()

                if var2 != 0:
                    for x in range(0, len(var2)):
                        name = "Naam: %s" % var2[x][0]
                        tid = "TID: %s" % var2[x][3]
                        cid = "Pasjes ID: %s" % var2[x][1]
                        time = "Tijd: %s" %var2[x][2]

                        Message(top, text=name, width=500, anchor=NE).pack()
                        Message(top, text=cid, width=500, anchor=NE).pack()
                        Message(top, text=time, width=500, anchor=NE).pack()
                        Message(top, text=tid, width=500, anchor=NE).pack()
                        Message(top, text=" ", width=500).pack()

                    top.geometry('{}x{}'.format(300, 300))
                else:
                    Message(top, text="Geschiedenis", width=500, anchor=NE).pack()
            else:
                popup("Geen data")
        else:
            tkinter.messagebox.showerror("Geen geldige invoer", "Er moet een geldige invoer worden gegeven (Gast, Schoonmaker, Beveiliging, Eigenaar)")

    def get_history_terminal():
        var1 = string_int(entryHistoryTerminal.get())
        if not var1:
            tkinter.messagebox.showerror("Geen invoer", "Er moet wat ingevoerd worden")
        elif var1 != -1:
            var2 = (UseDatabase.searchhistory_tid(var1))
            if var2:
                top = Toplevel()
                top.title("Geschiedenis")
                top.focus_set()

                if var2 != 0:
                    for x in range(0, len(var2)):
                        name = "Naam: %s" % var2[x][0]
                        tid = "TID: %s" % var2[x][3]
                        cid = "Pasjes ID: %s" % var2[x][1]
                        time = "Tijd: %s" %var2[x][2]

                        Message(top, text=name, width=500, anchor=NE).pack()
                        Message(top, text=cid, width=500, anchor=NE).pack()
                        Message(top, text=time, width=500, anchor=NE).pack()
                        Message(top, text=tid, width=500, anchor=NE).pack()
                        Message(top, text=" ", width=500).pack()

                    top.geometry('{}x{}'.format(300, 300))
                else:
                    Message(top, text="Geschiedenis", width=500, anchor=NE).pack()
            else:
                popup("Geen data")
        else:
            tkinter.messagebox.showerror("Verkeerde invoer", "Deur ID moet een integer zijn")



    def emergency():
        global firestate
        firestate = UseDatabase.fire()
        doorO_eigenaar = PhotoImage(file="door_eigenaar_open.png")
        doorC_eigenaar = PhotoImage(file="door_eigenaar_closed.png")
        doorO_beveiliging = PhotoImage(file="door_security_open.png")
        doorC_beveiliging = PhotoImage(file="door_security_closed.png")
        doorO_janitor = PhotoImage(file="door_schoonmaker_open.png")
        doorC_janitor = PhotoImage(file="door_schoonmaker_closed.png")
        doorO_guest1 = PhotoImage(file="door_1_open.png")
        doorC_guest1 = PhotoImage(file="door_1_closed.png")
        doorO_guest2 = PhotoImage(file="door_2_open.png")
        doorC_guest2 = PhotoImage(file="door_2_closed.png")
        doorO_guest3 = PhotoImage(file="door_3_open.png")
        doorC_guest3 = PhotoImage(file="door_3_closed.png")
        doorO_guest4 = PhotoImage(file="door_4_open.png")
        doorC_guest4 = PhotoImage(file="door_4_closed.png")
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
            door2.configure(image=doorO_beveiliging)
            door2.image = doorO_beveiliging
            door3.configure(image=doorO_janitor)
            door3.image = doorO_janitor
            door4.configure(image=doorO_guest1)
            door4.image = doorO_guest1
            door5.configure(image=doorO_guest2)
            door5.image = doorO_guest2
            door6.configure(image=doorO_guest3)
            door6.image = doorO_guest3
            door7.configure(image=doorO_guest4)
            door7.image = doorO_guest4
            ddoor1 = True
            ddoor2 = True
            ddoor3 = True
            ddoor4 = True
            ddoor5 = True
            ddoor6 = True
            ddoor7 = True
        else:
            root.configure(bg=stdbg)
            leftFrame.configure(bg=stdbg)
            rightFrame.configure(bg=stdbg)
            Whitespace9.configure(bg=stdbg)
            Whitespace8.configure(bg=stdbg)
            Whitespace7.configure(bg=stdbg)
            Whitespace6.configure(bg=stdbg)
            Whitespace5.configure(bg=stdbg)
            Whitespace4.configure(bg=stdbg)
            Whitespace3.configure(bg=stdbg)
            Whitespace2.configure(bg=stdbg)
            Whitespace1.configure(bg=stdbg)
            door1.configure(image=doorC_eigenaar)
            door1.image = doorC_eigenaar
            door2.configure(image=doorC_beveiliging)
            door2.image = doorC_beveiliging
            door3.configure(image=doorC_janitor)
            door3.image = doorC_janitor
            door4.configure(image=doorC_guest1)
            door4.image = doorC_guest1
            door5.configure(image=doorC_guest2)
            door5.image = doorC_guest2
            door6.configure(image=doorC_guest3)
            door6.image = doorC_guest3
            door7.configure(image=doorC_guest4)
            door7.image = doorC_guest4
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
        if firestate:
            print("This door is open")
        else:
            if ddoor1 == False:
                cid = python_code_for_reading_uid.readArduino()
                var = UseDatabase.check(cid, 1)
                if var == True:
                    door1.configure(image=doorO)
                    door1.image = doorO
                    ddoor1 = True
                else:
                    tkinter.messagebox.showerror("Geen toegang", "U bent niet bevoegd om deze deur te openen")
            else:
                door1.configure(image=doorC)
                door1.image = doorC
                ddoor1 = False


    def door2Func():
        doorO = PhotoImage(file="door_security_open.png")
        doorC = PhotoImage(file="door_security_closed.png")
        global ddoor2
        if firestate:
            print("This door is open")
        else:
            if ddoor2 == False:
                cid = python_code_for_reading_uid.readArduino()
                var = UseDatabase.check(cid, 2)
                if var == True:
                    door2.configure(image=doorO)
                    door2.image = doorO
                    ddoor2 = True
                else:
                    tkinter.messagebox.showerror("Geen toegang", "U bent niet bevoegd om deze deur te openen")
            else:
                door2.configure(image=doorC)
                door2.image = doorC
                ddoor2 = False


    def door3Func():
        doorO = PhotoImage(file="door_schoonmaker_open.png")
        doorC = PhotoImage(file="door_schoonmaker_closed.png")
        global ddoor3
        if firestate:
            print("This door is open")
        else:
            if ddoor3 == False:
                cid = python_code_for_reading_uid.readArduino()
                var = UseDatabase.check(cid, 3)
                if var == True:
                    door3.configure(image=doorO)
                    door3.image = doorO
                    ddoor3 = True
                else:
                    tkinter.messagebox.showerror("Geen toegang", "U bent niet bevoegd om deze deur te openen")
            else:
                door3.configure(image=doorC)
                door3.image = doorC
                ddoor3 = False


    def door4Func():
        doorO = PhotoImage(file="door_1_open.png")
        doorC = PhotoImage(file="door_1_closed.png")
        global ddoor4
        if firestate:
            print("this door is open")
        else:
            if ddoor4 == False:
                cid = python_code_for_reading_uid.readArduino()
                var = UseDatabase.check(cid, 4)
                if var == True:
                    door4.configure(image=doorO)
                    door4.image = doorO
                    ddoor4 = True
                else:
                    tkinter.messagebox.showerror("Geen toegang", "U bent niet bevoegd om deze deur te openen")
            else:
                door4.configure(image=doorC)
                door4.image = doorC
                ddoor4 = False


    def door5Func():
        doorO = PhotoImage(file="door_2_open.png")
        doorC = PhotoImage(file="door_2_closed.png")
        global ddoor5
        if firestate:
            print("This door is open")
        else:
            if ddoor5 == False:
                cid = python_code_for_reading_uid.readArduino()
                var = UseDatabase.check(cid, 5)
                if var == True:
                    door5.configure(image=doorO)
                    door5.image = doorO
                    ddoor5 = True
                else:
                    tkinter.messagebox.showerror("Geen toegang", "U bent niet bevoegd om deze deur te openen")
            else:
                door5.configure(image=doorC)
                door5.image = doorC
                ddoor5 = False


    def door6Func():
        doorO = PhotoImage(file="door_3_open.png")
        doorC = PhotoImage(file="door_3_closed.png")
        global ddoor6
        if firestate:
            print("This door is open")
        else:
            if ddoor6 == False:
                cid = python_code_for_reading_uid.readArduino()
                var = UseDatabase.check(cid, 6)
                if var == True:
                    door6.configure(image=doorO)
                    door6.image = doorO
                    ddoor6 = True
                else:
                    tkinter.messagebox.showerror("Geen toegang", "U bent niet bevoegd om deze deur te openen")
            else:
                door6.configure(image=doorC)
                door6.image = doorC
                ddoor6 = False


    def door7Func():
        doorO = PhotoImage(file="door_4_open.png")
        doorC = PhotoImage(file="door_4_closed.png")
        global ddoor7
        if firestate:
            print("This door is open")
        else:
            if ddoor7 == False:
                cid = python_code_for_reading_uid.readArduino()
                var = UseDatabase.check(cid, 7)
                if var == True:
                    door7.configure(image=doorO)
                    door7.image = doorO
                    ddoor7 = True
                else:
                    tkinter.messagebox.showerror("Geen toegang", "U bent niet bevoegd om deze deur te openen")
            else:
                door7.configure(image=doorC)
                door7.image = doorC
                ddoor7 = False


    def en_card():
        naam = UseDatabase.activeer_cid(python_code_for_reading_uid.readArduino())
        if naam:
            UseDatabase.activeer_cid(string_int(entryEnableID.get()))
            popup("%s is geactiveerd" % naam)
        else:
            popup("Gebruiker ID bestaat niet of is al geactiveerd")


    def dis_card():
        naam = UseDatabase.deactiveer_cid(python_code_for_reading_uid.readArduino())
        if naam:
            UseDatabase.deactiveer_uid(string_int(entryDisableID.get()))
            popup("%s is gedeactiveerd" % naam)
        else:
            popup("Gebruiker ID bestaat niet of is al gedeactiveerd")


    def dis_user():
        if string_int(entryDisableID.get()) != -1:
            naam = UseDatabase.deactiveer_uid(string_int(entryDisableID.get()))
            if naam:
                UseDatabase.deactiveer_uid(string_int(entryDisableID.get()))
                popup("%s is gedeactiveerd" % naam)
            else:
                popup("Gebruiker ID bestaat niet of is al gedeactiveerd")
        else:
            tkinter.messagebox.showerror("Ongeldige invoer", "Gebruiker ID moet een integer zijn")


    def en_user():
        if string_int(entryEnableID.get()) != -1:
            naam = UseDatabase.activeer_uid(string_int(entryEnableID.get()))
            if naam:
                popup("%s is geactiveerd" % naam)
            else:
                popup("Gebruiker ID bestaat niet of is al geactiveerd")
        else:
            tkinter.messagebox.showerror("Ongeldige invoer", "Gebruiker ID moet een integer zijn")


    def string_int(string):
        try:
            int(string)
            return int(string)
        except ValueError:
            return -1


    def delete_from_db():
        if string_int(entryDeleteID.get()) != -1:
            naam = UseDatabase.delete(string_int(entryDeleteID.get()))
            if naam:
                popup("%s is verwijderd" % naam)
            else:
                popup("Gebruiker ID bestaat niet")
        else:
            tkinter.messagebox.showerror("Ongeldige invoer", "Gebruiker ID moet een integer zijn")


    def search_name_gui():
        var1 = entryName1.get()
        if var1:
            popup_search_name(UseDatabase.search_name(var1))
        else:
            tkinter.messagebox.showerror("Geen invoer", "Er moet iets worden ingevoerd")


    def search_cid_gui():
        var1 = (python_code_for_reading_uid.readArduino())
        popup_search_name(UseDatabase.search_cid(string_int(var1)))


    def search_rights_gui():
        var1 = entryRights1.get()
        if var1:
            searchresults = UseDatabase.search_rights(var1)
            if searchresults:
                popup_search_rights(searchresults)
        else:
            tkinter.messagebox.showerror("Geen invoer", "Er moet iets worden ingevoerd")


    def opendoor():
        global ddoor1
        global ddoor2
        global ddoor3
        global ddoor4
        global ddoor5
        global ddoor6
        global ddoor7
        doorO_eigenaar = PhotoImage(file="door_eigenaar_open.png")
        doorO_beveiliging = PhotoImage(file="door_security_open.png")
        doorO_janitor = PhotoImage(file="door_schoonmaker_open.png")
        doorO_guest1 = PhotoImage(file="door_1_open.png")
        doorO_guest2 = PhotoImage(file="door_2_open.png")
        doorO_guest3 = PhotoImage(file="door_3_open.png")
        doorO_guest4 = PhotoImage(file="door_4_open.png")
        var1 = string_int(entryOpendeur.get())
        if var1:
            UseDatabase.opendoor(var1)
            if var1 == 1:
                door1.configure(image=doorO_eigenaar)
                door1.image = doorO_eigenaar
                ddoor1 = True
            elif var1 == 2:
                door2.configure(image=doorO_beveiliging)
                door2.image = doorO_beveiliging
                ddoor2 = True
            elif var1 == 3:
                door3.configure(image=doorO_janitor)
                door3.image = doorO_janitor
                ddoor3 = True
            elif var1 == 4:
                door4.configure(image=doorO_guest1)
                door4.image = doorO_guest1
                ddoor4 = True
            elif var1 == 5:
                door5.configure(image=doorO_guest2)
                door5.image = doorO_guest2
                ddoor51 = True
            elif var1 == 6:
                door6.configure(image=doorO_guest3)
                door6.image = doorO_guest3
                ddoor6 = True
            elif var1 == 7:
                door7.configure(image=doorO_guest4)
                door7.image = doorO_guest4
                ddoor7 = True


    def closedoor():
        if firestate:
            popup("Het brandalarm staat aan, doe geen deuren dicht!")
            return False
        global ddoor1
        global ddoor2
        global ddoor3
        global ddoor4
        global ddoor5
        global ddoor6
        global ddoor7
        doorC_eigenaar = PhotoImage(file="door_eigenaar_closed.png")
        doorC_beveiliging = PhotoImage(file="door_security_closed.png")
        doorC_janitor = PhotoImage(file="door_schoonmaker_closed.png")
        doorC_guest1 = PhotoImage(file="door_1_closed.png")
        doorC_guest2 = PhotoImage(file="door_2_closed.png")
        doorC_guest3 = PhotoImage(file="door_3_closed.png")
        doorC_guest4 = PhotoImage(file="door_4_closed.png")
        var1 = string_int(entrySluitdeur.get())
        if var1:
            UseDatabase.opendoor(var1)
            if var1 == 1:
                door1.configure(image=doorC_eigenaar)
                door1.image = doorC_eigenaar
                ddoor1 = False
            elif var1 == 2:
                door2.configure(image=doorC_beveiliging)
                door2.image = doorC_beveiliging
                ddoor2 = False
            elif var1 == 3:
                door3.configure(image=doorC_janitor)
                door3.image = doorC_janitor
                ddoor3 = False
            elif var1 == 4:
                door4.configure(image=doorC_guest1)
                door4.image = doorC_guest1
                ddoor4 = False
            elif var1 == 5:
                door5.configure(image=doorC_guest2)
                door5.image = doorC_guest2
                ddoor5 = False
            elif var1 == 6:
                door6.configure(image=doorC_guest3)
                door6.image = doorC_guest3
                ddoor6 = False
            elif var1 == 7:
                door7.configure(image=doorC_guest4)
                door7.image = doorC_guest4
                ddoor7 = False


    def add_user():
        var2, var3 = entryName2.get(), entryRights2.get()
        if var2 and var3:
            var1 = (python_code_for_reading_uid.readArduino())
            var4 = UseDatabase.add(var1, var2, var3)
            if var4:
                tid = var4[1]
                if var3 == 'Gast':
                    popup("%s toegevoegd, het kamernummer is %i" % (var2, tid-3))
                else:
                    popup("%s toegevoegd" % var2)
            else:
                popup("Geen kamer vrij")
        else:
            tkinter.messagebox.showerror("Geen invoer", "Er moet wat worden ingevoerd")


    def popup(string):
        top = Toplevel()
        top.title("Resultaten")
        top.focus_set()

        Message(top, text=string).pack()
        Button(top, text="OK", command=top.destroy).pack()


    def popup_search_name(data):
        top = Toplevel()
        top.title("Zoekresultaten")
        top.focus_set()

        if data != 0:
            for x in range(0, len(data)):
                name = "Naam: %s" % data[x][2]
                uid = "UID: %s" % data[x][0]
                cid = "Pasjes ID: %s" % data[x][1]
                if data[x][3] == 1:
                    rights = "Rechten: Gast"
                elif data[x][3] == 2:
                    rights = "Rechten: Schoonmaker"
                elif data[x][3] == 3:
                    rights = "Rechten: Beveiliger"
                elif data[x][3] == 4:
                    rights = "Rechten: Eigenaar"
                access = "Kaart staat: %s" % data[x][4]

                Message(top, text=name, width=500, anchor=NE).pack()
                Message(top, text=uid, width=500, anchor=NE).pack()
                Message(top, text=cid, width=500, anchor=NE).pack()
                Message(top, text=rights, width=500, anchor=NE).pack()
                Message(top, text=access, width=500, anchor=NE).pack()
                Message(top, text=" ", width=500).pack()

            top.geometry('{}x{}'.format(300, 300))
        else:
            Message(top, text="Persoon niet gevonden", width=500, anchor=NE).pack()


    def popup_search_rights(data):
        if data != 0:
            top = Toplevel()
            top.title("Zoekresultaten")
            top.focus_set()

            for x in range(0, len(data)):
                name = "Naam: %s" % data[x][2]
                uid = "UID: %s" % data[x][0]
                cid = "Pasjes ID: %s" % data[x][1]
                if data[x][3] == 1:
                    rights = "Rechten: Gast"
                elif data[x][3] == 2:
                    rights = "Rechten: Schoonmaker"
                elif data[x][3] == 3:
                    rights = "Rechten: Beveiliger"
                elif data[x][3] == 4:
                    rights = "Rechten: Eigenaar"
                access = "Kaart staat: %s" % data[x][4]

                Message(top, text=name, width=500, anchor=NE).pack()
                Message(top, text=uid, width=500, anchor=NE).pack()
                Message(top, text=cid, width=500, anchor=NE).pack()
                Message(top, text=rights, width=500, anchor=NE).pack()
                Message(top, text=access, width=500, anchor=NE).pack()
                Message(top, text=" ", width=500).pack()

            top.geometry('{}x{}'.format(300, 300))


    def popup_get_history(data):
        top = Toplevel()
        top.title("Resultaten")
        top.focus_set()
        scrollbar = Scrollbar(top)
        lbname = Listbox(top, yscrollcommand=scrollbar.set)
        lbcid = Listbox(top, yscrollcommand=scrollbar.set)
        lbdate = Listbox(top, yscrollcommand=scrollbar.set)
        lbtid = Listbox(top, yscrollcommand=scrollbar.set)

        if data:
            lbname.insert(END, "Naam:")
            lbcid.insert(END, "Card ID:")
            lbdate.insert(END, "Datum:")
            lbtid.insert(END, "Deur:")
            for x in range(0, len(data)):
                lbname.insert(END, data[x+2][0])
                lbcid.insert(END, data[x+2][1])
                lbdate.insert(END, data[x+2][2])
                lbtid.insert(END, data[x+2][3])
        else:
            lbname.insert(END, "Geen Data")
        lbname.grid(collumn=1)
        lbcid.grid(collumn=2)
        lbdate.grid(collumn=3)
        lbtid.grid(collumn=4)
        scrollbar.grid(collumn=5, fill=Y)
        scrollbar.config(command=(lbname.yview, lbcid.yview, lbdate.yview, lbtid.yview))

    root.title("Hotel Management")
    root.resizable(0, 0)

    leftFrame = Frame(root)
    rightFrame = Frame(root)
    leftFrame.pack(side=LEFT, anchor=NW)
    rightFrame.pack(side=RIGHT, anchor=NW)

    inputVar1 = ""  # Search name
    inputVar2 = ""  # Search rights
    inputVar3 = ""  # Input name
    inputVar4 = ""  # Input rights
    inputVar5 = ""  # Input Delete UID
    inputVar6 = ""  # Disable UID
    inputVar7 = ""  # Enable UID
    inputVar8 = ""  # History name
    inputVar9 = ""  # History rights
    inputVar10 = "" # History terminal
    inputVar11 = "" # Open door
    inputVar12 = "" # Close door

    doorStartEigenaar = PhotoImage(file="door_eigenaar_closed.png")
    doorStartbeveiliging = PhotoImage(file="door_security_closed.png")
    doorStartjanitor = PhotoImage(file="door_schoonmaker_closed.png")
    doorStartguest1 = PhotoImage(file="door_1_closed.png")
    doorStartguest2 = PhotoImage(file="door_2_closed.png")
    doorStartguest3 = PhotoImage(file="door_3_closed.png")
    doorStartguest4 = PhotoImage(file="door_4_closed.png")
    fire = PhotoImage(file="fire.png")

    door1 = Button(rightFrame, image=doorStartEigenaar, command=door1Func)
    door2 = Button(rightFrame, image=doorStartbeveiliging, command=door2Func)
    door3 = Button(rightFrame, image=doorStartjanitor, command=door3Func)
    door4 = Button(rightFrame, image=doorStartguest1, command=door4Func)
    door5 = Button(rightFrame, image=doorStartguest2, command=door5Func)
    door6 = Button(rightFrame, image=doorStartguest3, command=door6Func)
    door7 = Button(rightFrame, image=doorStartguest4, command=door7Func)
    history = Button(rightFrame, text="Geschiedenis", command=get_history)

    buttonSearchName = Button(leftFrame, text="Zoek", command=search_name_gui, width=6)
    buttonSearchCID = Button(leftFrame, text="Zoek", command=search_cid_gui, width=6)
    buttonSearchRights = Button(leftFrame, text="Zoek", command=search_rights_gui, width=6)

    entryName1 = Entry(leftFrame, textvariable=inputVar1)
    labelName1 = Label(leftFrame, text="Naam")
    # entryCID1 = Entry(leftFrame, textvariable=inputVar2)
    labelCID1 = Label(leftFrame, text="Gebruiker ID")
    entryRights1 = Entry(leftFrame, textvariable=inputVar2)
    labelRights1 = Label(leftFrame, text="Rechten")

    entryDeleteID = Entry(leftFrame, textvariable=inputVar5)
    labelDeleteID = Label(leftFrame, text="Gebruiker ID")
    buttonDeleteID = Button(leftFrame, text="Verwijder", command=delete_from_db, width=6)

    buttonEnter = Button(leftFrame, text="Enter", command=add_user, height=3, width=6)
    entryName2 = Entry(leftFrame, textvariable=inputVar3)
    labelName2 = Label(leftFrame, text="Naam")
    entryRights2 = Entry(leftFrame, textvariable=inputVar4)
    labelRights2 = Label(leftFrame, text="Rechten")

    labelSearch = Label(leftFrame, text="Zoek op naam, gebruiker ID of rechten")
    labelEnter = Label(leftFrame, text="Voeg iemand toe aan de database")
    labelDelete = Label(leftFrame, text="Verwijder iemand uit de database")

    door1Label = Label(rightFrame, text="1. Directiekamer")
    door2Label = Label(rightFrame, text="2. Beveiligingskamer")
    door3Label = Label(rightFrame, text="3. Schoonmaakhok")
    door4Label = Label(rightFrame, text="4. Gastkamer 1")
    door5Label = Label(rightFrame, text="5. Gastkamer 2")
    door6Label = Label(rightFrame, text="6. Gastkamer 3")
    door7Label = Label(rightFrame, text="7. Gastkamer 4")

    Whitespace1 = Label(leftFrame, text=" ")
    Whitespace2 = Label(leftFrame, text=" ")
    Whitespace3 = Label(leftFrame, text=" ")
    Whitespace4 = Label(leftFrame, text=" ")
    Whitespace5 = Label(leftFrame, text=" ")
    Whitespace6 = Label(leftFrame, text=" ")
    Whitespace7 = Label(rightFrame, text=" ")
    Whitespace8 = Label(rightFrame, text=" ")
    Whitespace9 = Label(leftFrame, text=" ")

    labelDisableID = Label(leftFrame, text="Gebruiker ID")
    labelDisable = Label(leftFrame, text="Deactiveer iemand in de database")
    entryDisableID = Entry(leftFrame, textvariable=inputVar6)
    disableButton = Button(leftFrame, text="Deactiveer", command=dis_user, width=6)
    labelEnableID = Label(leftFrame, text="Gebruiker ID")
    labelEnable = Label(leftFrame, text="Activeer iemand in de database")
    entryEnableID = Entry(leftFrame, textvariable=inputVar7)
    enableButton = Button(leftFrame, text="Activeer", command=en_user, width=6)

    labelENDIS = Label(leftFrame, text="Activeer of deactiveer met behulp van een pasje")
    buttonEN = Button(leftFrame, text="Activeer", command=en_card, width=7)
    buttonDIS = Button(leftFrame, text="Deactiveer", command=dis_card, width=7)

    buttonFire = Button(rightFrame, image=fire, command=emergency)
    labelFire = Label(rightFrame, text="Brand")

    labelHistory = Label(leftFrame, text="Doorzoek geschiedenis")
    labelHistoryName = Label(leftFrame, text="Naam")
    labelHistoryCID = Label(leftFrame, text="Pasjes ID")
    labelHistoryRights = Label(leftFrame, text="Rechten")
    labelHistoryTerminal = Label(leftFrame, text="Deur")
    entryHistoryName = Entry(leftFrame, textvariable=inputVar8)
    entryHistoryRights = Entry(leftFrame, textvariable=inputVar9)
    entryHistoryTerminal = Entry(leftFrame, textvariable=inputVar10)
    buttonHistoryName = Button(leftFrame, text="Zoek", command=get_history_name)
    buttonHistoryCID = Button(leftFrame, text="Zoek", command=get_history_cid)
    buttonHistoryRights = Button(leftFrame, text="Zoek", command=get_history_rights)
    buttonHistoryTerminal = Button(leftFrame, text="Zoek", command=get_history_terminal)

    labelOpendeur = Label(rightFrame, text="Open deur")
    entryOpendeur = Entry(rightFrame, textvariable=inputVar11)
    buttonOpendeur = Button(rightFrame, text="Open", command=opendoor)

    labelSluitdeur = Label(rightFrame, text="Sluit deur")
    entrySluitdeur = Entry(rightFrame, textvariable=inputVar12)
    buttonSluitdeur = Button(rightFrame, text="Sluit", command=closedoor)

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
    #entryCID1.grid(row=3, column=1)
    labelRights1.grid(row=4, column=0, sticky=E)
    entryRights1.grid(row=4, column=1)

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

    labelOpendeur.grid(row=11, column=0)
    entryOpendeur.grid(row=11, column=1)
    buttonOpendeur.grid(row=11, column=2)
    labelSluitdeur.grid(row=12, column=0)
    entrySluitdeur.grid(row=12, column=1)
    buttonSluitdeur.grid(row=12, column=2)

    Whitespace7.grid(row=0, column=0)
    Whitespace8.grid(row=0, column=3)

    door1Label.grid(row=1, column=1)
    door2Label.grid(row=2, column=1)
    door3Label.grid(row=3, column=1)
    door4Label.grid(row=4, column=1)
    door5Label.grid(row=5, column=1)
    door6Label.grid(row=6, column=1)
    door7Label.grid(row=7, column=1)

    labelHistory.grid(row=24, column=1)
    labelHistoryName.grid(row=25, column=0)
    entryHistoryName.grid(row=25, column=1)
    buttonHistoryName.grid(row=25, column=2)
    labelHistoryCID.grid(row=26, column=0)
    buttonHistoryCID.grid(row=26, column=2)
    labelHistoryRights.grid(row=27, column=0)
    entryHistoryRights.grid(row=27, column=1)
    buttonHistoryRights.grid(row=27, column=2)
    labelHistoryTerminal.grid(row=28, column=0)
    entryHistoryTerminal.grid(row=28, column=1)
    buttonHistoryTerminal.grid(row=28, column=2)


    root.mainloop()
else:
    print("Tot ziens")
