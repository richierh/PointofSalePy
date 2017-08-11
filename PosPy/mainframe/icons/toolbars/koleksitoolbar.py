import wx

import os
os.chdir("/home/pmc/mygit/PointofSalePy/PosPy")
 
#import mainframe

class self.createtoolbars(wx.ToolBar,wx.Bitmap):
    """
    kode file Tempat naruh gambar icons
    """
    def __init__(self,*args,**kwds):
        super(lokasitoolbar,self).__init__(*args,**kwds)        
        self.Bitmap=wx.Bitmap(os.path.realpath("PosPy/mainframe/\
        icons/Toolbars/software.png"),wx.BITMAP_TYPE_ANY)
        """disini sudah bisa """
        return None
    
    def __repr__(self):
        return "this is my functions"


