sensor "button1" pin 7
sensor "button2" pin 4
actuator "buzzer" pin 2

state "on" means "buzzer" becomes "high"
state "off" means "buzzer" becomes "low"

initial "off"

from "off" to "on" when "button1" becomes "high" and "button2" becomes "high"
from "on" to "off" when "button1" becomes "low"
from "on" to "off" when "button2" becomes "low"

export "Scenario 2"