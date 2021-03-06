from tkinter import Tk, N, S, E, W, Label, PhotoImage
from Views.InterLabel import InterLabel
from Views.InterfaceView import InterfaceView
from Views.InterButton import InterButton, AssetsNames


class MainView(Tk):
    class Constants:
        title = "Main Interface"
        height = 500
        width = 600
        normal_color = '#F5F5F5'
        center = W + E + N + S

        @classmethod
        def size(cls):
            return '{}x{}'.format(cls.width, cls.height)

    def __init__(self, rooms=None, door=None, alarm_status=None, tap_operator_handler=None):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.minsize(width=self.Constants.width, height=self.Constants.height)
        self.configure(bg=self.Constants.normal_color)
        self.__rooms = rooms
        self.__door = door
        self.__alarm_status = alarm_status
        self.__configure_grid()
        self.__tap_operator_handler = tap_operator_handler
        self.__configure_ui()

    def __configure_grid(self):
        self.grid_rowconfigure(0, minsize=InterfaceView.Constants.row_height)

        for row_index in range(1, InterfaceView.Constants.height + 1):
            self.grid_rowconfigure(row_index, minsize=InterfaceView.Constants.row_height, weight=True)

        for column_index in range (0, InterfaceView.Constants.width+1):
            self.grid_columnconfigure(0, minsize=InterLabel.Constants.width, weight=True)
            self.grid_columnconfigure(1, minsize=InterButton.Constants.width, weight=True)
            self.grid_columnconfigure(2, minsize=InterLabel.Constants.width, weight=True)
            self.grid_columnconfigure(3, minsize=InterButton.Constants.width, weight=True)

    def __configure_ui(self):
        self.__interface = InterfaceView(self, self.__rooms, alarm_status=self.__alarm_status, door_status=self.__door,
                                         tap_operator_handler=self.__tap_operator_handler)

        self.__title_image = PhotoImage(file=AssetsNames.title_file)
        self.__title_label = Label(image=self.__title_image)
        self.__title_label.grid(row=0, column=0, columnspan=self.Constants.width, sticky=self.Constants.center)

        self.__mark_image = PhotoImage(file=AssetsNames.mark_file)
        self.__mark_label = Label(image=self.__mark_image)
        self.__mark_label.grid(row=4, column=2, columnspan=2, sticky=self.Constants.center)

    def update_lights_buttons(self):
        self.__configure_ui()

    def update_temperature_value(self, text):
        self.__interface.update_temperature(text)

    def update_alarm_status(self, status):
        self.__interface.set_alarm_button(status=status)

    def update_door_status(self, status):
        self.__interface.set_door_button(status=status)


