import RPi.GPIO as GPIO
import time

# Define the GPIO pins
PWM_PIN = 18  # PWM input from the R8EF receiver
DIR_PIN = 20  # Direction pin for the DRV8824
STEP_PIN = 21  # Step pin for the DRV8824

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pins
GPIO.setup(PWM_PIN, GPIO.IN)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)

# Function to read the PWM signal
def read_pwm(pin):
    start_time = time.time()
    while GPIO.input(pin) == 0:
        start_time = time.time()

    while GPIO.input(pin) == 1:
        pass

    return time.time() - start_time

try:
    while True:
        # Read the PWM signal
        pwm_value = read_pwm(PWM_PIN)

        # Map the PWM value to a speed for the stepper motor
        speed = int(pwm_value * 1000)

        # Set the direction of the stepper motor
        GPIO.output(DIR_PIN, GPIO.HIGH if speed >= 0 else GPIO.LOW)

        # Step the motor
        for i in range(abs(speed)):
            GPIO.output(STEP_PIN, GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(STEP_PIN, GPIO.LOW)
            time.sleep(0.001)

except KeyboardInterrupt:
    GPIO.cleanup()
