from components.button import Button
from component.buzzer import Buzzer
from component.led import LED
from timer import Timer

button = Button()
buzzer = Buzzer()
led = LED()

increase = True
led_power = 255
color = (1,0,0)

class Creature:

    def __init__(self):
        self.ecosystem = None
	
	def message(message):
        # Activate the buzzer if we recieve ping
        if message == "ping":
            # Change led color to Green
            color = (0,1,0)
		    buzzer.update(100)
        
        # Send the ping message when we recive pong
        if message == "pong":
            # Change led color ot Red
            color = (1,0,0)
            self.ecosystem.send_message("ping")


	def sense():
		if button.sense() == True:
			return True

	# One iteration of the creatures main loop
	def loop():
        # increase or decease the brightness by 1 every loop.
        if increase:
            led_power += 1
            if led_power > 255:
                led_power = 255
                increase = False
        else:
            led_power -= 1
            if led_power < 0:
                led_power = 0
                increase = True

        # show the led color
        actual_color = Tuple([led_power * c for c in color])
        led.update_full_color(actual_color)
		
