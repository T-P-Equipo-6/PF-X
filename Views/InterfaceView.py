from tkinter import N, S, E, W
from Views.InterElement import InterElement
from Helpers.CustomTypes import LabelMessages


class InterfaceView:
    class Constants:
        height = 6
        width = 2
        row_height = 100
        center = W + E + N + S

    def __init__(self, master, rooms=None, tap_operator_handler = None):
        self.__tap_operator_handler = tap_operator_handler
        counter = 0

        for room in rooms:
            InterElement(master, counter, tap_operator_handler=None, text=room)
            counter += 1

