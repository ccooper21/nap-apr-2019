from machine import Pin
from utime import sleep

# ONE-TIME SETUP

# Pin 12 corresponds to the pin labeled "D6" on the NodeMCU development board.
# By setting the "PULL_UP" flag, the pin will be held at 3.3V when the button
# is not pressed.  When the button is pressed the pin will be connected to
# ground, and hence held at 0V.  Without the "PULL_UP" flag the pin would
# "float" when disconnected, which is generally undesirable.  As a result of
# all of this, the pin will have a value of 0 when the button is pressed, and
# a value of 1 when the button is not pressed.
p12 = Pin(12, Pin.IN, Pin.PULL_UP)

# Pin 14 corresponds to the pin labeled as "D5" on the NodeMCU development
# board.
p14 = Pin(14, Pin.OUT)

# RUN FOREVER

while True:
    if not p12.value():
        p14.on()
        sleep(3.0)
        p14.off()
