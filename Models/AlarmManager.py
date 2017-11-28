class AlarmManager():
    def __init__(self, event_handler=None):
        self.__sensor1 = None
        self.__actual_sensor1 = None
        self.__sensor1_values = []
        self.__actual_sensor1_values = []
        self.__counter = 0
        self.__max_values = 10
        self.alarm_status = False
        self.__event = event_handler

    def analyze_data(self, sensor1_data):
        if not self.__sensor1:
            if self.__counter <= self.__max_values:
                if sensor1_data is not None:
                    self.__sensor1_values.append(self.__turn_to_distance(sensor1_data))
                    self.__counter += 1

            if self.__counter == self.__max_values:
                self.__sensor1 = int((sum(self.__sensor1_values))/self.__max_values)
                self.__counter = 0
                self.__actual_sensor1 = self.__sensor1

        else:
            if self.__counter <= self.__max_values:
                self.__actual_sensor1_values.append(self.__turn_to_distance(sensor1_data))
                self.__counter += 1

            if self.__counter == self.__max_values and not self.alarm_status:
                self.__actual_sensor1 = 0
                self.__actual_sensor1 = int((sum(self.__actual_sensor1_values) / self.__max_values))
                self.__actual_sensor1_values = []
                self.__counter = 0

            if self.__actual_sensor1 is None:
                return

            if not (self.__sensor1 * .5 <= self.__actual_sensor1 <= self.__sensor1 * 1.5) and not self.alarm_status:
                self.__event(caller='VOICE', event='ALARM', action='SET', status=True)

    def __turn_to_distance(self, data):
        try:
            return int(data*0.034/2)
        except TypeError:
            return

    def alarm_status(self):
        if self.alarm_status:
            return 'The alarm is active'

        else:
            return 'The alarm is deactivated'

    def set_alarm(self, status):
        self.alarm_status = status
        if not status:
            self.__sensor1 = None
            self.__sensor1_values = []
            self.__actual_sensor1_values = []
            self.__counter = 0
