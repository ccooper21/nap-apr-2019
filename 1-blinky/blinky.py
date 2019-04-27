from machine import Pin
from utime import sleep

# ONE-TIME SETUP

# Pin 14 corresponds to the pin labeled "D5" on the NodeMCU development board.
p = Pin(14, Pin.OUT)

# RUN FOREVER

while True:
    p.on()
    sleep(1.0)
    p.off()
    sleep(1.0)
