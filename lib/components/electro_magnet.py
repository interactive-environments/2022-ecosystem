# electro_magnet.py

import board
import digitalio

class ElectroMagnet():
    def __init__(self):
        self.magnet = digitalio.DigitalInOut(board.D3)
        self.magnet.direction = digitalio.Direction.OUTPUT

    # Takes either true or false
    def update(self, value):
        print(value)
        if value > 10:
            self.magnet.value = True
        else:
            self.magnet.value = False
