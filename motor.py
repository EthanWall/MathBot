import RPi.GPIO as GPIO
from time import sleep

class StepperMotor:
    def __init__(self, step_pin, dir_pin, res_pins, resolution):
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        self.res_pins = res_pins
        self.resolution = resolution
        self.factor = int(self.resolution)
        self.delay = .002 / self.factor
        self.modes = {'1': (0, 0, 0),
            '2': (1, 0, 0),
            '4': (0, 1, 0),
            '8': (1, 1, 0),
            '16': (0, 0, 1),
            '32': (1, 0, 1)}

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(step_pin, GPIO.OUT)
        GPIO.setup(dir_pin, GPIO.OUT)
        GPIO.setup(res_pins, GPIO.OUT)

        GPIO.output(self.res_pins, self.modes[self.resolution])
        
    def run(self, steps, clockwise):
        GPIO.output(self.dir_pin, clockwise)
        steps *= self.factor
        for i in range(steps):
            GPIO.output(self.step_pin, GPIO.HIGH)
            sleep(self.delay)
            GPIO.output(self.step_pin, GPIO.LOW)
            sleep(self.delay)

if __name__ == "__main__":
    step_pin = int(input("Enter step_pin: "))
    dir_pin = int(input("Enter dir_pin: "))
    m0_pin = int(input("Enter m0 pin: "))
    m1_pin = int(input("Enter m1 pin: "))
    m2_pin = int(input("Enter m2 pin: "))
    steps = int(input("Enter amount of steps: "))
    resolution = input("Enter resolution: ")

    try:
        motor = StepperMotor(step_pin, dir_pin, (m0_pin, m1_pin, m2_pin), "32")
    
        motor.run(steps, True)
        motor.run(steps, False)
    finally:
        GPIO.cleanup()
