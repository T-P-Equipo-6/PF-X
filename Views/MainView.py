from tkinter import Tk, N, S, E, W, Label, PhotoImage

class MainView(Tk):
    class Constants:
        title = "Main Interfase"
        font = ("Phosphate", 48, "bold")
        height = 590
        width = 600
        center = N + S + E + W
        normal_color = '#F5F5F5'
        label_width = 500
        button_width = 100
        title_file = "Assets/house.ppm"
        off_file = "Assets/off.ppm"
        label_text = ["Light room 1", "Light room 2", "Light room 3",
                      "Light room 4", "Light room 1-4", "Protection system",
                      "Temperature"]

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
        for row in range(0, 5):
            self.grid_rowconfigure(row, weight=True)
        self.grid_columnconfigure(0, weight=True, minsize=self.Constants.label_width)
        self.grid_columnconfigure(1, weight=True, minsize=self.Constants.button_width)

    def __configure_UI(self):
        self.__title_image = PhotoImage(file=self.Constants.title_file)
        self.__title_label = Label(image=self.__title_image)
        self.__title_label.grid(row=0, column=0, columnspan=self.Constants.width, sticky=self.Constants.center)

        self.__off_image = PhotoImage(file=self.Constants.off_file)
        for i in range (1,7):
            self.__off_label = Label(image=self.__off_image)
            self.__off_label.grid(row=i, column=1, sticky=self.Constants.center)
            self.__text_label = Label(self)
            self.__text_label.configure(text=self.Constants.label_text[i-1])
            self.__text_label.grid(row=i, column=0, sticky=self.Constants.center)

        self.__temperature_label = Label(self)
        self.__temperature_label.configure(text=self.Constants.label_text[6])
        self.__temperature_label.grid(row=7, column=0, sticky=self.Constants.center)

        self.__temperature_value_label = Label(self)
        self.__temperature_value_label.configure(text="23")
        self.__temperature_value_label.grid(row=7, column=1, columnspan=self.Constants.button_width, sticky=self.Constants.center)



