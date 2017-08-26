#!/usr/bin/python
"""
This is the code for any of event handler being stack
"""
import frame.mainframe as fm

print (__doc__)
class FFormEvent(fm.FForm):
    """
    docstring
    """
    def __init__(self, *args, **kwds):
        """
        docstring
        """
        super(FFormEvent, self).__init__(*args, **kwds)

    def m_textCtrl1OnText(self, event):
        """
        docstring
        """
        print(self.m_textCtrl1.GetValue())
        event.Skip()
    def	m_textCtrl2OnText(self, event):
        """
        docstring
        """
        event.Skip()
    def m_textCtrl3OnText(self, event):
        """
        docstring
        """
        event.Skip()
    def m_textCtrl4OnText(self, event):
        """
        docstring
        """
        event.Skip()
    def m_textCtrl5OnText(self, event):
        """
        docstring
        """
        event.Skip()
    def m_textCtrl6OnText(self, event):
        """
        l
        """
        event.Skip()
    def m_button1OnButtonClick(self, event):
        """
        l
        """
        event.Skip()
    def m_button2OnButtonClick(self, event):
        """
        docstring
        """
        print(self.m_textCtrl1.GetValue())
        print(self.m_textCtrl2.GetValue())
        print(self.m_textCtrl3.GetValue())
        print(self.m_textCtrl4.GetValue())
        print(self.m_textCtrl5.GetValue())
        print(self.m_textCtrl6.GetValue())
        print("okay")
        event.Skip()

class FPenjualanEvent(fm.FPenjualan):
    """
    docstring
    """
    def __init__(self, *args, **kwds):
        """
        """
        super(FPenjualanEvent, self).__init__(*args, **kwds)
        self.Maximize(True)
        return None
    def FPenjualanOnClose(self,event):
        event.Skip()

class FUtamaEvent(fm.FUtama):
    """
    Entering MainFrame
    """
    def __init__(self, *args, **kwds):
        """
        Masuk Rangka
        """
        super(FUtamaEvent, self).__init__(*args, **kwds)
        print (FUtamaEvent.__doc__)
        self.framepenj = FPenjualanEvent(self)
        self.framepeng = FPengaturanEvent(self)

       
    def m_button1OnButtonClick(self, event):
        """
        docstring
        """
        print ("Menu Penjualan")
        try:
            self.framepenj.Maximize()
            self.framepenj.Show()
        except:
            self.framepenj = FPenjualanEvent(self)
            self.framepenj.Maximize()
            self.framepenj.Show()
        event.Skip()
        return 
    def m_button2OnButtonClick(self, event):
        """
        docstring
        """
        try:
            self.framepeng.Show()
        except:
            self.framepeng = FPengaturanEvent(self)
            self.framepeng.Show()
        event.Skip()
        return None
    def m_button3OnButtonClick(self, event):
        """
        docstring
        """
        event.Skip()
        return None
    def m_button4OnButtonClick(self, event):
        """
        docstring
        """
        event.Skip()
        return None
    def m_button5OnButtonClick(self, event):
        """
        docstring
        """
        event.Skip()
        return None
    def FUtamaOnClose(self,event):
        try:
            self.framepenj.Destroy()
            self.framepeng.Destroy()
            self.Destroy()
        except:
            self.Destroy()
        event.Skip()
        return None
    def m_menuItem2OnMenuSelection( self, event ):
        try:
            self.framepeng.Show()
        except:
            self.framepeng = FPengaturanEvent(self)
            self.framepeng.Show()
        event.Skip()
        return None
        event.Skip()
       
class FPengaturanEvent(fm.FPengaturan):
    """
    docstring
    """
    def __init__(self,*args,**kwds):
        super(FPengaturanEvent,self).__init__(*args,**kwds)
        self.bukaform = FFormEvent(self)
        print ("okay")
    def m_button18OnButtonClick( self, event ):
        event.Skip()
    
    def m_button19OnButtonClick( self, event ):
        event.Skip()
    
    def m_button20OnButtonClick( self, event ):
        print ("hello")
        try:
            self.bukaform.Show()
        except:
            self.bukaform = FFormEvent(self)
            self.bukaform.Show()
        event.Skip()
    
    def m_button21OnButtonClick( self, event ):
        event.Skip()
    
    def m_button22OnButtonClick( self, event ):
        event.Skip()
    
    def m_button23OnButtonClick( self, event ):
        event.Skip()
    
    
        
