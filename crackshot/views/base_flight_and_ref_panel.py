# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep 12 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

id_FlightAndRefPanel = 1000


###########################################################################
## Class FlightAndRefPanel
###########################################################################

class FlightAndRefPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=id_FlightAndRefPanel, pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.TAB_TRAVERSAL)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Flight Pana", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer5.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.SetSizer(bSizer5)
        self.Layout()

    def __del__(self):
        pass


