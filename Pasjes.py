#python code here!


def sendTo(packet, address)
	#als connectie niet open dan open connectie
	#stuur pakketje
	return True
	
def recieve('''hier misschien aangeven welke pakketjes hij accepteert?''')
	#als connectie niet open dan open connectie
	#headers erafhalen?
	return packet

def encrypt(packet, key)					#dit is ook kijken of de sign legit is
	#encrypt pakketje
	return encryptedPacket

def decrypt(encryptedPacket ''',key?''')	#dit is ook signen
	#decrypt met key
	return packet

def door(encryptedPacket)
	doorState = decrypt(encryptedPacket)

def leesPasje()
	#haal data van pasje
	return pasjeData
	
def checkMessage()
	#kijk of user door de deur mag
	
	



def Terminal()  #hier stop je pasje in
	terminalID = 001
	while True:
		doorState = False
		if leesPasje():	#als er data op pasje staat dan:
			packet = encrypt(leesPasje() ++ TerminalID, '''hier de key''')
			sendTo(packet, '''Server adres hier''')
		if recieve(): #als er data binnenkomt
			message = encrypt recieve() #kijk of de sign op de data legit is
			doorState = message
			#wacht een x aantal seconden

			

def Server() #de server die kijkt of iemand erin mag
	while True:
		if recieve(): #als er data inkomt
			message = decrypt(recieve, '''key hier''')
			if checkMessage() == True:
				sendTo(decrypt(True), '''terminal IP''') #stuur een gesigned bericht naar terminal
		if emergency == True:
			sendTo(decrypt(True), '''terminal IP''') #stuur een open bericht naar alle terminals
