import serial

def COMPOORT = "COM1"

## Boolean die aangeeft of de Arduino verbonden is of niet
connected = False

## Opent de poort waar de Arduino mee verbonden is
ser = serial.Serial(COMPOORT, 9600)

## Een loop die checkt of de Arduino verbinding heeft
while not connected:
	serin = ser.read()
	connected = True
	
## sluit de poort en eindigt het programma
ser.close()