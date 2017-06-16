# -*- coding: utf-8 -*-
from Tkinter import *


class BaseView:
    def __init__(self):
        pass

    def click_btn(self, root_window):
        self
        s = Label(root_window, text="click")
        s.pack()

    def init_window(self):
        root_window = Tk()
        root_window.wm_title("专家系统")
        btn1 = Button(root_window, text="按钮", command=self.click_btn(root_window))
        btn1.pack()
        root_window.mainloop()


if __name__ == "__main__":
    v = BaseView()
    v.init_window()
