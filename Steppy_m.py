import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#Stepper Motor IN Pins
GPIO.setup(17, GPIO.OUT) #IN1 Pin
GPIO.setup(27, GPIO.OUT) #IN2 Pin
GPIO.setup(22, GPIO.OUT) #IN3 Pin
GPIO.setup(23, GPIO.OUT) #IN4 Pin
#RC Receiver Pins
GPIO.setup(13, GPIO.IN) #CH.2: Right Stick

step_sequence = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1]
]
motor_direction = 1
step_size = 4
speed = 10
# Function to move the stepper motor
def move_motor(steps, direction, delay):
    for _ in range(steps):
        for pin in range(4):
            GPIO.output(17, step_sequence[pin][0])
            GPIO.output(27, step_sequence[pin][1])
            GPIO.output(22, step_sequence[pin][2])
            GPIO.output(23, step_sequence[pin][3])
            time.sleep(delay)
        if direction == 0:
            step_sequence.insert(0, step_sequence.pop())
        else:
            step_sequence.append(step_sequence.pop(0))

try:
    # Rotate the motor 200 steps in the initial direction
    move_motor(200, motor_direction, speed)

    # Pause for 1 second
    time.sleep(1)

    # Change the direction of rotation
    motor_direction = 1 - motor_direction

    # Rotate the motor 200 steps in the new direction
    move_motor(200, motor_direction, speed)

    # Read PWM signal from receiver
    while True:
        pwm_value = GPIO.input(13)
        print("PWM Value:", pwm_value)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program interrupted by user")

finally:
    # Clean up GPIO settings
    GPIO.cleanup()