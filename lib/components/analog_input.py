import board
import analogio

class AnalogInput():
    def __init__(self):
        self.input = analogio.AnalogIn(board.A0)

    def sense(self, threshold):
        return self.input.value > threshold

    def sense_value(self):
        return self.input.value / 65536 * 100
