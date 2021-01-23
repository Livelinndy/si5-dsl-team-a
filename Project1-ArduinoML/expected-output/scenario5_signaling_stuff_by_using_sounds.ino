const int buzzer = 2;

void setup() {
  pinMode(buzzer, OUTPUT);
}

void loop() {
  for (int i = 0; i < 3; i++) { // repeating short beep 3 times
	shortBeep();
	delay(200); // a short delay is necessary to be able to distinguish the beeps
  }
  delay(1000);
  longBeep();
  delay(1000);
}

void shortBeep() {
    for(int i = 0; i < 80; i++) { // the range of for influences the length of the beep (here the short beep is 2 times shorter than the long beep)
      digitalWrite(buzzer, HIGH);
      delay(1); // delay between signals influences the sound frequency (the shorter the delay, the higher the sound)
      digitalWrite(buzzer, LOW);
      delay(1);
    }
}

void longBeep() {
    for(int i = 0; i < 160; i++) {
      digitalWrite(buzzer, HIGH);
      delay(2);
      digitalWrite(buzzer, LOW);
      delay(2);
    }
}