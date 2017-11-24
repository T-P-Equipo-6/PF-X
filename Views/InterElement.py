from Views.InterLabel import InterLabel
from Views.InterButton import InterButton


class InterElement:

    def __init__(self, master, index_row, tap_operator_handler=None, text=None):
        label = InterLabel(text=(text + ' LIGHTS'))
        label.position(index_row + 1, 0)
        button = InterButton(master, tap_operator_handler)
        button.position(index_row + 1, 1)