import serial
import time
import sqlite3

conn = sqlite3.connect('data.db')
from random import randint
import UseDatabase

c = conn.cursor()

COMPOORT = int(input("De Arduino is aangesloten op COM-poort "))

ser = serial.Serial(COMPOORT - 1)
key = randint(10000, 90000)
key2 = int(key/1000)
key3 = int(key/100)
key4 = int(key/10)


def decrypt(userid):
    return userid + int(key4 - key2)*int(key - key3)


def readArduino():
    while ser.readline().strip() != b'test':
        time.sleep(1)

    ser.write(str(key).encode())
    s = ser.readline().strip()
    userid = decrypt(int(s))
    return userid