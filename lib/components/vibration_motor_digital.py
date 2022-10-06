# vibration motor

import board
import digitalio

class VibrationMotor():
    def __init__(self):
        self.motor = digitalio.DigitalInOut(board.D2)
        self.motor.direction = digitalio.Direction.OUTPUT

    # Takes either true or false
    def update(self, value):
        self.motor.value = value
