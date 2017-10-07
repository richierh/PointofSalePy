# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug 31 2017)
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
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.Colour( 74, 74, 74 ) )
		self.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )
		
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		self.p_main = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.p_main.SetForegroundColour( wx.Colour( 74, 74, 74 ) )
		self.p_main.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )
		
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		self.statictext = wx.StaticText( self.p_main, wx.ID_ANY, u"MODEL TAMPILAN APLIKASI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.statictext.Wrap( -1 )
		self.statictext.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.statictext.SetForegroundColour( wx.Colour( 74, 74, 74 ) )
		self.statictext.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )
		
		bSizer24.Add( self.statictext, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer6 = wx.FlexGridSizer( 5, 0, 0, 0 )
		fgSizer6.AddGrowableCol( 0 )
		fgSizer6.AddGrowableRow( 0 )
		fgSizer6.AddGrowableRow( 1 )
		fgSizer6.AddGrowableRow( 2 )
		fgSizer6.AddGrowableRow( 3 )
		fgSizer6.AddGrowableRow( 4 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.btnsale = wx.Button( self.p_main, wx.ID_ANY, u"Penjualan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnsale.SetForegroundColour( wx.Colour( 74, 74, 74 ) )
		self.btnsale.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )
		
		fgSizer6.Add( self.btnsale, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.btnset = wx.Button( self.p_main, wx.ID_ANY, u"Pengaturan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.btnset, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnbuy = wx.Button( self.p_main, wx.ID_ANY, u"Pembelian", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.btnbuy, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.btnreport = wx.Button( self.p_main, wx.ID_ANY, u"Laporan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.btnreport, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.btnhelp = wx.Button( self.p_main, wx.ID_ANY, u"Bantuan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.btnhelp, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer25.Add( fgSizer6, 1, wx.EXPAND, 5 )
		
		self.mainBitmap = wx.StaticBitmap( self.p_main, wx.ID_ANY, wx.Bitmap( u"/home/pmc/mygit/PointofSalePy/PosPy/frame/icons/store.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mainBitmap.SetForegroundColour( wx.Colour( 240, 240, 240 ) )
		self.mainBitmap.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )
		
		bSizer25.Add( self.mainBitmap, 3, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		bSizer24.Add( bSizer25, 1, wx.EXPAND, 5 )
		
		
		self.p_main.SetSizer( bSizer24 )
		self.p_main.Layout()
		bSizer24.Fit( self.p_main )
		bSizer23.Add( self.p_main, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer23 )
		self.Layout()
		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu2 = wx.Menu()
		self.m_menubar2.Append( self.m_menu2, u"Berkas" ) 
		
		self.m_menu5 = wx.Menu()
		self.menuitemsale = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Penjualan", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.menuitemsale )
		
		self.menuitembuy = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Pembelian", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.menuitembuy )
		
		self.m_menu5.AppendSeparator()
		
		self.menuitemreport = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Laporan", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.menuitemreport )
		
		self.m_menubar2.Append( self.m_menu5, u"Tampilan" ) 
		
		self.m_menu3 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Data", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem2 )
		
		self.m_menubar2.Append( self.m_menu3, u"Pengaturan" ) 
		
		self.m_menu4 = wx.Menu()
		self.m_menubar2.Append( self.m_menu4, u"Bantuan" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

