import RPi.GPIO as GPIO
from time import sleep

class StepperMotor:
    def __init__(self, step_pin, dir_pin):
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        self.delay = .0208

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(step_pin, GPIO.OUT)
        GPIO.setup(dir_pin, GPIO.OUT)
        
    def run(self, steps, clockwise):
        GPIO.output(self.dir_pin, clockwise)
        for i in range(steps):
            GPIO.output(self.step_pin, GPIO.HIGH)
            sleep(self.delay)
            GPIO.output(self.step_pin, GPIO.LOW)
            sleep(self.delay)

if __name__ == "__main__":
    step_pin = int(input("Enter step_pin: "))
    dir_pin = int(input("Enter dir_pin: "))

    try:
        motor = StepperMotor(step_pin, dir_pin)
    
        motor.run(5, True)
        motor.run(5, False)
    finally:
        GPIO.cleanup()
