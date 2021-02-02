sensor "button" pin 7
actuator "led" pin 8
actuator "buzzer" pin 2

state "buzz" means "led" becomes "low" and "buzzer" becomes "high"
state "on" means "led" becomes "high" and "buzzer" becomes "low"
state "off" means "led" becomes "low" and "buzzer" becomes "low"

before "off" with "buzzer" make "longbeep" and "shortbeep" and "longbeep"

initial "off"

from "off" to "buzz" when "button" becomes "high"
from "buzz" to "on" when "button" becomes "high"
from "on" to "off" when "button" becomes "high"

export "Scenario 5"