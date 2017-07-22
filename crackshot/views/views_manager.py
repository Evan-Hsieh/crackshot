# -*- coding: utf-8 -*-

import base_menu_bar
import base_main_window
import base_blank_panel
import base_shape_para_panel
import base_flight_and_ref_panel


class MainWindow(base_main_window.BaseMainWindow):
    def fill_sizer(self):
        content_sizer = self.GetSizer()
        content_sizer.Add()


class MenuBar(base_menu_bar.BaseMenuBar):
    def set_para(self, event):
        MenuBar.update_panel("ShapeParaPanel")

    def check_para(self, event):
        MenuBar.update_panel("BlankPanel")

    @staticmethod
    def update_panel(new_panel_name):
        vm = ViewsManager()
        if vm.content_panel is not None:
            vm.content_panel.Show(False)
        vm.content_panel = vm.get_window(new_panel_name)
        vm.content_panel.Show(True)


class ShapeParaPanel(base_shape_para_panel.ShapeParaPanel):
    pass


class FlightAndRefPanel(base_flight_and_ref_panel.FlightAndRefPanel):
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
        if window_name == "MenuBar":
            return MenuBar()
        if window_name == "MainWindow":
            return MainWindow(None)
        if window_name == "BlankPanel":
            return base_blank_panel.BlankPanel(self.main_window)
        if window_name == "ShapeParaPanel":
            return ShapeParaPanel(self.main_window)
        if window_name == "FlightAndRefPanel":
            return FlightAndRefPanel(self.main_window)
        else:
            return None


