# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep 12 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

id_ShapeParaPanel = 1000


###########################################################################
## Class ShapeParaPanel
###########################################################################

class ShapeParaPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=id_ShapeParaPanel, pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.TAB_TRAVERSAL)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"set para", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer4.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.SetSizer(bSizer4)
        self.Layout()

    def __del__(self):
        pass


