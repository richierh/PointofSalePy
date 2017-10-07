import wx


class rangkautama(wx.Frame):

    def __init__(self,*args,**kwds):
        super(rangkautama,self).__init__(*args,**kwds)
        self.SetTitle("Rangka Utama")
        self.Center()
        self.Maximize()
        self.panel = wx.Panel(self)
        button = wx.Button(self.panel,label="tombol saya", id= wx.ID_ANY,pos=(300,300))


    




if __name__=="__main__":
    root = wx.App()
    mainapp = rangkautama(None)
    mainapp.Show(True)
    root.MainLoop()