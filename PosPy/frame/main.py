#! /usr/bin/python
"""Application started"""
import wx
import frame.CUtama as EventU
print (__doc__)
root = wx.App()
frame = EventU.FUtamaEvent(None)
frame.Show()
root.MainLoop()
