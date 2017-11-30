from tkinter import N, S, E, W
from Views.InterElement import InterElement
from Views.InterLabel import InterLabel
from Views.InterButton import InterButton


class InterfaceView:
    class Constants:
        height = 6
        width = 2
        row_height = 100
        center = W + E + N + S

    def __init__(self, master, rooms=None, alarm_status=None, door_status=None, tap_operator_handler=None):
        counter = 0
        self.__master = master
        self.__tap_operator = tap_operator_handler

        for room in rooms:
            InterElement(master, counter, tap_operator_handler=tap_operator_handler, text=room, status=rooms[room])
            counter += 1

        self.set_alarm_button(alarm_status)
        self.set_door_button(door_status)

        temperature_label = InterLabel('TEMPERATURE')
        temperature_label.position(3, 2)
        self.temperature_value_label = InterLabel(text='')
        self.temperature_value_label.position(3, 3)

    def update_temperature(self, value):
        self.temperature_value_label.set_text(str(value) + ' ºC')

    def set_alarm_button(self, status):
        alarm_button = InterButton(self.__master, tap_toggle_handler=self.__tap_operator, status=status, event='ALARM')
        alarm_button.position(1, 3)
        alarm_label = InterLabel('ALARM')
        alarm_label.position(1, 2)

    def set_door_button(self, status):
        door_button = InterButton(self.__master, tap_toggle_handler=self.__tap_operator , status=status, event='DOOR')
        door_button.position(2, 3)
        door_label = InterLabel('DOOR')
        door_label.position(2, 2)
