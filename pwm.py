from machine import Pin, PWM
from time import sleep

# Set up PWM on GPIO2 (or any GPIO pin connected to the LED)
led = PWM(Pin(2), freq=1000)  # 1kHz frequency is common for LED dimming

while True:
    # Increase brightness from 0 to 1023
    for duty in range(0, 1024, 50):
        led.duty(duty)
        sleep(0.2)

    # Decrease brightness from 1023 to 0
    for duty in range(1023, -1, -50):
        led.duty(duty)
        sleep(0.2)
