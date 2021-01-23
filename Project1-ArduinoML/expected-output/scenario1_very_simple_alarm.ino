const int led = 8;
const int buzzer = 2;
const int button = 7;

void setup() {
  pinMode(led, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(button, INPUT);
}

void loop() {
  // turn on the led and the buzzer if the button is pressed
  if (digitalRead(button) == HIGH) {
    digitalWrite(led, HIGH);
    digitalWrite(buzzer, HIGH);
  } else {
    digitalWrite(led, LOW);
    digitalWrite(buzzer, LOW);
  }
}