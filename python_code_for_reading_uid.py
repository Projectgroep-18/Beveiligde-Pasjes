import serial
ser = serial.Serial(3)

#ser.print("password")

s = ser.read(10)
print( s )

#c.execute ('''SELECT (card id) FROM persoon WHERE (card id) == s''')

if s == b'3529442660':
	Door = True
else:
	Door = False
print( Door )