class TemperatureSensor:
    def __init__(self, location, temperature):
        self.location = location
        self.temperature = temperature

    def increase_temperature(self):
        self.temperature += 1

    def decrease_temperature(self):
        self.temperature -= 1

    def show_temperature(self):
        print(f"{self.location}: {self.temperature} degrees")


sensor1 = TemperatureSensor("Kitchen", 20)
sensor2 = TemperatureSensor("Bedroom", 20)

sensor1.show_temperature()
sensor2.show_temperature()

# Kitchen ökar 2 gånger
sensor1.increase_temperature()
sensor1.increase_temperature()

# Bedroom minskar 1 gång
sensor2.decrease_temperature()

# Visa temperaturerna
sensor1.show_temperature()
sensor2.show_temperature()