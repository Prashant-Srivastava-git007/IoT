from machine import Pin
from time import sleep

# D2 on ESP32 is usually GPIO2
led = Pin(2, Pin.OUT)

while True:
    led.value(1)  # LED ON
    sleep(3)
    led.value(0)  # LED OFF
    sleep(1)
