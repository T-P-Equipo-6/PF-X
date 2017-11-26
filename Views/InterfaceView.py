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

        for row_index in range(0, len((LabelMessages.labels_text['second_column']))):
            sample_button = InterButton(master, tap_operator_handler, None, False)
            sample_button.position(row_index+1, 3)
            sample_label = InterLabel(LabelMessages.labels_text['second_column'][row_index])
            sample_label.position(row_index + 1, 2)

        temperature_label = InterLabel(text='23')
        temperature_label.position(3, 3)



