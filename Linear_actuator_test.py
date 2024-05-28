import pigpio
import time

# Initialize pigpio
pi = pigpio.pi('192.168.0.14', 8888)

# Define the motor control pins
IN1 = 26
IN2 = 20
ENABLE = 12  # Assuming you connect the enable pin to GPIO 21

# Set up the motor control pins
pi.set_mode(IN1, pigpio.OUTPUT)
pi.set_mode(IN2, pigpio.OUTPUT)
pi.set_mode(ENABLE, pigpio.OUTPUT)

# Define the PWM input pin
PWM_INPUT = 13  # Assuming the PWM signal from the R8EF receiver is connected to GPIO 18

# Function to set the motor direction
def set_direction(direction):
    if direction == "extend":
        pi.write(IN1, 1)
        pi.write(IN2, 0)
    elif direction == "retract":
        pi.write(IN1, 0)
        pi.write(IN2, 1)
    else:
        pi.write(IN1, 0)
        pi.write(IN2, 0)

# Callback function to handle the PWM input
def pwm_callback(gpio, level, tick):
    # Read the PWM signal
    pwm_width = pi.get_current_tick() - tick

    # Control the motor based on the PWM signal
    if pwm_width > 1600:  # Adjust this value based on your specific PWM signal
        set_direction("extend")
        pi.write(ENABLE, 1)  # Enable the motor
    else:
        set_direction("retract")
        pi.write(ENABLE, 1)  # Enable the motor

# Set up the PWM callback
cb = pi.callback(PWM_INPUT, pigpio.EITHER_EDGE, pwm_callback)

# Keep the script running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    cb.cancel()  # Cancel the callback
    pi.stop()  # Stop pigpio

