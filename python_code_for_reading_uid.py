import serial
import time
import sqlite3

conn = sqlite3.connect('data.db')
from random import randint
import UseDatabase

c = conn.cursor()

COMPOORT = int(input("De Arduino is aangesloten op COM-poort "))

ser = serial.Serial(COMPOORT - 1)
key = randint(0, 10000000)


def decrypt(userid):
    return userid - key


def readArduino():
    while ser.readline().strip() != b'test':
        time.sleep(1)

    ser.write(str(key).encode())
    s = ser.readline().strip()
    userid = decrypt(int(s))
    return userid

