class TemperatureManager:
    def __init__(self, event_handler=None, update_handler=None):
        self.temperature = None
        self.__temperature_values = []
        self.__counter = 0
        self.__top_values = 5
        self.__max_temperature = 40
        self.__fan_status = False
        self.__event = event_handler
        self.__update = update_handler

    def analyze_temperature(self, value):
        try:
            raw_data = float(value)
        except ValueError:
            return
        except TypeError:
            return

        if self.__counter <= self.__top_values:
            self.__temperature_values.append(self.to_celsius(raw_data))
            self.__counter += 1

        if self.__counter == self.__top_values:
            self.__counter = 0
            self.temperature = (sum(self.__temperature_values))/self.__top_values
            self.__update(self.temperature)
            self.__temperature_values = []

        if self.temperature:
            if self.temperature >= self.__max_temperature and not self.__fan_status:
                self.__fan_status = True
                self.__event(caller=None, user=None, event='TEMPERATURE', place='HOUSE', action='FAN', status=self.__fan_status)

            if self.temperature < self.__max_temperature and self.__fan_status:
                self.__fan_status = False
                self.__event(caller=None, user=None, event='TEMPERATURE', place='HOUSE', action='FAN', status=self.__fan_status)

        return self.temperature

    def to_celsius(self, raw_data):
        milivolts = (raw_data/1023)*5000
        celsius = milivolts/10
        return celsius

    def get_temperature(self):
        try:
            message = 'THE TEMPERATURE IS ' + str(int(self.temperature)) + ' DEGREES CELSIUS'
        except TypeError:
            message = 'NO TEMPERATURE DATA'
        return message
