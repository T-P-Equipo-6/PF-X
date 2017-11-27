import json
from json import JSONDecodeError


class DataManager():

    def __init__(self, alarm_handler=None, temperature_handler=None):
        self.alarm_handler = alarm_handler
        self.temperature_handler = temperature_handler

        self.ultrasonic_1 = 0
        self.ultrasonic_2 = 0
        self.temperature = 0

    def analyze_data(self, raw_data):
        clean_data = raw_data.strip(" \n\r")
        try:
            data = json.loads(str(clean_data))
        except JSONDecodeError:
            print('bad data')
            return

        try:
            self.ultrasonic_1 = data['USV']
        except KeyError:
            self.ultrasonic_1 = None

        try:
            self.temperature = data['TEMP']
        except KeyError:
            self.temperature = None

        self.alarm_handler(self.ultrasonic_1)
        self.temperature_handler(self.temperature)


