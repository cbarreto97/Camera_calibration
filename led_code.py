from gpiozero import LED
import time

#Red is in Pin 3 (GPIO 2); Blue is in Pin 5 (GPIO 3)

led = LED(2) #instert GPIO num 
for _ in range(5):
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
