// Wiring code generated from an ArduinoML model
// Application name: dualCheckAlarm

long debounce = 200;

enum STATE {on, off};
STATE currentState = off;

boolean button1BounceGuard = false;
long button1LastDebounceTime = 0;
const int button1 = 7;

boolean button2BounceGuard = false;
long button2LastDebounceTime = 0;
const int button2 = 4;
const int buzzer = 2;

void setup(){
  pinMode(button1, INPUT);  // Sensor
  pinMode(button2, INPUT);  // Sensor
  pinMode(buzzer, OUTPUT); // Actuator
}

void loop() {
        switch(currentState){
                case on:
                        digitalWrite(buzzer,HIGH);
                        button1BounceGuard = millis() - button1LastDebounceTime > debounce;
                        if((digitalRead(button1) == LOW || digitalRead(button2) == LOW) && button1BounceGuard) {
                                button1LastDebounceTime = millis();
                                currentState = off;
                        }
                        break;
                case off:
                        digitalWrite(buzzer,LOW);
                        button1BounceGuard = millis() - button1LastDebounceTime > debounce;
                        if((digitalRead(button1) == HIGH && digitalRead(button2)) == HIGH && button1BounceGuard) {
                                button1LastDebounceTime = millis();
                                currentState = on;
                        }
                        break;
        }
}
