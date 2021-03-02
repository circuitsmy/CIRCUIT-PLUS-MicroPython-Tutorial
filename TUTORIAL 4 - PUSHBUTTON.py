# CIRCUIT PLUS - Tutorial 04 PUSHBUTTON

from machine import Pin
from time import sleep

push = Pin(0, Pin.IN, Pin.PULL_UP) # declaring GPIO0 as an INPUT pin.
led = Pin(2, Pin.OUT) # declaring GPIO2 as an OUTPUT pin.

while True:
    
    if push.value() == 0:
        led.value(0)
        sleep(0.5)
      
    led.value(1)