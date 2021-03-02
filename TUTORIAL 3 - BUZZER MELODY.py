# CIRCUIT PLUS - Tutorial 03 BUZZER MELODY 

from machine import Pin,PWM
from time import sleep

# declare the GPIO number for PWM signal output
buzzer = PWM(Pin(13))
# declare Tone frequency.
buzzer.freq(5000)

while True:
    
    # PWM duty cycle number.
    buzzer.duty(294)
    sleep(0.5)
    
    
    buzzer.duty(0) #buzzer has no sound since PWM duty cycle is 0.
    sleep(0.5)