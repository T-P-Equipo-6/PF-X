import json


class DataManager():

    def __init__(self, alarm_handler=None, temperature_handler=None):
        self.alarm_handler = alarm_handler
        self.temperature_handler = temperature_handler

        self.ultrasonic_1 = 0
        self.ultrasonic_2 = 0
        self.temperature = 0

    def analise_data(self, raw_data):
        clean_data = raw_data.strip(" \n\r")
        data = json.loads(str(clean_data))

        try:
            self.ultrasonic_1 = data['UltrasonicSensorValue1']
        except KeyError:
            self.ultrasonic_1 = None

        try:
            self.ultrasonic_2 = data['UltrasonicSensorValue2']
        except KeyError:
            self.ultrasonic_2 = None

        try:
            self.temperature = data['TemperatureValue']
        except KeyError:
            self.temperature = None

        self.alarm_handler(self.ultrasonic_1, self.ultrasonic_2)
        self.temperature_handler(self.temperature)


