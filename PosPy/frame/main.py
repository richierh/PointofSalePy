#! /usr/bin/python
"""docstring"""

import os
import sys
import frame.event as EventU
import wx
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MyApp(wx.App, EventU.FUtamaEvent):
    """docstring"""
    def __init__(self, *args, **kwds):
        """docstring"""
        super(MyApp, self).__init__(*args, **kwds)
        self.frame = EventU.FUtamaEvent(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        self.MainLoop()
        