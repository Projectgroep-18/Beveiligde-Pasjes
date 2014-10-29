__author__ = 'Joël'


import sqlite3
conn = sqlite3.connect('data.db')

c = conn.cursor()
# We gaan uit van byteorder = big
userid = 246452191867917525661493  # int.from_bytes(b'3529442660', byteorder='big')


def check(CID, TID=1):
    c.execute("""SELECT Rechten from persoon WHERE CID = %i AND Access='Aan' """ % CID)
    persoon = c.fetchall()
    if persoon:
        persoon = persoon[0][0]
    print("persoon =", persoon)
    c.execute("""SELECT Rechten from terminal WHERE TID = %i""" % TID)
    terminal = c.fetchall()
    if terminal:
        terminal = terminal[0][0]
    else:
        return "Deze deur bestaat niet!"
    print("terminal =", terminal)
    if not persoon:
        print('Deze Card ID staat niet in de database.')
        return False
    elif persoon >= terminal:
        print('Open deur!')
        return True
    else:
        print('Deze gebruiker heeft geen toegang tot deze deur.')
        return False


#functie om nieuwe users toe te voegen
def add(CID, Naam, Rechten):
    c.execute("""SELECT COUNT(UID) from persoon""")
    UID = c.fetchall()[0][0]+1
    c.execute("""INSERT INTO persoon VALUES (%i, %i, '%s', '%s', 'Aan') """ % (UID, CID, Naam, Rechten))
    conn.commit()
    print(Naam, ' toegevoegd')


# functie om users te verwijderen
def delete(CID):
    c.execute("""SELECT UID from persoon WHERE CID = %i """ % CID)
    UIDlist = c.fetchall()
    if UIDlist:
        UID = UIDlist[0][0]
        c.execute("""SELECT Naam from persoon WHERE CID = %i """ % CID)
        Naam = c.fetchall()[0][0]
        c.execute("""SELECT COUNT(CID) from persoon""")
        lastUID = c.fetchall()[0][0]
        c.execute("""DELETE from persoon WHERE CID=%i """ % CID)
        c.execute("""UPDATE persoon SET UID = %i WHERE UID = %i""" % (UID, lastUID))
        print(Naam, 'verwijderd')
    else:
        print('Invalid Card ID')
    conn.commit()


def activeer(CID):
    c.execute("""SELECT Naam FROM persoon WHERE CID = %i AND Access = 'Uit'""" % CID)
    NaamTupel = c.fetchall()
    if NaamTupel:
        c.execute("""UPDATE persoon SET Access = 'Aan' WHERE CID = %i """ % CID)
        Naam = NaamTupel[0][0]
        print('Het pasje van', Naam, 'staat nu aan!')
        return Naam
    else:
        print('Card ID bestaat niet of staat al aan.')
    conn.commit()


def deactiveer(CID):
    c.execute("""SELECT Naam FROM persoon WHERE CID = %i AND Access = 'Aan'""" % CID)
    NaamTupel = c.fetchall()
    if NaamTupel:
        c.execute("""UPDATE persoon SET Access = 'Uit' WHERE CID = %i""" % CID)
        Naam = NaamTupel[0][0]
        print('Het pasje van', Naam, 'staat nu uit!')
        return Naam
    else:
        print('Card ID bestaat niet of staat al uit.')
    conn.commit()



def search_naam(naam):
    c.execute("""SELECT * from persoon WHERE Naam LIKE '%%%s%%'""" % naam)
    data = c.fetchall()
    if data:
        for x in range(0, len(data)):
            print('Naam = ', data[x][2])
            print('Rechten = ', data[x][3])
            print('CID = ', data[x][1])
            print('Access = ', data[x][4])
        return data
    else:
        print('not found.')
        return False


def search_cid(CID):
    c.execute("""SELECT * from persoon WHERE CID = %i""" % CID)
    data = c.fetchall()
    if data:
        for x in range(0, len(data)):
            print('Naam = ', data[x][2])
            print('Rechten = ', data[x][3])
            print('CID = ', data[x][1])
            print('Access = ', data[x][4])
        return data
    else:
        print('not found.')
        return False



def search_rechten(Rechten):
    c.execute("""SELECT * from persoon WHERE Rechten LIKE '%%%s%%'""" % Rechten)
    data = c.fetchall()
    if data:
        for x in range(0, len(data)):
            print('Naam = ', data[x][2])
            print('Rechten = ', data[x][3])
            print('CID = ', data[x][1])
            print('Access = ', data[x][4])
        return data
    else:
        print('not found.')
        return False


# search_rechten('Eigenaar')
# activeer(246452191867917525661493)
# add(123123189371937128937912, 'Jan Jaap', 3)
# delete(241821987043432866395696)
# add(12, 'Piet Pietersen', -1)
# c.execute("""SELECT * from persoon where cid = 12""")
# persoon = c.fetchall()
# print(persoon)
# check(12)
# c.execute("""SELECT * from persoon""")
# persoon = (c.fetchall())
# print(persoon)
search
# Idee: Een knop/functie die voor 1 terminal de deur opent in geval van nood waarbij niet alle deuren openhoeven
# Je vult 1 terminal ID in, die deur gaat open, als je weer op de knop drukt gaat hij weer dicht.

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.