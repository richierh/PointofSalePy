#!/usr/bin/python

import wx
import os
#from mainframe import FPenjualan
#import mainframe

class CToolbar(wx.Frame):

    def __init__(self,*args,**kwds):
        super(CToolbar,self).__init__(None)
        self.SetTitle=("")
        self.SetPosition(wx.DefaultPosition)
        self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )

        self.m_toolBar2 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
        self.m_tool6 = self.m_toolBar2.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( os.path.realpath("PosPy/frame/icons/toolbars/software.png"), wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
        
        self.m_tool7 = self.m_toolBar2.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( os.path.realpath("PosPy/frame/icons/toolbars/software.png"), wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 

        self.m_tool8 = self.m_toolBar2.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( os.path.realpath("PosPy/frame/icons/toolbars/software.png"), wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 

        self.m_tool = self.m_toolBar2.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( os.path.realpath("PosPy/frame/icons/toolbars/software.png"), wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
        
        self.m_too2 = self.m_toolBar2.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( os.path.realpath("PosPy/frame/icons/toolbars/software.png"), wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 

        self.m_too3 = self.m_toolBar2.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( os.path.realpath("PosPy/frame/icons/toolbars/software.png"), wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 



        self.m_toolBar2.Realize() 


class CDataViewListCtrl( wx.Panel ):
	
	def __init__( self, *args,**kwds):
		super (CDataViewListCtrl,self).__init__()
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
	#	self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
	#	bSizer13.Add( self.m_dataViewListCtrl1, 0, wx.ALL, 5 )
		
		
	#	self.SetSizer( bSizer13 )
		self.Layout()
	
	#def __del__( self ):
	#	pass
	

class CStaticBitmap(wx.StaticBitmap,wx.Bitmap):
    """
    kode file Tempat naruh gambar icons
    """
    def __init__(self,*args,**kwds):
        super(CStaticBitmap,self).__init__(*args,**kwds)        
        self.Bitmap=wx.Bitmap(os.path.realpath("PosPy/frame/icons/store.png"),wx.BITMAP_TYPE_ANY)
        """disini sudah bisa """
        return None
    
    def __repr__(self):
        return "this is my functions"


