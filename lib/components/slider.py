# slider.py
import time
import board
from analogio import AnalogIn
from analogio import AnalogOut
import pwmio

class Slider():
    def __init__(self, port=None):
        if port == None:
            self.slider = AnalogIn(board.A2)
        else:
            self.slider = AnalogIn(port)

    def sense(self):
        return self.slider.value
