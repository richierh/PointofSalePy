#! /usr/bin/python
import wx
import os

from frame.event import *

class MyApp(wx.App):
    def OnInit(self):
        self.frame = FUtamaEvent(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True
import os

if __name__ == "__main__":
    
    app = MyApp(0)
    app.MainLoop()
