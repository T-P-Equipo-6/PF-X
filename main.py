from Views.MainView import MainView
from Models.DataManager import DataManager
from Models.TwitterManager import TwitterManager
from Models.LightsManager import LightsManager


class MainApp():
    def __init__(self):
        self.__master = MainView()
        self.__master.protocol("WM_DELETE_WINDOW")
        self.__data = DataManager(alarm_handler=self.alarm_handler, temperature_handler=self.temperature_handler)
        self.__lights = LightsManager()
        self.__twitter = TwitterManager(lights_manager=self.__lights)


    def run(self):
        self.__update_data()
        self.__master.mainloop()

    def __update_data(self):
        raw_data = '{"UltrasonicSensorValue1": "1000","UltrasonicSensorValue2": "1500","TemperatureValue": "20"}'
        self.__data.analise_data(raw_data)
        self.__twitter.run()
        self.__master.after(1000, self.__update_data())

    def alarm_handler(self, ultrasonic_value_1, ultrasonic_value_2):
        print(ultrasonic_value_1, ultrasonic_value_2)

    def temperature_handler(self, temperature):
        print(temperature)




if __name__ == '__main__':
    app = MainApp()
    app.run()