from tkinter import PhotoImage, Label, N, S, E, W
from Views.InterLabel import InterLabel
from Views.InterElement import InterElement
from Helpers.CustomTypes import LabelMessages


class InterfaceView:
    class Constants:
        height = 6
        width = 2
        row_height = 100
        center = W + E + N + S

    def __init__(self, master, tap_operator_handler = None):
        self.__tap_operator_handler = tap_operator_handler

        for index_row in range(0, len(LabelMessages.labels_text)):
            InterElement(master, index_row, tap_operator_handler=None)

