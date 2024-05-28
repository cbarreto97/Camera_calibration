import pigpio
import time
import RPi.GPIO as GPIO
#Run sudo pigpiod first
# Setup GPIO
#GPIO.setwarnings(False)  # Disable warnings
GPIO.setmode(GPIO.BCM)
#Stepper Motor IN Pins
GPIO.setup(17, GPIO.OUT) #IN1 Pin
GPIO.setup(27, GPIO.OUT) #IN2 Pin
GPIO.setup(22, GPIO.OUT) #IN3 Pin
GPIO.setup(23, GPIO.OUT) #IN4 Pin
#RC Receiver Pins
GPIO.setup(13, GPIO.IN) #CH.2: Right Stick
GPIO.setup(12, GPIO.IN) #CH.3: Left Stick

# Variables
delay = 0.005
steps = 500

# Function to control stepper motor
def setStep(w1, w2, w3, w4):
    GPIO.output(17, w1) 
    GPIO.output(27, w2)
    GPIO.output(22, w3)
    GPIO.output(23, w4)

def control_motor(gpio, level, tick):
   def control_motor(gpio, level, tick):
    #Read state of right stick
    right_stick = GPIO.input(13) 

    if right_stick == 1:  # Replace with your condition
        # Step 1: A+, B+
        setStep(1, 0, 0, 0)
        time.sleep(delay)
        # Step 2: A+, B+
        setStep(1, 1, 0, 0)
        time.sleep(delay)
        # Step 3: A-, B+
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        # Step 4: A-, B+
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        # Step 5: A-, B-
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        # Step 6: A-, B-
        setStep(0, 0, 1, 1)
        time.sleep(delay)
        # Step 7: A+, B-
        setStep(1, 0, 0, 1)
        time.sleep(delay)
        # Step 8: A+, B-
        setStep(1, 0, 0, 0)
        time.sleep(delay)
    else:
        setStep(0, 0, 0, 0)
# Setup pigpio: input from your RC receiver
pi = pigpio.pi('192.168.0.14', 8888)
pin = 13  # Replace with your GPIO pin number

# Set up servo pulse width
set_pulse_width = pi.set_servo_pulsewidth(pin, 17000)  # Set pulse width to ## microseconds
# Now you can get the servo pulse width
pulse_width = pi.get_servo_pulsewidth(pin)

cb = pi.callback(pin, pigpio.EITHER_EDGE, control_motor)

# Run for a while
time.sleep(60)

# Cancel the callback
cb.cancel()
pi.stop()
