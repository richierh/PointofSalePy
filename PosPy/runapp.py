import frame.FrameUtama

if __name__=="__main__":
    import wx
    root = wx.App()
    mainapp = frame.FrameUtama.FUtama(None)
    mainapp.Show()
    root.MainLoop()