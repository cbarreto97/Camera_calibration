from gpiozero import PWMInputDevice, OutputDevice
from time import sleep

# Define the GPIO pins
PWM_PIN = 18  # PWM input from the R8EF receiver
DIR_PIN = 20  # Direction pin for the DRV8824
STEP_PIN = 21  # Step pin for the DRV8824

# Set up the GPIO pins
pwm = PWMInputDevice(PWM_PIN)
dir = OutputDevice(DIR_PIN)
step = OutputDevice(STEP_PIN)

try:
    while True:
        # Read the PWM signal
        pwm_value = pwm.value

        # Map the PWM value to a speed for the stepper motor
        speed = int(pwm_value * 1000)

        # Set the direction of the stepper motor
        dir.value = 1 if speed >= 0 else 0

        # Step the motor
        for i in range(abs(speed)):
            step.on()
            sleep(0.001)
            step.off()
            sleep(0.001)

except KeyboardInterrupt:
    pass
