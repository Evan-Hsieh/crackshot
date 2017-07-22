# -*- coding: utf-8 -*-

import base_menu_bar
import base_main_window
import base_content_panel


class MainWindow(base_main_window.BaseMainWindow):
    def fill_sizer(self):
        content_sizer = self.GetSizer()
        content_sizer.Add()


class MenuBar(base_menu_bar.BaseMenuBar):
    def set_para(self, event):
        vm = ViewsManager()
        vm.content_panel = vm.get_window("ContentPanel")
        # vm.main_window.Refresh()

    def check_para(self, event):
        print("check para")


class ContentPanel(base_content_panel.MyPanel5):
    pass


# The decorator of singleton
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
        if window_name == "MenuBar":
            return MenuBar()
        if window_name == "MainWindow":
            return MainWindow(None)
        if window_name == "ContentPanel":
            return ContentPanel(self.main_window)
        else:
            return None


