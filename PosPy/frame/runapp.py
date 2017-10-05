#usr/bin/python
import wx
import FrameUtama

if __name__=="__main__":
    root = wx.App()
    mainapp = FrameUtama.FUtama(None)
    mainapp.Show()
    root.MainLoop()
