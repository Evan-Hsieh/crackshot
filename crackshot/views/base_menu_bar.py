# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep 12 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

id_m_file_create_project = 1000
id_file_open_project = 1001
id_m_file_save_project = 1002
id_m_para_set_para = 1003
id_m_para_check_para = 1004
id_m_cal_cal = 1005
id_m_cal_draw = 1006
id_m_help_guide = 1007
id_m_about_version = 1008
id_m_about_copyright = 1009


###########################################################################
## Class BaseMenuBar
###########################################################################

class BaseMenuBar(wx.MenuBar):
    def __init__(self):
        wx.MenuBar.__init__(self, style=0)

        self.m_file = wx.Menu()
        self.m_file_create_project = wx.MenuItem(self.m_file, id_m_file_create_project, u"新建工程", wx.EmptyString,
                                                 wx.ITEM_NORMAL)
        self.m_file.AppendItem(self.m_file_create_project)

        self.m_file_open_project = wx.MenuItem(self.m_file, id_file_open_project, u"打开工程", wx.EmptyString,
                                               wx.ITEM_NORMAL)
        self.m_file.AppendItem(self.m_file_open_project)

        self.m_file_save_project = wx.MenuItem(self.m_file, id_m_file_save_project, u"保存工程", wx.EmptyString,
                                               wx.ITEM_NORMAL)
        self.m_file.AppendItem(self.m_file_save_project)

        self.Append(self.m_file, u"文件")

        self.m_para = wx.Menu()
        self.m_para_set_para = wx.MenuItem(self.m_para, id_m_para_set_para, u"输入参数", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_para.AppendItem(self.m_para_set_para)

        self.m_para_check_para = wx.MenuItem(self.m_para, id_m_para_check_para, u"查看参数", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_para.AppendItem(self.m_para_check_para)

        self.Append(self.m_para, u"参数设置")

        self.m_cal = wx.Menu()
        self.m_cal_cal = wx.MenuItem(self.m_cal, id_m_cal_cal, u"计算", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_cal.AppendItem(self.m_cal_cal)

        self.m_cal_draw = wx.MenuItem(self.m_cal, id_m_cal_draw, u"绘图", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_cal.AppendItem(self.m_cal_draw)

        self.Append(self.m_cal, u"计算与绘图")

        self.m_help = wx.Menu()
        self.m_help_guide = wx.MenuItem(self.m_help, id_m_help_guide, u"软件指南", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_help.AppendItem(self.m_help_guide)

        self.Append(self.m_help, u"帮助")

        self.m_about = wx.Menu()
        self.m_about_version = wx.MenuItem(self.m_about, id_m_about_version, u"版本", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_about.AppendItem(self.m_about_version)

        self.m_about_copyright = wx.MenuItem(self.m_about, id_m_about_copyright, u"版权", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_about.AppendItem(self.m_about_copyright)

        self.Append(self.m_about, u"关于")

        # Connect Events
        self.Bind(wx.EVT_MENU, self.set_para, id=self.m_para_set_para.GetId())
        self.Bind(wx.EVT_MENU, self.check_para, id=self.m_para_check_para.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def set_para(self, event):
        event.Skip()

    def check_para(self, event):
        event.Skip()


