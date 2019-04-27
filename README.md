North Austin Pythonistas - Apr 2019: MicroPython on an ESP8266
==============================================================

This repository contains references and code for the MicroPython presentation and tutorial that I gave at the [North Austin Pythonistas](https://www.meetup.com/North-Austin-Pythonistas/events/260199633/) event on Apr 27th, 2019.  You can view the corresponding presentation [here](https://speakerdeck.com/ccooper21/micropython-on-an-esp8266-at-nap-apr-2019).


How to Use a Breadboard
-----------------------

[![image](https://cdn.sparkfun.com/r/600-600/assets/3/d/f/a/9/518c0b34ce395fea62000002.jpg)](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard/all)


NodeMCU (ESP8266) Pinout
------------------------

In general, the ESP8266 is a robust device.  However, one important thing to understand is that the ESP8266 operates at 3.3 volts, while 5 volts is provided to the NodeMCU development board via the USB connector.

**WARNING:** The ESP8266 will be damaged if you connect the 5V "Vin" pin to others pins on the NodeMCU development board.**

The following shows the pinout for the ESP8266.

[![image](https://raw.githubusercontent.com/nodemcu/nodemcu-devkit-v1.0/master/Documents/NODEMCU_DEVKIT_V1.0_PINMAP.png)](https://github.com/nodemcu/nodemcu-devkit-v1.0)


MicroPython Control Commands / Instructions for Pasting Code
------------------------------------------------------------

```
Control commands:
  CTRL-A        -- on a blank line, enter raw REPL mode
  CTRL-B        -- on a blank line, enter normal REPL mode
  CTRL-C        -- interrupt a running program
  CTRL-D        -- on a blank line, do a soft reset of the board
  CTRL-E        -- on a blank line, enter paste mode
```

To paste code into the MicroPython REPL, press CTRL-E on a blank line to enter paste mode.  Next, paste your code.  Lastly, press CTRL-D to exit paste mode.


MicroPython References
----------------------

[MicroPython Official Site](http://micropython.org/)
[MicroPython Getting Started Tutorial (ESP8266 variant)](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html)
[MicroPython Documentation (ESP8266 variant)](http://docs.micropython.org/en/latest/esp8266/)
[MicroPython Discussion Forum](https://forum.micropython.org/)


MicroPython GitHub Repositories
-------------------------------
[micropython](https://github.com/micropython/micropython/)
[micropython-lib](https://github.com/micropython/micropython-lib/)
[webrepl](https://github.com/micropython/webrepl/)
