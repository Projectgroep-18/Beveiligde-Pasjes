import serial
import time
import sqlite3
conn = sqlite3.connect('data.db')
from random import randint

c = conn.cursor()

COMPOORT = int(input("De Arduino is aangesloten op COM-poort "))					#De user wordt gevraagd om de COM-poort te specificeren die de Arduino gebruikt

def check(userid):																	#Checkt of de ontvangen UID voorkomt in onze database
	c.execute("""SELECT UID from persoon WHERE UID = %i """ % userid)
	persoon = c.fetchall()
	if persoon:
		return True
	else:
		return False

ser = serial.Serial(COMPOORT - 1)													#Hier wordt de eerder gevraagte COM-poort gebruikt
#key = randint(0, 100)																#Genereerd een 'random' getal tussen de 0 en de 100 als key

#ser.write(key)																		#Stuurt de key naar de Arduino


while True:
	print( 'Scan pasje a.u.b.' )
	s = ser.read(10)
	#print( s )																			#Hiermee kan eventueel de UID worden weergeven
	userid = int.from_bytes(s, byteorder='big')
	Door = check(userid)
	print( Door )

	if Door:																			#Wanneer de deur succesvol geopend is, sluit deze weer na 5 seconden
		time.sleep(5)
		Door = False
		print( Door )