import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the pin connected to the R8EF receiver
receiver_pin = 7

# Set up the GPIO pin
GPIO.setup(receiver_pin, GPIO.IN)

# Function to measure the pulse width
def measure_pulse_width(pin):
    start_time = time.time()
    while GPIO.input(pin) == 1:
        start_time = time.time()

    while GPIO.input(pin) == 0:
        pass

    while GPIO.input(pin) == 1:
        end_time = time.time()

    return end_time - start_time

try:
    # Loop to read the signals
    while True:
        pulse_width = measure_pulse_width(receiver_pin)
        print(f"Pulse width: {pulse_width} seconds")
        time.sleep(0.1)
except KeyboardInterrupt:
    # Clean up the GPIO pins
    GPIO.cleanup()
