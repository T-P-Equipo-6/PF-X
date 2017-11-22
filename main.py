from Views.MainView import MainView
from Models.DataManager import DataManager
from Models.TwitterManager import TwitterManager
from Models.LightsManager import LightsManager
import time

from serial import Serial


class MainApp():
    def __init__(self):
        self.__master = MainView()
        self.__master.protocol("WM_DELETE_WINDOW")
        self.__arduino = Serial('/dev/tty.usbmodem1441', 115200)
        self.__data = DataManager(alarm_handler=self.alarm_handler, temperature_handler=self.temperature_handler)
        self.__lights = LightsManager(house_handler=self.house_handler)
        self.__twitter = TwitterManager(lights_manager=self.__lights)


    def run(self):
        self.__update_data()
        self.__master.mainloop()

    def __update_data(self):
        raw_data = self.__arduino.readline().decode()
        print(raw_data)
        #self.__data.analise_data(raw_data)
        self.__twitter.run()
        self.__master.after(10, self.__update_data)


    def alarm_handler(self, ultrasonic_value_1, ultrasonic_value_2):
        print(ultrasonic_value_1, ultrasonic_value_2)

    def temperature_handler(self, temperature):
        print(temperature)

    def house_handler(self, object, location, status):
        value = str(object + location + status)
        value = value.encode('ascii')
        self.__arduino.write(value)
        time.sleep(2)


if __name__ == '__main__':
    app = MainApp()
    app.run()