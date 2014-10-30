__author__ = 'Joël'

import sqlite3

conn = sqlite3.connect('data.db')
import tkinter.messagebox
from time import strftime

c = conn.cursor()


#Functie om te controleren of de gebruiker de deur mag openen
def check(cid, tid=1):
    if cid == 1189998819991197253:
        print("Er gaat een deur open door het brandalarm, namelijk deur", tid)
        return True
    c.execute("""SELECT Naam from persoon where CID = %i""" % cid)
    naam = c.fetchall()
    if naam:
        naam = naam[0][0]
    else:
        print("De Card ID staat niet in de database")
        return False
    c.execute("""SELECT Rechten from persoon WHERE CID = %i AND Access='Aan' """ % cid)
    persoon = c.fetchall()
    c.execute("""SELECT Rechten from terminal where TID = %i""" % tid)
    rechten = c.fetchall()
    if rechten:
        rechten = rechten[0][0]
    else:
        print("Deze terminal bestaat niet")
        return False
    if persoon:
        persoon = persoon[0][0]
    if not persoon:
        print('Deze Card ID is gedisabled.')
        return False
    elif persoon > rechten:
        print('Welkom!')
        addhistory(naam, tid)
        return True
    elif persoon == rechten:
        c.execute("""SELECT cid FROM terminal WHERE tid = %i""" % tid)
        temp = c.fetchall()
        temp = temp[0][0]
        if temp != 0:
            c.execute("""SELECT Rechten from terminal WHERE TID = %i AND cid = %i""" % (tid, cid))
            terminal = c.fetchall()
            if terminal:
                terminal = terminal[0][0]
                if temp == cid:
                    print("Welkom!")
                    addhistory(naam, tid)
                    return True
            elif not terminal:
                print("Toegang geweigerd. Ongeautoriseerde gebruiker.")
                return False
        else:
            c.execute("""SELECT Rechten from terminal WHERE TID = %i""" % tid)
            terminal = c.fetchall()
            terminal = terminal[0][0]
            if persoon >= terminal:
                print("Welkom!")
                addhistory(naam, tid)
                return True
    else:
        print("Toegang geweigerd. Ongeautoriseerde gebruiker.")
        return False

#Is er een kamer vrij?
#Rechten in nieuwe gast = 1
#Rechten in terminal = 1
#CID in terminal = 0
#Return TID
#else false

def check_kamer():
    c.execute("""SELECT TID from terminal where rechten = 1 AND CID = 0""")
    temp = c.fetchall()
    if temp:
        return temp[0][0]
    else:
        return False


# Functie om nieuwe users toe te voegen aan de database
def add(cid, naam, rechten):
    rechtnum = 0
    if naam == '':
        tkinter.messagebox.showerror("Incorrecte input", "Vul een naam in")
    elif rechten == '':
        tkinter.messagebox.showerror("Incorrecte input", "Vul rechten in.")
    elif rechten != 'Eigenaar' and rechten != 'Gast' and rechten != 'Schoonmaker' and rechten != 'Beveiliging':
        tkinter.messagebox.showerror("Incorrecte input",
                                     "Vul een van de volgende rechten in: Eigenaar, Gast, Schoonmaker, Beveiliging")
        return False
    if rechten == 'Eigenaar':
        rechtnum = 4
    elif rechten == 'Gast':
        rechtnum = 1
        if check_kamer():
            tid = check_kamer()
            print("Je kamernummer is", tid-3)
            c.execute("""UPDATE terminal SET cid = %i WHERE TID = %i""" % (cid, tid))
        else:
            print("Er is geen kamer vrij.")
            return False
    elif rechten == 'Schoonmaker':
        rechtnum = 2
    elif rechten == 'Beveiliging':
        rechtnum = 3

    c.execute("""SELECT COUNT(UID) from persoon""")
    uid = c.fetchall()[0][0] + 1
    if rechtnum:
        c.execute("""INSERT INTO persoon VALUES (%i, %i, '%s', '%i', 'Aan') """ % (uid, cid, naam, rechtnum))
    conn.commit()
    print(naam, ' toegevoegd')

# Functie om users te verwijderen uit de database
def delete(uid):
    # Controleer of er überhaupt een gebruiker is met die uid
    c.execute("""SELECT UID from persoon WHERE UID = %i """ % uid)
    uidlist = c.fetchall()
    # Als die er wel is:
    if uidlist:
        # Selecteer de naam die bij de UID hoort
        c.execute("""SELECT Naam from persoon WHERE UID = %i """ % uid)
        naam = c.fetchall()[0][0]
        # Controleer of het een gast is
        c.execute("""SELECT rechten from persoon where UID = %i""" % uid)
        rechten = c.fetchall()[0][0]
        if rechten == 1:
            c.execute("""SELECT TID from terminal where CID IN (SELECT CID FROM persoon WHERE UID = %i)""" % uid)
            tid = c.fetchall()
            if tid:
                tid = tid[0][0]
            else:
                print("There is no such terminal!")
            c.execute("""UPDATE terminal SET CID = 0 WHERE TID = %i""" % tid)
        # Zet het element op de laatste index op de index van het verwijderde element.
        c.execute("""SELECT COUNT(UID) from persoon""")
        lastuid = c.fetchall()[0][0]
        c.execute("""DELETE from persoon WHERE UID=%i """ % uid)
        c.execute("""UPDATE persoon SET UID = %i WHERE UID = %i""" % (uid, lastuid))
        print(naam, 'verwijderd')
        # Als die gebruiker er niet is:
    else:
        print('Invalid User ID')
    conn.commit()


# Functie om een pasje te activeren die al in de database staat
def activeer_cid(cid):
    c.execute("""SELECT Naam FROM persoon WHERE CID = %i AND Access = 'Uit'""" % cid)
    naamtupel = c.fetchall()
    if naamtupel:
        c.execute("""UPDATE persoon SET Access = 'Aan' WHERE CID = %i """ % cid)
        naam = naamtupel[0][0]
        print('Het pasje van', naam, 'staat nu aan!')
        return naam
    else:
        print('Card ID bestaat niet of staat al aan.')
    conn.commit()


# Functie om een pasje te activeren die al in de database staat
def activeer_uid(uid):
    c.execute("""SELECT Naam FROM persoon WHERE UID = %i AND Access = 'Uit'""" % uid)
    naamtupel = c.fetchall()
    if naamtupel:
        c.execute("""UPDATE persoon SET Access = 'Aan' WHERE UID = %i """ % uid)
        naam = naamtupel[0][0]
        print('Het pasje van', naam, 'staat nu aan!')
        return naam
    else:
        print('User ID bestaat niet of staat al aan.')
    conn.commit()


# Functie om een pasje te deactiveren
def deactiveer_uid(uid):
    c.execute("""SELECT Naam FROM persoon WHERE UID = %i AND Access = 'Aan'""" % uid)
    naamtupel = c.fetchall()
    if naamtupel:
        c.execute("""UPDATE persoon SET Access = 'Uit' WHERE UID = %i""" % uid)
        naam = naamtupel[0][0]
        print('Het pasje van', naam, 'staat nu uit!')
        return naam
    else:
        print('User ID bestaat niet of staat al uit.')
    conn.commit()


# Functie om een pasje te deactiveren
def deactiveer_cid(cid):
    c.execute("""SELECT Naam FROM persoon WHERE CID = %i AND Access = 'Aan'""" % cid)
    naamtupel = c.fetchall()
    if naamtupel:
        c.execute("""UPDATE persoon SET Access = 'Uit' WHERE CID = %i""" % cid)
        naam = naamtupel[0][0]
        print('Het pasje van', naam, 'staat nu uit!')
        return naam
    else:
        print('Card ID bestaat niet of staat al uit.')
    conn.commit()


# Functie om naar een naam te zoeken in de database
def search_name(naam):
    c.execute("""SELECT * from persoon WHERE Naam LIKE '%%%s%%'""" % naam)
    data = c.fetchall()
    if data:
        for x in range(0, len(data)):
            print('')
            print('Naam = ', data[x][2])
            print('Rechten = ', data[x][3])
            print('CID = ', data[x][1])
            print('UID = ', data[x][0])
            print('Access = ', data[x][4])
        # print(data)
        return data
    else:
        print('not found.')
        return False


# Functie om naar een uid te zoeken in  de database
def search_cid(cid):
    c.execute("""SELECT * from persoon WHERE CID = %i""" % cid)
    data = c.fetchall()
    if data:
        for x in range(0, len(data)):
            print('')
            print('Naam = ', data[x][2])
            print('Rechten = ', data[x][3])
            print('CID = ', data[x][1])
            print('UID = ', data[x][0])
            print('Access = ', data[x][4])
        return data
    else:
        print('not found.')
        return False


# Functie om naar rechten te zoeken in de database
def search_rights(rechten):
    rechtnum = 0
    if rechten == '':
        tkinter.messagebox.showerror("Incorrecte input", "Vul rechten in.")
        return False
    elif rechten != 'Eigenaar' and rechten != 'Gast' and rechten != 'Schoonmaker' and rechten != 'Beveiliging':
        tkinter.messagebox.showerror("Incorrecte input",
                                     "Vul een van de volgende rechten in: Eigenaar, Gast, Schoonmaker, Beveiliging")
        return False
    elif rechten == 'Gast':
        rechtnum = 1
    elif rechten == 'Schoonmaker':
        rechtnum = 2
    elif rechten == 'Beveiliging':
        rechtnum = 3
    elif rechten == 'Eigenaar':
        rechtnum = 4
    c.execute("""SELECT * from persoon WHERE Rechten LIKE '%%%s%%'""" % rechtnum)
    data = c.fetchall()
    if data:
        for x in range(0, len(data)):
            print('')
            print('Naam = ', data[x][2])
            print('Rechten = ', data[x][3])
            print('CID = ', data[x][1])
            print('UID = ', data[x][0])
            print('Access = ', data[x][4])
        return data
    else:
        print('not found.')
        return False


# Functie om de naam van een entry in de database te veranderen
def verander_naam(naam, nieuwenaam):
    data = search_naam(naam)
    if len(data) > 1:
        print("Er zijn meerdere mensen met deze naam!")
        return "Niets veranderd."
    elif len(data) == 0:
        print("Er is niemand met deze naam!")
        return "Niets veranderd."
    data = data[0][0]
    c.execute("""UPDATE persoon SET naam = '%s' WHERE uid = %i""" % (nieuwenaam, data))
    print(naam, "is van naam veranderd. Hij/zij heet nu", nieuwenaam)
    return "Naam is veranderd."


# Functie die een entry toevoegt aan de database als een deur open gaat
def addhistory(naam, tid):
    time = strftime("%Y-%m-%d %H:%M:%S")
    c.execute("""SELECT cid from persoon WHERE naam = '%s'""" % naam)
    cid = c.fetchall()
    if cid:
        cid = cid[0][0]
    else:
        print("Deze gebruiker bestaat niet, lul!")
        return False
    c.execute("""INSERT INTO history VALUES ('%s', %i, '%s', %i)""" % (naam, cid, time, tid))
    conn.commit()


# Functie die de history-tabel van de database opvraagt.
def gethistory():
    c.execute("""SELECT * from history""")
    history = c.fetchall()
    return history


# Functie die in de history-tabel zoekt.
def searchhistory_name(naam):
    match = search_name(naam)
    print(match)
    if match:
        c.execute("""SELECT * from HISTORY where naam LIKE '%%%s%%'""" % naam)
        test = c.fetchall()
        if test:
            print(test)
            return test
        else:
            print("No results.")
            return False
    else:
        print('Name not found.')
        return False
    return match


def searchhistory_cid(cid):
    c.execute("""SELECT * FROM history WHERE CID = %i""" % cid)
    result = c.fetchall()
    print(result)
    return result


def searchhistory_tid(tid):
    c.execute("""SELECT * from history where tid = %i""" % tid)
    temp = c.fetchall()
    return temp


def searchhistory_rights(rechten):
    rechtnum = 0
    if rechten == 'Gast':
        rechtnum = 1
    elif rechten == 'Schoonmaker':
        rechtnum = 2
    elif rechten == 'Beveiliging':
        rechtnum = 3
    elif rechten == 'Eigenaar':
        rechtnum = 4
    elif rechten != 'Eigenaar' and rechten != 'Gast' and rechten != 'Schoonmaker' and rechten != 'Beveiliging':
        tkinter.messagebox.showerror("Incorrecte input",
                                     "Vul een van de volgende rechten in: Eigenaar, Gast, Schoonmaker, Beveiliging")
        return False
    data = search_rechten(rechten)
    if data:
        c.execute("""SELECT * FROM history WHERE Naam IN (SELECT Naam from persoon where Rechten = %i)""" % rechtnum)
        result = c.fetchall()
        print(result)
        return result
    else:
        print("Er is niemand met deze rechten!")
        return False


# Forces door of terminal TID open.
def opendoor(tid):
    Door = check(1189998819991197253, tid)
    return Door


# Forces door of terminal TID closed.
def closedoor(tid):
    Door = False
    return Door


# De functie die het brandalarm aan of uit zet.
def fire():
    c.execute("""SELECT count(*) FROM terminal""")
    amountofdoors = c.fetchall()[0][0] + 1
    c.execute("""SELECT Fire from fire""")
    firestate = c.fetchall()[0][0]
    if firestate == 1:
        for x in range(1, amountofdoors):
            closedoor(x)
            print("Er gaat een deur dicht, namelijk deur", x)
        c.execute("""UPDATE fire SET Fire = 0""")
        print("Het brandalarm staat nu weer uit.")
        firestate = 0
    elif firestate == 0:
        for x in range(1, amountofdoors):
            opendoor(x)
        c.execute("""UPDATE fire SET Fire = 1""")
        print("Het brandalarm staat nu aan.")
        firestate = 1
    conn.commit()
    return firestate


# Forces door of terminal TID open.
def opendoor(tid):
    Door = check(1189998819991197253, tid)
    return Door


# Forces door of terminal TID closed.
def closedoor(tid):
    Door = False
    return Door


# Idee: Een knop/functie die voor 1 terminal de deur opent in geval van nood waarbij niet alle deuren openhoeven
# Je vult 1 terminal ID in, die deur gaat open, als je weer op de knop drukt gaat hij weer dicht.

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.