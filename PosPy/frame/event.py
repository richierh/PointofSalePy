import frame.mainframe as fm
import frame.custom as fc
import wx
import os

class FFormEvent(fm.FForm):
    """
    """
    def __init__(self, *args, **kwds):
        """
        """
        super(FFormEvent, self).__init__(*args, **kwds)

    def m_textCtrl1OnText(self, event):
        """
        """
        print(self.m_textCtrl1.GetValue())
        event.Skip()
    def	m_textCtrl2OnText(self, event):
        """
        """
        event.Skip()
    def m_textCtrl3OnText(self, event):
        """
        """
        event.Skip()
    def m_textCtrl4OnText(self, event):
        """
        """
        event.Skip()
    def m_textCtrl5OnText(self, event):
        """
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
, fm.FUtama):
    """
    """
    def __init__(self, *args, **kwds):
        """
        """
        super(FPenjualanEvent, self).__init__(*args, **kwds)
        self.Maximize(True)

        return None

    def FPenjualanOnClose(self, event):
        """
        """
        pass
class FUtamaEvent(fm.FUtama):
    """
    """
    def __init__(self, *args, **kwds):
        """
        """
        super(FUtamaEvent, self).__init__(*args, **kwds)
    def m_button1OnButtonClick(self, event):
        """
        """
        l = FPenjualanEvent(self)
        l.Show()
        event.Skip()
        return None
    def m_button2OnButtonClick(self, event):
        """
        """
        event.Skip()
        return None
    def m_button3OnButtonClick(self, event):
        """
        """
        event.Skip()
        return None
    def m_button4OnButtonClick(self, event):
        """
        """
        event.Skip()
        return None
    def m_button5OnButtonClick(self, event):
        """
        """
        event.Skip()
        return None
