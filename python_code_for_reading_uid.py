import serial
import sqlite3
import time
conn = sqlite3.connect('data.db')
from random import randint

c = conn.cursor()

def check(userid):																	#Checkt of de ontvangen UID voorkomt in onze database
	c.execute("""SELECT UID from persoon WHERE UID = %i """ % userid)
	persoon = c.fetchall()
	if persoon:
		return True
	else:
		return False

ser = serial.Serial(3)
#key = randint(0, 100)																#Genereerd een 'random' getal tussen de 0 en de 100 als key

#ser.write(key)																		#Stuurt de key naar de Arduino

s = ser.read(10)
#print( s )
userid = int.from_bytes(s, byteorder='big')

Door = check(userid)
print( Door )

if Door:																			#Wanneer de deur succesvol geopend is, sluit deze weer na 5 seconden
	time.sleep(5)
	Door = False
	print( Door )