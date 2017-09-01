"""Subclass of FLaporan, which is generated by wxFormBuilder."""

import wx
import frame.mainframe as mainframe

# Implementing FLaporan
class FLaporanEvent( mainframe.FLaporan ):
	def __init__( self, parent ):
		mainframe.FLaporan.__init__( self, parent )
	
		self.custom_event()
	
	def custom_event(self):
		self.m_panel19.Bind(wx.EVT_CHAR_HOOK,self.m_panelclosehook)

		pass
	def m_panelclosehook(self,event):
		print ("okay")
		if event.GetKeyCode() == wx.WXK_ESCAPE :
			self.Destroy()
	
		event.Skip()

