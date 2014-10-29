import serial
import time
import sqlite3
conn = sqlite3.connect('data.db')
from random import randint

c = conn.cursor()

COMPOORT = int(input("De Arduino is aangesloten op COM-poort "))
TID = int(input("Ik wil graag toegang tot deur "))

def check(userid, TID):
	c.execute("""SELECT UID from persoon WHERE UID = %i """ % userid)
	persoon = c.fetchall()
	if persoon:
		return True
	else:
		return False

while True:
	#key = randint(1, 100)
	print('Scan pasje a.u.b.')
	ser = serial.Serial(COMPOORT - 1)
	#s = ser.read(1)
	#ser.write(bytes([key]))
	s = ser.read(10)
	userid = int.from_bytes(s, byteorder='big')
	Door = check(userid, TID)
	print(userid)
	print(Door)
	ser.close()

	if Door:
		time.sleep(5)
		Door = False
		print(Door)