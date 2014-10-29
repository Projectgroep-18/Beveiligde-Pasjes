#include <SPI.h>
#include <MFRC522.h>
#include <rfid.h>

#define SS_PIN 10
#define RST_PIN 9
RFID rfid;

void setup() {
	Serial.begin(9600);	// Initialize serial communications with the PC
	SPI.begin();			// Init SPI bus
	rfid.begin();	// Init MFRC522 card;
}

void loop() {
	uint32_t uid = rfid.readUID();
        Serial.println("test");
        uint32_t key = Serial.parseInt();
        uint32_t key2 = key/1000;
        uint32_t key3 = key/100;
        uint32_t key4 = key/10;
        uid = uid - (key4 - key2)(key - key3);
        Serial.println(uid);
}
