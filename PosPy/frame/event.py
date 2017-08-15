import frame.mainframe
#import frame.custom
import wx
import os

class FFormEvent(frame.mainframe.FForm):
    """
    """

    def __init__(self, *args, **kwds):
        super(FFormEvent, self).__init__(*args, **kwds)

    def m_textCtrl1OnText(self, event):
        print (self.m_textCtrl1.GetValue())
        event.Skip()
    
    def m_textCtrl1OnText( self, event ):
        event.Skip()
    
    def	m_textCtrl2OnText( self, event ):
        event.Skip()
    
    def m_textCtrl3OnText( self, event ):
        event.Skip()
    
    def m_textCtrl4OnText( self, event ):
        event.Skip()
    
    def m_textCtrl5OnText( self, event ):
        event.Skip()
    
    def m_textCtrl6OnText( self, event ):
        event.Skip()
    
    def m_button1OnButtonClick( self, event ):
        event.Skip()
    
    def m_button2OnButtonClick( self, event ):
        print (self.m_textCtrl1.GetValue())
        print (self.m_textCtrl2.GetValue())
        print (self.m_textCtrl3.GetValue())
        print (self.m_textCtrl4.GetValue())
        print (self.m_textCtrl5.GetValue())
        print (self.m_textCtrl6.GetValue())
        print ("okay")
        event.Skip()

class FPenjualanEvent(frame.mainframe.FPenjualan\
,frame.mainframe.FUtama):


    def __init__(self, *args, **kwds):
        super(FPenjualanEvent, self).__init__(*args, **kwds)

        #self.m_toolBar4.Realize() 
        self.Maximize(True)
        self.datalist

        self.CToolbar()
        return None
    
    def CToolbar(self):
        self.m_toolBar2 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
        self.m_toolBar2.SetToolBitmapSize((50, 50))
        self.m_tool6 = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( os.path.realpath("PosPy/frame/icons/toolbars/software.png"), wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 

        self.m_tool7 = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( os.path.realpath("PosPy/frame/icons/toolbars/software.png"), wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 

        self.m_tool8 = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( os.path.realpath("PosPy/frame/icons/toolbars/software.png"), wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 

        self.m_tool = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( os.path.realpath("PosPy/frame/icons/toolbars/software.png"), wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
        
        self.m_too2 = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( os.path.realpath("PosPy/frame/icons/toolbars/software.png"), wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 

        self.m_too3 = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( os.path.realpath("PosPy/frame/icons/toolbars/software.png"), wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 

        self.m_toolBar2.Realize() 
    

    def datalist():
        mycolumns=["A","B","C","D","E"]
        mywidth=[50,250,300,200,200]
        heading = list(mycolumns)
        print (len(mycolumns))
        l = [self.InsertColumn(i,heading=(str(heading[i])),width=mywidth[i]) for i in range(len(mycolumns))]

    def CToolbar(self):
        self.m_toolBar2 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
        self.m_toolBar2.SetToolBitmapSize(wx.Size(50,50))
        self.m_tool6 = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( os.path.realpath("PosPy/frame/icons/toolbars/software.png"), wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 

        self.m_tool7 = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( os.path.realpath("PosPy/frame/icons/toolbars/software.png"), wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 

        self.m_tool8 = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( os.path.realpath("PosPy/frame/icons/toolbars/software.png"), wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 

        self.m_tool = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( os.path.realpath("PosPy/frame/icons/toolbars/software.png"), wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
        
        self.m_too2 = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( os.path.realpath("PosPy/frame/icons/toolbars/software.png"), wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 

        self.m_too3 = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( os.path.realpath("PosPy/frame/icons/toolbars/software.png"), wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 

        self.m_toolBar2.Realize() 
        self.Layout()
    
    def FPenjualanOnClose(self,event):
        return None
        #self.FUtama.Show()

class FUtamaEvent(frame.mainframe.FUtama):
    """
    """
    def __init__(self, *args, **kwds):
        super(FUtamaEvent, self).__init__(*args, **kwds)
    
    def m_button1OnButtonClick(self,event):
        l = FPenjualanEvent(self)
        l.Show()
        #self.Hide()
        event.Skip()
        return None

    def m_button2OnButtonClick(self,event):
        event.Skip()
        return None
    
    def m_button3OnButtonClick(self,event):
        event.Skip()
        return None
    
    def m_button4OnButtonClick(self,event):
        event.Skip()
        return None
    
    def m_button5OnButtonClick(self,event):
        event.Skip()
        return None

    
