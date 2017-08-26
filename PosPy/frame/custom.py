#!/usr/bin/python

import os
#$import wx.dataview
import wx
#print (mpath)
class CToolbar(wx.Frame):

    def __init__(self,*args,**kwds):
        super(CToolbar,self).__init__(None)
        self.__settoolbar__()
    
    def __settoolbar__(self):
        """
        """
        #import frame.icons.getdir
        self.m_toolBar2=self.CreateToolBar(style=wx.TB_DEFAULT_STYLE,id=wx.ID_ANY)
        self.m_toolBar2.SetToolBitmapSize((50, 50))
        self.m_tool6 = self.m_toolBar2.AddTool(wx.ID_ANY, u"tool", \
        wx.Bitmap(os.path.realpath("frame/icons/toolbars/software.png"), \
        wx.BITMAP_TYPE_ANY), \
        wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)
        self.m_tool7 = self.m_toolBar2.AddTool(wx.ID_ANY, u"tool", \
        wx.Bitmap( os.path.realpath("frame/icons/toolbars/software.png"), \
        wx.BITMAP_TYPE_ANY), \
        wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)
        self.m_tool8 = self.m_toolBar2.AddTool(wx.ID_ANY, u"tool", \
        wx.Bitmap( os.path.realpath("frame/icons/toolbars/software.png"), \
        wx.BITMAP_TYPE_ANY), \
        wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )
        self.m_tool = self.m_toolBar2.AddTool(wx.ID_ANY, u"tool", \
        wx.Bitmap( os.path.realpath("frame/icons/toolbars/software.png"), \
        wx.BITMAP_TYPE_ANY), \
        wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )
        self.m_too2 = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", \
        wx.Bitmap( os.path.realpath("frame/icons/toolbars/software.png"), \
        wx.BITMAP_TYPE_ANY ), \
        wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )
        self.m_too3 = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", \
        wx.Bitmap( os.path.realpath("frame/icons/toolbars/software.png"), \
        wx.BITMAP_TYPE_ANY ), \
        wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )
        self.m_toolBar2.Realize() 

###Class making list control
###This class would make list control in the "Penjualan" Frame
class CDataListCtrl( wx.ListCtrl ):
    
    def __init__( self, *args,**kwds):
        super (CDataListCtrl,self).__init__(*args,**kwds)
        self.mycolumns=["A","B","C","D","E"]
        self.mywidth=[50,250,300,200,200]
        self.heading = list(self.mycolumns)
        self.__setlistctrl__()

    def __setlistctrl__(self):
        l = [self.InsertColumn(i,heading=(str(self.heading[i])), \
        width=self.mywidth[i]) for i in range(len(self.mycolumns))]

class CStaticBitmap(wx.StaticBitmap,wx.Bitmap):
    """
    kode file Tempat naruh gambar icons
    """
    def __init__(self,*args,**kwds):
        super(CStaticBitmap,self).__init__(*args,**kwds)        
        self.Bitmap=wx.Bitmap(os.path.realpath("frame/icons/store.png"),wx.BITMAP_TYPE_ANY)
      
        """disini sudah bisa """
        return None
    def __repr__(self):
        return "this is my functions"


