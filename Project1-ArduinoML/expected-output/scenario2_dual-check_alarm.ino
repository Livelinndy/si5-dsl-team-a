const int buzzer = 2;
const int button1 = 7;
const int button2 = 4;

void setup() {
  pinMode(buzzer, OUTPUT);
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
}

void loop() {
  // turn on the buzzer if the two buttons are pressed
  if (digitalRead(button1) == HIGH && digitalRead(button2) == HIGH) {
    digitalWrite(buzzer, HIGH);
  } else {
    digitalWrite(buzzer, LOW);
  }
}