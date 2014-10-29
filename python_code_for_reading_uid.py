import serial
import time
import sqlite3
conn = sqlite3.connect('data.db')
from random import randint
import UseDatabase

c = conn.cursor()

COMPOORT = int(input("De Arduino is aangesloten op COM-poort "))

def check(CID, TID):
    c.execute("""SELECT Rechten from persoon WHERE CID = %i AND Access='Aan' """ % CID)
    persoon = c.fetchall()
    if persoon:
        persoon = persoon[0][0]
    print("persoon =", persoon)
    c.execute("""SELECT Rechten from terminal WHERE TID = %i""" % TID)
    terminal = c.fetchall()
    if terminal:
        terminal = terminal[0][0]
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

while True:
    temp = []
    while not temp:
        TID = int(input("Ik wil graag toegang tot deur "))
        c.execute("""SELECT * from terminal where TID = %i""" % TID)
        temp = c.fetchall()
        if not temp:
            print('Maar deze deur bestaat helemaal niet! D:')
            time.sleep(3)

    #key = randint(1, 100)
    print('Scan pasje a.u.b.')
    ser = serial.Serial(COMPOORT - 1)
    #s = ser.read(1)
    #ser.write(bytes([key]))
    s = ser.read(10)
    userid = int.from_bytes(s, byteorder='big')
    Door = UseDatabase.check(userid, TID)
    print(Door)
    ser.close()

    if Door:
        time.sleep(5)
        Door = False
        print(Door)