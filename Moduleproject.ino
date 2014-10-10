void setup() {
  // Open serial connection
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  Serial.write('1');
}

void loop() {
  if (Serial.available() > 0) {  // als er data beschikbaar is...
  


  }
}
