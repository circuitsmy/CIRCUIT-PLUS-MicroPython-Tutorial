# CIRCUIT PLUS - Exercise 01 LED BLINKING

from machine import Pin
from time import sleep

# declaring GPIO2 as an OUTPUT pin.
led = Pin(2, Pin.OUT)

while True:
    
    led.value(0)
    sleep(0.1)
    led.value(1)
    sleep(0.1)

    led.value(0)
    sleep(0.1)
    led.value(1)
    sleep(2)

