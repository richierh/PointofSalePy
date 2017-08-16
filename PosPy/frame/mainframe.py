# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from frame.custom import CStaticBitmap
from frame.custom import CDataListCtrl
from frame.custom import CToolbar
import wx
import wx.xrc

###########################################################################
## Class FUtama
###########################################################################

class FUtama ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SOFTWARE", pos = wx.DefaultPosition, size = wx.Size( 500,350 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 500,350 ), wx.Size( -1,-1 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"MODEL TAMPILAN APLIKASI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer3.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel2 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer2 = wx.FlexGridSizer( 5, 0, 0, 0 )
		fgSizer2.AddGrowableCol( 0 )
		fgSizer2.AddGrowableRow( 0 )
		fgSizer2.AddGrowableRow( 1 )
		fgSizer2.AddGrowableRow( 2 )
		fgSizer2.AddGrowableRow( 3 )
		fgSizer2.AddGrowableRow( 4 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.m_button1 = wx.Button( self.m_panel2, wx.ID_ANY, u"Pilihan A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_button1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		fgSizer2.Add( self.m_button1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_button2 = wx.Button( self.m_panel2, wx.ID_ANY, u"Pilihan B", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button2, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button3 = wx.Button( self.m_panel2, wx.ID_ANY, u"Pilihan C", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button3, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button4 = wx.Button( self.m_panel2, wx.ID_ANY, u"Pilihan D", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button4, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button5 = wx.Button( self.m_panel2, wx.ID_ANY, u"Pilihan E", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button5, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer2.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		self.m_bitmap2 = CStaticBitmap( self.m_panel2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_bitmap2, 3, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		self.m_panel2.SetSizer( bSizer2 )
		self.m_panel2.Layout()
		bSizer2.Fit( self.m_panel2 )
		bSizer4.Add( self.m_panel2, 3, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer4, 5, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer3 )
		self.m_panel1.Layout()
		bSizer3.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )
		self.m_button2.Bind( wx.EVT_BUTTON, self.m_button2OnButtonClick )
		self.m_button3.Bind( wx.EVT_BUTTON, self.m_button3OnButtonClick )
		self.m_button4.Bind( wx.EVT_BUTTON, self.m_button4OnButtonClick )
		self.m_button5.Bind( wx.EVT_BUTTON, self.m_button5OnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_button1OnButtonClick( self, event ):
		event.Skip()
	
	def m_button2OnButtonClick( self, event ):
		event.Skip()
	
	def m_button3OnButtonClick( self, event ):
		event.Skip()
	
	def m_button4OnButtonClick( self, event ):
		event.Skip()
	
	def m_button5OnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class FForm
###########################################################################

class FForm ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Formulir Isian", pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_panel2.SetBackgroundColour( wx.Colour( 74, 74, 74 ) )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText7 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"FORMULIR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		
		bSizer6.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 6, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 600,-1 ), 0 )
		self.m_textCtrl1.SetMaxLength( 0 ) 
		fgSizer2.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer2.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl2.SetMaxLength( 0 ) 
		fgSizer2.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer2.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl3.SetMaxLength( 0 ) 
		fgSizer2.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer2.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl4.SetMaxLength( 0 ) 
		fgSizer2.Add( self.m_textCtrl4, 0, wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer2.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl5.SetMaxLength( 0 ) 
		fgSizer2.Add( self.m_textCtrl5, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer2.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl6 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl6.SetMaxLength( 0 ) 
		fgSizer2.Add( self.m_textCtrl6, 0, wx.ALL, 5 )
		
		
		bSizer6.Add( fgSizer2, 4, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button1 = wx.Button( self.m_panel2, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_button2 = wx.Button( self.m_panel2, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer6.Add( bSizer7, 2, wx.ALIGN_RIGHT, 5 )
		
		
		self.m_panel2.SetSizer( bSizer6 )
		self.m_panel2.Layout()
		bSizer6.Fit( self.m_panel2 )
		bSizer5.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_textCtrl1.Bind( wx.EVT_TEXT, self.m_textCtrl1OnText )
		self.m_textCtrl2.Bind( wx.EVT_TEXT, self.m_textCtrl2OnText )
		self.m_textCtrl3.Bind( wx.EVT_TEXT, self.m_textCtrl3OnText )
		self.m_textCtrl4.Bind( wx.EVT_TEXT, self.m_textCtrl4OnText )
		self.m_textCtrl5.Bind( wx.EVT_TEXT, self.m_textCtrl5OnText )
		self.m_textCtrl6.Bind( wx.EVT_TEXT, self.m_textCtrl6OnText )
		self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )
		self.m_button2.Bind( wx.EVT_BUTTON, self.m_button2OnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_textCtrl1OnText( self, event ):
		event.Skip()
	
	def m_textCtrl2OnText( self, event ):
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
		event.Skip()
	

###########################################################################
## Class FPenjualan
###########################################################################

class FPenjualan ( CToolbar ):
	
	def __init__( self, parent ):
		CToolbar.__init__ ( self, parent, id = wx.ID_ANY, title = u"Form Penjualan", pos = wx.Point( 600,300 ), size = wx.Size( 1280,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 900,600 ), wx.Size( -1,-1 ) )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel4.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_panel4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel9 = wx.Panel( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel9.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer4 = wx.FlexGridSizer( 2, 6, 0, 0 )
		fgSizer4.AddGrowableCol( 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.AddGrowableCol( 2 )
		fgSizer4.AddGrowableCol( 3 )
		fgSizer4.AddGrowableCol( 4 )
		fgSizer4.AddGrowableCol( 5 )
		fgSizer4.AddGrowableRow( 0 )
		fgSizer4.AddGrowableRow( 1 )
		fgSizer4.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.m_staticText16 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"No", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		self.m_staticText16.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		fgSizer4.Add( self.m_staticText16, 1, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_staticText17 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		self.m_staticText17.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		fgSizer4.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_staticText18 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		self.m_staticText18.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		fgSizer4.Add( self.m_staticText18, 1, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_staticText19 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		self.m_staticText19.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		fgSizer4.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_staticText20 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"D", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		self.m_staticText20.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		fgSizer4.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_staticText21 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"E", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		self.m_staticText21.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		fgSizer4.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_textCtrl13 = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_textCtrl13, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrl14 = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_textCtrl14, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrl15 = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_textCtrl15, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrl16 = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_textCtrl16, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrl17 = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_textCtrl17, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrl18 = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl18.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_textCtrl18.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		fgSizer4.Add( self.m_textCtrl18, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer12.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		self.m_listCtrl1 = CDataListCtrl( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		self.m_listCtrl1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_listCtrl1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer12.Add( self.m_listCtrl1, 6, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel9.SetSizer( bSizer12 )
		self.m_panel9.Layout()
		bSizer12.Fit( self.m_panel9 )
		bSizer11.Add( self.m_panel9, 5, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel10 = wx.Panel( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel8 = wx.Panel( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button14 = wx.Button( self.m_panel8, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button14, 0, wx.ALL, 5 )
		
		self.m_button15 = wx.Button( self.m_panel8, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button15, 0, wx.ALL, 5 )
		
		self.m_button16 = wx.Button( self.m_panel8, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button16, 0, wx.ALL, 5 )
		
		
		self.m_panel8.SetSizer( bSizer14 )
		self.m_panel8.Layout()
		bSizer14.Fit( self.m_panel8 )
		bSizer13.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel92 = wx.Panel( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel92.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer13.Add( self.m_panel92, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel10.SetSizer( bSizer13 )
		self.m_panel10.Layout()
		bSizer13.Fit( self.m_panel10 )
		bSizer11.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel4.SetSizer( bSizer11 )
		self.m_panel4.Layout()
		bSizer11.Fit( self.m_panel4 )
		bSizer10.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer10 )
		self.Layout()
		self.MenuPenjualan = wx.MenuBar( 0 )
		self.m_menu2 = wx.Menu()
		self.MenuPenjualan.Append( self.m_menu2, u"Berkas" ) 
		
		self.SetMenuBar( self.MenuPenjualan )
		
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 300,150 ), style = wx.TAB_TRAVERSAL )
		
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer8.AddSpacer( ( 0, 10), 0, wx.EXPAND, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Apakah anda yakin ingin ingin melanjutkan?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		self.m_staticText9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer8.Add( self.m_staticText9, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button8 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button8, 0, wx.ALL, 5 )
		
		self.m_button9 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button9, 0, wx.ALL, 5 )
		
		self.m_button10 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button10, 0, wx.ALL, 5 )
		
		
		bSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MyFrame5
###########################################################################

class MyFrame5 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_toolBar3 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.m_tool10 = self.m_toolBar3.AddLabelTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar3.Realize() 
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MyToolBar1
###########################################################################

class MyToolBar1 ( wx.ToolBar ):
	
	def __init__( self, parent ):
		wx.ToolBar.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TB_HORIZONTAL )
		
		
		self.Realize()
	
	def __del__( self ):
		pass
	

