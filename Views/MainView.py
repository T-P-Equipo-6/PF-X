from tkinter import Tk, N, S, E, W

class MainView(Tk):
    class Constants:
        title = "Pizarra Mágica"
        font = ("Phosphate", 48, "bold")
        height = 700
        width = 1200
        center = N + S + E + W
        normal_color = '#F5F5F5'

        @classmethod
        def size(cls):
            return '{}x{}'.format(cls.width, cls.height)

    def __init__(self):
        super().__init__()

        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.minsize(width=self.Constants.width, height=self.Constants.height)
        self.configure(bg=self.Constants.normal_color)
        self.grid_columnconfigure(0, weight=1)
