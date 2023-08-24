import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from functools import partial
import fct_partial.resources.module as m

class fct_partial(toga.App):

    def f(self, widget):
        print(self.f_var)

    def g(self, widget, g_var):
        print(g_var)

    def mf(self, widget):
        mf_var = m.f(self.f_var)
        print(mf_var)

    def mg(self, widget, g_var):
        mg_var = m.g(g_var)
        print(mg_var)

    def startup(self):

        def h(widget):
            print(self.h_var)

        def k(widget, k_var):
            print(k_var)

        def mh(widget):
            mh_var = m.h(self.h_var)
            print(mh_var)

        def mk(widget, k_var):
            mk_var = m.k(k_var)
            print(mk_var)

        self.f_var = 'my param f'
        self.h_var = 'my param h'
        self.font_size = 20
        main_box = toga.Box(style=Pack(direction=COLUMN, font_size=self.font_size))

        f_btn = toga.Button('Function f', on_press=self.f)
        f_btn.style.update(font_size=self.font_size, color='red')
        f_box = toga.Box(style=Pack(direction=ROW, padding=5))
        f_box.add(f_btn)

        g_btn = toga.Button('Function g', on_press=partial(self.g, g_var='g_var'))
        g_btn.style.update(font_size=self.font_size, color='green')
        g_box = toga.Box(style=Pack(direction=ROW, padding=5))
        g_box.add(g_btn)

        h_btn = toga.Button('Function h', on_press=h)
        h_btn.style.update(font_size=self.font_size, color='blue')
        h_box = toga.Box(style=Pack(direction=ROW, padding=5))
        h_box.add(h_btn)

        k_btn = toga.Button('Function k', on_press=partial(k, k_var='k_var'))
        k_btn.style.update(font_size=self.font_size, color='darkviolet')
        k_box = toga.Box(style=Pack(direction=ROW, padding=5))
        k_box.add(k_btn)

        mf_btn = toga.Button('Function mf', on_press=self.mf)
        mf_btn.style.update(font_size=self.font_size, color='red')
        mf_box = toga.Box(style=Pack(direction=ROW, padding=5))
        mf_box.add(mf_btn)

        mg_btn = toga.Button('Function mg', on_press=partial(self.mg, g_var='g_var'))
        mg_btn.style.update(font_size=self.font_size, color='green')
        mg_box = toga.Box(style=Pack(direction=ROW, padding=5))
        mg_box.add(mg_btn)

        mh_btn = toga.Button('Function mh', on_press=mh)
        mh_btn.style.update(font_size=self.font_size, color='blue')
        mh_box = toga.Box(style=Pack(direction=ROW, padding=5))
        mh_box.add(mh_btn)

        mk_btn = toga.Button('Function mk', on_press=partial(mk, k_var='k_var'))
        mk_btn.style.update(font_size=self.font_size, color='darkviolet')
        mk_box = toga.Box(style=Pack(direction=ROW, padding=5))
        mk_box.add(mk_btn)

        main_box.add(f_box)
        main_box.add(g_box)
        main_box.add(h_box)
        main_box.add(k_box)
        main_box.add(mf_box)
        main_box.add(mg_box)
        main_box.add(mh_box)
        main_box.add(mk_box)

        #mw_width = int(8*self.font_size) ; mw_height = int(11.4*self.font_size) # 4xbtn size=160x228
        #mw_width = int(9.2*self.font_size) ; mw_height = int(16.6*self.font_size) # 6xbtn size=184x332
        mw_width = int(9.2*self.font_size) ; mw_height = int(21.8*self.font_size) # 8xbtn size=184x436
        self.main_window = toga.MainWindow(title=self.formal_name, size=(mw_width, mw_height))
        #print(f'size={mw_width}x{mw_height}')
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return fct_partial()
'''
my param f
g_var
my param h
k_var
module.f : my param f
module.g : g_var
module.h : my param h
module.k : k_var
'''