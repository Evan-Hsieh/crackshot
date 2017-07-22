import wx
from views.views_manager import *


class MainApp(wx.App):
    def __init__(self):
        wx.App.__init__(self)
        # Initial the main window
        self.views_manager = ViewsManager()
        self.views_manager.main_window.Show()
        self.main_window = self.views_manager.get_window("MainWindow")
        self.SetTopWindow(self.main_window)

    def OnInit(self):
        return True


if __name__ == "__main__":
    app = MainApp()
    app.MainLoop()


