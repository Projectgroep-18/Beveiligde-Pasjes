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
        uid = uid + key;
        Serial.println(uid);
}
