import serial
import sqlite3
conn = sqlite3.connect('data.db')
from random import randint

c = conn.cursor()

def check(userid):
	c.execute("""SELECT UID from persoon WHERE UID = %i """ % userid)
	persoon = c.fetchall()
	if persoon:
		return True
	else:
		return False

ser = serial.Serial(3)
#key = randint(0, 100)

#ser.write(key)

s = ser.read(10)
print( s )
userid = int.from_bytes(s, byteorder='big')

Door = check(userid)
print( Door )