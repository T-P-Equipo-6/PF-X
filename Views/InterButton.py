from tkinter import W, E, N, S, Label, PhotoImage
from Helpers.CustomTypes import AssetsNames


class InterButton(Label):
    class Constants:
        width = 100
        center = W + E + N + S
        event = "<Button-1>"

    def __init__(self, master, tap_toggle_handler = None):
        super().__init__(master)
        self.__tap_handler = tap_toggle_handler
        self.__state = False
        self.__on_image = PhotoImage(file=AssetsNames.on_file)
        self.__off_image = PhotoImage(file =AssetsNames.off_file)
        self.__set_image(self.__on_image)
        self.bind(self.Constants.event, self.__toggle)

    def __toggle(self, event):
        self.__state = not self.__state
        image = self.__on_image if self.__state else self.__off_image
        self.__set_image(image)

        if self.__tap_handler is None: return
        self.__tap_handler(self.__state)

    def __set_image(self, image):
        self.configure(image = image)
        self.image = image

    def position(self, row, column):
        self.grid(row = row, column = column, sticky = self.Constants.center)