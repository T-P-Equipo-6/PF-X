from tkinter import N, S, E, W
from Views.InterElement import InterElement
from Views.InterLabel import InterLabel
from Views.InterButton import InterButton
from Helpers.CustomTypes import LabelMessages


class InterfaceView:
    class Constants:
        height = 6
        width = 2
        row_height = 100
        center = W + E + N + S

    def __init__(self, master, rooms=None, tap_operator_handler=None):
        counter = 0

        for room in rooms:
            InterElement(master, counter, tap_operator_handler=tap_operator_handler, text=room, status=rooms[room])
            counter += 1

        alarm_button = InterButton(master, tap_operator_handler, None, False)
        alarm_button.position(1, 3)
        alarm_label = InterLabel('ALARM')
        alarm_label.position(1, 2)

        door_button = InterButton(master, tap_operator_handler, None, False)
        door_button.position(2, 3)
        door_label = InterLabel('DOOR')
        door_label.position(2, 2)

        temperature_label = InterLabel('TEMPERATURE')
        temperature_label.position(3, 2)
        temperature_value_label = InterLabel(text='23')
        temperature_value_label.position(3, 3)



