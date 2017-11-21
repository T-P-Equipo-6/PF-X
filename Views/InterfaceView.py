from tkinter import PhotoImage, Label, N, S, E, W
from Views.InterLabel import InterLabel
from Views.InterButton import InterButton
from Helpers.CustomTypes import LabelMessages, AssetsNames


class InterfaceView:
    class Constants:
        height = 6
        width = 2
        row_height = 100
        center = W + E + N + S

    def __init__(self, master, tap_operator_handler = None):
        self.__tap_operator_handler = tap_operator_handler

        self.__title_image = PhotoImage(file=AssetsNames.title_file)
        self.__title_label = Label(image=self.__title_image)
        self.__title_label.grid(row=0, column=0, columnspan=self.Constants.width, sticky=self.Constants.center)

        for index_row in range(0, len(LabelMessages.labels_text)):
            label = InterLabel(text=LabelMessages.labels_text[index_row])
            label.position(index_row + 1, 0)
            button = InterButton(master, tap_toggle_handler=None)
            button.position(index_row + 1, 1)
