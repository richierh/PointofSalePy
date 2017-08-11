#! /usr/bin/python
import wx
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from frame.event import *

class MyApp(wx.App):
    def OnInit(self):
        self.frame = FUtamaEvent(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == "__main__":
    
    app = MyApp(0)
    app.MainLoop()
