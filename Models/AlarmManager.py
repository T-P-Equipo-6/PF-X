class AlarmManager():
    def __init__(self, event_handler=None):
        self.__sensor1 = None
        self.__sensor2 = None
        self.__actual_sensor1 = None
        self.__actual_sensor2 = None
        self.__sensor1_values = []
        self.__sensor2_values = []
        self.__actual_sensor1_values = []
        self.__actual_sensor2_values = []
        self.__counter = 0
        self.__max_values = 10
        self.__alarm_status = False
        self.__event = event_handler

    def analyze_data(self, sensor1_data, sensor2_data):
        if not self.__sensor1 and not self.__sensor2:
            if self.__counter <= self.__max_values:
                self.__sensor1_values.append(self.__turn_to_distance(sensor1_data))
                self.__sensor2_values.append(self.__turn_to_distance(sensor2_data))
                self.__counter += 1

            if self.__counter == self.__max_values:
                self.__sensor1 = int((sum(self.__sensor1_values))/self.__max_values)
                self.__sensor2 = int((sum(self.__sensor2_values))/self.__max_values)
                self.__counter = 0
                print('perimeter:', self.__sensor1, self.__sensor2)

        else:
            if self.__counter <= self.__max_values:
                self.__actual_sensor1_values.append(self.__turn_to_distance(sensor1_data))
                self.__actual_sensor2_values.append(self.__turn_to_distance(sensor2_data))
                self.__counter += 1

            if self.__counter == self.__max_values:
                self.__actual_sensor1 = int((sum(self.__actual_sensor1_values)) / self.__max_values)
                self.__actual_sensor2 = int((sum(self.__actual_sensor2_values)) / self.__max_values)
                self.__actual_sensor1_values = []
                self.__actual_sensor2_values = []
                self.__counter = 0

            if self.__actual_sensor1 is None or self.__actual_sensor2 is None:
                return

            if self.__actual_sensor1 != self.__sensor1 and not self.__alarm_status:
                self.__alarm_status = True
                self.__event(event='ALARM', place='HOUSE', action='ACTIVATE', status=True)

            if self.__actual_sensor2 != self.__sensor2 and not self.__alarm_status:
                self.__alarm_status = True
                self.__event(event='ALARM', place='HOUSE', action='ACTIVATE', status=True)

    def __turn_to_distance(self, data):
        try:
            return int(data*0.034/2)
        except TypeError:
            return

    def alarm_status(self):
        return self.__alarm_status

    def set_alarm_status(self, status):
        self.__alarm_status = status
        self.__sensor1 = None
        self.__sensor2 = None
