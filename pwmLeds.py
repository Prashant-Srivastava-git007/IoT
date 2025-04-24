from machine import Pin, PWM
from time import sleep

# Define LED pins
led_pins = [2, 4, 5, 18, 19]

# Create PWM objects for each LED
leds = [PWM(Pin(pin), freq=1000) for pin in led_pins]

while True:
    # Fade in all LEDs together
    for duty in range(0, 1024, 50):
        for led in leds:
            led.duty(duty)
        sleep(0.1)

    # Fade out all LEDs together
    for duty in range(1023, -1, -50):
        for led in leds:
            led.duty(duty)
        sleep(0.1)
