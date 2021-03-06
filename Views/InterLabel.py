from tkinter import W, E, N, S, Label

class InterLabel(Label):
    class Constants:
        width = 200
        border_type = 'groove'
        border_width = 1
        center = W + E + N + S
        font = ("Phosphate", 20)
        normal_color = 'white'#'#F5F5F5'

    def __init__(self, text=None):
        super().__init__()
        self.configure(font=self.Constants.font)
        self.configure(borderwidth=self.Constants.border_width, relief=self.Constants.border_type)
        self.configure(text=text)
        self.configure(bg = self.Constants.normal_color)

    def position(self, row, column):
        self.grid(row = row, column = column, sticky = self.Constants.center)

    def set_text(self, text):
        self.configure(text=text)
