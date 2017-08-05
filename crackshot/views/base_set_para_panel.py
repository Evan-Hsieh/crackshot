# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep 12 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx


###########################################################################
## Class SetParaPanel
###########################################################################

class SetParaPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(1000, 700),
                          style=wx.TAB_TRAVERSAL)

        BodySizer = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_TOP)
        self.m_notebook.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        self.body_para_panel = wx.Panel(self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        gbSizer5 = wx.GridBagSizer(0, 20)
        gbSizer5.SetFlexibleDirection(wx.BOTH)
        gbSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        sbSizer4 = wx.StaticBoxSizer(wx.StaticBox(self.body_para_panel, wx.ID_ANY, u"头部参数"), wx.VERTICAL)

        self.m_staticText12 = wx.StaticText(self.body_para_panel, wx.ID_ANY, u"头部曲线类型", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)
        sbSizer4.Add(self.m_staticText12, 0, wx.ALL, 5)

        m_choice8Choices = [u"锥形", u"弧形", u"卡门"]
        self.m_choice8 = wx.Choice(self.body_para_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                   m_choice8Choices, 0)
        self.m_choice8.SetSelection(0)
        sbSizer4.Add(self.m_choice8, 0, wx.ALIGN_CENTER | wx.EXPAND | wx.LEFT, 5)

        self.m_staticText13 = wx.StaticText(self.body_para_panel, wx.ID_ANY, u"头部长度", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)
        sbSizer4.Add(self.m_staticText13, 0, wx.ALL, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl6 = wx.TextCtrl(self.body_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer4.Add(self.m_textCtrl6, 0, wx.ALIGN_CENTER | wx.LEFT, 5)

        self.m_staticText7 = wx.StaticText(self.body_para_panel, wx.ID_ANY, u"米", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        bSizer4.Add(self.m_staticText7, 0, wx.ALIGN_CENTER, 5)

        sbSizer4.Add(bSizer4, 1, wx.EXPAND, 5)

        self.m_staticText14 = wx.StaticText(self.body_para_panel, wx.ID_ANY, u"头部末端直径", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)
        sbSizer4.Add(self.m_staticText14, 0, wx.ALL, 5)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl61 = wx.TextCtrl(self.body_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer3.Add(self.m_textCtrl61, 0, wx.ALIGN_CENTER | wx.LEFT, 5)

        self.m_staticText6 = wx.StaticText(self.body_para_panel, wx.ID_ANY, u"米", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer3.Add(self.m_staticText6, 0, wx.ALIGN_CENTER, 5)

        sbSizer4.Add(bSizer3, 1, wx.EXPAND, 5)

        gbSizer5.Add(sbSizer4, wx.GBPosition(0, 4), wx.GBSpan(3, 1), wx.ALL, 5)

        sbSizer14 = wx.StaticBoxSizer(wx.StaticBox(self.body_para_panel, wx.ID_ANY, u"圆柱段参数"), wx.VERTICAL)

        self.m_staticText15 = wx.StaticText(self.body_para_panel, wx.ID_ANY, u"圆柱段直径", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText15.Wrap(-1)
        sbSizer14.Add(self.m_staticText15, 0, wx.ALL, 5)

        bSizer51 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl7 = wx.TextCtrl(self.body_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer51.Add(self.m_textCtrl7, 0, wx.ALIGN_CENTER | wx.LEFT, 5)

        self.m_staticText8 = wx.StaticText(self.body_para_panel, wx.ID_ANY, u"米", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        bSizer51.Add(self.m_staticText8, 0, wx.ALIGN_CENTER, 5)

        sbSizer14.Add(bSizer51, 1, wx.EXPAND, 5)

        self.m_staticText10 = wx.StaticText(self.body_para_panel, wx.ID_ANY, u"圆柱段长度", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        sbSizer14.Add(self.m_staticText10, 0, wx.ALL, 5)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl8 = wx.TextCtrl(self.body_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer6.Add(self.m_textCtrl8, 0, wx.ALIGN_CENTER | wx.LEFT, 5)

        self.m_staticText11 = wx.StaticText(self.body_para_panel, wx.ID_ANY, u"米", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText11.Wrap(-1)
        bSizer6.Add(self.m_staticText11, 0, wx.ALIGN_CENTER, 5)

        sbSizer14.Add(bSizer6, 1, wx.EXPAND, 5)

        gbSizer5.Add(sbSizer14, wx.GBPosition(0, 5), wx.GBSpan(2, 1), wx.ALL, 5)

        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self.body_para_panel, wx.ID_ANY, u"收缩尾部参数"), wx.VERTICAL)

        self.m_staticText121 = wx.StaticText(self.body_para_panel, wx.ID_ANY, u"收缩尾部类型", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText121.Wrap(-1)
        sbSizer3.Add(self.m_staticText121, 0, wx.ALL, 5)

        m_choice2Choices = [u"锥形", u"弧形"]
        self.m_choice2 = wx.Choice(self.body_para_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                   m_choice2Choices, 0)
        self.m_choice2.SetSelection(0)
        sbSizer3.Add(self.m_choice2, 0, wx.EXPAND | wx.LEFT, 5)

        self.m_staticText131 = wx.StaticText(self.body_para_panel, wx.ID_ANY, u"收缩尾部长度", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText131.Wrap(-1)
        sbSizer3.Add(self.m_staticText131, 0, wx.ALL, 5)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl9 = wx.TextCtrl(self.body_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer7.Add(self.m_textCtrl9, 0, wx.LEFT, 5)

        self.m_staticText141 = wx.StaticText(self.body_para_panel, wx.ID_ANY, u"米", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText141.Wrap(-1)
        bSizer7.Add(self.m_staticText141, 0, wx.ALIGN_CENTER, 5)

        sbSizer3.Add(bSizer7, 1, wx.EXPAND, 5)

        gbSizer5.Add(sbSizer3, wx.GBPosition(0, 6), wx.GBSpan(2, 1), wx.ALL, 5)

        sbSizer5 = wx.StaticBoxSizer(wx.StaticBox(self.body_para_panel, wx.ID_ANY, u"底部参数"), wx.VERTICAL)

        self.m_staticText17 = wx.StaticText(self.body_para_panel, wx.ID_ANY, u"底部直径", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)
        sbSizer5.Add(self.m_staticText17, 0, wx.ALL, 5)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl11 = wx.TextCtrl(self.body_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer9.Add(self.m_textCtrl11, 0, wx.LEFT, 5)

        self.m_staticText18 = wx.StaticText(self.body_para_panel, wx.ID_ANY, u"米", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText18.Wrap(-1)
        bSizer9.Add(self.m_staticText18, 0, wx.ALIGN_CENTER, 5)

        sbSizer5.Add(bSizer9, 1, wx.EXPAND, 5)

        self.m_staticText171 = wx.StaticText(self.body_para_panel, wx.ID_ANY, u"喷管出口直径", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText171.Wrap(-1)
        sbSizer5.Add(self.m_staticText171, 0, wx.ALL, 5)

        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl91 = wx.TextCtrl(self.body_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer12.Add(self.m_textCtrl91, 0, wx.LEFT, 5)

        self.m_staticText181 = wx.StaticText(self.body_para_panel, wx.ID_ANY, u"米", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText181.Wrap(-1)
        bSizer12.Add(self.m_staticText181, 0, wx.ALIGN_CENTER, 5)

        sbSizer5.Add(bSizer12, 1, wx.EXPAND, 5)

        gbSizer5.Add(sbSizer5, wx.GBPosition(0, 7), wx.GBSpan(2, 1), wx.ALL, 5)

        bSizer5.Add(gbSizer5, 1, wx.ALL | wx.EXPAND, 20)

        self.body_para_panel.SetSizer(bSizer5)
        self.body_para_panel.Layout()
        bSizer5.Fit(self.body_para_panel)
        self.m_notebook.AddPage(self.body_para_panel, u"弹身参数", False)
        self.wings_para_panel = wx.Panel(self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TAB_TRAVERSAL)
        fgSizer1 = wx.FlexGridSizer(2, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_button6 = wx.Button(self.wings_para_panel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.m_button6, 0, wx.ALL, 5)

        self.m_textCtrl5 = wx.TextCtrl(self.wings_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        fgSizer1.Add(self.m_textCtrl5, 0, wx.ALL, 5)

        self.wings_para_panel.SetSizer(fgSizer1)
        self.wings_para_panel.Layout()
        fgSizer1.Fit(self.wings_para_panel)
        self.m_notebook.AddPage(self.wings_para_panel, u"弹翼参数", False)
        self.flight_condition_panel = wx.Panel(self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                               wx.TAB_TRAVERSAL)
        self.m_notebook.AddPage(self.flight_condition_panel, u"飞行条件", False)
        self.ref_para_panel = wx.Panel(self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_notebook.AddPage(self.ref_para_panel, u"参考值", False)

        BodySizer.Add(self.m_notebook, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(BodySizer)
        self.Layout()

    def __del__(self):
        pass


