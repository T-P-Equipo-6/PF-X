class AlarmManager():
    def __init__(self, event_handler=None):
        self.__perimeter = None
        self.__actual_perimeter = None
        self.__perimeter_values = []
        self.__actual_perimeter_values = []
        self.__counter = 0
        self.__max_values = 10
        self.alarm_status = False
        self.__event = event_handler
        self.__lowest_diff_percentage = 0.5
        self.__highest_diff_percentage = 1.5

    def analyze_data(self, sensor1_data):
        if not self.__perimeter:
            if self.__counter <= self.__max_values:
                if sensor1_data is not None:
                    self.__perimeter_values.append(self.__turn_to_distance(sensor1_data))
                    self.__counter += 1

            if self.__counter == self.__max_values:
                self.__perimeter = int((sum(self.__perimeter_values)) / self.__max_values)
                self.__counter = 0
                self.__actual_perimeter = self.__perimeter

        else:
            if self.__counter <= self.__max_values:
                self.__actual_perimeter_values.append(self.__turn_to_distance(sensor1_data))
                self.__counter += 1

            if self.__counter == self.__max_values and not self.alarm_status:
                self.__actual_perimeter = 0
                self.__actual_perimeter = int((sum(self.__actual_perimeter_values) / self.__max_values))
                self.__actual_perimeter_values = []
                self.__counter = 0

            if self.__actual_perimeter is None:
                return

            if not (self.__perimeter * self.__lowest_diff_percentage <= self.__actual_perimeter <= self.__perimeter * self.__highest_diff_percentage) and not self.alarm_status:
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
            self.__perimeter = None
            self.__perimeter_values = []
            self.__actual_perimeter_values = []
            self.__counter = 0
