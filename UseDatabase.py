__author__ = 'Joël'


import sqlite3
conn = sqlite3.connect('data.db')
import tkinter.messagebox
from time import strftime

c = conn.cursor()


def check(cid, tid=1):
    c.execute("""SELECT UID from persoon where CID = %i""" % cid)
    uid = c.fetchall()[0][0]
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
        print('Deze Card ID staat niet in de database, of de kaart is gedisabled.')
        return False
    elif persoon > rechten:
        print('Open deur!')
        opendoor(uid, tid)
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
                    opendoor(uid, tid)
                    return True
            elif not terminal:
                print("Deze gebruiker mag deze deur niet in.")
                return False
        else:
            c.execute("""SELECT Rechten from terminal WHERE TID = %i""" % tid)
            terminal = c.fetchall()
            terminal = terminal[0][0]
            if persoon >= terminal:
                print("Welkom!")
                opendoor(uid, tid)
                return True
    else:
        print("Toegang geweigerd. Ongeautoriseerde gebruiker.")
        return False

#functie om nieuwe users toe te voegen
def add(cid, naam, rechten):
    if naam == '':
        tkinter.messagebox.showerror("Incorrecte input", "Vul een naam in")
    elif rechten == '':
        tkinter.messagebox.showerror("Incorrecte input", "Vul rechten in.")
    elif rechten != 'Eigenaar' and rechten != 'Gast' and rechten != 'Schoonmaker' and rechten != 'Beveiliging':
        tkinter.messagebox.showerror("Incorrecte input", "Vul een van de volgende rechten in: Eigenaar, Gast, Schoonmaker, Beveiliging")
    c.execute("""SELECT COUNT(UID) from persoon""")
    uid = c.fetchall()[0][0]+1
    c.execute("""INSERT INTO persoon VALUES (%i, %i, '%s', '%i', 'Aan') """ % (uid, cid, naam, rechten))
    conn.commit()
    print(Naam, ' toegevoegd')


# functie om users te verwijderen
def delete(uid):
    c.execute("""SELECT UID from persoon WHERE UID = %i """ % uid)
    uidlist = c.fetchall()
    if uidlist:
        c.execute("""SELECT Naam from persoon WHERE UID = %i """ % uid)
        naam = c.fetchall()[0][0]
        c.execute("""SELECT COUNT(UID) from persoon""")
        # Zet het element op de laatste index op de index van het verwijderde element.
        lastuid = c.fetchall()[0][0]
        c.execute("""DELETE from persoon WHERE UID=%i """ % Uid)
        c.execute("""UPDATE persoon SET UID = %i WHERE UID = %i""" % (uid, lastuid))
        print(naam, 'verwijderd')
    else:
        print('Invalid User ID')
    conn.commit()


def activeer(cid):
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


def deactiveer(cid):
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


def search_naam(naam):
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
        print(data)
        return data
    else:
        print('not found.')
        return False


def search_uid(uid):
    c.execute("""SELECT * from persoon WHERE UID = %i""" % uid)
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


def search_rechten(rechten):
    c.execute("""SELECT * from persoon WHERE Rechten LIKE '%%%s%%'""" % rechten)
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


def opendoor(uid, tid):
    time = strftime("%Y-%m-%d %H:%M:%S")
    c.execute("""SELECT cid from persoon WHERE uid = %i""" % uid)
    cid = c.fetchall()[0][0]
    print(cid)
    c.execute("""INSERT INTO history VALUES (%i, %i, '%s', %i)""" % (uid, cid, time, tid))
    c.execute("""select * from history""")
    print(c.fetchall())
    conn.commit()



# Idee: Een knop/functie die voor 1 terminal de deur opent in geval van nood waarbij niet alle deuren openhoeven
# Je vult 1 terminal ID in, die deur gaat open, als je weer op de knop drukt gaat hij weer dicht.

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.

check(3529442660, 3)