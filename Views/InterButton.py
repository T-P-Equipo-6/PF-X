from tkinter import W, E, N, S, Label, PhotoImage
from Helpers.CustomTypes import AssetsNames


class InterButton(Label):
    class Constants:
        width = 100
        center = W + E + N + S
        border_type = 'groove'
        border_width = 1
        event = "<Button-1>"

    def __init__(self, master, tap_toggle_handler=None, place=None, status=False):
        super().__init__(master)
        self.__tap_handler = tap_toggle_handler
        self.__state = status
        self.__place = place
        self.__on_image = PhotoImage(file=AssetsNames.on_file)

        self.configure(borderwidth=self.Constants.border_width, relief=self.Constants.border_type)

        self.__off_image = PhotoImage(file =AssetsNames.off_file)
        image = self.__on_image if self.__state else self.__off_image
        self.__set_image(image)
        self.bind(self.Constants.event, self.__toggle)

    def __toggle(self, event):
        self.__state = not self.__state
        image = self.__on_image if self.__state else self.__off_image
        self.__set_image(image)

        if self.__tap_handler is None: return
        self.__tap_handler(object='LIGHTS', place=self.__place, action='SET', status=self.__state)

    def __set_image(self, image):
        self.configure(image=image)
        self.image = image

    def position(self, row, column):
        self.grid(row=row, column=column, sticky=self.Constants.center)