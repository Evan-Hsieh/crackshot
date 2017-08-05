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

        gbSizer5.Add(sbSizer4, wx.GBPosition(0, 3), wx.GBSpan(3, 1), wx.ALL, 5)

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

        gbSizer5.Add(sbSizer14, wx.GBPosition(0, 4), wx.GBSpan(2, 1), wx.ALL, 5)

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

        gbSizer5.Add(sbSizer3, wx.GBPosition(0, 5), wx.GBSpan(2, 1), wx.ALL, 5)

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

        gbSizer5.Add(sbSizer5, wx.GBPosition(0, 6), wx.GBSpan(2, 1), wx.ALL, 5)

        bSizer5.Add(gbSizer5, 1, wx.ALL | wx.EXPAND, 20)

        self.body_para_panel.SetSizer(bSizer5)
        self.body_para_panel.Layout()
        bSizer5.Fit(self.body_para_panel)
        self.m_notebook.AddPage(self.body_para_panel, u"弹身参数", False)
        self.wings_para_panel = wx.Panel(self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TAB_TRAVERSAL)
        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        gbSizer2 = wx.GridBagSizer(0, 20)
        gbSizer2.SetFlexibleDirection(wx.BOTH)
        gbSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        sbSizer51 = wx.StaticBoxSizer(wx.StaticBox(self.wings_para_panel, wx.ID_ANY, u"整体参数"), wx.VERTICAL)

        self.m_staticText19 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"弹翼组数", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText19.Wrap(-1)
        sbSizer51.Add(self.m_staticText19, 0, wx.ALL, 5)

        self.m_textCtrl10 = wx.TextCtrl(self.wings_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        sbSizer51.Add(self.m_textCtrl10, 0, wx.BOTTOM | wx.LEFT, 5)

        self.m_staticText20 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"弹翼位置", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText20.Wrap(-1)
        sbSizer51.Add(self.m_staticText20, 0, wx.ALL, 5)

        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl12 = wx.TextCtrl(self.wings_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer14.Add(self.m_textCtrl12, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.LEFT, 5)

        self.m_staticText21 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"米", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText21.Wrap(-1)
        bSizer14.Add(self.m_staticText21, 0, wx.ALIGN_CENTER, 5)

        sbSizer51.Add(bSizer14, 1, wx.EXPAND, 5)

        self.m_staticText22 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"翼片数据", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        sbSizer51.Add(self.m_staticText22, 0, wx.ALL, 5)

        m_choice3Choices = [u"2", u"4", u"6", u"8"]
        self.m_choice3 = wx.Choice(self.wings_para_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                   m_choice3Choices, 0)
        self.m_choice3.SetSelection(0)
        sbSizer51.Add(self.m_choice3, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText23 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"布局（周向角度）", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText23.Wrap(-1)
        sbSizer51.Add(self.m_staticText23, 0, wx.ALL, 5)

        bSizer15 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl15 = wx.TextCtrl(self.wings_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer15.Add(self.m_textCtrl15, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.LEFT, 5)

        self.m_staticText24 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"角度", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText24.Wrap(-1)
        bSizer15.Add(self.m_staticText24, 0, wx.ALIGN_CENTER, 5)

        sbSizer51.Add(bSizer15, 1, wx.EXPAND, 5)

        gbSizer2.Add(sbSizer51, wx.GBPosition(0, 3), wx.GBSpan(4, 1), wx.ALL, 5)

        sbSizer7 = wx.StaticBoxSizer(wx.StaticBox(self.wings_para_panel, wx.ID_ANY, u"根弦参数"), wx.VERTICAL)

        self.m_staticText31 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"根弦长度", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        sbSizer7.Add(self.m_staticText31, 0, wx.ALL, 5)

        bSizer21 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl21 = wx.TextCtrl(self.wings_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer21.Add(self.m_textCtrl21, 0, wx.BOTTOM | wx.LEFT, 5)

        self.m_staticText32 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"米", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText32.Wrap(-1)
        bSizer21.Add(self.m_staticText32, 0, wx.ALIGN_CENTER, 5)

        sbSizer7.Add(bSizer21, 1, wx.EXPAND, 5)

        self.m_staticText33 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"根弦到弹轴距离", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText33.Wrap(-1)
        sbSizer7.Add(self.m_staticText33, 0, wx.ALL, 5)

        bSizer22 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl22 = wx.TextCtrl(self.wings_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer22.Add(self.m_textCtrl22, 0, wx.BOTTOM | wx.LEFT, 5)

        self.m_staticText34 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"米", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText34.Wrap(-1)
        bSizer22.Add(self.m_staticText34, 0, wx.ALIGN_CENTER, 5)

        sbSizer7.Add(bSizer22, 1, wx.EXPAND, 5)

        self.m_staticText35 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"根弦厚度", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText35.Wrap(-1)
        sbSizer7.Add(self.m_staticText35, 0, wx.ALL, 5)

        bSizer23 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl23 = wx.TextCtrl(self.wings_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer23.Add(self.m_textCtrl23, 0, wx.BOTTOM | wx.LEFT, 5)

        self.m_staticText36 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"米", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText36.Wrap(-1)
        bSizer23.Add(self.m_staticText36, 0, wx.ALIGN_CENTER, 5)

        sbSizer7.Add(bSizer23, 1, wx.EXPAND, 5)

        gbSizer2.Add(sbSizer7, wx.GBPosition(0, 4), wx.GBSpan(3, 1), wx.ALL, 5)

        sbSizer8 = wx.StaticBoxSizer(wx.StaticBox(self.wings_para_panel, wx.ID_ANY, u"梢弦参数"), wx.VERTICAL)

        self.m_staticText37 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"梢弦长度", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText37.Wrap(-1)
        sbSizer8.Add(self.m_staticText37, 0, wx.ALL, 5)

        bSizer24 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl24 = wx.TextCtrl(self.wings_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer24.Add(self.m_textCtrl24, 0, wx.BOTTOM | wx.LEFT, 5)

        self.m_staticText38 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"米", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText38.Wrap(-1)
        bSizer24.Add(self.m_staticText38, 0, wx.ALIGN_CENTER, 5)

        sbSizer8.Add(bSizer24, 1, wx.EXPAND, 5)

        self.m_staticText39 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"梢弦到弹轴距离", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText39.Wrap(-1)
        sbSizer8.Add(self.m_staticText39, 0, wx.ALL, 5)

        bSizer25 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl25 = wx.TextCtrl(self.wings_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer25.Add(self.m_textCtrl25, 0, wx.BOTTOM | wx.LEFT, 5)

        self.m_staticText40 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"米", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText40.Wrap(-1)
        bSizer25.Add(self.m_staticText40, 0, wx.ALIGN_CENTER, 5)

        sbSizer8.Add(bSizer25, 1, wx.EXPAND, 5)

        self.m_staticText41 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"梢弦厚度", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText41.Wrap(-1)
        sbSizer8.Add(self.m_staticText41, 0, wx.ALL, 5)

        bSizer26 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl26 = wx.TextCtrl(self.wings_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer26.Add(self.m_textCtrl26, 0, wx.BOTTOM | wx.LEFT, 5)

        self.m_staticText42 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"米", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText42.Wrap(-1)
        bSizer26.Add(self.m_staticText42, 0, wx.ALIGN_CENTER, 5)

        sbSizer8.Add(bSizer26, 1, wx.EXPAND, 5)

        gbSizer2.Add(sbSizer8, wx.GBPosition(0, 5), wx.GBSpan(1, 1), wx.ALL, 5)

        sbSizer9 = wx.StaticBoxSizer(wx.StaticBox(self.wings_para_panel, wx.ID_ANY, u"其他参数"), wx.VERTICAL)

        gbSizer3 = wx.GridBagSizer(0, 0)
        gbSizer3.SetFlexibleDirection(wx.BOTH)
        gbSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText59 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"后掠角", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText59.Wrap(-1)
        gbSizer3.Add(self.m_staticText59, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_choice6Choices = [u"前缘后掠角", u"后缘后掠角"]
        self.m_choice6 = wx.Choice(self.wings_para_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                   m_choice6Choices, 0)
        self.m_choice6.SetSelection(0)
        gbSizer3.Add(self.m_choice6, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_textCtrl40 = wx.TextCtrl(self.wings_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        gbSizer3.Add(self.m_textCtrl40, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.BOTTOM | wx.RIGHT | wx.TOP, 5)

        self.m_staticText60 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"弹翼剖面类型", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText60.Wrap(-1)
        gbSizer3.Add(self.m_staticText60, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_choice7Choices = [u"对称六边形"]
        self.m_choice7 = wx.Choice(self.wings_para_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                   m_choice7Choices, 0)
        self.m_choice7.SetSelection(0)
        gbSizer3.Add(self.m_choice7, wx.GBPosition(3, 0), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        self.m_staticText54 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"LMAXU", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText54.Wrap(-1)
        gbSizer3.Add(self.m_staticText54, wx.GBPosition(4, 0), wx.GBSpan(1, 1), wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_textCtrl36 = wx.TextCtrl(self.wings_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        gbSizer3.Add(self.m_textCtrl36, wx.GBPosition(4, 1), wx.GBSpan(1, 1), wx.BOTTOM | wx.RIGHT | wx.TOP, 5)

        self.m_staticText55 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"LFLATU", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText55.Wrap(-1)
        gbSizer3.Add(self.m_staticText55, wx.GBPosition(5, 0), wx.GBSpan(1, 1), wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_textCtrl37 = wx.TextCtrl(self.wings_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        gbSizer3.Add(self.m_textCtrl37, wx.GBPosition(5, 1), wx.GBSpan(1, 1), wx.BOTTOM | wx.RIGHT | wx.TOP, 5)

        self.m_staticText56 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"ZUPPER", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText56.Wrap(-1)
        gbSizer3.Add(self.m_staticText56, wx.GBPosition(6, 0), wx.GBSpan(1, 1), wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_textCtrl38 = wx.TextCtrl(self.wings_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        gbSizer3.Add(self.m_textCtrl38, wx.GBPosition(6, 1), wx.GBSpan(1, 1), wx.BOTTOM | wx.RIGHT | wx.TOP, 5)

        self.m_staticText57 = wx.StaticText(self.wings_para_panel, wx.ID_ANY, u"ZLOWER", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText57.Wrap(-1)
        gbSizer3.Add(self.m_staticText57, wx.GBPosition(7, 0), wx.GBSpan(1, 1), wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_textCtrl39 = wx.TextCtrl(self.wings_para_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        gbSizer3.Add(self.m_textCtrl39, wx.GBPosition(7, 1), wx.GBSpan(1, 1), wx.BOTTOM | wx.RIGHT | wx.TOP, 5)

        sbSizer9.Add(gbSizer3, 1, wx.EXPAND, 5)

        gbSizer2.Add(sbSizer9, wx.GBPosition(0, 6), wx.GBSpan(1, 1), wx.ALL, 5)

        bSizer13.Add(gbSizer2, 1, wx.EXPAND | wx.TOP, 20)

        self.wings_para_panel.SetSizer(bSizer13)
        self.wings_para_panel.Layout()
        bSizer13.Fit(self.wings_para_panel)
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


