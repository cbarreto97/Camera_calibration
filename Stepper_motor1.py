import pigpio
import time
import RPi.GPIO as GPIO

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

# Variables
delay = 0.005
steps = 500

# Function to control stepper motor
def setStep(w1, w2):
    GPIO.output(18, w1)
    GPIO.output(23, w2)

# Function to read PWM and control stepper motor
def control_motor(gpio, level, tick):
    if level == 1:  # Replace with your condition
        setStep(1, 0)
        time.sleep(delay)
        setStep(0, 1)
        time.sleep(delay)
    else:
        setStep(0, 0)

# Setup pigpio
pi = pigpio.pi()
pin = 18  # Replace with your GPIO pin number
cb = pi.callback(pin, pigpio.EITHER_EDGE, control_motor)

# Run for a while
time.sleep(60)

# Cancel the callback
cb.cancel()
pi.stop()
