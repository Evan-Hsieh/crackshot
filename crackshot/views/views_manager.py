# -*- coding: utf-8 -*-

import wx
import base_main_window
import base_menu_bar
import base_blank_panel
import base_set_para_panel
import re


class MainWindow(base_main_window.BaseMainWindow):
    pass


class MenuBar(base_menu_bar.BaseMenuBar):
    def set_para(self, event):
        MenuBar.update_panel("SetParaPanel")

    def check_para(self, event):
        MenuBar.update_panel("BlankPanel")

    @staticmethod
    def update_panel(new_panel_name):
        vm = ViewsManager()
        if vm.content_panel is not None:
            vm.content_panel.Show(False)
        vm.content_panel = vm.get_window(new_panel_name)
        vm.content_panel.Show(True)


class BlankPanel(base_blank_panel.BlankPanel):
    pass


class SetParaPanel(base_set_para_panel.SetParaPanel):
    def onclick_finish_set_para(self, event):
        print("*****")
        t = self.text_length_warhead
        v = t.GetValue()
        print(self.text_length_warhead.GetValue())

    def onchar_validate_input_num(self, event):
        value = event.GetKeyCode()
        print(value)
        if is_digits_by_ascii(value) is True:
            event.Skip()

    # Clear the textCtrl if the input is not number when lose focus
    def onkillfocus_validate_input_num(self, event):
        obj = event.GetEventObject()
        pattern = re.compile(r'^([-]?[0-9]+)?\.?[0-9]*$')
        if pattern.match(obj.GetValue()):
            event.Skip
        else:
            vm = ViewsManager()
            vm.show_message_dialog(u"消息提示", u"输入数据需要为数字，且不能含有任何中文符号！")
            obj.Clear()


# Judge if the char is not digits
def is_digits_by_ascii(value):
    if 48 <= value <= 57 or 45 <= value <= 46:
        return True
    return False


# The decorator of singleton class
def singleton(cls, *args, **kwargs):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton


@singleton
class ViewsManager(object):
    # Initial the main window and menubar
    def __init__(self):
        self.alive_windows = {}
        self.content_panel = None
        self.main_window = self.get_window("MainWindow")
        self.menubar = self.get_window("MenuBar")
        self.main_window.SetMenuBar(self.menubar)

    # Get instance of window by name
    def get_window(self, window_name):
        windows = self.alive_windows
        if windows.get(window_name) is None:
            windows[window_name] = self.create_window(window_name)
        return windows.get(window_name)

    # Create instance of window by name
    def create_window(self, window_name):
        if window_name == "MainWindow":
            return MainWindow(None)
        if window_name == "MenuBar":
            return MenuBar()
        else:
            obj = eval(window_name + "(self.main_window)")
            return obj

    # Show message dialog
    def show_message_dialog(self, title, msg):
        wx.MessageBox(msg, title)


