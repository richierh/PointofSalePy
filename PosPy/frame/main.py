#! /usr/bin/python
"""docstring"""
import wx
import frame.event as EventU

root = wx.App()
frame = EventU.FUtamaEvent(None)
frame.Show()
root.MainLoop()
