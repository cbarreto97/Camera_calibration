import time
import pigpio

#run sudo pigpiod
pi = pigpio.pi('192.168.0.14', 8888)
pin = 13  # Replace with your GPIO pin number for the right stick

while True:
    set_pulse_width = pi.set_servo_pulsewidth(pin, 1500)  # Set pulse width to 1500 microseconds
    pulse_width = pi.get_servo_pulsewidth(pin)
    print("Pulse width: ", pulse_width)
    time.sleep(0.1)
