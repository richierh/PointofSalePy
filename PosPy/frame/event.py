#!/usr/bin/python
"""
docstring
"""
import frame.mainframe as fm


class FFormEvent(fm.FForm):
    """
    docstring
    """
    def __init__(self, *args, **kwds):
        """
        docstring
        """
        super(FFormEvent, self).__init__(*args, **kwds)
        self.hidup = fm.FForm(self)

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

class FPenjualanEvent(fm.FPenjualan\
):
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
    docstring
    """
    def __init__(self, *args, **kwds):
        """
        docstring
        """
        super(FUtamaEvent, self).__init__(*args, **kwds)
        self.framepenj = fm.FPenjualan(self)

        
    def m_button1OnButtonClick(self, event):
        """
        docstring
        """
        try:
            self.framepenj.Maximize()
            self.framepenj.Show()
        except:
            self.framepenj = fm.FPenjualan(self)
            self.framepenj.Maximize()
            self.framepenj.Show()
        event.Skip()
        return 
    def m_button2OnButtonClick(self, event):
        """
        docstring
        """
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
        #mylists = [self.framepenj.Destroy()]
        #try:
        #dest = [mylist for mylist in range(1)]
        #self.Destroy()
        #except:
        #self.Destroy()
        event.Skip()
        return None   

