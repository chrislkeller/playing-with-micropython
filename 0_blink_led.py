"""
                board
     pin 15                  gnd
       |                      |
positive of led               |
                              |
        negative of led    resistor
"""

import time
import machine
from machine import Pin

led = machine.Pin(15, machine.Pin.OUT)
for i in range(10):
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
