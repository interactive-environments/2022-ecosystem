# slider.py
import time
import board
from analogio import AnalogIn
from analogio import AnalogOut
import pwmio

class Slider():
    def __init__(self):
        self.slider = AnalogIn(board.A2)

    def sense(self):
        return self.slider.value
