# CIRCUIT PLUS - Tutorial 08 LCD DISPLAY

from machine import I2C, Pin
from mp_i2c_lcd1602 import LCD1602
from time import sleep_ms

i2c = I2C(1, sda=Pin(9), scl=Pin(10))

LCD = LCD1602(i2c)

LCD.puts("HELLO CIRCUIT PLUS")