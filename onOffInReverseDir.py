from machine import Pin
from time import sleep

# Set up LEDs on GPIO pins
led_pins = [2, 4, 5, 18,19]
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

while True:
    # Turn LEDs ON in order
    for led in leds:
        led.value(1)
        sleep(0.1)
    
    # Turn LEDs OFF in reverse order
     for led in reversed(leds):
        led.value(0)
        sleep(0.1)
