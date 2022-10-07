from components.wifi_setup import WiFi
from components.mqtt_setup import MQTT
from timer import Timer
import random

# All messages in this list will be send as part of the 
offline_messages = ["ping", "pong", "pow"]

offline_timer = Timer()
offline_timer.set_duration(5)

class EcoSystem:
    def __init__(self, ecosystem, creature, connect_to_ecosystem):
        self.connect_to_ecosystem = connect_to_ecosystem
        self.creature = creature

        if self.connect_to_ecosystem:
            wifi = WiFi()
            self.mqtt = MQTT(wifi, ecosystem, self.creature)

    # Sends a message in the ecosystem
    def send_message(self, message):
        print("sending: " + message)
        if self.connect_to_ecosystem:
            self.mqtt.send(self.mqtt.client_id + "$$$" + message)

    # Checks if there is a message from the eco system
    def check_for_messages(self):
        global offline_messages, offline_timer
        if self.connect_to_ecosystem:
            self.mqtt.loop()
        else:
            # fake the ecosystem
            if offline_timer.expired():
                offline_timer.set_duration(random.randint(3,8))
                offline_timer.start()
                self.creature.message(random.choice(offline_messages))



        
        
