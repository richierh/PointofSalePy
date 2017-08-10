#! /usr/bin/python
import wx
from mainframe.fungsievent import *
print ("hhh")

class MyApp(wx.App):
    def OnInit(self):
        self.frame = FUtamaEvent(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
