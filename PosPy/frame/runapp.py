#usr/bin/python
import wx
import frameutama

if __name__=="__main__":
    root = wx.App()
    mainapp = frameutama.FUtama(None)
    mainapp.Show()
    root.MainLoop()
