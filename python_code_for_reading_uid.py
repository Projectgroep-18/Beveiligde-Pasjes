import serial
import time
import sqlite3
conn = sqlite3.connect('data.db')
from random import randint

c = conn.cursor()

def check(userid):
COMPOORT = int(input("De Arduino is aangesloten op COM-poort "))					#De user wordt gevraagd om de COM-poort te specificeren die de Arduino gebruikt

def check(userid):																	#Checkt of de ontvangen UID voorkomt in onze database
	c.execute("""SELECT UID from persoon WHERE UID = %i """ % userid)
	persoon = c.fetchall()
	if persoon:
@@ -13,14 +16,23 @@ def check(userid):
	else:
		return False

ser = serial.Serial(3)
#key = randint(0, 100)
													#Hier wordt de eerder gevraagte COM-poort gebruikt
#key = randint(0, 100)																#Genereerd een 'random' getal tussen de 0 en de 100 als key

#ser.write(key)																		#Stuurt de key naar de Arduino

#ser.write(key)

s = ser.read(10)
print( s )
userid = int.from_bytes(s, byteorder='big')
while 1==1:
	print( 'Scan pasje a.u.b.' )
	ser = serial.Serial(COMPOORT - 1)
	s = ser.read(10)
	#print( s )																			#Hiermee kan eventueel de UID worden weergeven
	userid = int.from_bytes(s, byteorder='big')
	Door = check(userid)
	print( Door )
	ser.close()

Door = check(userid)
print( Door )
 No newline at end of file
	if Door:																			#Wanneer de deur succesvol geopend is, sluit deze weer na 5 seconden
		time.sleep(5)
		Door = False
		print( Door )