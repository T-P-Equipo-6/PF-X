from tkinter import Tk, N, S, E, W, Label, PhotoImage
from Views.InterLabel import InterLabel
from Views.InterfaceView import InterfaceView
from Views.InterButton import InterButton, AssetsNames

class MainView(Tk):
    class Constants:
        title = "Main Interface"
        height = 700
        width = 600
        normal_color = '#F5F5F5'
        center = W + E + N + S

        @classmethod
        def size(cls):
            return '{}x{}'.format(cls.width, cls.height)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.minsize(width=self.Constants.width, height=self.Constants.height)
        self.configure(bg=self.Constants.normal_color)
        self.__configure_grid()
        self.__configure_UI()

    def __configure_grid(self):
        self.grid_rowconfigure(0, minsize=InterfaceView.Constants.row_height)

        for row_index in range(1, InterfaceView.Constants.height + 1):
            self.grid_rowconfigure(row_index, minsize=InterfaceView.Constants.row_height, weight=True)

        self.grid_columnconfigure(0, minsize=InterLabel.Constants.width, weight=True)
        self.grid_columnconfigure(1, minsize=InterButton.Constants.width, weight=True)


    def __configure_UI(self, tap_operator_handler = None):
        self.__interface = InterfaceView(self, tap_operator_handler=tap_operator_handler)

        self.__title_image = PhotoImage(file=AssetsNames.title_file)
        self.__title_label = Label(image=self.__title_image)
        self.__title_label.grid(row=0, column=0, columnspan=self.Constants.width, sticky=self.Constants.center)

