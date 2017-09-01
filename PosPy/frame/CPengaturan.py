"""Subclass of FPengaturan, which is generated by wxFormBuilder."""

import wx
import frame.mainframe as mainframe
import frame.CForm
import frame.cdataimport

# Implementing FPengaturan
class FPengaturanEvent( mainframe.FPengaturan ):
    def __init__( self, parent ):
        mainframe.FPengaturan.__init__( self, parent )
        self.bukaform = frame.CForm.FFormEvent(self)
        self.dataimport =frame.cdataimport.FDataImportEvent(self)
        self.custom_events()
    
    # Handlers for events.

    def custom_events(self):        
        self.m_panel9.Bind( wx.EVT_CHAR_HOOK, self.m_panel9OnChar )
        self.Bind( wx.EVT_CLOSE, self.FPengaturanOnClose )
        self.m_button18.Bind( wx.EVT_BUTTON, self.tombol1 )
        self.m_button19.Bind( wx.EVT_BUTTON, self.tombol2 )
        self.m_button20.Bind( wx.EVT_BUTTON, self.tombol3 )
        self.m_button21.Bind( wx.EVT_BUTTON, self.tombol4 )
        self.m_button22.Bind( wx.EVT_BUTTON, self.tombol5)
        self.m_button23.Bind( wx.EVT_BUTTON, self.tombol6 )


    def FPengaturanOnClose(self,event):
        # TODO: Implement FUtamaOnClose
        try:
            self.bukaform.Destroy()
            self.dataimport.Destroy()
            self.Destroy()
        except:
            self.Destroy()
        pass              
        
    def m_panel9OnChar(self,event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:

            print ("it's working, YOU press Escape so it\
            will close the frame Penjualan")
            self.FPengaturanOnClose(self)
        else :
            """Wrong button, or not exiting"""
            print (FPengaturanEvent.FPengaturanOnKeyDown.__doc__)
            print ("youre not doing the right thing,it's not working")
        event.Skip()
    def tombol1( self, event ):
        # TODO: Implement tombol1
        try :
            self.dataimport.Show()
        except :
            self.dataimport = frame.cdataimport.FDataImportEvent(self)
            self.dataimport.Show()
        
        pass
    
    def tombol2( self, event ):
        # TODO: Implement tombol2
        """This is the tombol2 working\
        test okay"""
        print (FPengaturanEvent.tombol2.__doc__)
        try:
            self.bukaform.Show()
        except:
            self.bukaform = frame.CForm.FFormEvent(self)
            self.bukaform.Show()
        pass
    
    def tombol3( self, event ):
        # TODO: Implement tombol3
        pass
    
    def tombol4( self, event ):
        # TODO: Implement tombol4
        pass
    
    def tombol5( self, event ):
        # TODO: Implement tombol5        pass
        pass
    def tombol6( self, event ):
        # TODO: Implement tombol5
        pass
    
    
