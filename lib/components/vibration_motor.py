# vibration motor

import time
import board
import pwmio

class VibrationMotor():
    def __init__(self,port=board.D2):
        self.motor = pwmio.PWMOut(port, frequency=300, duty_cycle=0)
        self.motor.direction = digitalio.Direction.OUTPUT

    # Takes either true or false
    def update(self, value):
        self.motor.duty_cycle = value
