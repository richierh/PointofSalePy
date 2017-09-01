# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FUtama
###########################################################################

class FUtama ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SOFTWARE", pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 500,400 ), wx.Size( -1,-1 ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"MODEL TAMPILAN APLIKASI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer3.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer2 = wx.FlexGridSizer( 5, 0, 0, 0 )
		fgSizer2.AddGrowableCol( 0 )
		fgSizer2.AddGrowableRow( 0 )
		fgSizer2.AddGrowableRow( 1 )
		fgSizer2.AddGrowableRow( 2 )
		fgSizer2.AddGrowableRow( 3 )
		fgSizer2.AddGrowableRow( 4 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"Penjualan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_button1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		fgSizer2.Add( self.m_button1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_button2 = wx.Button( self.m_panel1, wx.ID_ANY, u"Pengaturan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button2, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button3 = wx.Button( self.m_panel1, wx.ID_ANY, u"Pembelian", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button3, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button4 = wx.Button( self.m_panel1, wx.ID_ANY, u"Laporan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button4, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button5 = wx.Button( self.m_panel1, wx.ID_ANY, u"Bantuan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button5, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer28.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		self.m_bitmap2 = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"/home/richie/mygit/PointofSalePy/PosPy/frame/icons/store.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bitmap2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.m_bitmap2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer28.Add( self.m_bitmap2, 3, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer28, 1, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer3 )
		self.m_panel1.Layout()
		bSizer3.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu2 = wx.Menu()
		self.m_menubar2.Append( self.m_menu2, u"Berkas" ) 
		
		self.m_menu5 = wx.Menu()
		self.m_menuItem3 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Penjualan", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.AppendItem( self.m_menuItem3 )
		
		self.m_menuItem4 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Pembelian", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.AppendItem( self.m_menuItem4 )
		
		self.m_menu5.AppendSeparator()
		
		self.m_menuItem5 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Laporan", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.AppendItem( self.m_menuItem5 )
		
		self.m_menubar2.Append( self.m_menu5, u"Tampilan" ) 
		
		self.m_menu3 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Data", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.m_menuItem2 )
		
		self.m_menubar2.Append( self.m_menu3, u"Pengaturan" ) 
		
		self.m_menu4 = wx.Menu()
		self.m_menubar2.Append( self.m_menu4, u"Bantuan" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FUtamaOnClose )
		self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )
		self.m_button2.Bind( wx.EVT_BUTTON, self.m_button2OnButtonClick )
		self.m_button3.Bind( wx.EVT_BUTTON, self.m_button3OnButtonClick )
		self.m_button4.Bind( wx.EVT_BUTTON, self.m_button4OnButtonClick )
		self.m_button5.Bind( wx.EVT_BUTTON, self.m_button5OnButtonClick )
		self.Bind( wx.EVT_MENU, self.m_menuItem3OnMenuSelection, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItem4OnMenuSelection, id = self.m_menuItem4.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItem5OnMenuSelection, id = self.m_menuItem5.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItem2OnMenuSelection, id = self.m_menuItem2.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FUtamaOnClose( self, event ):
		event.Skip()
	
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
	
	def m_menuItem3OnMenuSelection( self, event ):
		event.Skip()
	
	def m_menuItem4OnMenuSelection( self, event ):
		event.Skip()
	
	def m_menuItem5OnMenuSelection( self, event ):
		event.Skip()
	
	def m_menuItem2OnMenuSelection( self, event ):
		event.Skip()
	

###########################################################################
## Class FForm
###########################################################################

class FForm ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Formulir Isian", pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText7 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"FORMULIR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		
		bSizer6.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 6, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Label A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 600,-1 ), 0 )
		self.m_textCtrl1.SetMaxLength( 0 ) 
		fgSizer2.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Label B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer2.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 600,-1 ), 0 )
		self.m_textCtrl2.SetMaxLength( 0 ) 
		fgSizer2.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Label 3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer2.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 600,-1 ), 0 )
		self.m_textCtrl3.SetMaxLength( 0 ) 
		fgSizer2.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Label 4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer2.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 600,-1 ), 0 )
		self.m_textCtrl4.SetMaxLength( 0 ) 
		fgSizer2.Add( self.m_textCtrl4, 0, wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Label 6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer2.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 600,-1 ), 0 )
		self.m_textCtrl5.SetMaxLength( 0 ) 
		fgSizer2.Add( self.m_textCtrl5, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Label 7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer2.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl6 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 600,-1 ), 0 )
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

class FPenjualan ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Form Penjualan", pos = wx.Point( 600,300 ), size = wx.Size( 1280,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 900,600 ), wx.Size( -1,-1 ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_panel4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer4 = wx.FlexGridSizer( 2, 6, 0, 0 )
		fgSizer4.AddGrowableCol( 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.AddGrowableCol( 2 )
		fgSizer4.AddGrowableCol( 3 )
		fgSizer4.AddGrowableCol( 4 )
		fgSizer4.AddGrowableCol( 5 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.m_staticText16 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"No", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		self.m_staticText16.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		fgSizer4.Add( self.m_staticText16, 1, wx.ALL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )
		
		self.m_staticText17 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		self.m_staticText17.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		fgSizer4.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_staticText18 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Kuantiti", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		self.m_staticText18.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		fgSizer4.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_staticText19 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		self.m_staticText19.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		fgSizer4.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_staticText20 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"D", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		self.m_staticText20.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		fgSizer4.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_staticText21 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"E", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		self.m_staticText21.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		fgSizer4.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_textCtrl13 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, u"c", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_textCtrl13.SetFont( wx.Font( 13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		
		fgSizer4.Add( self.m_textCtrl13, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrl14 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.m_textCtrl14.SetFont( wx.Font( 13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_textCtrl14.Enable( False )
		
		fgSizer4.Add( self.m_textCtrl14, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrl15 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl15.SetFont( wx.Font( 13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_textCtrl15.Enable( False )
		
		fgSizer4.Add( self.m_textCtrl15, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrl16 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl16.SetFont( wx.Font( 13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_textCtrl16.Enable( False )
		
		fgSizer4.Add( self.m_textCtrl16, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrl17 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl17.SetFont( wx.Font( 13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_textCtrl17.Enable( False )
		
		fgSizer4.Add( self.m_textCtrl17, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrl18 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl18.SetFont( wx.Font( 13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_textCtrl18.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_textCtrl18.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.m_textCtrl18.Enable( False )
		
		fgSizer4.Add( self.m_textCtrl18, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer27.Add( fgSizer4, 0, wx.EXPAND, 5 )
		
		bSizer26 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrl1 = wx.ListCtrl( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		self.m_listCtrl1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_listCtrl1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.m_listCtrl1.Enable( False )
		
		bSizer26.Add( self.m_listCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer27.Add( bSizer26, 5, wx.EXPAND, 5 )
		
		
		bSizer11.Add( bSizer27, 1, wx.EXPAND, 5 )
		
		bSizer29 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer11.Add( bSizer29, 1, wx.EXPAND, 5 )
		
		
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
		
		self.m_toolBar4 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.m_tool3 = self.m_toolBar4.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"/home/richie/mygit/PointofSalePy/PosPy/frame/icons/toolbars/software.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_tool4 = self.m_toolBar4.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"/home/richie/mygit/PointofSalePy/PosPy/frame/icons/toolbars/software.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_tool5 = self.m_toolBar4.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"/home/richie/mygit/PointofSalePy/PosPy/frame/icons/toolbars/software.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_tool6 = self.m_toolBar4.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"/home/richie/mygit/PointofSalePy/PosPy/frame/icons/toolbars/software.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar4.Realize() 
		
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FPenjualanOnClose )
		self.m_textCtrl13.Bind( wx.EVT_KEY_DOWN, self.m_textCtrl13OnKeyDown )
		self.m_textCtrl13.Bind( wx.EVT_TEXT, self.m_textCtrl13OnText )
		self.m_textCtrl13.Bind( wx.EVT_TEXT_ENTER, self.m_textCtrl13OnTextEnter )
		self.Bind( wx.EVT_TOOL, self.m_tool3OnToolClicked, id = self.m_tool3.GetId() )
		self.Bind( wx.EVT_TOOL, self.m_tool4OnToolClicked, id = self.m_tool4.GetId() )
		self.Bind( wx.EVT_TOOL, self.m_tool5OnToolClicked, id = self.m_tool5.GetId() )
		self.Bind( wx.EVT_TOOL, self.m_tool6OnToolClicked, id = self.m_tool6.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FPenjualanOnClose( self, event ):
		event.Skip()
	
	def m_textCtrl13OnKeyDown( self, event ):
		event.Skip()
	
	def m_textCtrl13OnText( self, event ):
		event.Skip()
	
	def m_textCtrl13OnTextEnter( self, event ):
		event.Skip()
	
	def m_tool3OnToolClicked( self, event ):
		event.Skip()
	
	def m_tool4OnToolClicked( self, event ):
		event.Skip()
	
	def m_tool5OnToolClicked( self, event ):
		event.Skip()
	
	def m_tool6OnToolClicked( self, event ):
		event.Skip()
	

###########################################################################
## Class FPengaturan
###########################################################################

class FPengaturan ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pengaturan", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_panel9.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText16 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Pengaturan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		self.m_staticText16.SetFont( wx.Font( 15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		
		bSizer17.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.AddGrowableCol( 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.AddGrowableRow( 0 )
		fgSizer4.AddGrowableRow( 1 )
		fgSizer4.AddGrowableRow( 2 )
		fgSizer4.AddGrowableRow( 3 )
		fgSizer4.AddGrowableRow( 4 )
		fgSizer4.AddGrowableRow( 5 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText17 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		fgSizer4.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText18 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		fgSizer4.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button18 = wx.Button( self.m_panel9, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_button18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button19 = wx.Button( self.m_panel9, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_button19, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText19 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		fgSizer4.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText20 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		fgSizer4.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button20 = wx.Button( self.m_panel9, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_button20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button21 = wx.Button( self.m_panel9, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_button21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText21 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		fgSizer4.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText22 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		fgSizer4.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button22 = wx.Button( self.m_panel9, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_button22, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button23 = wx.Button( self.m_panel9, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_button23, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer17.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		
		self.m_panel9.SetSizer( bSizer17 )
		self.m_panel9.Layout()
		bSizer17.Fit( self.m_panel9 )
		bSizer16.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer16 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FPengaturanOnClose )
		self.m_button18.Bind( wx.EVT_BUTTON, self.m_button18OnButtonClick )
		self.m_button19.Bind( wx.EVT_BUTTON, self.m_button19OnButtonClick )
		self.m_button20.Bind( wx.EVT_BUTTON, self.m_button20OnButtonClick )
		self.m_button21.Bind( wx.EVT_BUTTON, self.m_button21OnButtonClick )
		self.m_button22.Bind( wx.EVT_BUTTON, self.m_button22OnButtonClick )
		self.m_button23.Bind( wx.EVT_BUTTON, self.m_button23OnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FPengaturanOnClose( self, event ):
		event.Skip()
	
	def m_button18OnButtonClick( self, event ):
		event.Skip()
	
	def m_button19OnButtonClick( self, event ):
		event.Skip()
	
	def m_button20OnButtonClick( self, event ):
		event.Skip()
	
	def m_button21OnButtonClick( self, event ):
		event.Skip()
	
	def m_button22OnButtonClick( self, event ):
		event.Skip()
	
	def m_button23OnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class FDialog
###########################################################################

class FDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel12 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText9 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"Apakah anda yakin ingin ingin melanjutkan?", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText9.Wrap( 200 )
		self.m_staticText9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer9.Add( self.m_staticText9, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer9.AddSpacer( ( 0, 10), 0, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.m_staticline1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticline1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer9.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer24.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button9 = wx.Button( self.m_panel12, wx.ID_ANY, u"Lanjut", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button9, 1, wx.ALL, 5 )
		
		self.m_button10 = wx.Button( self.m_panel12, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button10, 0, wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer24, 1, wx.EXPAND, 5 )
		
		
		self.m_panel12.SetSizer( bSizer9 )
		self.m_panel12.Layout()
		bSizer9.Fit( self.m_panel12 )
		bSizer8.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		bSizer8.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class Panel2
###########################################################################

class Panel2 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 200,200 ), style = wx.TAB_TRAVERSAL )
		
		self.SetMinSize( wx.Size( 200,200 ) )
		self.SetMaxSize( wx.Size( 200,200 ) )
		
	
	def __del__( self ):
		pass
	

###########################################################################
## Class FDataImport
###########################################################################

class FDataImport ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Import", pos = wx.DefaultPosition, size = wx.Size( 200,200 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_panel11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText23 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Silahkan Pilih File untuk di import (xls)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
		self.m_staticText23.Wrap( 150 )
		bSizer22.Add( self.m_staticText23, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_filePicker1 = wx.FilePickerCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer22.Add( self.m_filePicker1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_button24 = wx.Button( self.m_panel11, wx.ID_ANY, u"Proses", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button24.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer22.Add( self.m_button24, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_button25 = wx.Button( self.m_panel11, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_button25, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel11.SetSizer( bSizer22 )
		self.m_panel11.Layout()
		bSizer22.Fit( self.m_panel11 )
		bSizer18.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer18 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.m_filePicker1OnFileChanged )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_filePicker1OnFileChanged( self, event ):
		event.Skip()
	

###########################################################################
## Class FLaporan
###########################################################################

class FLaporan ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Laporan", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer35 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel19 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer36 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer36.Add( self.m_customControl3, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel19.SetSizer( bSizer36 )
		self.m_panel19.Layout()
		bSizer36.Fit( self.m_panel19 )
		bSizer35.Add( self.m_panel19, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer35 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel3 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

