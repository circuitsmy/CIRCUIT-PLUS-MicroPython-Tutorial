# CIRCUIT PLUS - Tutorial 02 LED PWM

from machine import Pin,PWM
from time import sleep

# configure PWM controller congfiguration and declare the GPIO number for PWM signal output.
led = PWM(Pin(2))

duty_cycle=0

while True:

    for duty_cycle in range (1023, 0, -1):
        led.duty(duty_cycle)
        
        # wait for 0.005 seconds before start again.
        sleep(0.005)
        