#--------------------------------------------------------------------------------------------------
import wx

class MyPanel(wx.Panel):

    def __init__(self, *args, **kwargs):
        count = kwargs.pop('count')
        wx.Panel.__init__(self, *args, **kwargs)
        ctrls = [wx.TextCtrl(self, -1, '%d-%d' % (count, i+1)) for i
in range(5)]
        sizer = wx.BoxSizer(wx.VERTICAL)
        for c in ctrls:
            sizer.Add(c, 0, wx.ALL|wx.EXPAND, 2)
        self.SetSizerAndFit(sizer)

class MyFrame(wx.Frame):

    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        panels = [MyPanel(self, -1,
style=wx.RAISED_BORDER|wx.TAB_TRAVERSAL, count=i+1) for i in range(3)]
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        for p in panels:
            sizer.Add(p, 0, wx.ALL|wx.EXPAND, 0)
        self.SetSizerAndFit(sizer)


app = wx.App(False)
f = MyFrame(None, -1, u'Test Frame',
style=wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
f.Show(True)
app.MainLoop() 