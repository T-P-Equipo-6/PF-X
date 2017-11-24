from Views.MainView import MainView
from Models.DataManager import DataManager
from Models.TwitterManager import TwitterManager
from Models.LightsManager import LightsManager
from Models.EventsManager import EventsManager
import time

from serial import Serial


class MainApp():
    def __init__(self):
        self.__arduino = Serial('/dev/tty.usbmodem1441', 115200)

        self.__data = DataManager(alarm_handler=self.alarm_handler, temperature_handler=self.temperature_handler)

        self.__lights = LightsManager()
        self.__twitter = TwitterManager(event_handler=self.event_handler, rooms=self.__lights.rooms)
        self.__events = EventsManager(lights_handler=self.__lights,
                                      serial_handler=self.house_handler,
                                      twitter_handler=self.__twitter)

        self.__master = MainView(rooms=self.__lights.rooms, tap_operator_handler=self.event_handler)
        self.__master.protocol("WM_DELETE_WINDOW")

    def run(self):
        self.__update_data()
        self.__master.mainloop()

    def __update_data(self):
        raw_data = self.__arduino.readline().decode()
        #print(raw_data)
        #self.__data.analise_data(raw_data)
        self.__twitter.run()
        self.__master.after(10, self.__update_data)


    def alarm_handler(self, ultrasonic_value_1, ultrasonic_value_2):
        print(ultrasonic_value_1, ultrasonic_value_2)

    def temperature_handler(self, temperature):
        print(temperature)

    def house_handler(self, value):
        value = value.encode('ascii')
        self.__arduino.write(value)
        time.sleep(2)

    def event_handler(self, caller=None, user=None, object=None, place=None, action=None, status=None):
        self.__events.analyze_event(caller=caller, user=user, object=object, place=place, action=action, status=status)


if __name__ == '__main__':
    app = MainApp()
    app.run()