from machine import Pin
from time import sleep

# GPIO pins connected to 4 LEDs
led_pins = [2, 4, 5, 18]
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

while True:
    # Turn ON LEDs in pairs (forward)
    for i in range(0, len(leds), 2):
        leds[i].value(1)
        leds[i + 1].value(1)
        sleep(0.2)

    # Turn OFF LEDs in pairs (reverse)
    for i in range(len(leds) - 2, -1, -2):
        leds[i].value(0)
        leds[i + 1].value(0)
        sleep(0.2)

