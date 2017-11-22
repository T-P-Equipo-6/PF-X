from tkinter import W, E, N, S
from Views.InterLabel import InterLabel
from Views.InterButton import InterButton
from Helpers.CustomTypes import LabelMessages

class InterElement:

    def __init__(self, master, index_row, tap_operator_handler=None):
        label = InterLabel(text=LabelMessages.labels_text[index_row])
        label.position(index_row + 1, 0)
        button = InterButton(master, tap_operator_handler)
        button.position(index_row + 1, 1)