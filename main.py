from Views.MainView import MainView
from Models.DataManager import DataManager
from Models.TwitterManager import TwitterManager
from Models.LightsManager import LightsManager
from Models.TemperatureManager import TemperatureManager
from Models.EventsManager import EventsManager
from Models.AlarmManager import AlarmManager
from Models.VoiceManager import VoiceCommands

from serial import Serial


class MainApp():
    def __init__(self):
        self.__arduino = Serial('/dev/tty.usbmodem1441', 9600)

        self.__data = DataManager(alarm_handler=self.alarm_handler, temperature_handler=self.temperature_handler)

        self.__lights = LightsManager()
        self.__alarm = AlarmManager(event_handler=self.event_handler)
        self.__temperature = TemperatureManager(event_handler=self.event_handler, update_handler=self.update_temperature)
        self.__voice = VoiceCommands(event_handler=self.event_handler, rooms=self.__lights.rooms)
        #self.__twitter = TwitterManager(event_handler=self.event_handler, rooms=self.__lights.rooms)
        self.__master = MainView(rooms=self.__lights.rooms, tap_operator_handler=self.event_handler)
        self.__master.protocol("WM_DELETE_WINDOW")

        self.__events = EventsManager(lights_handler=self.__lights,
                                      serial_handler=self.house_handler,
                                      twitter_handler=None,
                                      buttons_update=self.__master.update_lights_buttons,
                                      temperature_handler=self.__temperature,
                                      voice_handler=self.__voice)

        self.__master.bind('<space>', self.__on_space_clicked)

    def run(self):
        self.__update_data()
        self.__master.mainloop()

    def __update_data(self):
        try:
            raw_data = self.__arduino.readline().decode()
        except UnicodeDecodeError:
            raw_data = 'Bad data'
        self.__data.analyze_data(raw_data)
        #self.__twitter.run()
        self.__master.after(1, self.__update_data)

    def alarm_handler(self, ultrasonic_value_1):
        self.__alarm.analyze_data(ultrasonic_value_1)

    def temperature_handler(self, data):
        self.__temperature.analyze_temperature(data)

    def house_handler(self, value):
        value = value.encode('ascii')
        self.__arduino.write(value)

    def event_handler(self, caller=None, user=None, event=None, place=None, action=None, status=None):
        self.__events.analyze_event(caller=caller, user=user, event=event, place=place, action=action, status=status)

    def update_temperature(self, value):
        if value is None:
            return
        try:
            value = int(value)
        except ValueError:
            value = 'GETTING DATA'

        self.__master.update_temperature_value(value)

    def __on_space_clicked(self, event):
        self.__voice.say('Say your command')
        self.__voice.run()


if __name__ == '__main__':
    app = MainApp()
    app.run()