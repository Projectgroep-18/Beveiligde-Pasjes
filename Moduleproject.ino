void setup() {
  // Open serial connection
  Serial.begin(9600);
  pinMode(5V , OUTPUT);
  pinMode(GND , OUTPUT);
  pinMode(13 , OUTPUT);
  pinMode(12 , OUTPUT);
  pinMode(11 , OUTPUT);
  pinMode(10 , OUTPUT);
  pinMode(9 , OUTPUT);

}

void main() {
  if (Serial.available() > 0) {  // als er data beschikbaar is...
  


  }
}
