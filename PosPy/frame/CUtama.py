"""Subclass of FUtama, which is generated by wxFormBuilder."""

import wx
import frame.mainframe as mainframe
import frame.CPenjualan
import frame.CPengaturan
import frame.CLaporan

# Implementing FUtama
class FUtamaEvent( mainframe.FUtama ):
    def __init__( self, parent ):
        mainframe.FUtama.__init__( self, parent )
        print (FUtamaEvent.__doc__)
        self.framepenj = frame.CPenjualan.FPenjualanEvent(self)
        self.framepeng = frame.CPengaturan.FPengaturanEvent(self)
        self.framereport = frame.CLaporan.FLaporanEvent(self)
        self.framereport.Maximize()

        self.custom_event()
    
    def custom_event(self):
        # Connect Events
        self.Bind(wx.EVT_CHAR_HOOK,self.futamaoncloseescape)
        self.Bind( wx.EVT_CLOSE, self.FUtamaOnClose )
        self.btnsale.Bind( wx.EVT_BUTTON, self.btnsaleOnButtonClick )
        self.btnset.Bind( wx.EVT_BUTTON, self.btnsetOnButtonClick )
        self.btnbuy.Bind( wx.EVT_BUTTON, self.tombolpembelian )
        self.btnreport.Bind( wx.EVT_BUTTON, self.btnreportOnButtonClick )
        self.btnhelp.Bind( wx.EVT_BUTTON, self.btnhelpOnButtonClick )
        self.Bind( wx.EVT_MENU, self.menuitemsaleOnMenuSelection, id = self.menuitemsale.GetId() )
        self.Bind( wx.EVT_MENU, self.mitembuyOnMenuSelection, id = self.menuitembuy.GetId() )
        self.Bind( wx.EVT_MENU, self.menuitemreportOnMenuSelection, id = self.menuitemreport.GetId() )
        self.Bind( wx.EVT_MENU, self.m_menuItem2OnMenuSelection, id = self.m_menuItem2.GetId() )
    
        # Virtual event handlers, overide them in your derived class
 
    def futamaoncloseescape(self,event):
        if event.GetKeyCode()==wx.WXK_ESCAPE:
            self.Destroy()
        event.Skip()

    def tombolpembelian( self, event ):
        event.Skip()
        
    def btnreportOnButtonClick( self, event ):
        try:
            self.framereport.Show()
        except:
            self.framereport = frame.CLaporan.FLaporanEvent(self)
            self.framereport.Maximize()
            self.framereport.Show()

        event.Skip()
        
    def btnhelpOnButtonClick( self, event ):
        event.Skip()
    def menuitemsaleOnMenuSelection( self, event ):
        self.btnsaleOnButtonClick(self)
        event.Skip()
    
    def mitembuyOnMenuSelection( self, event ):
        self.tombolpembelian(self)
        event.Skip()
    
    def menuitemreportOnMenuSelection( self, event ):
        self.btnreportOnButtonClick(self)
        event.Skip()
    
    
    # Handlers for FUtama events.
    def FUtamaOnClose( self, event ):
        # TODO: Implement FUtamaOnClose
        try:
            self.framepenj.Destroy()
            self.framepeng.Destroy()
            self.Destroy()
        except:
            self.Destroy()
        pass      
    
    def btnsaleOnButtonClick( self, event ):
        # TODO: Implement m_button1OnButtonClick
        try:
            self.framepenj.Maximize()
            self.framepenj.Show()
        except:
            self.framepenj =  frame.CPenjualan.FPenjualanEvent(self)
            self.framepenj.Maximize()
            self.framepenj.Show()
        pass
    
    def btnsetOnButtonClick( self, event ):
        # TODO: Implement m_button2OnButtonClick

        try:
            self.framepeng.Show()
        except:
            self.framepeng = frame.CPengaturan.FPengaturanEvent(self)
            self.framepeng.Show()
        pass        