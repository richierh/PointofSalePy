import wx

import os

#print (os.path.realpath("PosPy/mainframe/icons/store.png"))

class lokasigambar(wx.StaticBitmap,wx.Bitmap):
    """
    kode file Tempat naruh gambar icons
    """
    def __init__(self,*args,**kwds):
        super(lokasigambar,self).__init__(*args,**kwds)        
        self.Bitmap=wx.Bitmap(os.path.realpath("PosPy/mainframe/icons/store.png"),wx.BITMAP_TYPE_ANY)
        """disini sudah bisa """
        return None
    
    def __repr__(self):
        return "this is my functions"


