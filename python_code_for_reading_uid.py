import serial
import time
import sqlite3
conn = sqlite3.connect('data.db')
from random import randint
import UseDatabase

c = conn.cursor()

COMPOORT = int(input("De Arduino is aangesloten op COM-poort "))

ser = serial.Serial(COMPOORT - 1)

while True:
	temp = []
	while not temp:
		TID = int(input("Ik wil graag toegang tot deur "))
		c.execute("""SELECT * from terminal where TID = %i""" % TID)
		temp = c.fetchall()
		if not temp:
			print('Maar deze deur bestaat helemaal niet! D:')
			time.sleep(3)
			
	key = randint(1, 100)
	print('Scan pasje a.u.b.')
	
	while ser.readline().strip() != b'test':
		time.sleep(1)
	
	ser.write(str(key).encode())
	s = ser.readline().strip()
	userid = int(s)
	print(userid)
	userid = userid - key
	Door = UseDatabase.check(userid, TID)
	print(Door)

	if Door:
		time.sleep(5)
		Door = False
		print(Door)
		
ser.close()