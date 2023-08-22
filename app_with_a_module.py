import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from functools import partial
import fct_partial.resources.module as m

class fct_partial(toga.App):

    def startup(self):

        self.f_var = 'my param f'
        self.h_var = 'my param h'
        main_box = toga.Box(style=Pack(direction=COLUMN))

        mf_btn = toga.Button('Function mf', on_press=m.f)
        mf_box = toga.Box(style=Pack(direction=ROW, padding=5))
        mf_box.add(mf_btn)

        mg_btn = toga.Button('Function mg', on_press=partial(m.g, g_var='g_var'))
        mg_box = toga.Box(style=Pack(direction=ROW, padding=5))
        mg_box.add(mg_btn)

        main_box.add(mf_box)
        main_box.add(mg_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return fct_partial()
