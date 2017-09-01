#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade not found on Tue Aug 29 07:57:42 2017
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_3 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_4 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.list_ctrl_1 = wx.ListCtrl(self, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(_("frame"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(2, 5, 0, 0)
        label_1 = wx.StaticText(self, wx.ID_ANY, _("label_1"))
        grid_sizer_1.Add(label_1, 0, 0, 0)
        label_2 = wx.StaticText(self, wx.ID_ANY, _("label_2"))
        grid_sizer_1.Add(label_2, 0, 0, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, _("label_3"))
        grid_sizer_1.Add(label_3, 0, 0, 0)
        label_4 = wx.StaticText(self, wx.ID_ANY, _("label_4"))
        grid_sizer_1.Add(label_4, 0, 0, 0)
        label_5 = wx.StaticText(self, wx.ID_ANY, _("label_5"))
        grid_sizer_1.Add(label_5, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_1, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_2, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_3, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_4, 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        sizer_2.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        sizer_2.Add(self.list_ctrl_1, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_1.Add((50, 0), 0, 0, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MyFrame
class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = MyApp(0)
    app.MainLoop()