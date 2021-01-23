const int led = 8;
const int button = 7;

boolean buttonPressed = false;

void setup() {
  pinMode(led, OUTPUT);
  pinMode(button, INPUT);
}

void loop() {
  // initially the led is off (state 1),
  // pushing the button once switches the led on (state 2),
  // pushing it the second time switches the led off (back to state 1)
  if (digitalRead(button) == HIGH && !buttonPressed) {
    buttonPressed = true;
	if (digitalRead(led) == LOW) {
		digitalWrite(led, HIGH);
	} else {
		digitalWrite(led, LOW);
	}
  } else if (digitalRead(button) == LOW) {
    buttonPressed = false;
  }
}