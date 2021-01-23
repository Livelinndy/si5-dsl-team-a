const int led = 8;
const int buzzer = 2;
const int button = 7;

boolean buttonPressed = false;

void setup() {
  pinMode(led, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(button, INPUT);
}

void loop() {
  // initially the buzzer and the led are off (state 1),
  // pushing the button once switches the buzzer on (state 2),
  // pushing it the second time switches the buzzer off and turns the led on (state 3),
  // pushing it the third time turns the led off (back to state 1)
  if (digitalRead(button) == HIGH && !buttonPressed) {
    buttonPressed = true;
	if (digitalRead(buzzer) == LOW && digitalRead(led) == LOW) { // if state 1
		digitalWrite(buzzer, HIGH);
	} else if (digitalRead(buzzer) == HIGH && digitalRead(led) == LOW) { // if state 2
		digitalWrite(buzzer, LOW);
		digitalWrite(led, HIGH);
	} else if (digitalRead(buzzer) == LOW && digitalRead(led) == HIGH) { // if state 3
		digitalWrite(led, LOW);
	}
  } else if (digitalRead(button) == LOW) {
    buttonPressed = false;
  }
}