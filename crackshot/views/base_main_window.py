# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep 12 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

id_BaseMainWindow = 1088


###########################################################################
## Class BaseMainWindow
###########################################################################

class BaseMainWindow(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=id_BaseMainWindow, title=u"导弹专家系统", pos=wx.DefaultPosition,
                          size=wx.Size(1000, 700), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        content_sizer = wx.BoxSizer(wx.VERTICAL)

        self.SetSizer(content_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


